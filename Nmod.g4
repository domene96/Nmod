// Define a grammar called Nmod
grammar Nmod;

@header {
from Compiler import *
c = Compiler()
}

// Parser rules

program:
  ( {c.initialGoto()} PROGRAM ID {c.localFunc = 'global'} {c.insertFunctionDirectory(c.localFunc, 'void')} COLON ( variables )* ( modules )* main );
f_type
  returns[Object type]:
  ( INT {$type = $INT.text}
  | FLOAT {$type = $FLOAT.text}
  | CHAR {$type = $CHAR.text} );
variables:
  ( VARIABLES f_type {c.localType = $f_type.text} COLON id_decl {c.insertVarTable(c.localFunc, $id_decl.text, c.localType)} ( COMMA id_decl {c.insertVarTable(c.localFunc, $id_decl.text, c.localType)} )* );
id_decl:
  ( ID ( LBRACKET {c.initDimVar()} CTEI {c.insertConstant('int', $CTEI.text)} {c.setDimLowBound($CTEI.text)} COLON CTEI {c.insertConstant('int', $CTEI.text)} {c.setDimHighBound($CTEI.text)} ( COMMA {c.addDimension()} CTEI {c.insertConstant('int', $CTEI.text)} {c.setDimLowBound($CTEI.text)} COLON CTEI {c.insertConstant('int', $CTEI.text)} {c.setDimHighBound($CTEI.text)} )* RBRACKET {c.calculateK()} )? );
id_access:
  ( ID {c.insertStackOperand($ID.text)} {c.insertStackType(c.getVarType(c.localFunc, $ID.text))} ( LBRACKET {c.dimVarBegin()} exp {c.generateDimVarQuad($ID.text)} ( COMMA {c.nextDimension($ID.text)} exp {c.generateDimVarQuad($ID.text)} )* RBRACKET {c.dimVarEnd($ID.text)} )? );
modules:
  ( ID {c.localFunc = $ID.text} ISFUNCTION ( VOID {c.localType = 'void'} {c.insertFunctionDirectory($ID.text, 'void')} | f_type {c.localType = $f_type.text} {c.insertFunctionDirectory($ID.text, $f_type.text)} {c.insertVarTable('global', $ID.text, $f_type.text)} ) FUNC LPRACKET ( f_type {c.localType = $f_type.text} ID {c.insertVarTable(c.localFunc, $ID.text, $f_type.text)} {c.insertParam(c.localFunc, $ID.text, $f_type.text)} ( COMMA f_type {c.localType = $f_type.text} ID {c.insertVarTable(c.localFunc, $ID.text, $f_type.text)} {c.insertParam(c.localFunc, $ID.text, $f_type.text)} )* )? RPRACKET ( variables )* {c.moduleBegin()} block {c.moduleEnd()} );
main:
  ( MAIN {c.localFunc = 'global'} {c.mainBegin()} LPRACKET RPRACKET block {c.mainEnd()} );
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
  ( id_access EQUALS {c.insertStackOperator($EQUALS.text)} exp {c.generateAssignmentQuad()} );
condition:
  ( IF LPRACKET expression RPRACKET {c.conditionStart('condition')} block ( ELSE {c.conditionElse()} block )? {c.conditionEnd()} );
cicle:
  ( WHILE {c.insertStackJump(c.quadCount)} LPRACKET expression RPRACKET {c.conditionStart('cicle')} block {c.cicleEnd()} );
reading:
  ( READ LPRACKET ( STRING {c.insertConstant('char', $STRING.text)} {c.insertStackOperand($STRING.text)} {c.insertStackType('char')} | expression ( COMMA expression )* )? RPRACKET {c.generateCommonQuad('read')} );
writing:
  ( PRINT LPRACKET ( STRING {c.insertConstant('char', $STRING.text)} {c.insertStackOperand($STRING.text)} {c.insertStackType('char')} ( COMMA STRING {c.insertConstant('char', $STRING.text)} {c.insertStackOperand($STRING.text)} {c.insertStackType('char')} )* | expression ( COMMA expression )* )? RPRACKET {c.generateCommonQuad('print')} );
