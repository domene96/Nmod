// Define a grammar called Nmod
grammar Nmod;

@header {
from Compiler import *
# from VirtualMachine import *
c = Compiler()
# vm = VirtualMachine()
}

// Parser rules

program:
  ( PROGRAM ID {c.insertFunctionDirectory($ID.text, 'void')} COLON ( variables )* ( modules )* main );
f_type
  returns[Object type]:
  ( INT {$type = $INT.text}
  | FLOAT {$type = $FLOAT.text}
  | CHAR {$type = $CHAR.text} );
variables:
  ( VARIABLES f_type COLON id_decl {c.insertVarTable('global', $id_decl.text, $f_type.text)} ( COMMA id_decl {c.insertVarTable('global',$id_decl.text, $f_type.text)} )* SEMICOLON );
id_decl:
  ( ID {c.insertStackOperand($ID.text)} {c.insertStackType(c.getVarType(c.localFunc, $ID.text))} ( LBRACKET {c.initDimVar()} {c.nextDimension()} CTEI {c.setDimLowBound($CTEI.text)} COLON CTEI {c.setDimHighBound($CTEI.text)} ( COMMA {c.addDimension()} CTEI {c.setDimLowBound($CTEI.text)} COLON CTEI {c.setDimHighBound($CTEI.text)} )* RBRACKET {c.calculateK()} )? {c.associateBaseAddr()} );
id_access:
  ( ID {c.insertStackOperand($ID.text)} ( LBRACKET {c.dimVarBegin()} exp {c.generateQuad('exp')} ( COMMA {c.nextDimension()} exp {c.generateQuad('exp')} )* RBRACKET {c.dimVarEnd()} )? );
modules:
  ( ID {c.localFunc = $ID.text} ISFUNCTION ( VOID {c.insertFunctionDirectory($ID.text, 'void')} | f_type {c.insertFunctionDirectory($ID.text, $f_type.text)} {c.insertVarTable(c.localFunc, $ID.text, $f_type.text)} ) FUNC LPRACKET ( f_type ID {c.insertVarTable(c.localFunc, $ID.text, $f_type.text)} {c.insertParamTable(c.localFunc, $ID.text, $f_type.text)} ( COMMA f_type ID {c.insertVarTable(c.localFunc, $ID.text, $f_type.text)} {c.insertParamTable(c.localFunc, $ID.text, $f_type.text)} )* )? RPRACKET {c.validateParameters(c.localFunc)} ( variables )* {c.moduleBegin()} block {c.moduleEnd()} );
main:
  ( MAIN {c.mainBegin()} LPRACKET RPRACKET block {c.mainEnd()} );
block:
  ( LCRACKET ( statute )* RCRACKET );
statute:
  ( assignment
  | condition
  | reading
  | writing
  | cicle
  | call_module );
assignment:
  ( id_access {c.insertStackOperand($id_access.text)} EQUALS {c.insertStackOperator($EQUALS.text)} exp {c.generateQuad('exp')} SEMICOLON );
condition:
  ( IF LPRACKET expression RPRACKET {c.conditionStart()} block ( ELSE {c.conditionElse()} block )? {c.conditionEnd()} );
cicle:
  ( WHILE {c.insertStackJump()} LPRACKET expression RPRACKET {c.cicleStart()} block {c.cicleEnd()} );
reading:
  ( READ LPRACKET ( STRING | expression+ ( COMMA expression )* )? RPRACKET SEMICOLON );
writing:
  ( PRINT LPRACKET ( STRING | expression+ ( COMMA expression )* )? RPRACKET SEMICOLON );
