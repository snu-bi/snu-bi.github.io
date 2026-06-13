/*******************************************************************/
/***** Bayesian Network Learning (BNL) Tool by Kyu-Baek Hwang ******/
/*****               BioIntelligence (BI) Lab                 ******/
/*****           Limited version without ZS_SEARCH            ******/
/*****          Department of Computer Engineering            ******/
/*****              Seoul National University                 ******/
/*****                 Republic of Korea                      ******/
/*****            Last modified: Nov. 15, 2001                ******/
/*******************************************************************/
 
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <math.h>
#include <time.h>
#include "bnl.h"

int dcycle;

BNODE local_bn[MAX_MBL + 1]; /* the local Bayesian network structure for ZS algorithm */
char larc_exist[MAX_MBL + 1][MAX_MBL + 1]; /* 0: none, 1: -->, 2: <-- , 3: ==>, 4: <== */
int lnode_order[MAX_MBL + 1]; /* local Bayesian network node order */

BNODE global_bn[NUM_ATTRIBUTE]; /* the present Bayesian network structure */
char arc_exist[NUM_ATTRIBUTE][NUM_ATTRIBUTE]; /* 0: none, 1: -->, 2: <--, 3: ==>, 4: <==, 5: collision */
int node_order[NUM_ATTRIBUTE];

BNODE best_bn[NUM_ATTRIBUTE]; /* the best scored Bayesian network structure */

int sufficient_n[NUM_ATTRIBUTE][MAX_JSIZE][MAX_CATEGORY];

/* the best structure and its score */
double best_score = -1000000000.0, pres_score;
int best_order[NUM_ATTRIBUTE];
char best_arc[NUM_ATTRIBUTE][NUM_ATTRIBUTE];

/* Initialize global Bayesian network */
void init_bn(BNODE bn_node[NUM_ATTRIBUTE])
{
	int i, j;

	for(i = 0; i < NUM_ATTRIBUTE; i++){
		bn_node[i].node_number = i;
		bn_node[i].num_state = num_category[i];
		bn_node[i].num_parent = (char) 0;
		for(j = 0; j < MAX_PARENT; j++){
			bn_node[i].pnode[j] = NULL;
		}
		bn_node[i].jsize = (char) 0;
		bn_node[i].cnode = NULL;
		bn_node[i].num_mbl = (char) 0;
		for(j = 0; j < MAX_MBL; j++){
			bn_node[i].mbl[j] = NULL;
		}
		bn_node[i].localpd = NULL;
	}

	return;
}

/* Depth-first search for the detection of directed cycles */
void DFS_visit(BNODE *bn_node)
{
	CNODEPTR child_ptr;

	bn_node->color = (char) 2;
	child_ptr = bn_node->cnode;
	while(child_ptr != NULL){
		if(child_ptr->node->color == (char) 2){
			dcycle = 1;
			return;
		}
		else if(child_ptr->node->color == (char) 0)
			DFS_visit(child_ptr->node);
		child_ptr = child_ptr->next;
	}
	bn_node->color = (char) 3;

	return;
}

void DF_search(BNODE bn_node[NUM_ATTRIBUTE])
{
	int i;

	dcycle = 0;
	for(i = 0; i < NUM_ATTRIBUTE; i++){
		bn_node[i].color = 0;
	}

	for(i = 0; i < NUM_ATTRIBUTE; i++){
		if(bn_node[i].color == 0)
			DFS_visit(&(bn_node[i]));
	}

	return;
}

void lDFS_visit(BNODE *bnnode)
{
	CNODEPTR child_ptr;

	bnnode->color = (char) 2;
	child_ptr = bnnode->cnode;
	while(child_ptr != NULL){
		if(child_ptr->node->color == (char) 2){
			dcycle = 1;
			return;
		}
		else if(child_ptr->node->color == (char) 0)
			lDFS_visit(child_ptr->node);
		child_ptr = child_ptr->next;
	}
	bnnode->color = (char) 3;

	return;
}

void lDF_search(BNODE bn_node[MAX_MBL + 1])
{
	int i;

	dcycle = 0;
	for(i = 0; i < MAX_MBL + 1; i++){
		bn_node[i].color = (char) 0;
	}

	for(i = 0; i < MAX_MBL + 1; i++){
		if(bn_node[i].color == (char) 0)
			lDFS_visit(&(bn_node[i]));
	}

	return;
}