call_module
  returns[Object type, val]:
  ( ID {c.generateERA($ID.text)} {c.functionDirectory.functionExists($ID.text)} {c.localFunc = $ID.text} {$val = c.getModuleReturnAddr($ID.text)} {$type = c.getModuleReturnType($ID.text)} LPRACKET {c.insertFalseBottom()} ( exp {c.generateActionParameter()} ( COMMA {c.moveParameterPointer()} exp {c.generateActionParameter()} )* )? RPRACKET {c.removeFalseBottom()} {c.resetParameterPointer()} | special_function );
special_function:
  ( r_return | rnom | rexp | rgamma | points | lines | text | barplot | piechart | xyplot | densityplot | histogram | sin | cos | tan | asin | acos | atan | atan2 | log | log10 | exponent | f_max | f_min | f_range | f_sum | diff | prod | mean | median | quantile | rank | var | sd | cor | cov | f_round | transpose | diagonal | ginv | rowsum | colsum | load | data | library | rpois | rweibull | rbinom | rgeom | runif );
expression:
  ( sub_exp {c.generateQuad(c.localFunc, 'sub_exp')} ( ( AND {c.insertStackOperator($AND.text)} | OR {c.insertStackOperator($OR.text)} ) sub_exp {c.generateQuad(c.localFunc, 'sub_exp')} )* );
sub_exp:
  ( exp {c.generateQuad(c.localFunc, 'exp')} ( ( EQUAL {c.insertStackOperator($EQUAL.text)} | GREATEROR {c.insertStackOperator($GREATEROR.text)} | GREATERTHAN {c.insertStackOperator($GREATERTHAN.text)} | LESSEROR {c.insertStackOperator($LESSEROR.text)} | LESSERTHAN {c.insertStackOperator($LESSERTHAN.text)} ) exp {c.generateQuad(c.localFunc, 'exp')} )* );
exp:
  ( term {c.generateQuad(c.localFunc, 'term')} ( ( MINUS {c.insertStackOperator($MINUS.text)} | PLUS {c.insertStackOperator($PLUS.text)} ) term {c.generateQuad(c.localFunc, 'term')} )* );
term:
  ( factor {c.generateQuad(c.localFunc, 'factor')} ( ( DIVISION {c.insertStackOperator($DIVISION.text)} | TIMES {c.insertStackOperator($TIMES.text)} ) factor {c.generateQuad(c.localFunc, 'factor')} )* );
factor:
  ( LPRACKET {c.insertFalseBottom()} expression RPRACKET {c.removeFalseBottom()}
  | ( PLUS | MINUS )? var_cte );
var_cte
  returns[Object type, val]:
  ( call_module {$type = $call_module.type} {$val = $call_module.val}
  | id_access {$type = c.getVarType(c.localFunc, $id_access.text)} {$val = c.getVarVal(c.localFunc, $id_access.text)}
  | CTEI {$type = 'int'} {$val = c.insertConstant($type, $CTEI.text)} {c.insertStackOperand($CTEI.text)} {c.insertStackType($type)}
  | CTEF {$type = 'float'} {$val = c.insertConstant($type, $CTEF.text)} {c.insertStackOperand($CTEF.text)} {c.insertStackType($type)}
  | CTEC {$type = 'char'} {$val = c.insertConstant($type, $CTEC.text)} {c.insertStackOperand($CTEC.text)} {c.insertStackType($type)} );
r_return:
  ( RETURN expression {c.generateReturn()} );
rnom
  returns[Object type, val]:
  ( RNOM {c.generateSpecialERA($RNOM.text)} LPRACKET {c.insertFalseBottom()} exp {c.generateSpecialActionParam($RNOM.text)} ( COMMA {c.moveParameterPointer()} exp {c.generateSpecialActionParam($RNOM.text)} )* RPRACKET {c.removeFalseBottom()} {c.resetParameterPointerSpecialFunction($RNOM.text)} );