call_module
  returns[Object type, val]:
  ( r_return | rnom | rexp | rgamma | points | lines | text | barplot | piechart | xyplot | densityplot | histogram | sin | cos | tan | asin | acos | atan | atan2 | log | log10 | exponent | f_max | f_min | f_range | f_sum | diff | prod | mean | median | quantile | weighedmean | rank | var | sd | cor | cov | f_round | transpose | diagonal | ginv | rowsum | colsum | load | data | library | rpois | rweibull | rbinom | rgeom | runif | ( ID {c.functionDirectory.functionExists($ID.text)} {$val = c.getModuleReturnAddr($ID.text)} {$type = c.getModuleReturnType($ID.text)} LPRACKET {c.generateERA()} ( exp {c.generateActionParameter()} ( COMMA {c.moveParameterPointer()} exp {c.generateActionParameter()} )* )? RPRACKET {c.nullParameterPointer()} ) {c.generateGoSub()} );
expression:
  ( sub_exp {c.generateQuad('sub_exp')} ( ( AND {c.insertStackOperator($AND.text)} | OR {c.insertStackOperator($OR.text)} )+ sub_exp+ {c.generateQuad('sub_exp')} )? );
sub_exp:
  ( exp {c.generateQuad('exp')} ( ( EQUAL {c.insertStackOperator($EQUAL.text)} | GREATEROR {c.insertStackOperator($GREATEROR.text)} | GREATERTHAN {c.insertStackOperator($GREATERTHAN.text)} | LESSEROR {c.insertStackOperator($LESSEROR.text)} | LESSERTHAN {c.insertStackOperator($LESSERTHAN.text)} )+ exp+ {c.generateQuad('exp')} )? );
exp:
  ( term {c.generateQuad('term')} ( ( MINUS {c.insertStackOperator($MINUS.text)} | PLUS {c.insertStackOperator($PLUS.text)} )+ term+ {c.generateQuad('term')} )? );
term:
  ( factor {c.generateQuad('factor')} ( ( DIVISION {c.insertStackOperator($DIVISION.text)} | TIMES {c.insertStackOperator($TIMES.text)} )+ factor+ {c.generateQuad('factor')} )? );
factor:
  ( LPRACKET {c.insertFalseBottom()} expression RPRACKET {c.removeFalseBottom()}
  | ( PLUS | MINUS )? var_cte {c.insertStackOperand($var_cte.text)} {c.insertStackType($var_cte.type)} );
var_cte
  returns[Object type, val]:
  ( id_access {$type = c.getVarType(c.localFunc, $id_access.text)} {$val = c.getVarVal(c.localFunc, $id_access.text)}
  | CTEI {$type = 'int'} {$val = c.insertConstant($type, $CTEI.text)}
  | CTEF {$type = 'float'} {$val = c.insertConstant($type, $CTEF.text)}
  | call_module {$type = $call_module.type} {$val = $call_module.val} );
r_return:
  ( RETURN expression SEMICOLON );
rnom:
  ( RNOM LPRACKET var_cte COMMA var_cte COMMA var_cte COMMA var_cte RPRACKET SEMICOLON );
rexp:
  ( REXP LPRACKET var_cte COMMA var_cte RPRACKET SEMICOLON );
rgamma:
  ( RGAMMA LPRACKET var_cte COMMA var_cte COMMA var_cte RPRACKET SEMICOLON );
points:
  ( POINTS LPRACKET var_cte COMMA var_cte RPRACKET SEMICOLON );
lines:
  ( LINES LPRACKET var_cte COMMA var_cte RPRACKET SEMICOLON );
text:
  ( TEXT LPRACKET CTEI COMMA CTEI COMMA id_decl RPRACKET SEMICOLON );
barplot:
  ( BARPLOT LPRACKET var_cte COMMA var_cte COMMA var_cte COMMA var_cte RPRACKET SEMICOLON );
piechart:
  ( PIECHART LPRACKET var_cte COMMA var_cte COMMA var_cte COMMA var_cte RPRACKET SEMICOLON );
xyplot:
  ( XYPLOT LPRACKET var_cte COMMA var_cte COMMA var_cte COMMA var_cte RPRACKET SEMICOLON );
densityplot:
  ( DENSITYPLOT LPRACKET var_cte COMMA var_cte COMMA var_cte COMMA var_cte RPRACKET SEMICOLON );