/* Make the global BN structure with a given node order and arcs */
/* 0: success, 1: failure */
int make_bn(BNODE bn_node[NUM_ATTRIBUTE])
{
	int i, j, jsize;
	CNODEPTR child_ptr;

	for(i = 0; i < NUM_ATTRIBUTE; i++){
		for(j = i + 1; j < NUM_ATTRIBUTE; j++){
			if(arc_exist[i][j] == (char) 1 || arc_exist[i][j] == (char) 3){ /* --> */
				/* The limit in the number of parents */
				if(bn_node[node_order[j]].num_parent >= MAX_PARENT){
					return 1;
				}
				bn_node[node_order[j]].pnode[bn_node[node_order[j]].num_parent++] = &(bn_node[node_order[i]]);
				child_ptr = bn_node[node_order[i]].cnode;
				if(child_ptr == NULL){
					bn_node[node_order[i]].cnode = (CNODEPTR) malloc(sizeof(CNODE));
					bn_node[node_order[i]].cnode->node = &(bn_node[node_order[j]]);
					bn_node[node_order[i]].cnode->next = NULL;
				}
				else{
					while(child_ptr->next != NULL){
						child_ptr = child_ptr->next;
					}
					child_ptr->next = (CNODEPTR) malloc(sizeof(CNODE));
					child_ptr->next->node = &(bn_node[node_order[j]]);
					child_ptr->next->next = NULL;
				}
			}
			else if(arc_exist[i][j] == (char) 2 || arc_exist[i][j] == (char) 4){ /* <-- */
				/* The limit in the number of parents */
				if(bn_node[node_order[i]].num_parent >= MAX_PARENT){
					return 1;
				}
				bn_node[node_order[i]].pnode[bn_node[node_order[i]].num_parent++] = &(bn_node[node_order[j]]);
				child_ptr = bn_node[node_order[j]].cnode;
				if(child_ptr == NULL){
					bn_node[node_order[j]].cnode = (CNODEPTR) malloc(sizeof(CNODE));
					bn_node[node_order[j]].cnode->node = &(bn_node[node_order[i]]);
					bn_node[node_order[j]].cnode->next = NULL;
				}
				else{
					while(child_ptr->next != NULL){
						child_ptr = child_ptr->next;
					}
					child_ptr->next = (CNODEPTR) malloc(sizeof(CNODE));
					child_ptr->next->node = &(bn_node[node_order[i]]);
					child_ptr->next->next = NULL;
				}
			}
		}
	}

	for(i = 0; i < NUM_ATTRIBUTE; i++){
		jsize = 1;
		for(j = 0; j < (int) bn_node[i].num_parent; j++){
			jsize *= (int) bn_node[i].pnode[j]->num_state;
		}
		if(jsize > MAX_JSIZE){
			return 1;
		}
	}

	/* Check for directed cycles */
	dcycle = 0; /* global variable */
	DF_search(bn_node);
	if(dcycle == 1)
		return 1;

	return 0;
}

/* Delete parent-child relationship between pnode and cnode */
void delete_pc(BNODEPTR p_node, BNODEPTR c_node)
{
	int i, j;
	CNODEPTR child_ptr, prev_ptr = NULL;

	/* Delete a parent */
	for(i = 0; i < (int) c_node->num_parent; i++){
		if(c_node->pnode[i] == p_node)
			break;
	}
	if(i == (int) c_node->num_parent){
		fprintf(stderr, "Unacceptable error\n");
		exit(1);
	}
	for(j = i; j < ((int) c_node->num_parent) - 1; j++){
		c_node->pnode[j] = c_node->pnode[j + 1];
	}
	c_node->num_parent -= (char) 1;

	/* Delete a child */
	child_ptr = p_node->cnode;
	prev_ptr = NULL;
	while(child_ptr != NULL){
		if(child_ptr->node == c_node)
			break;
		prev_ptr = child_ptr;
		child_ptr = child_ptr->next;
	}
	if(child_ptr == NULL){
		fprintf(stderr, "Unacceptable error\n");
		exit(1);
	}
	if(prev_ptr == NULL){
		prev_ptr = p_node->cnode;
		p_node->cnode = p_node->cnode->next;
		free(prev_ptr);
	}
	else{
		prev_ptr->next = child_ptr->next;
		free(child_ptr);
	}

	return;
}

/* Make a parent-child relationship between pnode and cnode in gloabl_bn */
int make_pc(BNODEPTR p_node, BNODEPTR c_node)
{
	int i, jsize;
	CNODEPTR child_ptr;

	/* The limit in the number of parents */
	if((int) c_node->num_parent >= MAX_PARENT){
		return 1;
	}
	c_node->pnode[(int) c_node->num_parent] = p_node;
	c_node->num_parent += (char) 1;
	child_ptr = p_node->cnode;
	if(child_ptr == NULL){
		p_node->cnode = (CNODEPTR) malloc(sizeof(CNODE));
		p_node->cnode->node = c_node;
		p_node->cnode->next = NULL;
	}
	else{
		while(child_ptr->next != NULL){
			child_ptr = child_ptr->next;
		}
		child_ptr->next = (CNODEPTR) malloc(sizeof(CNODE));
		child_ptr->next->node = c_node;
		child_ptr->next->next = NULL;
	}

	jsize = 1;
	for(i = 0; i < (int) c_node->num_parent; i++){
		jsize *= (int) c_node->pnode[i]->num_state;
	}
	if(jsize > MAX_JSIZE){
		delete_pc(p_node, c_node);
		return 1;
	}

	/* Check if there exists a directed cycle */
	dcycle = 0;
	DF_search(global_bn);
	if(dcycle == 1){
		delete_pc(p_node, c_node);
		return 1;
	}

	return 0;
}

int lmake_pc(BNODEPTR p_node, BNODEPTR c_node)
{
	int i, jsize;
	CNODEPTR child_ptr;

	/* The limit in the number of parents */
	if(c_node->num_parent >= (char) MAX_PARENT){
		return 1;
	}
	c_node->pnode[(int) c_node->num_parent] = p_node;
	c_node->num_parent += (char) 1;
	child_ptr = p_node->cnode;
	if(child_ptr == NULL){
		p_node->cnode = (CNODEPTR) malloc(sizeof(CNODE));
		p_node->cnode->node = c_node;
		p_node->cnode->next = NULL;
	}
	else{
		while(child_ptr->next != NULL){
			child_ptr = child_ptr->next;
		}
		child_ptr->next = (CNODEPTR) malloc(sizeof(CNODE));
		child_ptr->next->node = c_node;
		child_ptr->next->next = NULL;
	}

	jsize = 1;
	for(i = 0; i < (int) c_node->num_parent; i++){
		jsize *= (int) c_node->pnode[i]->num_state;
	}
	if(jsize > MAX_JSIZE){
		delete_pc(p_node, c_node);
		return 1;
	}

	/* Check if there exists a directed cycle */
	dcycle = 0;
	lDF_search(local_bn);
	if(dcycle == 1){
		delete_pc(p_node, c_node);
		return 1;
	}

	return 0;
}