rexp:
  ( REXP {c.generateSpecialERA($REXP.text)} LPRACKET {c.insertFalseBottom()} exp {c.generateSpecialActionParam($REXP.text)} ( COMMA {c.moveParameterPointer()} exp {c.generateSpecialActionParam($REXP.text)} )* RPRACKET {c.removeFalseBottom()} {c.resetParameterPointerSpecialFunction($REXP.text)} );
rgamma:
  ( RGAMMA {c.generateSpecialERA($RGAMMA.text)} LPRACKET {c.insertFalseBottom()} exp {c.generateSpecialActionParam($RGAMMA.text)} ( COMMA {c.moveParameterPointer()} exp {c.generateSpecialActionParam($RGAMMA.text)} )* RPRACKET {c.removeFalseBottom()} {c.resetParameterPointerSpecialFunction($RGAMMA.text)} );
points:
  ( POINTS {c.generateSpecialERA($POINTS.text)} LPRACKET {c.insertFalseBottom()} exp {c.generateSpecialActionParam($POINTS.text)} ( COMMA {c.moveParameterPointer()} exp {c.generateSpecialActionParam($POINTS.text)} )* RPRACKET {c.removeFalseBottom()} {c.resetParameterPointerSpecialFunction($POINTS.text)} );
lines:
  ( LINES {c.generateSpecialERA($LINES.text)} LPRACKET {c.insertFalseBottom()} exp {c.generateSpecialActionParam($LINES.text)} ( COMMA {c.moveParameterPointer()} exp {c.generateSpecialActionParam($LINES.text)} )* RPRACKET {c.removeFalseBottom()} {c.resetParameterPointerSpecialFunction($LINES.text)} );
text:
  ( TEXT {c.generateSpecialERA($TEXT.text)} LPRACKET {c.insertFalseBottom()} CTEI {c.insertConstant('int', $CTEI.text)} {c.generateSpecialActionParam($TEXT.text)} COMMA {c.moveParameterPointer()} CTEI {c.insertConstant('int', $CTEI.text)} {c.generateSpecialActionParam($TEXT.text)} COMMA {c.moveParameterPointer()} id_access RPRACKET {c.removeFalseBottom()} {c.resetParameterPointerSpecialFunction($TEXT.text)} );
barplot:
  ( BARPLOT {c.generateSpecialERA($BARPLOT.text)} LPRACKET {c.insertFalseBottom()} exp {c.generateSpecialActionParam($BARPLOT.text)} ( COMMA {c.moveParameterPointer()} exp {c.generateSpecialActionParam($BARPLOT.text)} )* RPRACKET {c.removeFalseBottom()} {c.resetParameterPointerSpecialFunction($BARPLOT.text)} );
dotchart:
  ( DOTCHART {c.generateSpecialERA($DOTCHART.text)} LPRACKET {c.insertFalseBottom()} exp {c.generateSpecialActionParam($DOTCHART.text)} ( COMMA {c.moveParameterPointer()} exp {c.generateSpecialActionParam($DOTCHART.text)} )* RPRACKET {c.removeFalseBottom()} {c.resetParameterPointerSpecialFunction($DOTCHART.text)} );
piechart:
  ( PIECHART {c.generateSpecialERA($PIECHART.text)} LPRACKET {c.insertFalseBottom()} exp {c.generateSpecialActionParam($PIECHART.text)} ( COMMA {c.moveParameterPointer()} exp {c.generateSpecialActionParam($PIECHART.text)} )* RPRACKET {c.removeFalseBottom()} {c.resetParameterPointerSpecialFunction($PIECHART.text)} );
xyplot:
  ( XYPLOT {c.generateSpecialERA($XYPLOT.text)} LPRACKET {c.insertFalseBottom()} exp {c.generateSpecialActionParam($XYPLOT.text)} ( COMMA {c.moveParameterPointer()} exp {c.generateSpecialActionParam($XYPLOT.text)} )* RPRACKET {c.removeFalseBottom()} {c.resetParameterPointerSpecialFunction($XYPLOT.text)} );
densityplot:
  ( DENSITYPLOT {c.generateSpecialERA($DENSITYPLOT.text)} LPRACKET {c.insertFalseBottom()} exp {c.generateSpecialActionParam($DENSITYPLOT.text)} ( COMMA {c.moveParameterPointer()} exp {c.generateSpecialActionParam($DENSITYPLOT.text)} )* RPRACKET {c.removeFalseBottom()} {c.resetParameterPointerSpecialFunction($DENSITYPLOT.text)} );
