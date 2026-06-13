<!--=============================================================


                   -----------------------------
                         W a y - B O A R D
                   -----------------------------

                                Version 2.2.0
                                by  Lim, Dae-Ho


-----------------------------------------------------------------
= Powered by Way-SERIES ...... http://way.co.kr = Since 1998-08 =
=================================================================
  Web Server : Apache/2.0.40 (Red Hat Linux)
  PHP : 4.2.2
  MySQL : 3.23.54
  Process : 0.09sec
==============================================================-->




<HTML>
<HEAD>



<!-------------------- USER BROWSER TITLE -------------------->
<TITLE>한국데이타마이닝학회</TITLE>



<!-------------------- USER HEAD TAG -------------------->
<META NAME="Generator" CONTENT="Way-BOARD">

<META HTTP-EQUIV="Content-Type" CONTENT="text/html; charset=EUC-KR">

<STYLE TYPE="text/css">
<!--
	.base
		{ text-decoration:none; font-size:9pt; line-height:1.2 }
	.big
		{ text-decoration:none; font-size:10pt }
	.small
		{ text-decoration:none; font-size:8pt }
// -->
</STYLE>

<SCRIPT LANGUAGE="JavaScript">
<!--
function DirectView(URL) {
	window.open(URL, '_DirectView', 'resizable=1,scrollbars=1,status=0,width=450,height=550');
}
// -->
</SCRIPT>

</HEAD>





<!-------------------- USER BODY TAG -------------------->
<BODY BGCOLOR=WHITE TEXT=BLACK>





<!-------------------- USER-HEADER -------------------->
<DIV ALIGN=CENTER>
<TABLE BORDER=0 CELLPADDING=0 CELLSPACING=0 WIDTH=600>
<TR>
<TD ALIGN=CENTER>
<BR>
<BR>
</TD>
</TR>
</TABLE>
</DIV>
<!-------------------- / USER-HEADER -------------------->





<!-------------------- SYSTEM-BODY -------------------->

<DIV ALIGN=CENTER>
<TABLE BORDER=0 CELLPADDING=0 CELLSPACING=0 WIDTH=545>




<TR>
<TD ALIGN=LEFT>
<A HREF="http://bi.snu.ac.kr/KDMS" TARGET=_self><IMG SRC=./img/ficon/mori2/home.gif ALT="홈" BORDER=0 WIDTH=31 HEIGHT=36></A><A HREF="/board/way-board.php?db=kdms&j=lv&pg=3&cv=&sf=&sd=&sw=" ><IMG SRC=./img/ficon/mori2/list.gif ALT="목록" BORDER=0 WIDTH=31 HEIGHT=36></A></TD>
</TR>


<TR>

<TD WIDTH=545 VALIGN=TOP>

<TABLE BORDER=0 CELLPADDING=0 CELLSPACING=0 WIDTH=545>
<TR>
<TD BGCOLOR=SILVER>

<TABLE BORDER=0 CELLPADDING=2 CELLSPACING=1 WIDTH=545>




<TR>
<TD BGCOLOR=#FFCC00 ALIGN=CENTER>
<FONT CLASS=big COLOR=BLACK>
110.1번 글쓴이(simon@kw.ac.kr)에게 관련메일 쓰기
</FONT>
</TD>
</TR>




<FORM METHOD=POST ACTION=/board/way-board.php NAME=form ENCTYPE="multipart/form-data">
<TR>
<TD BGCOLOR=WHITE ALIGN=CENTER>

<TABLE BORDER=0 CELLPADDING=0 CELLSPACING=0 WIDTH=95%>
<TR><TD BGCOLOR=WHITE COLSPAN=3>&nbsp; </TD></TR>

<TR>
<TD BGCOLOR=WHITE ALIGN=RIGHT><FONT CLASS=base COLOR=BLACK>이름</FONT></TD>
<TD>&nbsp; </TD>
<TD BGCOLOR=WHITE><FONT SIZE=3><INPUT TYPE=TEXT NAME=name SIZE=15 VALUE="" ></FONT></TD>
</TR>

<TR>
<TD BGCOLOR=WHITE ALIGN=RIGHT><FONT CLASS=base COLOR=BLACK>메일</FONT></TD>
<TD>&nbsp; </TD>
<TD BGCOLOR=WHITE><FONT SIZE=3><INPUT TYPE=TEXT NAME=mail SIZE=30 VALUE="" ></FONT>
</TD>
</TR>

<TR>
<TD BGCOLOR=WHITE ALIGN=RIGHT><FONT CLASS=base COLOR=BLACK>첨부파일</FONT></TD>
<TD>&nbsp; </TD>
<TD BGCOLOR=WHITE><FONT SIZE=3><INPUT TYPE=HIDDEN NAME=MAX_FILE_SIZE VALUE=1048576>
<INPUT TYPE=FILE NAME=filename SIZE=35 ></FONT><FONT CLASS=base>&nbsp; (최대 1MB)</FONT>