/* Free allocated memory to the BN */
void post_bn(BNODE bn_node[NUM_ATTRIBUTE])
{
	int i, j;
	CNODEPTR p, q;

	for(i = 0; i < NUM_ATTRIBUTE; i++){
		p = bn_node[i].cnode;
		for(; p != NULL;){
			q = p->next;
			free(p);
			p = q;
		}
		for(j = 0; j < bn_node[i].jsize; j++){
			free(bn_node[i].localpd[j]);
		}
		free(bn_node[i].localpd);
	}

	return;
}

/* Calculate all the sufficient statistics from the training data */
void calculate_statistics(BNODE bn_node[NUM_ATTRIBUTE])
{
	int i, j, k, jsize, jvalue, itmp;

	/* Initialize all the statistics */
	for(i = 0; i < NUM_ATTRIBUTE; i++){
		jsize = 1;
		for(j = 0; j < (int) bn_node[i].num_parent; j++){
			jsize *= (int) bn_node[i].pnode[j]->num_state;
		}
		for(j = 0; j < jsize; j++){
			for(k = 0; k < (int) bn_node[i].num_state; k++){
				sufficient_n[i][j][k] = 0;
			}
		}
	}

	/* Calculate all the statistics for the given BN structure */
	for(i = 0; i < NUM_EXAMPLE; i++){
		for(j = 0; j < NUM_ATTRIBUTE; j++){
			jvalue = 0; itmp = 1;
			for(k = 0; k < (int) bn_node[j].num_parent; k++){
				if(k != 0){
					itmp *= (int) bn_node[j].pnode[k - 1]->num_state;
				}
				jvalue += itmp * (int) training_data[i][bn_node[j].pnode[k]->node_number];
			}
			sufficient_n[j][jvalue][(int) training_data[i][j]]++;
		}
		
	}

	return;
}

/* Calculate necessary sufficient statistics from the training data */
void calculate_nstatistics(BNODE node)
{
	int i, j, jsize, jvalue, itmp;

	/* Initialize only the necessary statistics */
	jsize = 1;
	for(i = 0; i < (int) node.num_parent; i++){
		jsize *= (int) node.pnode[i]->num_state;
	}
	for(i = 0; i < jsize; i++){
		for(j = 0; j < (int) node.num_state; j++){
			sufficient_n[node.node_number][i][j] = 0;
		}
	}

	/* Calculate only the necessary statistics for the BN structure */
	for(i = 0; i < NUM_EXAMPLE; i++){
		jvalue = 0; itmp = 1;
		for(j = 0; j < (int) node.num_parent; j++){
			if(j != 0){
				itmp *= (int) node.pnode[j - 1]->num_state;
			}
			jvalue += itmp * (int) training_data[i][node.pnode[j]->node_number];
		}
		sufficient_n[node.node_number][jvalue][(int) training_data[i][node.node_number]]++;
	}

	return;
}

/* Parametric learning */
void calculate_lpd(BNODE bn_node[NUM_ATTRIBUTE])
{
	int i, j, k, jsize, itmp;
	int atmp[MAX_PARENT];
	
	calculate_statistics(bn_node);

	for(i = 0; i < NUM_ATTRIBUTE; i++){
		jsize = 1;
		for(j = 0; j < (int) bn_node[i].num_parent; j++){
			jsize *= (int) bn_node[i].pnode[j]->num_state;
		}
		bn_node[i].jsize = (char) jsize;

		/* Record the configuration of parents */
		itmp = 1;
		for(j = 0; j < (int) bn_node[i].num_parent; j++){
			atmp[j] = itmp;
			itmp *= (int) bn_node[i].pnode[j]->num_state;
		}
		for(j = 0; j < jsize; j++){
			itmp = j;
			for(k = ((int) bn_node[i].num_parent) - 1; k >= 0 ; k--){
				bn_node[i].jconfig[j][k] = (char) (itmp / atmp[k]);
				itmp %= atmp[k];
			}
		}

		/* Calculate the local probability distribution */
		bn_node[i].localpd = (double **) calloc((size_t) jsize, sizeof(double *));
		for(j = 0; j < jsize ; j++){
			itmp = 0;
			bn_node[i].localpd[j] = (double *) calloc((size_t) bn_node[i].num_state, sizeof(double));
			for(k = 0; k < (int) bn_node[i].num_state; k++){
				bn_node[i].localpd[j][k] = (double) sufficient_n[i][j][k] + 1.0;
				itmp += sufficient_n[i][j][k] + 1;
			}
			for(k = 0; k < (int) bn_node[i].num_state; k++){
				bn_node[i].localpd[j][k] /= (double) itmp;
			}
		}
	}

	return;
}

/* Logarithmic Gamma function */
double gammaln(double xx)
{
	double x, y, tmp, ser;
	static double cof[6] = {76.18009172947146, -86.50532032941677,
							24.01409824083091, -1.231739572450155,
							0.1208650973866179e-2, -0.5395239384953e-5};
	int j;

	y = x = xx;
	tmp = x + 5.5;
	tmp -= (x + 0.5) * log(tmp);
	ser = 1.000000000190015;
	for(j = 0; j <= 5; j++)
		ser += cof[j] / ++y;
	return -tmp + log(2.5066282746310005 * ser / x);
}