histogram:
  ( HISTOGRAM {c.generateSpecialERA($HISTOGRAM.text)} LPRACKET {c.insertFalseBottom()} exp {c.generateSpecialActionParam($HISTOGRAM.text)} ( COMMA {c.moveParameterPointer()} exp {c.generateSpecialActionParam($HISTOGRAM.text)} )* RPRACKET {c.removeFalseBottom()} {c.resetParameterPointerSpecialFunction($HISTOGRAM.text)} );
sin:
  ( SIN LPRACKET exp RPRACKET );
cos:
  ( COS LPRACKET exp RPRACKET );
tan:
  ( TAN LPRACKET exp RPRACKET );
asin:
  ( ASIN LPRACKET exp RPRACKET );
acos:
  ( ACOS LPRACKET exp RPRACKET );
atan:
  ( ATAN LPRACKET exp RPRACKET );
atan2:
  ( ATAN2 LPRACKET exp RPRACKET );
log:
  ( LOG LPRACKET exp RPRACKET );
log10:
  ( LOG10 LPRACKET exp RPRACKET );
exponent:
  ( EXPONENT LPRACKET exp RPRACKET );
f_max:
  ( MAX {c.generateSpecialERA($MAX.text)} LPRACKET {c.insertFalseBottom()} exp {c.generateSpecialActionParam($MAX.text)} ( COMMA {c.moveParameterPointer()} exp {c.generateSpecialActionParam($MAX.text)} )* RPRACKET {c.removeFalseBottom()} {c.resetParameterPointerSpecialFunction($MAX.text)} );
f_min:
  ( MIN {c.generateSpecialERA($MIN.text)} LPRACKET {c.insertFalseBottom()} exp {c.generateSpecialActionParam($MIN.text)} ( COMMA {c.moveParameterPointer()} exp {c.generateSpecialActionParam($MIN.text)} )* RPRACKET {c.removeFalseBottom()} {c.resetParameterPointerSpecialFunction($MIN.text)} );
f_range:
  ( RANGE {c.generateSpecialERA($RANGE.text)} LPRACKET {c.insertFalseBottom()} exp {c.generateSpecialActionParam($RANGE.text)} ( COMMA {c.moveParameterPointer()} exp {c.generateSpecialActionParam($RANGE.text)} )* RPRACKET {c.removeFalseBottom()} {c.resetParameterPointerSpecialFunction($RANGE.text)} );
f_sum:
  ( SUM {c.generateSpecialERA($SUM.text)} LPRACKET {c.insertFalseBottom()} exp {c.generateSpecialActionParam($SUM.text)} ( COMMA {c.moveParameterPointer()} exp {c.generateSpecialActionParam($SUM.text)} )* RPRACKET {c.removeFalseBottom()} {c.resetParameterPointerSpecialFunction($SUM.text)} );
diff:
  ( DIFF LPRACKET exp COMMA CTEI RPRACKET );
prod:
  ( PROD {c.generateSpecialERA($PROD.text)} LPRACKET {c.insertFalseBottom()} exp {c.generateSpecialActionParam($PROD.text)} ( COMMA {c.moveParameterPointer()} exp {c.generateSpecialActionParam($PROD.text)} )* RPRACKET {c.removeFalseBottom()} {c.resetParameterPointerSpecialFunction($PROD.text)} );
mean:
  ( MEAN LPRACKET exp RPRACKET );
median:
  ( MEDIAN LPRACKET exp RPRACKET );
quantile:
  ( QUANTILE {c.generateSpecialERA($QUANTILE.text)} LPRACKET {c.insertFalseBottom()} exp {c.generateSpecialActionParam($QUANTILE.text)} ( COMMA {c.moveParameterPointer()} exp {c.generateSpecialActionParam($QUANTILE.text)} )* RPRACKET {c.removeFalseBottom()} {c.resetParameterPointerSpecialFunction($QUANTILE.text)} );
