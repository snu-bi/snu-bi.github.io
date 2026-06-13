/* Global constants */
#define MAX_LINE 1024 * 10
#define MAX_NAME 1024 /* maximum length of the attribute name */
#define FULL_SEARCH 0
#define GREEDY_SEARCH 1
#define ZS_SEARCH 2

#define MAX_PARENT 4
#define MAX_CATEGORY 2 /* maximum category number */
#define MAX_JSIZE 25

#define MAX_MBL 10 /* maximum size of Markov blanket */

/* Description of the training data */
#define NUM_ATTRIBUTE 8 /* the number of nodes */
#define NUM_EXAMPLE 10000 
char training_data[NUM_EXAMPLE][NUM_ATTRIBUTE];
char num_category[NUM_ATTRIBUTE];
typedef struct tag_cateassoc{
	char name[MAX_NAME];
	char state_num;
} CATEASSOC;
CATEASSOC cate_assoc[NUM_ATTRIBUTE][MAX_CATEGORY];

/* Description of the Bayesian network */
typedef struct tag_cpd *CPDPTR;
typedef struct tag_cpd{
	double (*pb_table)[MAX_CATEGORY];
} CPD;

typedef struct tag_bnode *BNODEPTR;
typedef struct tag_cnode *CNODEPTR;
typedef struct tag_cnode{
	BNODEPTR node;
	CNODEPTR next;
} CNODE;

typedef struct tag_bnode{
	char name[MAX_NAME]; /* the name of node */
	int node_number; /* unique node number */
	char num_state; /* the number of states of this node */

	char num_parent; /* the number of parents of this node */
	BNODEPTR pnode[MAX_PARENT]; /* pointers to parents */
	char jsize; /* the number of configuration of parents */
	char jconfig[MAX_JSIZE][MAX_PARENT]; /* the unique number for a configuration of parents */
	
	CNODEPTR cnode; /* pointer to children */

	/* Markov blanket of this node */
	char num_mbl; /* the size of Markov blanket */
	BNODEPTR mbl[MAX_MBL]; /* pointers to the members of Markov blanket */

	double **localpd; /* pointer to the local probability distribution */

	char color; /* for DFS and detecting cycles (0, 1, 2, 3) */
	double c_mi; /* for selection of candidate Markov blanket */
} BNODE;

/* For calculation of P(Xi, Xj, BL(Xi)) */
typedef struct tag_prow *PROWPTR;
typedef struct tag_prow{
	int *row;
	PROWPTR next;
} PROW;
PROWPTR ptable;

/* Following definitions are for the function of ran1() */
#define IA 16807
#define IM 2147483647
#define AM (1.0 / IM)
#define IQ 127773
#define IR 2836
#define NTAB 32
#define NDIV (1 + (IM - 1) / NTAB)
#define EPS 1.2e-7
#define RNMX (1.0 - EPS)

/* Function prototypes */
void init_bn(BNODE [NUM_ATTRIBUTE]);
void make_nodepair(void);
void full_search(void);
void generate_order(int);
void generate_arc(void);
int make_bn(BNODE [NUM_ATTRIBUTE]);
void DF_search(BNODE [NUM_ATTRIBUTE]);
void DF_visit(BNODE *);
void calculate_statistics(BNODE [NUM_ATTRIBUTE]);
double BDeScore(BNODE [NUM_ATTRIBUTE]);
void post_bn(BNODE [NUM_ATTRIBUTE]);

void make_lnodepair(void);