/* Calculate the BDe Score of the Bayesian network structure */
double BDeScore(BNODE bn_node[NUM_ATTRIBUTE])
{
	int i, j, k, jsize;
	int alphaij, nij;
	double return_val = 0.0, prior_score = 0.0;

	for(i = 0; i < NUM_ATTRIBUTE; i++){
		jsize = 1;
		for(j = 0; j < (int) bn_node[i].num_parent; j++){
			jsize *= (int) bn_node[i].pnode[j]->num_state;
		}
		for(j = 0; j < jsize; j++){
			alphaij = 0; nij = 0;
			for(k = 0; k < (int) bn_node[i].num_state; k++){
				return_val += gammaln((double) (sufficient_n[i][j][k] + 1)) - gammaln((double) 1);
				alphaij++;
				nij += sufficient_n[i][j][k];
			}
			return_val += gammaln((double) alphaij) - gammaln((double) (alphaij + nij));
		}
	}

	return (return_val + prior_score);
}

/* Calculate the BDe Score of a node in the Bayesian network structure */
double N_BDeScore(BNODE node)
{
	int i, j, jsize;
	int alphaij, nij;
	double return_val = 0.0, prior_score = 0.0;

	jsize = 1;
	for(i = 0; i < (int) node.num_parent; i++){
		jsize *= (int) node.pnode[i]->num_state;
	}
	for(i = 0; i < jsize; i++){
		alphaij = 0; nij = 0;
		for(j = 0; j < (int) node.num_state; j++){
			return_val += gammaln((double) (sufficient_n[node.node_number][i][j] + 1)) - gammaln((double) 1);
			alphaij++;
			nij += sufficient_n[node.node_number][i][j];
		}
		return_val += gammaln((double) alphaij) - gammaln((double) (alphaij + nij));
	}
	
	return (return_val + prior_score);
}

/* For the entire structural search in one node order */
void generate_arc(void)
{
	int i, j, k, ret;
	unsigned int ui;
	double bn_score;

	for(i = 0; i < NUM_ATTRIBUTE; i++){
		for(j = i + 1; j < NUM_ATTRIBUTE; j++){
			arc_exist[i][j] = (char) 0;
			fprintf(stderr, "%d", (int) arc_exist[i][j]);
		}
	}
	fprintf(stderr, "\n");

	/* Calculate the score of this BN */
	ret = make_bn(global_bn); /* ret is always false in this case (empty network) */
	calculate_statistics(global_bn);
	bn_score = BDeScore(global_bn);
	fprintf(stderr, "%.5lf : %.5lf\n", best_score, bn_score);
	if(bn_score > best_score){
		best_score = bn_score;
		for(i = 0; i < NUM_ATTRIBUTE; i++){
			best_order[i] = node_order[i];
		}
		for(i = 0; i < NUM_ATTRIBUTE; i++){
			for(j = i + 1; j < NUM_ATTRIBUTE; j++){
				best_arc[i][j] = arc_exist[i][j];
			}
		}
	}
	post_bn(global_bn);
	init_bn(global_bn);

	for(ui = (unsigned int) 1; ui < (unsigned int) pow(2.0, NUM_ATTRIBUTE * (NUM_ATTRIBUTE - 1) / 2); ui++){
		/* From the arithmetic adder algorithm */
		k = 0;
		for(i = 0; i < NUM_ATTRIBUTE; i++){
			for(j = i + 1; j < NUM_ATTRIBUTE; j++){
				if(arc_exist[i][j] == 0){
					arc_exist[i][j] = 1;
					k = 1;
					break;
				}
				arc_exist[i][j] = 0;
			}
			if(k == 1)
				break;
		}
		for(i = 0; i < NUM_ATTRIBUTE; i++){
			for(j = i + 1; j < NUM_ATTRIBUTE; j++){
				fprintf(stderr, "%d", (int) arc_exist[i][j]);
			}
		}
		fprintf(stderr, "\n");

		/* Calculate the score of this BN */
		if(make_bn(global_bn)){	/* num_parent limit over */
			init_bn(global_bn);
			continue;
		}
		calculate_statistics(global_bn);
		bn_score = BDeScore(global_bn);
		fprintf(stderr, "%.5lf : %.5lf\n", best_score, bn_score);
		if(bn_score > best_score){
			best_score = bn_score;
			for(i = 0; i < NUM_ATTRIBUTE; i++){
				best_order[i] = node_order[i];
			}
			for(i = 0; i < NUM_ATTRIBUTE; i++){
				for(j = i + 1; j < NUM_ATTRIBUTE; j++){
					best_arc[i][j] = arc_exist[i][j];
				}
			}	
		}
		post_bn(global_bn);
		init_bn(global_bn);
	}

	return;
}

/* For the generation of all node orders */
int candidate_node[NUM_ATTRIBUTE][NUM_ATTRIBUTE];

void generate_order(int start_point)
{
	int i, j;

	if(start_point == NUM_ATTRIBUTE){
		/* One node order was generated */
		for(i = 0; i < NUM_ATTRIBUTE; i++){
			fprintf(stderr, "%d ", node_order[i]);
		}
		fprintf(stderr, "\n");
		generate_arc();
		return;
	}
	for(i = 0; i < NUM_ATTRIBUTE; i++){
		if(candidate_node[start_point][i] == 0){
			node_order[start_point] = i;
			for(j = start_point; j < NUM_ATTRIBUTE; j++)
				candidate_node[j][i] = -1;
			generate_order(start_point + 1);
			for(j = start_point; j < NUM_ATTRIBUTE; j++)
				candidate_node[j][i] = 0;
		}
	}

	return;
}