</TD>
</TR>

<TR>
<TD BGCOLOR=WHITE ALIGN=RIGHT><FONT CLASS=base COLOR=BLACK>제목</FONT></TD>
<TD>&nbsp; </TD>
<TD BGCOLOR=WHITE><FONT SIZE=3><INPUT TYPE=TEXT NAME=title SIZE=58 VALUE="Re: 진행요원 관련" ></FONT></TD>
</TR>

<TR>
<TD BGCOLOR=WHITE ALIGN=RIGHT VALIGN=TOP><FONT CLASS=base COLOR=BLACK>내용</FONT></TD>
<TD>&nbsp; </TD>
<TD BGCOLOR=WHITE><FONT SIZE=3><TEXTAREA NAME=content COLS=67 ROWS=15 WRAP=VIRTUAL ></TEXTAREA></FONT></TD></TR>

<TR>
<TD BGCOLOR=WHITE ALIGN=RIGHT><FONT CLASS=base COLOR=BLACK>&nbsp; </FONT></TD>
<TD>&nbsp; </TD>
<TD BGCOLOR=WHITE><FONT SIZE=2>
<INPUT TYPE=HIDDEN NAME=ori_content VALUE="

2003-06-05 15:30:34, &quot;조재희 교수&quot; 님이 쓰신 글입니다.
&gt; 안 교수님 그리고 신 조교 진행요원 가능자 이름을 올려 주십시오.">
<INPUT TYPE=BUTTON NAME=ori_content_include VALUE="원문 인용"
 onClick="this.form.content.value=this.form.content.value+this.form.ori_content.value;this.form.content.focus();" >
</FONT>
</TD>
</TR>

</TABLE>

</TD>
</TR>

<TR>
<TD BGCOLOR=#FFCC00 ALIGN=RIGHT>
<FONT CLASS=big>&nbsp; </FONT>
</TD>
</TR>

</TABLE>

</TD>
</TR>
</TABLE>

</TD>
</TR>





<TR>
<TD ALIGN=RIGHT>
<A HREF="http://bi.snu.ac.kr/KDMS" TARGET=_self><IMG SRC=./img/ficon/mori2/home.gif ALT="홈" BORDER=0 WIDTH=31 HEIGHT=36></A><A HREF="/board/way-board.php?db=kdms&j=lv&pg=3&cv=&sf=&sd=&sw=" ><IMG SRC=./img/ficon/mori2/list.gif ALT="목록" BORDER=0 WIDTH=31 HEIGHT=36></A></TD>
</TR>

<SCRIPT LANGUAGE="JavaScript">
<!--
function SubmitConfirm(form) {
	
	if (form.name.value == "") {
		alert("이름 : 필수항목입니다.");
	 	form.name.focus();
		return;
	}
	
	if (form.title.value == "") {
		alert("제목 : 필수항목입니다.");
	 	form.title.focus();
		return;
	}
	
	if (form.content.value == "") {
		alert("내용 : 필수항목입니다.");
	 	form.content.focus();
		return;
	}
	
	form.submit();
}
// -->
</SCRIPT>




<TR>

<TD ALIGN=CENTER>
<INPUT TYPE=HIDDEN NAME=db VALUE=kdms>
<INPUT TYPE=HIDDEN NAME=j  VALUE=tmr>
<INPUT TYPE=HIDDEN NAME=number VALUE=260>
<INPUT TYPE=HIDDEN NAME=pg VALUE=3>
<INPUT TYPE=HIDDEN NAME=cv VALUE=>
<INPUT TYPE=HIDDEN NAME=sf VALUE=>
<INPUT TYPE=HIDDEN NAME=sd VALUE=>
<INPUT TYPE=HIDDEN NAME=sw VALUE="">
<FONT SIZE=2><INPUT TYPE=BUTTON VALUE=" 취소 " onClick="history.go(-1)" >
<INPUT TYPE=RESET VALUE=" 원래대로 " > &nbsp; &nbsp; &nbsp;
<INPUT TYPE=BUTTON VALUE="           확        인           " onClick="SubmitConfirm(this.form);" ></FONT>
</TD>
</TR></FORM>


</TABLE>
</DIV>

<!-------------------- / SYSTEM-BODY -------------------->





<!-------------------- USER-FOOTER -------------------->
<BR>
<BR>
<DIV ALIGN=CENTER>
<TABLE BORDER=0 CELLPADDING=0 CELLSPACING=0 WIDTH=600>
<TR>
<TD>
<FONT STYLE="text-decoration:none; font-size:9pt; line-height:1.2">
Powered by</FONT>
<A HREF=http://bi.snu.ac.kr/KDMS target=_top><FONT STYLE="text-decoration:none; font-size:9pt; line-height:1.2">한국데이타마이닝학회</FONT></A>
</TD>
</TR>
</TABLE>
</DIV>
<!-------------------- / USER-FOOTER -------------------->





</BODY>
</HTML>