rank:
  ( RANK LPRACKET exp COMMA ZERO RPRACKET
  | RANK LPRACKET exp COMMA ONE RPRACKET );
var:
  ( VARIANCE {c.generateSpecialERA($VARIANCE.text)} LPRACKET {c.insertFalseBottom()} exp {c.generateSpecialActionParam($VARIANCE.text)} ( COMMA {c.moveParameterPointer()} exp {c.generateSpecialActionParam($VARIANCE.text)} )* RPRACKET {c.removeFalseBottom()} {c.resetParameterPointerSpecialFunction($VARIANCE.text)} );
sd:
  ( SD {c.generateSpecialERA($SD.text)} LPRACKET {c.insertFalseBottom()} exp {c.generateSpecialActionParam($SD.text)} ( COMMA {c.moveParameterPointer()} exp {c.generateSpecialActionParam($SD.text)} )* RPRACKET {c.removeFalseBottom()} {c.resetParameterPointerSpecialFunction($SD.text)} );
cor:
  ( COR LPRACKET ( PEARSON | KENDALL | SPEARMAN ) RPRACKET );
cov:
  ( COV {c.generateSpecialERA($COV.text)} LPRACKET {c.insertFalseBottom()} exp {c.generateSpecialActionParam($COV.text)} ( COMMA {c.moveParameterPointer()} exp {c.generateSpecialActionParam($COV.text)} )* RPRACKET {c.removeFalseBottom()} {c.resetParameterPointerSpecialFunction($COV.text)} );
f_round:
  ( ROUND {c.generateSpecialERA($ROUND.text)} LPRACKET {c.insertFalseBottom()} exp {c.generateSpecialActionParam($ROUND.text)} ( COMMA {c.moveParameterPointer()} exp {c.generateSpecialActionParam($ROUND.text)} )* RPRACKET {c.removeFalseBottom()} {c.resetParameterPointerSpecialFunction($ROUND.text)} );
transpose:
  ( TRANSPOSE {c.generateSpecialERA($TRANSPOSE.text)} LPRACKET {c.insertFalseBottom()} exp {c.generateSpecialActionParam($TRANSPOSE.text)} ( COMMA {c.moveParameterPointer()} exp {c.generateSpecialActionParam($TRANSPOSE.text)} )* RPRACKET {c.removeFalseBottom()} {c.resetParameterPointerSpecialFunction($TRANSPOSE.text)} );
diagonal:
  ( DIAGONAL {c.generateSpecialERA($DIAGONAL.text)} LPRACKET {c.insertFalseBottom()} exp {c.generateSpecialActionParam($DIAGONAL.text)} ( COMMA {c.moveParameterPointer()} exp {c.generateSpecialActionParam($DIAGONAL.text)} )* RPRACKET {c.removeFalseBottom()} {c.resetParameterPointerSpecialFunction($DIAGONAL.text)} );
ginv:
  ( GINV {c.generateSpecialERA($GINV.text)} LPRACKET {c.insertFalseBottom()} exp {c.generateSpecialActionParam($GINV.text)} ( COMMA {c.moveParameterPointer()} exp {c.generateSpecialActionParam($GINV.text)} )* RPRACKET {c.removeFalseBottom()} {c.resetParameterPointerSpecialFunction($GINV.text)} );
rowsum:
  ( ROWSUM {c.generateSpecialERA($ROWSUM.text)} LPRACKET {c.insertFalseBottom()} exp {c.generateSpecialActionParam($ROWSUM.text)} ( COMMA {c.moveParameterPointer()} exp {c.generateSpecialActionParam($ROWSUM.text)} )* RPRACKET {c.removeFalseBottom()} {c.resetParameterPointerSpecialFunction($ROWSUM.text)} );
colsum:
  ( COLSUM {c.generateSpecialERA($COLSUM.text)} LPRACKET {c.insertFalseBottom()} exp {c.generateSpecialActionParam($COLSUM.text)} ( COMMA {c.moveParameterPointer()} exp {c.generateSpecialActionParam($COLSUM.text)} )* RPRACKET {c.removeFalseBottom()} {c.resetParameterPointerSpecialFunction($COLSUM.text)} );