/* Full search structural learning */
void full_search(void)
{
	generate_order(0);
}

void print_bn(FILE *ofile, BNODE bn_node[NUM_ATTRIBUTE])
{
	int i, j, k;

	if(!ofile){
		fprintf(stderr, "Network file open error\n");
		exit(1);
	}

	fprintf(ofile, "Belief Network \"untitled\"\n\n");

	for(i = 0; i < NUM_ATTRIBUTE; i++){
		fprintf(ofile, "node node_%d\n", i);
		fprintf(ofile, "{\n");
		fprintf(ofile, "\tname: \"%s\";\n", bn_node[i].name);
		fprintf(ofile, "\ttype: discrete[%d] = \n", bn_node[i].num_state);
		fprintf(ofile, "\t{\n");
		for(j = 0; j < bn_node[i].num_state - 1; j++){
			//fprintf(ofile, "\t\t\"%d\",\n", j);
			fprintf(ofile, "\t\t\"%s\",\n", cate_assoc[i][j].name);
		}
		//fprintf(ofile, "\t\t\"%d\"\n", j);
		fprintf(ofile, "\t\t\"%s\"\n", cate_assoc[i][j].name);
		fprintf(ofile, "\t};\n");
		fprintf(ofile, "}\n\n");
	}

	fprintf(ofile, "\n\n");

	for(i = 0; i < NUM_ATTRIBUTE; i++){
		fprintf(ofile, "probability(node_%d", i);
		if(bn_node[i].num_parent == 0){
			fprintf(ofile, ")\n");
			fprintf(ofile, "{\n");
			fprintf(ofile, "\t%lf", bn_node[i].localpd[0][0]);
			for(j = 1; j < bn_node[i].num_state; j++){
				fprintf(ofile, ", %lf", bn_node[i].localpd[0][j]);
			}
			fprintf(ofile, ";\n");
		}
		else{
			fprintf(ofile, " |");
			for(j = 0; j < bn_node[i].num_parent - 1; j++){
				fprintf(ofile, " node_%d,", bn_node[i].pnode[j]->node_number);
			}
			fprintf(ofile, " node_%d)\n", bn_node[i].pnode[j]->node_number);
			fprintf(ofile, "{\n");
			for(j = 0; j < bn_node[i].jsize; j++){
				fprintf(ofile, "\t(");
				for(k = 0; k < bn_node[i].num_parent - 1; k++){
					fprintf(ofile, "%d, ", bn_node[i].jconfig[j][k]);
					//fprintf(ofile, "%s, ", cate_assoc[bn_node[i].pnode[k]->node_number][bn_node[i].jconfig[j][k]].name);
				}
				fprintf(ofile, "%d): ", bn_node[i].jconfig[j][k]);
				//fprintf(ofile, "%s):", cate_assoc[bn_node[i].pnode[k]->node_number][bn_node[i].jconfig[j][k]].name);
				fprintf(ofile, "\t%lf", bn_node[i].localpd[j][0]);
				for(k = 1; k < bn_node[i].num_state; k++){
					fprintf(ofile, ", %lf", bn_node[i].localpd[j][k]);
				}
				fprintf(ofile, ";\n");
			}
		}
		fprintf(ofile, "}\n\n");
	}

	fprintf(ofile, "\n//Best Score: %.2lf\n", best_score / (double) NUM_EXAMPLE);
	return;
}

float ran1(long *idum)
/* "Minimal" random number generator of Park and Miller with Bays-Durham shuffle
 and added safeguards. Returns a uniform random deviate between 0.0 and 1.0 (exclusive
 of the endpoint values). Call with idum a negative integer to initialize; thereafter,
 do not alter idum between succesive deviates in a sequence. RNMX should approximate
 the largest floating value that is less than 1 */
{
	int j;
	long k;
	static long iy = 0;
	static long iv[NTAB];
	float temp;

	if(*idum <= 0 || !iy){
		if(-(*idum) < 1) *idum = 1;	/* Initialize */
		else *idum = -(*idum);		/* Be sure to prevent idum = 0 */
		for(j = NTAB + 7; j >= 0; j--){	/* Load the shuffle table (after 8 warm-ups) */
			k = (*idum) / IQ;
			*idum = IA * (*idum - k * IQ)- IR * k;
			if(*idum < 0) *idum += IM;
			if(j < NTAB) iv[j] = *idum;
		}
		iy = iv[0];
	}
	
	k = (*idum) / IQ;	/* Start here when not initializing */
	*idum = IA * (*idum - k * IQ) - IR * k;	/* Compute idum = (IA * idum) % IM without overflows */
	if(*idum < 0) *idum += IM;				/*	by Schrage's method */
	j = iy / NDIV;	/* Will be in the range 0..NTAB - 1 */
	iy = iv[j];		/* Output previously stored value and refill the shuffle table */
	iv[j] = *idum;
	if((temp = AM * iy) > RNMX) return RNMX;	/* Because users don't expect endpoint values */
	else return temp;
}