histogram:
  ( HISTOGRAM LPRACKET var_cte COMMA var_cte COMMA var_cte COMMA var_cte RPRACKET SEMICOLON );
sin:
  ( SIN LPRACKET expression RPRACKET SEMICOLON );
cos:
  ( COS LPRACKET expression RPRACKET SEMICOLON );
tan:
  ( TAN LPRACKET expression RPRACKET SEMICOLON );
asin:
  ( ASIN LPRACKET expression RPRACKET SEMICOLON );
acos:
  ( ACOS LPRACKET expression RPRACKET SEMICOLON );
atan:
  ( ATAN LPRACKET expression RPRACKET SEMICOLON );
atan2:
  ( ATAN2 LPRACKET expression RPRACKET SEMICOLON );
log:
  ( LOG LPRACKET expression RPRACKET SEMICOLON );
log10:
  ( LOG10 LPRACKET expression RPRACKET SEMICOLON );
exponent:
  ( EXPONENT LPRACKET expression RPRACKET SEMICOLON );
f_max:
  ( MAX LPRACKET expression ( COMMA expression )* RPRACKET SEMICOLON );
f_min:
  ( MIN LPRACKET expression ( COMMA expression )* RPRACKET SEMICOLON );
f_range:
  ( RANGE LPRACKET expression ( COMMA expression )* RPRACKET SEMICOLON );
f_sum:
  ( SUM LPRACKET expression ( COMMA expression )* RPRACKET SEMICOLON );
diff:
  ( DIFF LPRACKET id_decl COMMA CTEI RPRACKET SEMICOLON );
prod:
  ( PROD LPRACKET expression ( COMMA expression )* RPRACKET SEMICOLON );
mean:
  ( MEAN LPRACKET id_decl RPRACKET SEMICOLON );
median:
  ( MEDIAN LPRACKET id_decl RPRACKET SEMICOLON );
quantile:
  ( QUANTILE LPRACKET expression ( COMMA expression )* RPRACKET SEMICOLON );
weighedmean:
  ( WEIGHEDMEAN LPRACKET expression ( COMMA expression )* RPRACKET SEMICOLON );
rank:
  ( RANK LPRACKET id_decl COMMA ZERO RPRACKET SEMICOLON
  | RANK LPRACKET id_decl COMMA ONE RPRACKET SEMICOLON );
var:
  ( VARIANCE LPRACKET var_cte COMMA var_cte RPRACKET SEMICOLON );
sd:
  ( SD LPRACKET var_cte RPRACKET SEMICOLON );
cor:
  ( COR LPRACKET var_cte COMMA var_cte COMMA ( PEARSON | KENDALL | SPEARMAN ) RPRACKET SEMICOLON );
cov:
  ( COV LPRACKET var_cte RPRACKET SEMICOLON );
f_round:
  ( ROUND LPRACKET var_cte ( COMMA var_cte )* RPRACKET SEMICOLON );
transpose:
  ( TRANSPOSE LPRACKET var_cte RPRACKET SEMICOLON );
diagonal:
  ( DIAGONAL LPRACKET var_cte RPRACKET SEMICOLON );
ginv:
  ( GINV LPRACKET var_cte RPRACKET SEMICOLON );
rowsum:
  ( ROWSUM LPRACKET var_cte RPRACKET SEMICOLON );
colsum:
  ( COLSUM LPRACKET var_cte RPRACKET SEMICOLON );
load:
  ( LOAD LPRACKET var_cte ( COMMA var_cte )* RPRACKET SEMICOLON );
data:
  ( DATA LPRACKET expression ( COMMA expression )* RPRACKET SEMICOLON );
library:
  ( LIBRARY LPRACKET ( STRING | var_cte ) RPRACKET SEMICOLON );
rpois:
  ( RPOIS LPRACKET var_cte COMMA var_cte COMMA var_cte RPRACKET SEMICOLON );
rweibull:
  ( RWEIBULL LPRACKET var_cte RPRACKET SEMICOLON );
rbinom:
  ( RBINOM LPRACKET var_cte COMMA var_cte COMMA var_cte RPRACKET SEMICOLON );