load:
  ( LOAD {c.generateSpecialERA($LOAD.text)} LPRACKET {c.insertFalseBottom()} exp {c.generateSpecialActionParam($LOAD.text)} ( COMMA {c.moveParameterPointer()} exp {c.generateSpecialActionParam($LOAD.text)} )* RPRACKET {c.removeFalseBottom()} {c.resetParameterPointerSpecialFunction($LOAD.text)} );
data:
  ( DATA {c.generateSpecialERA($DATA.text)} LPRACKET {c.insertFalseBottom()} exp {c.generateSpecialActionParam($DATA.text)} ( COMMA {c.moveParameterPointer()} exp {c.generateSpecialActionParam($DATA.text)} )* RPRACKET {c.removeFalseBottom()} {c.resetParameterPointerSpecialFunction($DATA.text)} );
library:
  ( LIBRARY LPRACKET ( STRING | id_access ) RPRACKET );
rpois:
  ( RPOIS {c.generateSpecialERA($RPOIS.text)} LPRACKET {c.insertFalseBottom()} exp {c.generateSpecialActionParam($RPOIS.text)} ( COMMA {c.moveParameterPointer()} exp {c.generateSpecialActionParam($RPOIS.text)} )* RPRACKET {c.removeFalseBottom()} {c.resetParameterPointerSpecialFunction($RPOIS.text)} );
rweibull:
  ( RWEIBULL {c.generateSpecialERA($RWEIBULL.text)} LPRACKET {c.insertFalseBottom()} exp {c.generateSpecialActionParam($RWEIBULL.text)} ( COMMA {c.moveParameterPointer()} exp {c.generateSpecialActionParam($RWEIBULL.text)} )* RPRACKET {c.removeFalseBottom()} {c.resetParameterPointerSpecialFunction($RWEIBULL.text)} );
rbinom:
  ( RBINOM {c.generateSpecialERA($RBINOM.text)} LPRACKET {c.insertFalseBottom()} exp {c.generateSpecialActionParam($RBINOM.text)} ( COMMA {c.moveParameterPointer()} exp {c.generateSpecialActionParam($RBINOM.text)} )* RPRACKET {c.removeFalseBottom()} {c.resetParameterPointerSpecialFunction($RBINOM.text)} );
rgeom:
  ( RGEOM {c.generateSpecialERA($RGEOM.text)} LPRACKET {c.insertFalseBottom()} exp {c.generateSpecialActionParam($RGEOM.text)} ( COMMA {c.moveParameterPointer()} exp {c.generateSpecialActionParam($RGEOM.text)} )* RPRACKET {c.removeFalseBottom()} {c.resetParameterPointerSpecialFunction($RGEOM.text)} );
runif:
  ( RUNIF {c.generateSpecialERA($RUNIF.text)} LPRACKET {c.insertFalseBottom()} exp {c.generateSpecialActionParam($RUNIF.text)} ( COMMA {c.moveParameterPointer()} exp {c.generateSpecialActionParam($RUNIF.text)} )* RPRACKET {c.removeFalseBottom()} {c.resetParameterPointerSpecialFunction($RUNIF.text)} );

// Lexer rules

fragment LOWERCASE: [a-z];
fragment UPPERCASE: [A-Z];
fragment DIGIT: [0-9];
PROGRAM       : 'nmod';
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
DOTCHART      : 'dotchart';
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
WHITESPACE    : ( ' ' | '\t' ) -> skip;
NEWLINE       : ( '\r'? '\n' | '\r' ) -> skip;
LINECOMMENT   : '#' ~[\r\n]* -> skip;
MULTICOMMENT  : '/#' .*? '#/' -> skip;
CTEI          : ( ( MINUS )? DIGIT+ );
CTEF          : ( ( MINUS )? CTEI ( PERIOD DIGIT+ )? );
CTEC          : '\'' .? '\'';
STRING        : '"' .*? '"';
ID            : ( LOWERCASE | UPPERCASE | DIGIT | '_' )+;
ZERO          : '0';
ONE           : '1';
