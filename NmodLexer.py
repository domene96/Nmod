# Generated from Nmod.g4 by ANTLR 4.7
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from Compiler import *
# from VirtualMachine import *
c = Compiler()
# vm = VirtualMachine()


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2l")
        buf.write("\u031f\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\4F\tF\4G\tG\4H\tH\4I\tI\4J\tJ\4K\tK\4L\t")
        buf.write("L\4M\tM\4N\tN\4O\tO\4P\tP\4Q\tQ\4R\tR\4S\tS\4T\tT\4U\t")
        buf.write("U\4V\tV\4W\tW\4X\tX\4Y\tY\4Z\tZ\4[\t[\4\\\t\\\4]\t]\4")
        buf.write("^\t^\4_\t_\4`\t`\4a\ta\4b\tb\4c\tc\4d\td\4e\te\4f\tf\4")
        buf.write("g\tg\4h\th\4i\ti\4j\tj\4k\tk\4l\tl\4m\tm\4n\tn\3\2\3\2")
        buf.write("\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\3\3\3\3\4\3\4\3\5\3\5\3")
        buf.write("\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\b")
        buf.write("\3\b\3\b\3\b\3\t\3\t\3\t\3\t\5\t\u0102\n\t\6\t\u0104\n")
        buf.write("\t\r\t\16\t\u0105\3\n\3\n\3\13\3\13\3\f\3\f\3\r\3\r\3")
        buf.write("\16\3\16\3\17\3\17\3\20\3\20\3\21\3\21\3\22\3\22\3\23")
        buf.write("\3\23\3\24\3\24\3\24\3\25\3\25\3\26\3\26\3\26\3\26\3\26")
        buf.write("\3\27\3\27\3\27\3\27\3\27\3\27\3\30\3\30\3\30\3\30\3\30")
        buf.write("\3\31\3\31\3\31\3\31\3\31\3\32\3\32\3\32\3\32\3\33\3\33")
        buf.write("\3\33\3\33\3\33\3\33\3\34\3\34\3\34\3\34\3\34\3\35\3\35")
        buf.write("\7\35\u0147\n\35\f\35\16\35\u014a\13\35\3\35\3\35\3\36")
        buf.write("\3\36\3\36\3\37\3\37\3\37\3\37\3\37\3 \3 \3 \3 \3 \3 ")
        buf.write("\3!\3!\3!\3!\3!\3\"\3\"\3\"\3\"\3\"\3\"\3#\3#\3$\3$\3")
        buf.write("%\3%\3&\3&\3\'\3\'\3\'\3(\3(\3)\3)\3)\3*\3*\3+\3+\3,\3")
        buf.write(",\3-\3-\3.\3.\3/\3/\3/\3/\3/\3\60\3\60\3\60\3\60\3\60")
        buf.write("\3\61\3\61\3\61\3\61\3\61\3\62\3\62\3\62\3\62\3\62\3\62")
        buf.write("\3\62\3\63\3\63\3\63\3\63\3\63\3\64\3\64\3\64\3\64\3\64")
        buf.write("\3\65\3\65\3\65\3\65\3\65\3\65\3\65\3\66\3\66\3\66\3\66")
        buf.write("\3\66\3\66\3\66\3\67\3\67\3\67\3\67\3\67\3\67\38\38\3")
        buf.write("8\38\38\39\39\39\39\39\39\39\39\3:\3:\3:\3:\3:\3:\3:\3")
        buf.write(":\3:\3;\3;\3;\3;\3;\3;\3;\3<\3<\3<\3<\3<\3<\3<\3<\3<\3")
        buf.write("<\3<\3<\3=\3=\3=\3=\3=\3=\3=\3=\3=\3=\3>\3>\3>\3>\3?\3")
        buf.write("?\3?\3?\3@\3@\3@\3@\3A\3A\3A\3A\3A\3B\3B\3B\3B\3B\3C\3")
        buf.write("C\3C\3C\3C\3D\3D\3D\3D\3D\3D\3E\3E\3E\3E\3F\3F\3F\3F\3")
        buf.write("F\3F\3G\3G\3G\3G\3H\3H\3H\3H\3H\3H\3I\3I\3I\3I\3I\3I\3")
        buf.write("J\3J\3J\3J\3J\3J\3J\3J\3K\3K\3K\3K\3K\3K\3L\3L\3L\3L\3")
        buf.write("L\3M\3M\3M\3M\3M\3N\3N\3N\3N\3N\3O\3O\3O\3O\3O\3O\3O\3")
        buf.write("P\3P\3P\3P\3P\3P\3P\3P\3P\3Q\3Q\3Q\3Q\3Q\3Q\3Q\3Q\3Q\3")
        buf.write("Q\3Q\3Q\3R\3R\3R\3R\3R\3S\3S\3S\3S\3S\3S\3S\3S\3S\3T\3")
        buf.write("T\3T\3U\3U\3U\3U\3V\3V\3V\3V\3W\3W\3W\3W\3W\3W\3W\3W\3")
        buf.write("X\3X\3X\3X\3X\3X\3X\3X\3X\3X\3Y\3Y\3Y\3Y\3Y\3Y\3Y\3Y\3")
        buf.write("Y\3Z\3Z\3Z\3Z\3Z\3[\3[\3[\3[\3[\3[\3[\3\\\3\\\3\\\3\\")
        buf.write("\3\\\3\\\3\\\3]\3]\3]\3]\3]\3^\3^\3^\3^\3^\3_\3_\3_\3")
        buf.write("_\3_\3_\3_\3_\3`\3`\3`\3`\3`\3`\3a\3a\3a\3a\3a\3a\3a\3")
        buf.write("a\3a\3b\3b\3b\3b\3b\3b\3b\3c\3c\3c\3c\3c\3c\3d\3d\3d\3")
        buf.write("d\3d\3d\3e\3e\3f\3f\3g\3g\3g\3g\3g\3g\3g\3g\3h\3h\3h\3")
        buf.write("h\3h\3h\3h\3h\3i\3i\3i\3i\3i\3i\3i\3i\3i\3j\3j\3j\3j\3")
        buf.write("k\5k\u02f9\nk\3k\3k\5k\u02fd\nk\3k\3k\3l\3l\7l\u0303\n")
        buf.write("l\fl\16l\u0306\13l\3l\3l\3m\3m\3m\3m\7m\u030e\nm\fm\16")
        buf.write("m\u0311\13m\3m\3m\3m\3m\3m\3n\3n\3n\3n\6n\u031c\nn\rn")
        buf.write("\16n\u031d\4\u0148\u030f\2o\3\3\5\2\7\2\t\2\13\4\r\5\17")
        buf.write("\6\21\7\23\b\25\t\27\n\31\13\33\f\35\r\37\16!\17#\20%")
        buf.write("\21\'\22)\23+\24-\25/\26\61\27\63\30\65\31\67\329\33;")
        buf.write("\34=\35?\36A\37C E!G\"I#K$M%O&Q\'S(U)W*Y+[,]-_.a/c\60")
        buf.write("e\61g\62i\63k\64m\65o\66q\67s8u9w:y;{<}=\177>\u0081?\u0083")
        buf.write("@\u0085A\u0087B\u0089C\u008bD\u008dE\u008fF\u0091G\u0093")
        buf.write("H\u0095I\u0097J\u0099K\u009bL\u009dM\u009fN\u00a1O\u00a3")
        buf.write("P\u00a5Q\u00a7R\u00a9S\u00abT\u00adU\u00afV\u00b1W\u00b3")
        buf.write("X\u00b5Y\u00b7Z\u00b9[\u00bb\\\u00bd]\u00bf^\u00c1_\u00c3")
        buf.write("`\u00c5a\u00c7b\u00c9c\u00cbd\u00cde\u00cff\u00d1g\u00d3")
        buf.write("h\u00d5i\u00d7j\u00d9k\u00dbl\3\2\7\3\2c|\3\2C\\\3\2\62")
        buf.write(";\4\2\13\13\"\"\4\2\f\f\17\17\2\u0326\2\3\3\2\2\2\2\13")
        buf.write("\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3")
        buf.write("\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2")
        buf.write("\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2")
        buf.write("%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2")
        buf.write("\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67")
        buf.write("\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2")
        buf.write("A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2")
        buf.write("\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2")
        buf.write("\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2")
        buf.write("\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3")
        buf.write("\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2q")
        buf.write("\3\2\2\2\2s\3\2\2\2\2u\3\2\2\2\2w\3\2\2\2\2y\3\2\2\2\2")
        buf.write("{\3\2\2\2\2}\3\2\2\2\2\177\3\2\2\2\2\u0081\3\2\2\2\2\u0083")
        buf.write("\3\2\2\2\2\u0085\3\2\2\2\2\u0087\3\2\2\2\2\u0089\3\2\2")
        buf.write("\2\2\u008b\3\2\2\2\2\u008d\3\2\2\2\2\u008f\3\2\2\2\2\u0091")
        buf.write("\3\2\2\2\2\u0093\3\2\2\2\2\u0095\3\2\2\2\2\u0097\3\2\2")
        buf.write("\2\2\u0099\3\2\2\2\2\u009b\3\2\2\2\2\u009d\3\2\2\2\2\u009f")
        buf.write("\3\2\2\2\2\u00a1\3\2\2\2\2\u00a3\3\2\2\2\2\u00a5\3\2\2")
        buf.write("\2\2\u00a7\3\2\2\2\2\u00a9\3\2\2\2\2\u00ab\3\2\2\2\2\u00ad")
        buf.write("\3\2\2\2\2\u00af\3\2\2\2\2\u00b1\3\2\2\2\2\u00b3\3\2\2")
        buf.write("\2\2\u00b5\3\2\2\2\2\u00b7\3\2\2\2\2\u00b9\3\2\2\2\2\u00bb")
        buf.write("\3\2\2\2\2\u00bd\3\2\2\2\2\u00bf\3\2\2\2\2\u00c1\3\2\2")
        buf.write("\2\2\u00c3\3\2\2\2\2\u00c5\3\2\2\2\2\u00c7\3\2\2\2\2\u00c9")
        buf.write("\3\2\2\2\2\u00cb\3\2\2\2\2\u00cd\3\2\2\2\2\u00cf\3\2\2")
        buf.write("\2\2\u00d1\3\2\2\2\2\u00d3\3\2\2\2\2\u00d5\3\2\2\2\2\u00d7")
        buf.write("\3\2\2\2\2\u00d9\3\2\2\2\2\u00db\3\2\2\2\3\u00dd\3\2\2")
        buf.write("\2\5\u00e6\3\2\2\2\7\u00e8\3\2\2\2\t\u00ea\3\2\2\2\13")
        buf.write("\u00ec\3\2\2\2\r\u00f4\3\2\2\2\17\u00f9\3\2\2\2\21\u0103")
        buf.write("\3\2\2\2\23\u0107\3\2\2\2\25\u0109\3\2\2\2\27\u010b\3")
        buf.write("\2\2\2\31\u010d\3\2\2\2\33\u010f\3\2\2\2\35\u0111\3\2")
        buf.write("\2\2\37\u0113\3\2\2\2!\u0115\3\2\2\2#\u0117\3\2\2\2%\u0119")
        buf.write("\3\2\2\2\'\u011b\3\2\2\2)\u011e\3\2\2\2+\u0120\3\2\2\2")
        buf.write("-\u0125\3\2\2\2/\u012b\3\2\2\2\61\u0130\3\2\2\2\63\u0135")
        buf.write("\3\2\2\2\65\u0139\3\2\2\2\67\u013f\3\2\2\29\u0144\3\2")
        buf.write("\2\2;\u014d\3\2\2\2=\u0150\3\2\2\2?\u0155\3\2\2\2A\u015b")
        buf.write("\3\2\2\2C\u0160\3\2\2\2E\u0166\3\2\2\2G\u0168\3\2\2\2")
        buf.write("I\u016a\3\2\2\2K\u016c\3\2\2\2M\u016e\3\2\2\2O\u0171\3")
        buf.write("\2\2\2Q\u0173\3\2\2\2S\u0176\3\2\2\2U\u0178\3\2\2\2W\u017a")
        buf.write("\3\2\2\2Y\u017c\3\2\2\2[\u017e\3\2\2\2]\u0180\3\2\2\2")
        buf.write("_\u0185\3\2\2\2a\u018a\3\2\2\2c\u018f\3\2\2\2e\u0196\3")
        buf.write("\2\2\2g\u019b\3\2\2\2i\u01a0\3\2\2\2k\u01a7\3\2\2\2m\u01ae")
        buf.write("\3\2\2\2o\u01b4\3\2\2\2q\u01b9\3\2\2\2s\u01c1\3\2\2\2")
        buf.write("u\u01ca\3\2\2\2w\u01d1\3\2\2\2y\u01dd\3\2\2\2{\u01e7\3")
        buf.write("\2\2\2}\u01eb\3\2\2\2\177\u01ef\3\2\2\2\u0081\u01f3\3")
        buf.write("\2\2\2\u0083\u01f8\3\2\2\2\u0085\u01fd\3\2\2\2\u0087\u0202")
        buf.write("\3\2\2\2\u0089\u0208\3\2\2\2\u008b\u020c\3\2\2\2\u008d")
        buf.write("\u0212\3\2\2\2\u008f\u0216\3\2\2\2\u0091\u021c\3\2\2\2")
        buf.write("\u0093\u0222\3\2\2\2\u0095\u022a\3\2\2\2\u0097\u0230\3")
        buf.write("\2\2\2\u0099\u0235\3\2\2\2\u009b\u023a\3\2\2\2\u009d\u023f")
        buf.write("\3\2\2\2\u009f\u0246\3\2\2\2\u00a1\u024f\3\2\2\2\u00a3")
        buf.write("\u025b\3\2\2\2\u00a5\u0260\3\2\2\2\u00a7\u0269\3\2\2\2")
        buf.write("\u00a9\u026c\3\2\2\2\u00ab\u0270\3\2\2\2\u00ad\u0274\3")
        buf.write("\2\2\2\u00af\u027c\3\2\2\2\u00b1\u0286\3\2\2\2\u00b3\u028f")
        buf.write("\3\2\2\2\u00b5\u0294\3\2\2\2\u00b7\u029b\3\2\2\2\u00b9")
        buf.write("\u02a2\3\2\2\2\u00bb\u02a7\3\2\2\2\u00bd\u02ac\3\2\2\2")
        buf.write("\u00bf\u02b4\3\2\2\2\u00c1\u02ba\3\2\2\2\u00c3\u02c3\3")
        buf.write("\2\2\2\u00c5\u02ca\3\2\2\2\u00c7\u02d0\3\2\2\2\u00c9\u02d6")
        buf.write("\3\2\2\2\u00cb\u02d8\3\2\2\2\u00cd\u02da\3\2\2\2\u00cf")
        buf.write("\u02e2\3\2\2\2\u00d1\u02ea\3\2\2\2\u00d3\u02f3\3\2\2\2")
        buf.write("\u00d5\u02fc\3\2\2\2\u00d7\u0300\3\2\2\2\u00d9\u0309\3")
        buf.write("\2\2\2\u00db\u031b\3\2\2\2\u00dd\u00de\7f\2\2\u00de\u00df")
        buf.write("\7q\2\2\u00df\u00e0\7v\2\2\u00e0\u00e1\7e\2\2\u00e1\u00e2")
        buf.write("\7j\2\2\u00e2\u00e3\7c\2\2\u00e3\u00e4\7t\2\2\u00e4\u00e5")
        buf.write("\7v\2\2\u00e5\4\3\2\2\2\u00e6\u00e7\t\2\2\2\u00e7\6\3")
        buf.write("\2\2\2\u00e8\u00e9\t\3\2\2\u00e9\b\3\2\2\2\u00ea\u00eb")
        buf.write("\t\4\2\2\u00eb\n\3\2\2\2\u00ec\u00ed\7r\2\2\u00ed\u00ee")
        buf.write("\7t\2\2\u00ee\u00ef\7q\2\2\u00ef\u00f0\7i\2\2\u00f0\u00f1")
        buf.write("\7t\2\2\u00f1\u00f2\7c\2\2\u00f2\u00f3\7o\2\2\u00f3\f")
        buf.write("\3\2\2\2\u00f4\u00f5\7o\2\2\u00f5\u00f6\7c\2\2\u00f6\u00f7")
        buf.write("\7k\2\2\u00f7\u00f8\7p\2\2\u00f8\16\3\2\2\2\u00f9\u00fa")
        buf.write("\7x\2\2\u00fa\u00fb\7c\2\2\u00fb\u00fc\7t\2\2\u00fc\20")
        buf.write("\3\2\2\2\u00fd\u0101\5\t\5\2\u00fe\u00ff\5\23\n\2\u00ff")
        buf.write("\u0100\5\t\5\2\u0100\u0102\3\2\2\2\u0101\u00fe\3\2\2\2")
        buf.write("\u0101\u0102\3\2\2\2\u0102\u0104\3\2\2\2\u0103\u00fd\3")
        buf.write("\2\2\2\u0104\u0105\3\2\2\2\u0105\u0103\3\2\2\2\u0105\u0106")
        buf.write("\3\2\2\2\u0106\22\3\2\2\2\u0107\u0108\7\60\2\2\u0108\24")
        buf.write("\3\2\2\2\u0109\u010a\7=\2\2\u010a\26\3\2\2\2\u010b\u010c")
        buf.write("\7<\2\2\u010c\30\3\2\2\2\u010d\u010e\7.\2\2\u010e\32\3")
        buf.write("\2\2\2\u010f\u0110\7]\2\2\u0110\34\3\2\2\2\u0111\u0112")
        buf.write("\7_\2\2\u0112\36\3\2\2\2\u0113\u0114\7*\2\2\u0114 \3\2")
        buf.write("\2\2\u0115\u0116\7+\2\2\u0116\"\3\2\2\2\u0117\u0118\7")
        buf.write("}\2\2\u0118$\3\2\2\2\u0119\u011a\7\177\2\2\u011a&\3\2")
        buf.write("\2\2\u011b\u011c\7>\2\2\u011c\u011d\7/\2\2\u011d(\3\2")
        buf.write("\2\2\u011e\u011f\7?\2\2\u011f*\3\2\2\2\u0120\u0121\7h")
        buf.write("\2\2\u0121\u0122\7w\2\2\u0122\u0123\7p\2\2\u0123\u0124")
        buf.write("\7e\2\2\u0124,\3\2\2\2\u0125\u0126\7g\2\2\u0126\u0127")
        buf.write("\7t\2\2\u0127\u0128\7t\2\2\u0128\u0129\7q\2\2\u0129\u012a")
        buf.write("\7t\2\2\u012a.\3\2\2\2\u012b\u012c\7p\2\2\u012c\u012d")
        buf.write("\7w\2\2\u012d\u012e\7n\2\2\u012e\u012f\7n\2\2\u012f\60")
        buf.write("\3\2\2\2\u0130\u0131\7x\2\2\u0131\u0132\7q\2\2\u0132\u0133")
        buf.write("\7k\2\2\u0133\u0134\7f\2\2\u0134\62\3\2\2\2\u0135\u0136")
        buf.write("\7k\2\2\u0136\u0137\7p\2\2\u0137\u0138\7v\2\2\u0138\64")
        buf.write("\3\2\2\2\u0139\u013a\7h\2\2\u013a\u013b\7n\2\2\u013b\u013c")
        buf.write("\7q\2\2\u013c\u013d\7c\2\2\u013d\u013e\7v\2\2\u013e\66")
        buf.write("\3\2\2\2\u013f\u0140\7e\2\2\u0140\u0141\7j\2\2\u0141\u0142")
        buf.write("\7c\2\2\u0142\u0143\7t\2\2\u01438\3\2\2\2\u0144\u0148")
        buf.write("\7$\2\2\u0145\u0147\13\2\2\2\u0146\u0145\3\2\2\2\u0147")
        buf.write("\u014a\3\2\2\2\u0148\u0149\3\2\2\2\u0148\u0146\3\2\2\2")
        buf.write("\u0149\u014b\3\2\2\2\u014a\u0148\3\2\2\2\u014b\u014c\7")
        buf.write("$\2\2\u014c:\3\2\2\2\u014d\u014e\7k\2\2\u014e\u014f\7")
        buf.write("h\2\2\u014f<\3\2\2\2\u0150\u0151\7g\2\2\u0151\u0152\7")
        buf.write("n\2\2\u0152\u0153\7u\2\2\u0153\u0154\7g\2\2\u0154>\3\2")
        buf.write("\2\2\u0155\u0156\7y\2\2\u0156\u0157\7j\2\2\u0157\u0158")
        buf.write("\7k\2\2\u0158\u0159\7n\2\2\u0159\u015a\7g\2\2\u015a@\3")
        buf.write("\2\2\2\u015b\u015c\7t\2\2\u015c\u015d\7g\2\2\u015d\u015e")
        buf.write("\7c\2\2\u015e\u015f\7f\2\2\u015fB\3\2\2\2\u0160\u0161")
        buf.write("\7r\2\2\u0161\u0162\7t\2\2\u0162\u0163\7k\2\2\u0163\u0164")
        buf.write("\7p\2\2\u0164\u0165\7v\2\2\u0165D\3\2\2\2\u0166\u0167")
        buf.write("\7(\2\2\u0167F\3\2\2\2\u0168\u0169\7~\2\2\u0169H\3\2\2")
        buf.write("\2\u016a\u016b\7#\2\2\u016bJ\3\2\2\2\u016c\u016d\7@\2")
        buf.write("\2\u016dL\3\2\2\2\u016e\u016f\7@\2\2\u016f\u0170\7?\2")
        buf.write("\2\u0170N\3\2\2\2\u0171\u0172\7>\2\2\u0172P\3\2\2\2\u0173")
        buf.write("\u0174\7>\2\2\u0174\u0175\7?\2\2\u0175R\3\2\2\2\u0176")
        buf.write("\u0177\7-\2\2\u0177T\3\2\2\2\u0178\u0179\7/\2\2\u0179")
        buf.write("V\3\2\2\2\u017a\u017b\7,\2\2\u017bX\3\2\2\2\u017c\u017d")
        buf.write("\7\61\2\2\u017dZ\3\2\2\2\u017e\u017f\7\'\2\2\u017f\\\3")
        buf.write("\2\2\2\u0180\u0181\7e\2\2\u0181\u0182\7v\2\2\u0182\u0183")
        buf.write("\7g\2\2\u0183\u0184\7k\2\2\u0184^\3\2\2\2\u0185\u0186")
        buf.write("\7e\2\2\u0186\u0187\7v\2\2\u0187\u0188\7g\2\2\u0188\u0189")
        buf.write("\7h\2\2\u0189`\3\2\2\2\u018a\u018b\7e\2\2\u018b\u018c")
        buf.write("\7v\2\2\u018c\u018d\7g\2\2\u018d\u018e\7e\2\2\u018eb\3")
        buf.write("\2\2\2\u018f\u0190\7t\2\2\u0190\u0191\7g\2\2\u0191\u0192")
        buf.write("\7v\2\2\u0192\u0193\7w\2\2\u0193\u0194\7t\2\2\u0194\u0195")
        buf.write("\7p\2\2\u0195d\3\2\2\2\u0196\u0197\7t\2\2\u0197\u0198")
        buf.write("\7p\2\2\u0198\u0199\7q\2\2\u0199\u019a\7o\2\2\u019af\3")
        buf.write("\2\2\2\u019b\u019c\7t\2\2\u019c\u019d\7g\2\2\u019d\u019e")
        buf.write("\7z\2\2\u019e\u019f\7r\2\2\u019fh\3\2\2\2\u01a0\u01a1")
        buf.write("\7t\2\2\u01a1\u01a2\7i\2\2\u01a2\u01a3\7c\2\2\u01a3\u01a4")
        buf.write("\7o\2\2\u01a4\u01a5\7o\2\2\u01a5\u01a6\7c\2\2\u01a6j\3")
        buf.write("\2\2\2\u01a7\u01a8\7r\2\2\u01a8\u01a9\7q\2\2\u01a9\u01aa")
        buf.write("\7k\2\2\u01aa\u01ab\7p\2\2\u01ab\u01ac\7v\2\2\u01ac\u01ad")
        buf.write("\7u\2\2\u01adl\3\2\2\2\u01ae\u01af\7n\2\2\u01af\u01b0")
        buf.write("\7k\2\2\u01b0\u01b1\7p\2\2\u01b1\u01b2\7g\2\2\u01b2\u01b3")
        buf.write("\7u\2\2\u01b3n\3\2\2\2\u01b4\u01b5\7v\2\2\u01b5\u01b6")
        buf.write("\7g\2\2\u01b6\u01b7\7z\2\2\u01b7\u01b8\7v\2\2\u01b8p\3")
        buf.write("\2\2\2\u01b9\u01ba\7d\2\2\u01ba\u01bb\7c\2\2\u01bb\u01bc")
        buf.write("\7t\2\2\u01bc\u01bd\7r\2\2\u01bd\u01be\7n\2\2\u01be\u01bf")
        buf.write("\7q\2\2\u01bf\u01c0\7v\2\2\u01c0r\3\2\2\2\u01c1\u01c2")
        buf.write("\7r\2\2\u01c2\u01c3\7k\2\2\u01c3\u01c4\7g\2\2\u01c4\u01c5")
        buf.write("\7e\2\2\u01c5\u01c6\7j\2\2\u01c6\u01c7\7c\2\2\u01c7\u01c8")
        buf.write("\7t\2\2\u01c8\u01c9\7v\2\2\u01c9t\3\2\2\2\u01ca\u01cb")
        buf.write("\7z\2\2\u01cb\u01cc\7{\2\2\u01cc\u01cd\7r\2\2\u01cd\u01ce")
        buf.write("\7n\2\2\u01ce\u01cf\7q\2\2\u01cf\u01d0\7v\2\2\u01d0v\3")
        buf.write("\2\2\2\u01d1\u01d2\7f\2\2\u01d2\u01d3\7g\2\2\u01d3\u01d4")
        buf.write("\7p\2\2\u01d4\u01d5\7u\2\2\u01d5\u01d6\7k\2\2\u01d6\u01d7")
        buf.write("\7v\2\2\u01d7\u01d8\7{\2\2\u01d8\u01d9\7r\2\2\u01d9\u01da")
        buf.write("\7n\2\2\u01da\u01db\7q\2\2\u01db\u01dc\7v\2\2\u01dcx\3")
        buf.write("\2\2\2\u01dd\u01de\7j\2\2\u01de\u01df\7k\2\2\u01df\u01e0")
        buf.write("\7u\2\2\u01e0\u01e1\7v\2\2\u01e1\u01e2\7q\2\2\u01e2\u01e3")
        buf.write("\7i\2\2\u01e3\u01e4\7t\2\2\u01e4\u01e5\7c\2\2\u01e5\u01e6")
        buf.write("\7o\2\2\u01e6z\3\2\2\2\u01e7\u01e8\7u\2\2\u01e8\u01e9")
        buf.write("\7k\2\2\u01e9\u01ea\7p\2\2\u01ea|\3\2\2\2\u01eb\u01ec")
        buf.write("\7e\2\2\u01ec\u01ed\7q\2\2\u01ed\u01ee\7u\2\2\u01ee~\3")
        buf.write("\2\2\2\u01ef\u01f0\7v\2\2\u01f0\u01f1\7c\2\2\u01f1\u01f2")
        buf.write("\7p\2\2\u01f2\u0080\3\2\2\2\u01f3\u01f4\7c\2\2\u01f4\u01f5")
        buf.write("\7u\2\2\u01f5\u01f6\7k\2\2\u01f6\u01f7\7p\2\2\u01f7\u0082")
        buf.write("\3\2\2\2\u01f8\u01f9\7c\2\2\u01f9\u01fa\7e\2\2\u01fa\u01fb")
        buf.write("\7q\2\2\u01fb\u01fc\7u\2\2\u01fc\u0084\3\2\2\2\u01fd\u01fe")
        buf.write("\7c\2\2\u01fe\u01ff\7v\2\2\u01ff\u0200\7c\2\2\u0200\u0201")
        buf.write("\7p\2\2\u0201\u0086\3\2\2\2\u0202\u0203\7c\2\2\u0203\u0204")
        buf.write("\7v\2\2\u0204\u0205\7c\2\2\u0205\u0206\7p\2\2\u0206\u0207")
        buf.write("\7\64\2\2\u0207\u0088\3\2\2\2\u0208\u0209\7n\2\2\u0209")
        buf.write("\u020a\7q\2\2\u020a\u020b\7i\2\2\u020b\u008a\3\2\2\2\u020c")
        buf.write("\u020d\7n\2\2\u020d\u020e\7q\2\2\u020e\u020f\7i\2\2\u020f")
        buf.write("\u0210\7\63\2\2\u0210\u0211\7\62\2\2\u0211\u008c\3\2\2")
        buf.write("\2\u0212\u0213\7g\2\2\u0213\u0214\7z\2\2\u0214\u0215\7")
        buf.write("r\2\2\u0215\u008e\3\2\2\2\u0216\u0217\7h\2\2\u0217\u0218")
        buf.write("\7a\2\2\u0218\u0219\7o\2\2\u0219\u021a\7c\2\2\u021a\u021b")
        buf.write("\7z\2\2\u021b\u0090\3\2\2\2\u021c\u021d\7h\2\2\u021d\u021e")
        buf.write("\7a\2\2\u021e\u021f\7o\2\2\u021f\u0220\7k\2\2\u0220\u0221")
        buf.write("\7p\2\2\u0221\u0092\3\2\2\2\u0222\u0223\7h\2\2\u0223\u0224")
        buf.write("\7a\2\2\u0224\u0225\7t\2\2\u0225\u0226\7c\2\2\u0226\u0227")
        buf.write("\7p\2\2\u0227\u0228\7i\2\2\u0228\u0229\7g\2\2\u0229\u0094")
        buf.write("\3\2\2\2\u022a\u022b\7h\2\2\u022b\u022c\7a\2\2\u022c\u022d")
        buf.write("\7u\2\2\u022d\u022e\7w\2\2\u022e\u022f\7o\2\2\u022f\u0096")
        buf.write("\3\2\2\2\u0230\u0231\7f\2\2\u0231\u0232\7k\2\2\u0232\u0233")
        buf.write("\7h\2\2\u0233\u0234\7h\2\2\u0234\u0098\3\2\2\2\u0235\u0236")
        buf.write("\7r\2\2\u0236\u0237\7t\2\2\u0237\u0238\7q\2\2\u0238\u0239")
        buf.write("\7f\2\2\u0239\u009a\3\2\2\2\u023a\u023b\7o\2\2\u023b\u023c")
        buf.write("\7g\2\2\u023c\u023d\7c\2\2\u023d\u023e\7p\2\2\u023e\u009c")
        buf.write("\3\2\2\2\u023f\u0240\7o\2\2\u0240\u0241\7g\2\2\u0241\u0242")
        buf.write("\7f\2\2\u0242\u0243\7k\2\2\u0243\u0244\7c\2\2\u0244\u0245")
        buf.write("\7p\2\2\u0245\u009e\3\2\2\2\u0246\u0247\7s\2\2\u0247\u0248")
        buf.write("\7w\2\2\u0248\u0249\7c\2\2\u0249\u024a\7p\2\2\u024a\u024b")
        buf.write("\7v\2\2\u024b\u024c\7k\2\2\u024c\u024d\7n\2\2\u024d\u024e")
        buf.write("\7g\2\2\u024e\u00a0\3\2\2\2\u024f\u0250\7y\2\2\u0250\u0251")
        buf.write("\7g\2\2\u0251\u0252\7k\2\2\u0252\u0253\7i\2\2\u0253\u0254")
        buf.write("\7j\2\2\u0254\u0255\7g\2\2\u0255\u0256\7f\2\2\u0256\u0257")
        buf.write("\7o\2\2\u0257\u0258\7g\2\2\u0258\u0259\7c\2\2\u0259\u025a")
        buf.write("\7p\2\2\u025a\u00a2\3\2\2\2\u025b\u025c\7t\2\2\u025c\u025d")
        buf.write("\7c\2\2\u025d\u025e\7p\2\2\u025e\u025f\7m\2\2\u025f\u00a4")
        buf.write("\3\2\2\2\u0260\u0261\7x\2\2\u0261\u0262\7c\2\2\u0262\u0263")
        buf.write("\7t\2\2\u0263\u0264\7k\2\2\u0264\u0265\7c\2\2\u0265\u0266")
        buf.write("\7p\2\2\u0266\u0267\7e\2\2\u0267\u0268\7g\2\2\u0268\u00a6")
        buf.write("\3\2\2\2\u0269\u026a\7u\2\2\u026a\u026b\7f\2\2\u026b\u00a8")
        buf.write("\3\2\2\2\u026c\u026d\7e\2\2\u026d\u026e\7q\2\2\u026e\u026f")
        buf.write("\7t\2\2\u026f\u00aa\3\2\2\2\u0270\u0271\7e\2\2\u0271\u0272")
        buf.write("\7q\2\2\u0272\u0273\7x\2\2\u0273\u00ac\3\2\2\2\u0274\u0275")
        buf.write("\7h\2\2\u0275\u0276\7a\2\2\u0276\u0277\7t\2\2\u0277\u0278")
        buf.write("\7q\2\2\u0278\u0279\7w\2\2\u0279\u027a\7p\2\2\u027a\u027b")
        buf.write("\7f\2\2\u027b\u00ae\3\2\2\2\u027c\u027d\7v\2\2\u027d\u027e")
        buf.write("\7t\2\2\u027e\u027f\7c\2\2\u027f\u0280\7p\2\2\u0280\u0281")
        buf.write("\7u\2\2\u0281\u0282\7r\2\2\u0282\u0283\7q\2\2\u0283\u0284")
        buf.write("\7u\2\2\u0284\u0285\7g\2\2\u0285\u00b0\3\2\2\2\u0286\u0287")
        buf.write("\7f\2\2\u0287\u0288\7k\2\2\u0288\u0289\7c\2\2\u0289\u028a")
        buf.write("\7i\2\2\u028a\u028b\7q\2\2\u028b\u028c\7p\2\2\u028c\u028d")
        buf.write("\7c\2\2\u028d\u028e\7n\2\2\u028e\u00b2\3\2\2\2\u028f\u0290")
        buf.write("\7i\2\2\u0290\u0291\7k\2\2\u0291\u0292\7p\2\2\u0292\u0293")
        buf.write("\7x\2\2\u0293\u00b4\3\2\2\2\u0294\u0295\7t\2\2\u0295\u0296")
        buf.write("\7q\2\2\u0296\u0297\7y\2\2\u0297\u0298\7u\2\2\u0298\u0299")
        buf.write("\7w\2\2\u0299\u029a\7o\2\2\u029a\u00b6\3\2\2\2\u029b\u029c")
        buf.write("\7e\2\2\u029c\u029d\7q\2\2\u029d\u029e\7n\2\2\u029e\u029f")
        buf.write("\7u\2\2\u029f\u02a0\7w\2\2\u02a0\u02a1\7o\2\2\u02a1\u00b8")
        buf.write("\3\2\2\2\u02a2\u02a3\7n\2\2\u02a3\u02a4\7q\2\2\u02a4\u02a5")
        buf.write("\7c\2\2\u02a5\u02a6\7f\2\2\u02a6\u00ba\3\2\2\2\u02a7\u02a8")
        buf.write("\7f\2\2\u02a8\u02a9\7c\2\2\u02a9\u02aa\7v\2\2\u02aa\u02ab")
        buf.write("\7c\2\2\u02ab\u00bc\3\2\2\2\u02ac\u02ad\7n\2\2\u02ad\u02ae")
        buf.write("\7k\2\2\u02ae\u02af\7d\2\2\u02af\u02b0\7t\2\2\u02b0\u02b1")
        buf.write("\7c\2\2\u02b1\u02b2\7t\2\2\u02b2\u02b3\7{\2\2\u02b3\u00be")
        buf.write("\3\2\2\2\u02b4\u02b5\7t\2\2\u02b5\u02b6\7r\2\2\u02b6\u02b7")
        buf.write("\7q\2\2\u02b7\u02b8\7k\2\2\u02b8\u02b9\7u\2\2\u02b9\u00c0")
        buf.write("\3\2\2\2\u02ba\u02bb\7t\2\2\u02bb\u02bc\7y\2\2\u02bc\u02bd")
        buf.write("\7g\2\2\u02bd\u02be\7k\2\2\u02be\u02bf\7d\2\2\u02bf\u02c0")
        buf.write("\7w\2\2\u02c0\u02c1\7n\2\2\u02c1\u02c2\7n\2\2\u02c2\u00c2")
        buf.write("\3\2\2\2\u02c3\u02c4\7t\2\2\u02c4\u02c5\7d\2\2\u02c5\u02c6")
        buf.write("\7k\2\2\u02c6\u02c7\7p\2\2\u02c7\u02c8\7q\2\2\u02c8\u02c9")
        buf.write("\7o\2\2\u02c9\u00c4\3\2\2\2\u02ca\u02cb\7t\2\2\u02cb\u02cc")
        buf.write("\7i\2\2\u02cc\u02cd\7g\2\2\u02cd\u02ce\7q\2\2\u02ce\u02cf")
        buf.write("\7o\2\2\u02cf\u00c6\3\2\2\2\u02d0\u02d1\7t\2\2\u02d1\u02d2")
        buf.write("\7w\2\2\u02d2\u02d3\7p\2\2\u02d3\u02d4\7k\2\2\u02d4\u02d5")
        buf.write("\7h\2\2\u02d5\u00c8\3\2\2\2\u02d6\u02d7\7\62\2\2\u02d7")
        buf.write("\u00ca\3\2\2\2\u02d8\u02d9\7\63\2\2\u02d9\u00cc\3\2\2")
        buf.write("\2\u02da\u02db\7r\2\2\u02db\u02dc\7g\2\2\u02dc\u02dd\7")
        buf.write("c\2\2\u02dd\u02de\7t\2\2\u02de\u02df\7u\2\2\u02df\u02e0")
        buf.write("\7q\2\2\u02e0\u02e1\7p\2\2\u02e1\u00ce\3\2\2\2\u02e2\u02e3")
        buf.write("\7m\2\2\u02e3\u02e4\7g\2\2\u02e4\u02e5\7p\2\2\u02e5\u02e6")
        buf.write("\7f\2\2\u02e6\u02e7\7c\2\2\u02e7\u02e8\7n\2\2\u02e8\u02e9")
        buf.write("\7n\2\2\u02e9\u00d0\3\2\2\2\u02ea\u02eb\7u\2\2\u02eb\u02ec")
        buf.write("\7r\2\2\u02ec\u02ed\7g\2\2\u02ed\u02ee\7c\2\2\u02ee\u02ef")
        buf.write("\7t\2\2\u02ef\u02f0\7o\2\2\u02f0\u02f1\7c\2\2\u02f1\u02f2")
        buf.write("\7p\2\2\u02f2\u00d2\3\2\2\2\u02f3\u02f4\t\5\2\2\u02f4")
        buf.write("\u02f5\3\2\2\2\u02f5\u02f6\bj\2\2\u02f6\u00d4\3\2\2\2")
        buf.write("\u02f7\u02f9\7\17\2\2\u02f8\u02f7\3\2\2\2\u02f8\u02f9")
        buf.write("\3\2\2\2\u02f9\u02fa\3\2\2\2\u02fa\u02fd\7\f\2\2\u02fb")
        buf.write("\u02fd\7\17\2\2\u02fc\u02f8\3\2\2\2\u02fc\u02fb\3\2\2")
        buf.write("\2\u02fd\u02fe\3\2\2\2\u02fe\u02ff\bk\2\2\u02ff\u00d6")
        buf.write("\3\2\2\2\u0300\u0304\7%\2\2\u0301\u0303\n\6\2\2\u0302")
        buf.write("\u0301\3\2\2\2\u0303\u0306\3\2\2\2\u0304\u0302\3\2\2\2")
        buf.write("\u0304\u0305\3\2\2\2\u0305\u0307\3\2\2\2\u0306\u0304\3")
        buf.write("\2\2\2\u0307\u0308\bl\2\2\u0308\u00d8\3\2\2\2\u0309\u030a")
        buf.write("\7\61\2\2\u030a\u030b\7%\2\2\u030b\u030f\3\2\2\2\u030c")
        buf.write("\u030e\13\2\2\2\u030d\u030c\3\2\2\2\u030e\u0311\3\2\2")
        buf.write("\2\u030f\u0310\3\2\2\2\u030f\u030d\3\2\2\2\u0310\u0312")
        buf.write("\3\2\2\2\u0311\u030f\3\2\2\2\u0312\u0313\7%\2\2\u0313")
        buf.write("\u0314\7\61\2\2\u0314\u0315\3\2\2\2\u0315\u0316\bm\2\2")
        buf.write("\u0316\u00da\3\2\2\2\u0317\u031c\5\7\4\2\u0318\u031c\5")
        buf.write("\5\3\2\u0319\u031c\5\t\5\2\u031a\u031c\7a\2\2\u031b\u0317")
        buf.write("\3\2\2\2\u031b\u0318\3\2\2\2\u031b\u0319\3\2\2\2\u031b")
        buf.write("\u031a\3\2\2\2\u031c\u031d\3\2\2\2\u031d\u031b\3\2\2\2")
        buf.write("\u031d\u031e\3\2\2\2\u031e\u00dc\3\2\2\2\f\2\u0101\u0105")
        buf.write("\u0148\u02f8\u02fc\u0304\u030f\u031b\u031d\3\b\2\2")
        return buf.getvalue()


class NmodLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    PROGRAM = 2
    MAIN = 3
    VARIABLES = 4
    NUMBER = 5
    PERIOD = 6
    SEMICOLON = 7
    COLON = 8
    COMMA = 9
    LBRACKET = 10
    RBRACKET = 11
    LPRACKET = 12
    RPRACKET = 13
    LCRACKET = 14
    RCRACKET = 15
    ISFUNCTION = 16
    EQUALS = 17
    FUNC = 18
    ERROR = 19
    NULL = 20
    VOID = 21
    INT = 22
    FLOAT = 23
    CHAR = 24
    STRING = 25
    IF = 26
    ELSE = 27
    WHILE = 28
    READ = 29
    PRINT = 30
    AND = 31
    OR = 32
    NOT = 33
    GREATERTHAN = 34
    GREATEROR = 35
    LESSERTHAN = 36
    LESSEROR = 37
    PLUS = 38
    MINUS = 39
    TIMES = 40
    DIVISION = 41
    MODULE = 42
    CTEI = 43
    CTEF = 44
    CTEC = 45
    RETURN = 46
    RNOM = 47
    REXP = 48
    RGAMMA = 49
    POINTS = 50
    LINES = 51
    TEXT = 52
    BARPLOT = 53
    PIECHART = 54
    XYPLOT = 55
    DENSITYPLOT = 56
    HISTOGRAM = 57
    SIN = 58
    COS = 59
    TAN = 60
    ASIN = 61
    ACOS = 62
    ATAN = 63
    ATAN2 = 64
    LOG = 65
    LOG10 = 66
    EXPONENT = 67
    MAX = 68
    MIN = 69
    RANGE = 70
    SUM = 71
    DIFF = 72
    PROD = 73
    MEAN = 74
    MEDIAN = 75
    QUANTILE = 76
    WEIGHEDMEAN = 77
    RANK = 78
    VARIANCE = 79
    SD = 80
    COR = 81
    COV = 82
    ROUND = 83
    TRANSPOSE = 84
    DIAGONAL = 85
    GINV = 86
    ROWSUM = 87
    COLSUM = 88
    LOAD = 89
    DATA = 90
    LIBRARY = 91
    RPOIS = 92
    RWEIBULL = 93
    RBINOM = 94
    RGEOM = 95
    RUNIF = 96
    ZERO = 97
    ONE = 98
    PEARSON = 99
    KENDALL = 100
    SPEARMAN = 101
    WHITESPACE = 102
    NEWLINE = 103
    LINECOMMENT = 104
    MULTICOMMENT = 105
    ID = 106

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'dotchart'", "'program'", "'main'", "'var'", "'.'", "';'", 
            "':'", "','", "'['", "']'", "'('", "')'", "'{'", "'}'", "'<-'", 
            "'='", "'func'", "'error'", "'null'", "'void'", "'int'", "'float'", 
            "'char'", "'if'", "'else'", "'while'", "'read'", "'print'", 
            "'&'", "'|'", "'!'", "'>'", "'>='", "'<'", "'<='", "'+'", "'-'", 
            "'*'", "'/'", "'%'", "'ctei'", "'ctef'", "'ctec'", "'return'", 
            "'rnom'", "'rexp'", "'rgamma'", "'points'", "'lines'", "'text'", 
            "'barplot'", "'piechart'", "'xyplot'", "'densityplot'", "'histogram'", 
            "'sin'", "'cos'", "'tan'", "'asin'", "'acos'", "'atan'", "'atan2'", 
            "'log'", "'log10'", "'exp'", "'f_max'", "'f_min'", "'f_range'", 
            "'f_sum'", "'diff'", "'prod'", "'mean'", "'median'", "'quantile'", 
            "'weighedmean'", "'rank'", "'variance'", "'sd'", "'cor'", "'cov'", 
            "'f_round'", "'transpose'", "'diagonal'", "'ginv'", "'rowsum'", 
            "'colsum'", "'load'", "'data'", "'library'", "'rpois'", "'rweibull'", 
            "'rbinom'", "'rgeom'", "'runif'", "'0'", "'1'", "'pearson'", 
            "'kendall'", "'spearman'" ]

    symbolicNames = [ "<INVALID>",
            "PROGRAM", "MAIN", "VARIABLES", "NUMBER", "PERIOD", "SEMICOLON", 
            "COLON", "COMMA", "LBRACKET", "RBRACKET", "LPRACKET", "RPRACKET", 
            "LCRACKET", "RCRACKET", "ISFUNCTION", "EQUALS", "FUNC", "ERROR", 
            "NULL", "VOID", "INT", "FLOAT", "CHAR", "STRING", "IF", "ELSE", 
            "WHILE", "READ", "PRINT", "AND", "OR", "NOT", "GREATERTHAN", 
            "GREATEROR", "LESSERTHAN", "LESSEROR", "PLUS", "MINUS", "TIMES", 
            "DIVISION", "MODULE", "CTEI", "CTEF", "CTEC", "RETURN", "RNOM", 
            "REXP", "RGAMMA", "POINTS", "LINES", "TEXT", "BARPLOT", "PIECHART", 
            "XYPLOT", "DENSITYPLOT", "HISTOGRAM", "SIN", "COS", "TAN", "ASIN", 
            "ACOS", "ATAN", "ATAN2", "LOG", "LOG10", "EXPONENT", "MAX", 
            "MIN", "RANGE", "SUM", "DIFF", "PROD", "MEAN", "MEDIAN", "QUANTILE", 
            "WEIGHEDMEAN", "RANK", "VARIANCE", "SD", "COR", "COV", "ROUND", 
            "TRANSPOSE", "DIAGONAL", "GINV", "ROWSUM", "COLSUM", "LOAD", 
            "DATA", "LIBRARY", "RPOIS", "RWEIBULL", "RBINOM", "RGEOM", "RUNIF", 
            "ZERO", "ONE", "PEARSON", "KENDALL", "SPEARMAN", "WHITESPACE", 
            "NEWLINE", "LINECOMMENT", "MULTICOMMENT", "ID" ]

    ruleNames = [ "T__0", "LOWERCASE", "UPPERCASE", "DIGIT", "PROGRAM", 
                  "MAIN", "VARIABLES", "NUMBER", "PERIOD", "SEMICOLON", 
                  "COLON", "COMMA", "LBRACKET", "RBRACKET", "LPRACKET", 
                  "RPRACKET", "LCRACKET", "RCRACKET", "ISFUNCTION", "EQUALS", 
                  "FUNC", "ERROR", "NULL", "VOID", "INT", "FLOAT", "CHAR", 
                  "STRING", "IF", "ELSE", "WHILE", "READ", "PRINT", "AND", 
                  "OR", "NOT", "GREATERTHAN", "GREATEROR", "LESSERTHAN", 
                  "LESSEROR", "PLUS", "MINUS", "TIMES", "DIVISION", "MODULE", 
                  "CTEI", "CTEF", "CTEC", "RETURN", "RNOM", "REXP", "RGAMMA", 
                  "POINTS", "LINES", "TEXT", "BARPLOT", "PIECHART", "XYPLOT", 
                  "DENSITYPLOT", "HISTOGRAM", "SIN", "COS", "TAN", "ASIN", 
                  "ACOS", "ATAN", "ATAN2", "LOG", "LOG10", "EXPONENT", "MAX", 
                  "MIN", "RANGE", "SUM", "DIFF", "PROD", "MEAN", "MEDIAN", 
                  "QUANTILE", "WEIGHEDMEAN", "RANK", "VARIANCE", "SD", "COR", 
                  "COV", "ROUND", "TRANSPOSE", "DIAGONAL", "GINV", "ROWSUM", 
                  "COLSUM", "LOAD", "DATA", "LIBRARY", "RPOIS", "RWEIBULL", 
                  "RBINOM", "RGEOM", "RUNIF", "ZERO", "ONE", "PEARSON", 
                  "KENDALL", "SPEARMAN", "WHITESPACE", "NEWLINE", "LINECOMMENT", 
                  "MULTICOMMENT", "ID" ]

    grammarFileName = "Nmod.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