int main(int argc, char *argv[])
{
	FILE *ifile	/* training data file */, *ofile /* Bayesian network file */;
	FILE *lfile; /* training log file */
	int learn_type;
	char iline[MAX_LINE], *lptr, tmpstr[MAX_LINE];
	int i, j, k, l, ret;

	int change_position_i, change_position_j; /* for greedy search */
	char change_value, prev_value;
	double changed_score, prev_score = -1000000000.0, bchanged_score = -1000000000.0;
	long seed, t1, t2;
	float ran_num;
	
	/* For calculation of I(Xi; Xj, BL(Xi)) */
	int *tmp_iptr;
	PROWPTR prev_prow, pres_prow, tmp_prow;
	int i_tmp1, i_tmp2;
	double d_tmp1, d_tmp2, d_tmp3;

	CNODEPTR child_ptr, child_ptr2;
	
	if(argc != 4){
		fprintf(stderr, "Usage: bnl <data file> <network file> <log file>\n");
		exit(1);
	}
	
	/* Determine the learning strategy */
	//learn_type = FULL_SEARCH;
	learn_type = GREEDY_SEARCH;
	//learn_type = ZS_SEARCH;

	/* Read the training data */
	ifile = fopen(argv[1], "r");
	if(!ifile){
		fprintf(stderr, "Data file open error\n");
		exit(1);
	}

#ifdef TRANSPOSE
	/* Read the transposed data */
	i = 0;
	while(fgets(iline, MAX_LINE, ifile)){
		lptr = iline; j = 0;
		/* Read the attribute name */
		while(*lptr != '\t' && *lptr != '\n'){
			global_bn[i].name[j++] = *lptr;
			if(j >= MAX_NAME){
				fprintf(stderr, "Invalid name size in the attribute %d\n", i + 1);
				exit(1);
			}
			lptr++;
		}
		if(*lptr == '\n'){
			fprintf(stderr, "Unacceptable data format in line %d\n", i + 1);
			exit(1);
		}
		global_bn[i].name[j] = '\0';
		strcpy(best_bn[i].name, global_bn[i].name);
		while(*lptr == '\t')
			lptr++;

		/* Read training examples */
		j = 0;
		while(*lptr != '\n'){
			k = 0;
			while(*lptr != '\t' && *lptr != '\n'){
				tmpstr[k++] = *lptr;
				if(k >= MAX_NAME){
					fprintf(stderr, "Invalid category name size in the attribute %d and the training example %d\n", i + 1, j + 1);
					exit(1);
				}
				lptr++;
			}
			tmpstr[k] = '\0';
			for(k = 0; k < (int) num_category[i]; k++){
				if(!strcmp(cate_assoc[i][k].name, tmpstr))
					break;
			}
			if(k == (int) num_category[i]){ /* create new category for this attribute */
				if((int) num_category[i] >= MAX_CATEGORY){
					fprintf(stderr, "Invalid category size in the attribute %d\n", i + 1);
					exit(1);
				}
				strcpy(cate_assoc[i][(int) num_category[i]].name, tmpstr);
				cate_assoc[i][(int) num_category[i]].state_num = num_category[i];
				num_category[i] += (char) 1;
			}
			if(j >= NUM_EXAMPLE){
				fprintf(stderr, "Invalid line %d\n", i + 1);
				exit(1);
			}
			training_data[j][i] = (char) k;
			while(*lptr == '\t')
				lptr++;
			j++;
		}
		if(j != NUM_EXAMPLE){
			fprintf(stderr, "Invalid data at line %d\n", i + 1);
			exit(1);
		}
		i++;
	}
	if(i != NUM_ATTRIBUTE){
		fprintf(stderr, "Invalid number of attributes in the training data\n");
		exit(1);
	}
#else
	/* Read all attribute (node) names */
	if(!fgets(iline, MAX_LINE, ifile)){
		fprintf(stderr, "Invalid data file\n");
		exit(1);
	}
	lptr = iline; i = 0;
	while(1){
		j = 0;
		if(i >= NUM_ATTRIBUTE){
			fprintf(stderr, "Too many attributes in the training data\n");
			exit(1);
		}
		while(*lptr != '\t' && *lptr != '\n'){
			global_bn[i].name[j++] = *lptr;
			if(j >= MAX_NAME){
				fprintf(stderr, "Invalid name size in the attribute %d\n", i + 1);
				exit(1);
			}
			lptr++;
		}
		global_bn[i++].name[j] = '\0';
		strcpy(best_bn[i - 1].name, global_bn[i - 1].name);
		if(*lptr == '\n')
			break;
		lptr++;
	}
	if(i != NUM_ATTRIBUTE){
		fprintf(stderr, "Invalid number of attributes in the training data\n");
		exit(1);
	}

	/* Read all training examples */
	i = 0;
	while(fgets(iline, MAX_LINE, ifile)){
		j = 0;
		lptr = iline;
		while(1){
			if(j >= NUM_ATTRIBUTE){
				fprintf(stderr, "Invalid training data %d\n", i + 1);
				exit(1);
			}
			k = 0;
			while(*lptr != '\t' && *lptr != '\n'){
				tmpstr[k++] = *lptr;
				if(k >= MAX_NAME){
					fprintf(stderr, "Invalid category name size in the attribute %d and the training example %d\n", j + 1, i + 1);
					exit(1);
				}
				lptr++;
			}
			tmpstr[k] = '\0';
			for(k = 0; k < (int) num_category[j]; k++){
				if(!strcmp(cate_assoc[j][k].name, tmpstr))
					break;
			}
			if(k == (int) num_category[j]){ /* create new category for this attribute */
				if((int) num_category[j] >= MAX_CATEGORY){
					fprintf(stderr, "Invalid category size in the attribute %d\n", j + 1);
					exit(1);
				}
				strcpy(cate_assoc[j][(int) num_category[j]].name, tmpstr);
				cate_assoc[j][(int) num_category[j]].state_num = num_category[j];
				num_category[j] += (char) 1;
			}
			if(i >= NUM_EXAMPLE){
				fprintf(stderr, "Invalid training data size\n");
				exit(1);
			}
			training_data[i][j++] = (char) k;
			if(*lptr == '\n')
				break;
			lptr++;
		}
		i++;
	}
	if(i != NUM_EXAMPLE){
		fprintf(stderr, "Invalud training data size\n");
		exit(1);
	}
#endif
	fprintf(stderr, "Training data reading is completed...\n");
	fclose(ifile);

	/* Check the network availability */
	/*if((i = (int) pow((double) MAX_CATEGORY, (double) MAX_PARENT)) > MAX_JSIZE){
		fprintf(stderr, "Invalid j-size\n");
		exit(1);
	}*/

	/* Open the Bayesian network file */
	ofile = fopen(argv[2], "w");
	if(!ofile){
		fprintf(stderr, "Network file open error\n");
		exit(1);
	}

	if(learn_type == FULL_SEARCH){
		/* Initialize BN structure */
		init_bn(global_bn);

		/* Structural learning of BN */
		full_search();

		/* Record the best BN */
		for(i = 0; i < NUM_ATTRIBUTE; i++){
			node_order[i] = best_order[i];
		}
		for(i = 0; i < NUM_ATTRIBUTE; i++){
			for(j = i + 1; j < NUM_ATTRIBUTE; j++){
				arc_exist[i][j] = best_arc[i][j];
			}
		}
		ret = make_bn(global_bn);	/* ret is alwasy false (already checked) */
		calculate_lpd(global_bn);
	}
	else if(learn_type == GREEDY_SEARCH){
		int iterate_cnt = 0; /* greedy iteration count */

		t1 = (long) time(NULL);

		/* Initialize BN structure */
		init_bn(global_bn);
		for(i = 0; i < NUM_ATTRIBUTE; i++)
			node_order[i] = i;
		
		lfile = fopen(argv[3], "w"); /* training log file open */
		if(!lfile){
			fprintf(stderr, "Log file open error\n");
			exit(1);
		}

		/* Randomly initialize the network structure */
		seed = (long) time(NULL);
		seed = -1 * seed;
		for(i = 0; i < NUM_ATTRIBUTE; i++){
			for(j = i + 1; j < NUM_ATTRIBUTE; j++){
				ran_num = ran1(&seed);
				if(ran_num < (float) 0.6){
					arc_exist[i][j] = (char) 0;
				}
				else if(ran_num < (float) 0.8){
					arc_exist[i][j] = (char) 1;
					if(make_pc(&(global_bn[i]), &(global_bn[j])))
						arc_exist[i][j] = (char) 0;
				}
				else{
					arc_exist[i][j] = (char) 2;
					if(make_pc(&(global_bn[j]), &(global_bn[i])))
						arc_exist[i][j] = (char) 0;
				}
			}
		}
		calculate_statistics(global_bn);

		/* Structural learning of BN */
		fprintf(stderr, "Now, greedy searching...\n");
		while(1){
			/* For learning log */
			iterate_cnt++;

			/* For all possible arc changes */
			bchanged_score = 0.0;
			for(i = 0; i < NUM_ATTRIBUTE; i++){
				for(j = i + 1; j < NUM_ATTRIBUTE; j++){
					if(arc_exist[i][j] == (char) 0){ /* for non-existence */
						prev_score = N_BDeScore(global_bn[j]);
						arc_exist[i][j] = (char) 1; /* make --> */
						if(!make_pc(&(global_bn[i]), &(global_bn[j]))){
							calculate_nstatistics(global_bn[j]);
							changed_score = N_BDeScore(global_bn[j]);
							if(bchanged_score < (changed_score - prev_score)){
								bchanged_score = changed_score - prev_score;
								change_position_i = i; change_position_j = j;
								change_value = (char) 1;
							}
							arc_exist[i][j] = (char) 0;
							delete_pc(&(global_bn[i]), &(global_bn[j]));
							calculate_nstatistics(global_bn[j]);
						}
						else
							arc_exist[i][j] = (char) 0;
						prev_score = N_BDeScore(global_bn[i]);
						arc_exist[i][j] = (char) 2; /* make <-- */
						if(!make_pc(&(global_bn[j]), &(global_bn[i]))){
							calculate_nstatistics(global_bn[i]);
							changed_score = N_BDeScore(global_bn[i]);
							if(bchanged_score < (changed_score - prev_score)){
								bchanged_score = changed_score - prev_score;
								change_position_i = i; change_position_j = j;
								change_value = (char) 2;
							}
							arc_exist[i][j] = (char) 0;
							delete_pc(&(global_bn[j]), &(global_bn[i]));
							calculate_nstatistics(global_bn[i]);
						}
						else
							arc_exist[i][j] = (char) 0;
					}
					else if(arc_exist[i][j] == (char) 1){ /* for --> */
						prev_score = N_BDeScore(global_bn[i]);
						prev_score += N_BDeScore(global_bn[j]);
						arc_exist[i][j] = (char) 2; /* make <-- */
						delete_pc(&(global_bn[i]), &(global_bn[j]));
						if(!make_pc(&(global_bn[j]), &(global_bn[i]))){
							calculate_nstatistics(global_bn[i]);
							calculate_nstatistics(global_bn[j]);
							changed_score = N_BDeScore(global_bn[i]);
							changed_score += N_BDeScore(global_bn[j]);
							if(bchanged_score < (changed_score - prev_score)){
								bchanged_score = changed_score - prev_score;
								change_position_i = i; change_position_j = j;
								change_value = (char) 2;
							}
							arc_exist[i][j] = (char) 1;
							delete_pc(&(global_bn[j]), &(global_bn[i]));
							ret = make_pc(&(global_bn[i]), &(global_bn[j]));
							calculate_nstatistics(global_bn[i]);
							calculate_nstatistics(global_bn[j]);
						}
						else{
							arc_exist[i][j] = (char) 1;
							ret = make_pc(&(global_bn[i]), &(global_bn[j]));
						}
						prev_score = N_BDeScore(global_bn[j]);
						arc_exist[i][j] = (char) 0; /* make non-existence */
						delete_pc(&(global_bn[i]), &(global_bn[j]));
						calculate_nstatistics(global_bn[j]);
						changed_score = N_BDeScore(global_bn[j]);
						if(bchanged_score < (changed_score - prev_score)){
							bchanged_score = changed_score - prev_score;
							change_position_i = i; change_position_j = j;
							change_value = (char) 0;
						}
						arc_exist[i][j] = (char) 1;
						ret = make_pc(&(global_bn[i]), &(global_bn[j]));
						calculate_nstatistics(global_bn[j]);
					}
					else if(arc_exist[i][j] == (char) 2){ /* for <-- */
						prev_score = N_BDeScore(global_bn[i]);
						prev_score += N_BDeScore(global_bn[j]);
						arc_exist[i][j] = (char) 1; /* make --> */
						delete_pc(&(global_bn[j]), &(global_bn[i]));
						if(!make_pc(&(global_bn[i]), &(global_bn[j]))){
							calculate_nstatistics(global_bn[i]);
							calculate_nstatistics(global_bn[j]);
							changed_score = N_BDeScore(global_bn[i]);
							changed_score += N_BDeScore(global_bn[j]);
							if(bchanged_score < (changed_score - prev_score)){
								bchanged_score = changed_score - prev_score;
								change_position_i = i; change_position_j = j;
								change_value = (char) 1;
							}
							arc_exist[i][j] = (char) 2;
							delete_pc(&(global_bn[i]), &(global_bn[j]));
							ret = make_pc(&(global_bn[j]), &(global_bn[i]));
							calculate_nstatistics(global_bn[i]);
							calculate_nstatistics(global_bn[j]);
						}
						else{
							arc_exist[i][j] = (char) 2;
							ret = make_pc(&(global_bn[j]), &(global_bn[i]));
						}
						prev_score = N_BDeScore(global_bn[i]);
						arc_exist[i][j] = (char) 0; /* make non-existence */
						delete_pc(&(global_bn[j]), &(global_bn[i]));
						calculate_nstatistics(global_bn[i]);
						changed_score = N_BDeScore(global_bn[i]);
						if(bchanged_score < (changed_score - prev_score)){
							bchanged_score = changed_score - prev_score;
							change_position_i = i; change_position_j = j;
							change_value = (char) 0;
						}
						arc_exist[i][j] = (char) 2;
						ret = make_pc(&(global_bn[j]), &(global_bn[i]));
						calculate_nstatistics(global_bn[i]);
					}
				}
			}
			if(bchanged_score <= 7.105427357601e-10)
				break;
			prev_value = arc_exist[change_position_i][change_position_j];
			arc_exist[change_position_i][change_position_j] = change_value;
			if(change_value == (char) 0){
				if(prev_value == (char) 1){
					delete_pc(&(global_bn[change_position_i]), &(global_bn[change_position_j]));
					calculate_nstatistics(global_bn[change_position_j]);
				}
				else{ /* prev_value == 2 */
					delete_pc(&(global_bn[change_position_j]), &(global_bn[change_position_i]));
					calculate_nstatistics(global_bn[change_position_i]);
				}
			}
			else if(change_value == (char) 1){
				if(prev_value == (char) 0){
					ret = make_pc(&(global_bn[change_position_i]), &(global_bn[change_position_j]));
					calculate_nstatistics(global_bn[change_position_j]);
				}
				else{ /* prev_value == 2 */
					delete_pc(&(global_bn[change_position_j]), &(global_bn[change_position_i]));
					ret = make_pc(&(global_bn[change_position_i]), &(global_bn[change_position_j]));
					calculate_nstatistics(global_bn[change_position_i]);
					calculate_nstatistics(global_bn[change_position_j]);
				}
			}
			else{ /* change_value == 2 */
				if(prev_value == (char) 0){
					ret = make_pc(&(global_bn[change_position_j]), &(global_bn[change_position_i]));
					calculate_nstatistics(global_bn[change_position_i]);
				}
				else{ /* prev_value == 1 */
					delete_pc(&(global_bn[change_position_i]), &(global_bn[change_position_j]));
					ret = make_pc(&(global_bn[change_position_j]), &(global_bn[change_position_i]));
					calculate_nstatistics(global_bn[change_position_i]);
					calculate_nstatistics(global_bn[change_position_j]);
				}
			}
			fprintf(stderr, "\nChanged score * %d: %.5lf\n", NUM_EXAMPLE, bchanged_score);
			best_score = BDeScore(global_bn);
			fprintf(stderr, "\nBest score: %.5lf\n", best_score / (double) NUM_EXAMPLE);

			fprintf(lfile, "%d: %lf\n", iterate_cnt, best_score / (double) NUM_EXAMPLE);
			if(iterate_cnt >= 1200)
				break;
		}
		calculate_lpd(global_bn);

		t2 = (long) time(NULL);
		fprintf(lfile, "Total time: %ld (secs)\n", t2 - t1);
		fclose(lfile);
	}
	else if(learn_type == ZS_SEARCH){
		fprintf(stderr, "Not applied in thie version\n");
	}

	/* Print the found network structure */
	print_bn(ofile, global_bn);
	post_bn(global_bn);

	fclose(ofile);

	return 0;
}