rgeom:
  ( RGEOM LPRACKET var_cte COMMA var_cte RPRACKET SEMICOLON );
runif:
  ( RUNIF LPRACKET var_cte COMMA var_cte RPRACKET SEMICOLON );

// Lexer rules

fragment LOWERCASE: [a-z];
fragment UPPERCASE: [A-Z];
fragment DIGIT: [0-9];
PROGRAM       : 'program';
MAIN          : 'main';
VARIABLES     : 'var';
PERIOD        : '.';
SEMICOLON     : ';';
COLON         : ':';
COMMA         : ',';
LBRACKET      : '[';
RBRACKET      : ']';
LPRACKET      : '(';
RPRACKET      : ')';
LCRACKET      : '{';
RCRACKET      : '}';
ISFUNCTION    : '<-';
FUNC          : 'func';
ERROR         : 'error';
NULL          : 'null';
VOID          : 'void';
INT           : 'int';
FLOAT         : 'float';
CHAR          : 'char';
IF            : 'if';
ELSE          : 'else';
WHILE         : 'while';
READ          : 'read';
PRINT         : 'print';
EQUALS        : '=';
AND           : 'and';
OR            : 'or';
NOT           : 'not';
GREATERTHAN   : '>';
GREATEROR     : '>=';
LESSERTHAN    : '<';
LESSEROR      : '<=';
EQUAL         : 'equal';
PLUS          : '+';
MINUS         : '-';
TIMES         : '*';
DIVISION      : '/';
MODULE        : '%';
RETURN        : 'return';
RNOM          : 'rnom';
REXP          : 'rexp';
RGAMMA        : 'rgamma';
POINTS        : 'points';
LINES         : 'lines';
TEXT          : 'text';
BARPLOT       : 'barplot';
dotchart      : 'dotchart';
PIECHART      : 'piechart';
XYPLOT        : 'xyplot';
DENSITYPLOT   : 'densityplot';
HISTOGRAM     : 'histogram';
SIN           : 'sin';
COS           : 'cos';
TAN           : 'tan';
ASIN          : 'asin';
ACOS          : 'acos';
ATAN          : 'atan';
ATAN2         : 'atan2';
LOG           : 'log';
LOG10         : 'log10';
EXPONENT      : 'exp';
MAX           : 'f_max';
MIN           : 'f_min';
RANGE         : 'f_range';
SUM           : 'f_sum';
DIFF          : 'diff';
PROD          : 'prod';
MEAN          : 'mean';
MEDIAN        : 'median';
QUANTILE      : 'quantile';
WEIGHEDMEAN   : 'weighedmean';
RANK          : 'rank';
VARIANCE      : 'variance';
SD            : 'sd';
COR           : 'cor';
COV           : 'cov';
ROUND         : 'f_round';
TRANSPOSE     : 'transpose';
DIAGONAL      : 'diagonal';
GINV          : 'ginv';
ROWSUM        : 'rowsum';
COLSUM        : 'colsum';
LOAD          : 'load';
DATA          : 'data';
LIBRARY       : 'library';
RPOIS         : 'rpois';
RWEIBULL      : 'rweibull';
RBINOM        : 'rbinom';
RGEOM         : 'rgeom';
RUNIF         : 'runif';
PEARSON       : 'pearson';
KENDALL       : 'kendall';
SPEARMAN      : 'spearman';
STRING        : '"' .*? '"';
WHITESPACE    : ( ' ' | '\t' ) -> skip;
NEWLINE       : ( '\r'? '\n' | '\r' ) -> skip;
LINECOMMENT   : '#' ~[\r\n]* -> skip;
MULTICOMMENT  : '/#' .*? '#/' -> skip;
CTEI          : ( ( MINUS )? DIGIT+ );
CTEF          : ( ( MINUS )? CTEI ( PERIOD DIGIT+ )? );
ID            : ( LOWERCASE | UPPERCASE | DIGIT | '_' )+;
ZERO          : '0';
ONE           : '1';
