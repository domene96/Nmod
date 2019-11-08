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
  ( PROGRAM ID {c.insertFunctionDirectory($ID.text,"void")} COLON ( variables )* ( modules )* main );
f_type:
  ( INT | FLOAT | CHAR );
variables:
  ( VARIABLES f_id {c.storeVariable($f_id.text)} ( COMMA f_id {c.storeVariable($f_id.text)} )* COLON f_type SEMICOLON {c.declareVariables(c.getStoredVariables(),$f_type.text)} );
f_id:
  ( ID ( LBRACKET expression RBRACKET )? );
modules:
  ( ID {c.storeVariable($ID.text)} ISFUNCTION ( VOID | f_type ) FUNC {c.declareModule($ID.text)} LPRACKET ( parameter {c.storeParameter($parameter.text)} ( COMMA parameter {c.storeParameter($parameter.text)} )* )? {c.validateParameters()} RPRACKET block );
main:
  ( MAIN LPRACKET RPRACKET block );
block:
  ( LCRACKET ( statute )* RCRACKET );
parameter:
  ( f_type var_cte );
statute:
  ( assignment
  | condition
  | reading
  | writing
  | cicle
  | call_module );
assignment:
  ( f_id {c.insertStackOperand($f_id.text)} EQUALS {c.insertStackOperator($EQUALS.text)} expression {c.validateExpression()} SEMICOLON {c.generateAssignmentQuadruples()} );
condition:
  ( IF LPRACKET expression {c.validateExpression(), c.insertStackJump(quadPlace), c.generateGotoFQuadruples()} RPRACKET block ( ELSE {c.popStackJump(), c.generateGotoQuadruples()} block )? {c.popStackJump()} );
cicle:
  ( WHILE LPRACKET expression {c.validateExpression(), c.insertStackJump(quadPlace), c.generateGotoFQuadruples()} RPRACKET block {c.popStackJump(), c.generateGotoQuadruples(), c.popStackJump()} );
reading:
  ( READ {c.insertFunctionDirectory(READ,VOID)} LPRACKET ( expression ( COMMA expression )* )? RPRACKET SEMICOLON );
writing:
  ( PRINT {c.insertFunctionDirectory(PRINT,VOID)} LPRACKET ( expression {c.validateExpression()} ( COMMA expression )* )? RPRACKET SEMICOLON );
call_module:
  ( r_return | rnom | rexp | rgamma | points | lines | text | barplot | piechart | xyplot | densityplot | histogram | sin | cos | tan | asin | acos | atan | atan2 | log | log10 | exponent | f_max | f_min | f_range | f_sum | diff | prod | mean | median | quantile | weighedmean | rank | var | sd | cor | cov | f_round | transpose | diagonal | ginv | rowsum | colsum | load | data | library | rpois | rweibull | rbinom | rgeom | runif | ( ID {c.procedureExists(ID)} LPRACKET {c.generateERA()} ( expression {c.validateExpression()} ( COMMA {c.raiseParamCounter()} expression {c.validateExpression()} )* )? RPRACKET {c.generateGoSub()} ) );
expression:
  ( sub_exp {c.validateSubExp(), c.topStackOperatorLogical()} ( ( AND AND | OR OR )+ {c.insertStackOperator()} sub_exp+ {c.validateSubExp()} )? );
sub_exp:
  ( exp {c.validateExp(), c.topStackOperatorComparative()} ( ( EQUALS EQUALS | GREATEROR | GREATERTHAN | LESSEROR | LESSERTHAN )+ {c.insertStackOperator()} exp+ {c.validateExp()})? );
exp:
  ( term {c.validateTerm(), c.topStackOperatorTerms()} ( ( MINUS | PLUS )+ term+ {c.validateTerm()} )? );
term:
  ( factor {c.validateFactor(), c.topStackOperatorFactors()} ( ( DIVISION | TIMES )+ factor+ {c.validateFactor()} )? );
factor:
  ( LPRACKET expression RPRACKET
  | ( PLUS | MINUS )? var_cte {c.insertStackType(), c.popStackOperand()} );
var_cte:
  ( f_id | NUMBER | STRING | CTEI | CTEF | CTEC | call_module );
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
  ( TEXT LPRACKET CTEI COMMA CTEI COMMA f_id RPRACKET SEMICOLON );
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
  ( DIFF LPRACKET f_id COMMA CTEI RPRACKET SEMICOLON );
prod:
  ( PROD LPRACKET expression ( COMMA expression )* RPRACKET SEMICOLON );
mean:
  ( MEAN LPRACKET f_id RPRACKET SEMICOLON );
median:
  ( MEDIAN LPRACKET f_id RPRACKET SEMICOLON );
quantile:
  ( QUANTILE LPRACKET expression ( COMMA expression )* RPRACKET SEMICOLON );
weighedmean:
  ( WEIGHEDMEAN LPRACKET expression ( COMMA expression )* RPRACKET SEMICOLON );
rank:
  ( RANK LPRACKET f_id COMMA ZERO RPRACKET SEMICOLON
  | RANK LPRACKET f_id COMMA ONE RPRACKET SEMICOLON );
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
  ( LIBRARY LPRACKET var_cte RPRACKET SEMICOLON );
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
  NUMBER        : ( DIGIT ( PERIOD DIGIT )? )+;
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
  EQUALS        : '=';
  FUNC          : 'func';
  ERROR         : 'error';
  NULL          : 'null';
  VOID          : 'void';
  INT           : 'int';
  FLOAT         : 'float';
  CHAR          : 'char';
  STRING        : '"' .*? '"';
  IF            : 'if';
  ELSE          : 'else';
  WHILE         : 'while';
  READ          : 'read';
  PRINT         : 'print';
  AND           : '&';
  OR            : '|';
  NOT           : '!';
  GREATERTHAN   : '>';
  GREATEROR     : '>=';
  LESSERTHAN    : '<';
  LESSEROR      : '<=';
  PLUS          : '+';
  MINUS         : '-';
  TIMES         : '*';
  DIVISION      : '/';
  MODULE        : '%';
  CTEI          : 'ctei';
  CTEF          : 'ctef';
  CTEC          : 'ctec';
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
  ZERO          : '0';
  ONE           : '1';
  PEARSON       : 'pearson';
  KENDALL       : 'kendall';
  SPEARMAN      : 'spearman';
  WHITESPACE    : ( ' ' | '\t' ) -> skip;
  NEWLINE       : ( '\r'? '\n' | '\r' ) -> skip;
  LINECOMMENT   : '#' ~[\r\n]* -> skip;
  MULTICOMMENT  : '/#' .*? '#/' -> skip;
  ID            : ( UPPERCASE | LOWERCASE | DIGIT | '_' )+;
