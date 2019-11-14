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
        buf.write("\u032b\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
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
        buf.write("\3\b\3\b\3\b\3\t\3\t\3\n\3\n\3\13\3\13\3\f\3\f\3\r\3\r")
        buf.write("\3\16\3\16\3\17\3\17\3\20\3\20\3\21\3\21\3\22\3\22\3\23")
        buf.write("\3\23\3\23\3\24\3\24\3\24\3\24\3\24\3\25\3\25\3\25\3\25")
        buf.write("\3\25\3\25\3\26\3\26\3\26\3\26\3\26\3\27\3\27\3\27\3\27")
        buf.write("\3\27\3\30\3\30\3\30\3\30\3\31\3\31\3\31\3\31\3\31\3\31")
        buf.write("\3\32\3\32\3\32\3\32\3\32\3\33\3\33\3\33\3\34\3\34\3\34")
        buf.write("\3\34\3\34\3\35\3\35\3\35\3\35\3\35\3\35\3\36\3\36\3\36")
        buf.write("\3\36\3\36\3\37\3\37\3\37\3\37\3\37\3\37\3 \3 \3!\3!\3")
        buf.write("!\3!\3\"\3\"\3\"\3#\3#\3#\3#\3$\3$\3%\3%\3%\3&\3&\3\'")
        buf.write("\3\'\3\'\3(\3(\3(\3(\3(\3(\3)\3)\3*\3*\3+\3+\3,\3,\3-")
        buf.write("\3-\3.\3.\3.\3.\3.\3.\3.\3/\3/\3/\3/\3/\3\60\3\60\3\60")
        buf.write("\3\60\3\60\3\61\3\61\3\61\3\61\3\61\3\61\3\61\3\62\3\62")
        buf.write("\3\62\3\62\3\62\3\62\3\62\3\63\3\63\3\63\3\63\3\63\3\63")
        buf.write("\3\64\3\64\3\64\3\64\3\64\3\65\3\65\3\65\3\65\3\65\3\65")
        buf.write("\3\65\3\65\3\66\3\66\3\66\3\66\3\66\3\66\3\66\3\66\3\66")
        buf.write("\3\67\3\67\3\67\3\67\3\67\3\67\3\67\38\38\38\38\38\38")
        buf.write("\38\38\38\38\38\38\39\39\39\39\39\39\39\39\39\39\3:\3")
        buf.write(":\3:\3:\3;\3;\3;\3;\3<\3<\3<\3<\3=\3=\3=\3=\3=\3>\3>\3")
        buf.write(">\3>\3>\3?\3?\3?\3?\3?\3@\3@\3@\3@\3@\3@\3A\3A\3A\3A\3")
        buf.write("B\3B\3B\3B\3B\3B\3C\3C\3C\3C\3D\3D\3D\3D\3D\3D\3E\3E\3")
        buf.write("E\3E\3E\3E\3F\3F\3F\3F\3F\3F\3F\3F\3G\3G\3G\3G\3G\3G\3")
        buf.write("H\3H\3H\3H\3H\3I\3I\3I\3I\3I\3J\3J\3J\3J\3J\3K\3K\3K\3")
        buf.write("K\3K\3K\3K\3L\3L\3L\3L\3L\3L\3L\3L\3L\3M\3M\3M\3M\3M\3")
        buf.write("M\3M\3M\3M\3M\3M\3M\3N\3N\3N\3N\3N\3O\3O\3O\3O\3O\3O\3")
        buf.write("O\3O\3O\3P\3P\3P\3Q\3Q\3Q\3Q\3R\3R\3R\3R\3S\3S\3S\3S\3")
        buf.write("S\3S\3S\3S\3T\3T\3T\3T\3T\3T\3T\3T\3T\3T\3U\3U\3U\3U\3")
        buf.write("U\3U\3U\3U\3U\3V\3V\3V\3V\3V\3W\3W\3W\3W\3W\3W\3W\3X\3")
        buf.write("X\3X\3X\3X\3X\3X\3Y\3Y\3Y\3Y\3Y\3Z\3Z\3Z\3Z\3Z\3[\3[\3")
        buf.write("[\3[\3[\3[\3[\3[\3\\\3\\\3\\\3\\\3\\\3\\\3]\3]\3]\3]\3")
        buf.write("]\3]\3]\3]\3]\3^\3^\3^\3^\3^\3^\3^\3_\3_\3_\3_\3_\3_\3")
        buf.write("`\3`\3`\3`\3`\3`\3a\3a\3a\3a\3a\3a\3a\3a\3b\3b\3b\3b\3")
        buf.write("b\3b\3b\3b\3c\3c\3c\3c\3c\3c\3c\3c\3c\3d\3d\3d\3d\3e\5")
        buf.write("e\u02de\ne\3e\3e\5e\u02e2\ne\3e\3e\3f\3f\7f\u02e8\nf\f")
        buf.write("f\16f\u02eb\13f\3f\3f\3g\3g\3g\3g\7g\u02f3\ng\fg\16g\u02f6")
        buf.write("\13g\3g\3g\3g\3g\3g\3h\5h\u02fe\nh\3h\6h\u0301\nh\rh\16")
        buf.write("h\u0302\3i\5i\u0306\ni\3i\3i\3i\6i\u030b\ni\ri\16i\u030c")
        buf.write("\5i\u030f\ni\3j\3j\5j\u0313\nj\3j\3j\3k\3k\7k\u0319\n")
        buf.write("k\fk\16k\u031c\13k\3k\3k\3l\3l\3l\3l\6l\u0324\nl\rl\16")
        buf.write("l\u0325\3m\3m\3n\3n\4\u02f4\u031a\2o\3\3\5\2\7\2\t\2\13")
        buf.write("\4\r\5\17\6\21\7\23\b\25\t\27\n\31\13\33\f\35\r\37\16")
        buf.write("!\17#\20%\21\'\22)\23+\24-\25/\26\61\27\63\30\65\31\67")
        buf.write("\329\33;\34=\35?\36A\37C E!G\"I#K$M%O&Q\'S(U)W*Y+[,]-")
        buf.write("_.a/c\60e\61g\62i\63k\64m\65o\66q\67s8u9w:y;{<}=\177>")
        buf.write("\u0081?\u0083@\u0085A\u0087B\u0089C\u008bD\u008dE\u008f")
        buf.write("F\u0091G\u0093H\u0095I\u0097J\u0099K\u009bL\u009dM\u009f")
        buf.write("N\u00a1O\u00a3P\u00a5Q\u00a7R\u00a9S\u00abT\u00adU\u00af")
        buf.write("V\u00b1W\u00b3X\u00b5Y\u00b7Z\u00b9[\u00bb\\\u00bd]\u00bf")
        buf.write("^\u00c1_\u00c3`\u00c5a\u00c7b\u00c9c\u00cbd\u00cde\u00cf")
        buf.write("f\u00d1g\u00d3h\u00d5i\u00d7j\u00d9k\u00dbl\3\2\7\3\2")
        buf.write("c|\3\2C\\\3\2\62;\4\2\13\13\"\"\4\2\f\f\17\17\2\u0336")
        buf.write("\2\3\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21")
        buf.write("\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3")
        buf.write("\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2")
        buf.write("\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2")
        buf.write("\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2")
        buf.write("\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2")
        buf.write("\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3")
        buf.write("\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q")
        buf.write("\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2")
        buf.write("[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2")
        buf.write("\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2m\3\2\2")
        buf.write("\2\2o\3\2\2\2\2q\3\2\2\2\2s\3\2\2\2\2u\3\2\2\2\2w\3\2")
        buf.write("\2\2\2y\3\2\2\2\2{\3\2\2\2\2}\3\2\2\2\2\177\3\2\2\2\2")
        buf.write("\u0081\3\2\2\2\2\u0083\3\2\2\2\2\u0085\3\2\2\2\2\u0087")
        buf.write("\3\2\2\2\2\u0089\3\2\2\2\2\u008b\3\2\2\2\2\u008d\3\2\2")
        buf.write("\2\2\u008f\3\2\2\2\2\u0091\3\2\2\2\2\u0093\3\2\2\2\2\u0095")
        buf.write("\3\2\2\2\2\u0097\3\2\2\2\2\u0099\3\2\2\2\2\u009b\3\2\2")
        buf.write("\2\2\u009d\3\2\2\2\2\u009f\3\2\2\2\2\u00a1\3\2\2\2\2\u00a3")
        buf.write("\3\2\2\2\2\u00a5\3\2\2\2\2\u00a7\3\2\2\2\2\u00a9\3\2\2")
        buf.write("\2\2\u00ab\3\2\2\2\2\u00ad\3\2\2\2\2\u00af\3\2\2\2\2\u00b1")
        buf.write("\3\2\2\2\2\u00b3\3\2\2\2\2\u00b5\3\2\2\2\2\u00b7\3\2\2")
        buf.write("\2\2\u00b9\3\2\2\2\2\u00bb\3\2\2\2\2\u00bd\3\2\2\2\2\u00bf")
        buf.write("\3\2\2\2\2\u00c1\3\2\2\2\2\u00c3\3\2\2\2\2\u00c5\3\2\2")
        buf.write("\2\2\u00c7\3\2\2\2\2\u00c9\3\2\2\2\2\u00cb\3\2\2\2\2\u00cd")
        buf.write("\3\2\2\2\2\u00cf\3\2\2\2\2\u00d1\3\2\2\2\2\u00d3\3\2\2")
        buf.write("\2\2\u00d5\3\2\2\2\2\u00d7\3\2\2\2\2\u00d9\3\2\2\2\2\u00db")
        buf.write("\3\2\2\2\3\u00dd\3\2\2\2\5\u00e6\3\2\2\2\7\u00e8\3\2\2")
        buf.write("\2\t\u00ea\3\2\2\2\13\u00ec\3\2\2\2\r\u00f4\3\2\2\2\17")
        buf.write("\u00f9\3\2\2\2\21\u00fd\3\2\2\2\23\u00ff\3\2\2\2\25\u0101")
        buf.write("\3\2\2\2\27\u0103\3\2\2\2\31\u0105\3\2\2\2\33\u0107\3")
        buf.write("\2\2\2\35\u0109\3\2\2\2\37\u010b\3\2\2\2!\u010d\3\2\2")
        buf.write("\2#\u010f\3\2\2\2%\u0111\3\2\2\2\'\u0114\3\2\2\2)\u0119")
        buf.write("\3\2\2\2+\u011f\3\2\2\2-\u0124\3\2\2\2/\u0129\3\2\2\2")
        buf.write("\61\u012d\3\2\2\2\63\u0133\3\2\2\2\65\u0138\3\2\2\2\67")
        buf.write("\u013b\3\2\2\29\u0140\3\2\2\2;\u0146\3\2\2\2=\u014b\3")
        buf.write("\2\2\2?\u0151\3\2\2\2A\u0153\3\2\2\2C\u0157\3\2\2\2E\u015a")
        buf.write("\3\2\2\2G\u015e\3\2\2\2I\u0160\3\2\2\2K\u0163\3\2\2\2")
        buf.write("M\u0165\3\2\2\2O\u0168\3\2\2\2Q\u016e\3\2\2\2S\u0170\3")
        buf.write("\2\2\2U\u0172\3\2\2\2W\u0174\3\2\2\2Y\u0176\3\2\2\2[\u0178")
        buf.write("\3\2\2\2]\u017f\3\2\2\2_\u0184\3\2\2\2a\u0189\3\2\2\2")
        buf.write("c\u0190\3\2\2\2e\u0197\3\2\2\2g\u019d\3\2\2\2i\u01a2\3")
        buf.write("\2\2\2k\u01aa\3\2\2\2m\u01b3\3\2\2\2o\u01ba\3\2\2\2q\u01c6")
        buf.write("\3\2\2\2s\u01d0\3\2\2\2u\u01d4\3\2\2\2w\u01d8\3\2\2\2")
        buf.write("y\u01dc\3\2\2\2{\u01e1\3\2\2\2}\u01e6\3\2\2\2\177\u01eb")
        buf.write("\3\2\2\2\u0081\u01f1\3\2\2\2\u0083\u01f5\3\2\2\2\u0085")
        buf.write("\u01fb\3\2\2\2\u0087\u01ff\3\2\2\2\u0089\u0205\3\2\2\2")
        buf.write("\u008b\u020b\3\2\2\2\u008d\u0213\3\2\2\2\u008f\u0219\3")
        buf.write("\2\2\2\u0091\u021e\3\2\2\2\u0093\u0223\3\2\2\2\u0095\u0228")
        buf.write("\3\2\2\2\u0097\u022f\3\2\2\2\u0099\u0238\3\2\2\2\u009b")
        buf.write("\u0244\3\2\2\2\u009d\u0249\3\2\2\2\u009f\u0252\3\2\2\2")
        buf.write("\u00a1\u0255\3\2\2\2\u00a3\u0259\3\2\2\2\u00a5\u025d\3")
        buf.write("\2\2\2\u00a7\u0265\3\2\2\2\u00a9\u026f\3\2\2\2\u00ab\u0278")
        buf.write("\3\2\2\2\u00ad\u027d\3\2\2\2\u00af\u0284\3\2\2\2\u00b1")
        buf.write("\u028b\3\2\2\2\u00b3\u0290\3\2\2\2\u00b5\u0295\3\2\2\2")
        buf.write("\u00b7\u029d\3\2\2\2\u00b9\u02a3\3\2\2\2\u00bb\u02ac\3")
        buf.write("\2\2\2\u00bd\u02b3\3\2\2\2\u00bf\u02b9\3\2\2\2\u00c1\u02bf")
        buf.write("\3\2\2\2\u00c3\u02c7\3\2\2\2\u00c5\u02cf\3\2\2\2\u00c7")
        buf.write("\u02d8\3\2\2\2\u00c9\u02e1\3\2\2\2\u00cb\u02e5\3\2\2\2")
        buf.write("\u00cd\u02ee\3\2\2\2\u00cf\u02fd\3\2\2\2\u00d1\u0305\3")
        buf.write("\2\2\2\u00d3\u0310\3\2\2\2\u00d5\u0316\3\2\2\2\u00d7\u0323")
        buf.write("\3\2\2\2\u00d9\u0327\3\2\2\2\u00db\u0329\3\2\2\2\u00dd")
        buf.write("\u00de\7f\2\2\u00de\u00df\7q\2\2\u00df\u00e0\7v\2\2\u00e0")
        buf.write("\u00e1\7e\2\2\u00e1\u00e2\7j\2\2\u00e2\u00e3\7c\2\2\u00e3")
        buf.write("\u00e4\7t\2\2\u00e4\u00e5\7v\2\2\u00e5\4\3\2\2\2\u00e6")
        buf.write("\u00e7\t\2\2\2\u00e7\6\3\2\2\2\u00e8\u00e9\t\3\2\2\u00e9")
        buf.write("\b\3\2\2\2\u00ea\u00eb\t\4\2\2\u00eb\n\3\2\2\2\u00ec\u00ed")
        buf.write("\7r\2\2\u00ed\u00ee\7t\2\2\u00ee\u00ef\7q\2\2\u00ef\u00f0")
        buf.write("\7i\2\2\u00f0\u00f1\7t\2\2\u00f1\u00f2\7c\2\2\u00f2\u00f3")
        buf.write("\7o\2\2\u00f3\f\3\2\2\2\u00f4\u00f5\7o\2\2\u00f5\u00f6")
        buf.write("\7c\2\2\u00f6\u00f7\7k\2\2\u00f7\u00f8\7p\2\2\u00f8\16")
        buf.write("\3\2\2\2\u00f9\u00fa\7x\2\2\u00fa\u00fb\7c\2\2\u00fb\u00fc")
        buf.write("\7t\2\2\u00fc\20\3\2\2\2\u00fd\u00fe\7\60\2\2\u00fe\22")
        buf.write("\3\2\2\2\u00ff\u0100\7=\2\2\u0100\24\3\2\2\2\u0101\u0102")
        buf.write("\7<\2\2\u0102\26\3\2\2\2\u0103\u0104\7.\2\2\u0104\30\3")
        buf.write("\2\2\2\u0105\u0106\7]\2\2\u0106\32\3\2\2\2\u0107\u0108")
        buf.write("\7_\2\2\u0108\34\3\2\2\2\u0109\u010a\7*\2\2\u010a\36\3")
        buf.write("\2\2\2\u010b\u010c\7+\2\2\u010c \3\2\2\2\u010d\u010e\7")
        buf.write("}\2\2\u010e\"\3\2\2\2\u010f\u0110\7\177\2\2\u0110$\3\2")
        buf.write("\2\2\u0111\u0112\7>\2\2\u0112\u0113\7/\2\2\u0113&\3\2")
        buf.write("\2\2\u0114\u0115\7h\2\2\u0115\u0116\7w\2\2\u0116\u0117")
        buf.write("\7p\2\2\u0117\u0118\7e\2\2\u0118(\3\2\2\2\u0119\u011a")
        buf.write("\7g\2\2\u011a\u011b\7t\2\2\u011b\u011c\7t\2\2\u011c\u011d")
        buf.write("\7q\2\2\u011d\u011e\7t\2\2\u011e*\3\2\2\2\u011f\u0120")
        buf.write("\7p\2\2\u0120\u0121\7w\2\2\u0121\u0122\7n\2\2\u0122\u0123")
        buf.write("\7n\2\2\u0123,\3\2\2\2\u0124\u0125\7x\2\2\u0125\u0126")
        buf.write("\7q\2\2\u0126\u0127\7k\2\2\u0127\u0128\7f\2\2\u0128.\3")
        buf.write("\2\2\2\u0129\u012a\7k\2\2\u012a\u012b\7p\2\2\u012b\u012c")
        buf.write("\7v\2\2\u012c\60\3\2\2\2\u012d\u012e\7h\2\2\u012e\u012f")
        buf.write("\7n\2\2\u012f\u0130\7q\2\2\u0130\u0131\7c\2\2\u0131\u0132")
        buf.write("\7v\2\2\u0132\62\3\2\2\2\u0133\u0134\7e\2\2\u0134\u0135")
        buf.write("\7j\2\2\u0135\u0136\7c\2\2\u0136\u0137\7t\2\2\u0137\64")
        buf.write("\3\2\2\2\u0138\u0139\7k\2\2\u0139\u013a\7h\2\2\u013a\66")
        buf.write("\3\2\2\2\u013b\u013c\7g\2\2\u013c\u013d\7n\2\2\u013d\u013e")
        buf.write("\7u\2\2\u013e\u013f\7g\2\2\u013f8\3\2\2\2\u0140\u0141")
        buf.write("\7y\2\2\u0141\u0142\7j\2\2\u0142\u0143\7k\2\2\u0143\u0144")
        buf.write("\7n\2\2\u0144\u0145\7g\2\2\u0145:\3\2\2\2\u0146\u0147")
        buf.write("\7t\2\2\u0147\u0148\7g\2\2\u0148\u0149\7c\2\2\u0149\u014a")
        buf.write("\7f\2\2\u014a<\3\2\2\2\u014b\u014c\7r\2\2\u014c\u014d")
        buf.write("\7t\2\2\u014d\u014e\7k\2\2\u014e\u014f\7p\2\2\u014f\u0150")
        buf.write("\7v\2\2\u0150>\3\2\2\2\u0151\u0152\7?\2\2\u0152@\3\2\2")
        buf.write("\2\u0153\u0154\7c\2\2\u0154\u0155\7p\2\2\u0155\u0156\7")
        buf.write("f\2\2\u0156B\3\2\2\2\u0157\u0158\7q\2\2\u0158\u0159\7")
        buf.write("t\2\2\u0159D\3\2\2\2\u015a\u015b\7p\2\2\u015b\u015c\7")
        buf.write("q\2\2\u015c\u015d\7v\2\2\u015dF\3\2\2\2\u015e\u015f\7")
        buf.write("@\2\2\u015fH\3\2\2\2\u0160\u0161\7@\2\2\u0161\u0162\7")
        buf.write("?\2\2\u0162J\3\2\2\2\u0163\u0164\7>\2\2\u0164L\3\2\2\2")
        buf.write("\u0165\u0166\7>\2\2\u0166\u0167\7?\2\2\u0167N\3\2\2\2")
        buf.write("\u0168\u0169\7g\2\2\u0169\u016a\7s\2\2\u016a\u016b\7w")
        buf.write("\2\2\u016b\u016c\7c\2\2\u016c\u016d\7n\2\2\u016dP\3\2")
        buf.write("\2\2\u016e\u016f\7-\2\2\u016fR\3\2\2\2\u0170\u0171\7/")
        buf.write("\2\2\u0171T\3\2\2\2\u0172\u0173\7,\2\2\u0173V\3\2\2\2")
        buf.write("\u0174\u0175\7\61\2\2\u0175X\3\2\2\2\u0176\u0177\7\'\2")
        buf.write("\2\u0177Z\3\2\2\2\u0178\u0179\7t\2\2\u0179\u017a\7g\2")
        buf.write("\2\u017a\u017b\7v\2\2\u017b\u017c\7w\2\2\u017c\u017d\7")
        buf.write("t\2\2\u017d\u017e\7p\2\2\u017e\\\3\2\2\2\u017f\u0180\7")
        buf.write("t\2\2\u0180\u0181\7p\2\2\u0181\u0182\7q\2\2\u0182\u0183")
        buf.write("\7o\2\2\u0183^\3\2\2\2\u0184\u0185\7t\2\2\u0185\u0186")
        buf.write("\7g\2\2\u0186\u0187\7z\2\2\u0187\u0188\7r\2\2\u0188`\3")
        buf.write("\2\2\2\u0189\u018a\7t\2\2\u018a\u018b\7i\2\2\u018b\u018c")
        buf.write("\7c\2\2\u018c\u018d\7o\2\2\u018d\u018e\7o\2\2\u018e\u018f")
        buf.write("\7c\2\2\u018fb\3\2\2\2\u0190\u0191\7r\2\2\u0191\u0192")
        buf.write("\7q\2\2\u0192\u0193\7k\2\2\u0193\u0194\7p\2\2\u0194\u0195")
        buf.write("\7v\2\2\u0195\u0196\7u\2\2\u0196d\3\2\2\2\u0197\u0198")
        buf.write("\7n\2\2\u0198\u0199\7k\2\2\u0199\u019a\7p\2\2\u019a\u019b")
        buf.write("\7g\2\2\u019b\u019c\7u\2\2\u019cf\3\2\2\2\u019d\u019e")
        buf.write("\7v\2\2\u019e\u019f\7g\2\2\u019f\u01a0\7z\2\2\u01a0\u01a1")
        buf.write("\7v\2\2\u01a1h\3\2\2\2\u01a2\u01a3\7d\2\2\u01a3\u01a4")
        buf.write("\7c\2\2\u01a4\u01a5\7t\2\2\u01a5\u01a6\7r\2\2\u01a6\u01a7")
        buf.write("\7n\2\2\u01a7\u01a8\7q\2\2\u01a8\u01a9\7v\2\2\u01a9j\3")
        buf.write("\2\2\2\u01aa\u01ab\7r\2\2\u01ab\u01ac\7k\2\2\u01ac\u01ad")
        buf.write("\7g\2\2\u01ad\u01ae\7e\2\2\u01ae\u01af\7j\2\2\u01af\u01b0")
        buf.write("\7c\2\2\u01b0\u01b1\7t\2\2\u01b1\u01b2\7v\2\2\u01b2l\3")
        buf.write("\2\2\2\u01b3\u01b4\7z\2\2\u01b4\u01b5\7{\2\2\u01b5\u01b6")
        buf.write("\7r\2\2\u01b6\u01b7\7n\2\2\u01b7\u01b8\7q\2\2\u01b8\u01b9")
        buf.write("\7v\2\2\u01b9n\3\2\2\2\u01ba\u01bb\7f\2\2\u01bb\u01bc")
        buf.write("\7g\2\2\u01bc\u01bd\7p\2\2\u01bd\u01be\7u\2\2\u01be\u01bf")
        buf.write("\7k\2\2\u01bf\u01c0\7v\2\2\u01c0\u01c1\7{\2\2\u01c1\u01c2")
        buf.write("\7r\2\2\u01c2\u01c3\7n\2\2\u01c3\u01c4\7q\2\2\u01c4\u01c5")
        buf.write("\7v\2\2\u01c5p\3\2\2\2\u01c6\u01c7\7j\2\2\u01c7\u01c8")
        buf.write("\7k\2\2\u01c8\u01c9\7u\2\2\u01c9\u01ca\7v\2\2\u01ca\u01cb")
        buf.write("\7q\2\2\u01cb\u01cc\7i\2\2\u01cc\u01cd\7t\2\2\u01cd\u01ce")
        buf.write("\7c\2\2\u01ce\u01cf\7o\2\2\u01cfr\3\2\2\2\u01d0\u01d1")
        buf.write("\7u\2\2\u01d1\u01d2\7k\2\2\u01d2\u01d3\7p\2\2\u01d3t\3")
        buf.write("\2\2\2\u01d4\u01d5\7e\2\2\u01d5\u01d6\7q\2\2\u01d6\u01d7")
        buf.write("\7u\2\2\u01d7v\3\2\2\2\u01d8\u01d9\7v\2\2\u01d9\u01da")
        buf.write("\7c\2\2\u01da\u01db\7p\2\2\u01dbx\3\2\2\2\u01dc\u01dd")
        buf.write("\7c\2\2\u01dd\u01de\7u\2\2\u01de\u01df\7k\2\2\u01df\u01e0")
        buf.write("\7p\2\2\u01e0z\3\2\2\2\u01e1\u01e2\7c\2\2\u01e2\u01e3")
        buf.write("\7e\2\2\u01e3\u01e4\7q\2\2\u01e4\u01e5\7u\2\2\u01e5|\3")
        buf.write("\2\2\2\u01e6\u01e7\7c\2\2\u01e7\u01e8\7v\2\2\u01e8\u01e9")
        buf.write("\7c\2\2\u01e9\u01ea\7p\2\2\u01ea~\3\2\2\2\u01eb\u01ec")
        buf.write("\7c\2\2\u01ec\u01ed\7v\2\2\u01ed\u01ee\7c\2\2\u01ee\u01ef")
        buf.write("\7p\2\2\u01ef\u01f0\7\64\2\2\u01f0\u0080\3\2\2\2\u01f1")
        buf.write("\u01f2\7n\2\2\u01f2\u01f3\7q\2\2\u01f3\u01f4\7i\2\2\u01f4")
        buf.write("\u0082\3\2\2\2\u01f5\u01f6\7n\2\2\u01f6\u01f7\7q\2\2\u01f7")
        buf.write("\u01f8\7i\2\2\u01f8\u01f9\7\63\2\2\u01f9\u01fa\7\62\2")
        buf.write("\2\u01fa\u0084\3\2\2\2\u01fb\u01fc\7g\2\2\u01fc\u01fd")
        buf.write("\7z\2\2\u01fd\u01fe\7r\2\2\u01fe\u0086\3\2\2\2\u01ff\u0200")
        buf.write("\7h\2\2\u0200\u0201\7a\2\2\u0201\u0202\7o\2\2\u0202\u0203")
        buf.write("\7c\2\2\u0203\u0204\7z\2\2\u0204\u0088\3\2\2\2\u0205\u0206")
        buf.write("\7h\2\2\u0206\u0207\7a\2\2\u0207\u0208\7o\2\2\u0208\u0209")
        buf.write("\7k\2\2\u0209\u020a\7p\2\2\u020a\u008a\3\2\2\2\u020b\u020c")
        buf.write("\7h\2\2\u020c\u020d\7a\2\2\u020d\u020e\7t\2\2\u020e\u020f")
        buf.write("\7c\2\2\u020f\u0210\7p\2\2\u0210\u0211\7i\2\2\u0211\u0212")
        buf.write("\7g\2\2\u0212\u008c\3\2\2\2\u0213\u0214\7h\2\2\u0214\u0215")
        buf.write("\7a\2\2\u0215\u0216\7u\2\2\u0216\u0217\7w\2\2\u0217\u0218")
        buf.write("\7o\2\2\u0218\u008e\3\2\2\2\u0219\u021a\7f\2\2\u021a\u021b")
        buf.write("\7k\2\2\u021b\u021c\7h\2\2\u021c\u021d\7h\2\2\u021d\u0090")
        buf.write("\3\2\2\2\u021e\u021f\7r\2\2\u021f\u0220\7t\2\2\u0220\u0221")
        buf.write("\7q\2\2\u0221\u0222\7f\2\2\u0222\u0092\3\2\2\2\u0223\u0224")
        buf.write("\7o\2\2\u0224\u0225\7g\2\2\u0225\u0226\7c\2\2\u0226\u0227")
        buf.write("\7p\2\2\u0227\u0094\3\2\2\2\u0228\u0229\7o\2\2\u0229\u022a")
        buf.write("\7g\2\2\u022a\u022b\7f\2\2\u022b\u022c\7k\2\2\u022c\u022d")
        buf.write("\7c\2\2\u022d\u022e\7p\2\2\u022e\u0096\3\2\2\2\u022f\u0230")
        buf.write("\7s\2\2\u0230\u0231\7w\2\2\u0231\u0232\7c\2\2\u0232\u0233")
        buf.write("\7p\2\2\u0233\u0234\7v\2\2\u0234\u0235\7k\2\2\u0235\u0236")
        buf.write("\7n\2\2\u0236\u0237\7g\2\2\u0237\u0098\3\2\2\2\u0238\u0239")
        buf.write("\7y\2\2\u0239\u023a\7g\2\2\u023a\u023b\7k\2\2\u023b\u023c")
        buf.write("\7i\2\2\u023c\u023d\7j\2\2\u023d\u023e\7g\2\2\u023e\u023f")
        buf.write("\7f\2\2\u023f\u0240\7o\2\2\u0240\u0241\7g\2\2\u0241\u0242")
        buf.write("\7c\2\2\u0242\u0243\7p\2\2\u0243\u009a\3\2\2\2\u0244\u0245")
        buf.write("\7t\2\2\u0245\u0246\7c\2\2\u0246\u0247\7p\2\2\u0247\u0248")
        buf.write("\7m\2\2\u0248\u009c\3\2\2\2\u0249\u024a\7x\2\2\u024a\u024b")
        buf.write("\7c\2\2\u024b\u024c\7t\2\2\u024c\u024d\7k\2\2\u024d\u024e")
        buf.write("\7c\2\2\u024e\u024f\7p\2\2\u024f\u0250\7e\2\2\u0250\u0251")
        buf.write("\7g\2\2\u0251\u009e\3\2\2\2\u0252\u0253\7u\2\2\u0253\u0254")
        buf.write("\7f\2\2\u0254\u00a0\3\2\2\2\u0255\u0256\7e\2\2\u0256\u0257")
        buf.write("\7q\2\2\u0257\u0258\7t\2\2\u0258\u00a2\3\2\2\2\u0259\u025a")
        buf.write("\7e\2\2\u025a\u025b\7q\2\2\u025b\u025c\7x\2\2\u025c\u00a4")
        buf.write("\3\2\2\2\u025d\u025e\7h\2\2\u025e\u025f\7a\2\2\u025f\u0260")
        buf.write("\7t\2\2\u0260\u0261\7q\2\2\u0261\u0262\7w\2\2\u0262\u0263")
        buf.write("\7p\2\2\u0263\u0264\7f\2\2\u0264\u00a6\3\2\2\2\u0265\u0266")
        buf.write("\7v\2\2\u0266\u0267\7t\2\2\u0267\u0268\7c\2\2\u0268\u0269")
        buf.write("\7p\2\2\u0269\u026a\7u\2\2\u026a\u026b\7r\2\2\u026b\u026c")
        buf.write("\7q\2\2\u026c\u026d\7u\2\2\u026d\u026e\7g\2\2\u026e\u00a8")
        buf.write("\3\2\2\2\u026f\u0270\7f\2\2\u0270\u0271\7k\2\2\u0271\u0272")
        buf.write("\7c\2\2\u0272\u0273\7i\2\2\u0273\u0274\7q\2\2\u0274\u0275")
        buf.write("\7p\2\2\u0275\u0276\7c\2\2\u0276\u0277\7n\2\2\u0277\u00aa")
        buf.write("\3\2\2\2\u0278\u0279\7i\2\2\u0279\u027a\7k\2\2\u027a\u027b")
        buf.write("\7p\2\2\u027b\u027c\7x\2\2\u027c\u00ac\3\2\2\2\u027d\u027e")
        buf.write("\7t\2\2\u027e\u027f\7q\2\2\u027f\u0280\7y\2\2\u0280\u0281")
        buf.write("\7u\2\2\u0281\u0282\7w\2\2\u0282\u0283\7o\2\2\u0283\u00ae")
        buf.write("\3\2\2\2\u0284\u0285\7e\2\2\u0285\u0286\7q\2\2\u0286\u0287")
        buf.write("\7n\2\2\u0287\u0288\7u\2\2\u0288\u0289\7w\2\2\u0289\u028a")
        buf.write("\7o\2\2\u028a\u00b0\3\2\2\2\u028b\u028c\7n\2\2\u028c\u028d")
        buf.write("\7q\2\2\u028d\u028e\7c\2\2\u028e\u028f\7f\2\2\u028f\u00b2")
        buf.write("\3\2\2\2\u0290\u0291\7f\2\2\u0291\u0292\7c\2\2\u0292\u0293")
        buf.write("\7v\2\2\u0293\u0294\7c\2\2\u0294\u00b4\3\2\2\2\u0295\u0296")
        buf.write("\7n\2\2\u0296\u0297\7k\2\2\u0297\u0298\7d\2\2\u0298\u0299")
        buf.write("\7t\2\2\u0299\u029a\7c\2\2\u029a\u029b\7t\2\2\u029b\u029c")
        buf.write("\7{\2\2\u029c\u00b6\3\2\2\2\u029d\u029e\7t\2\2\u029e\u029f")
        buf.write("\7r\2\2\u029f\u02a0\7q\2\2\u02a0\u02a1\7k\2\2\u02a1\u02a2")
        buf.write("\7u\2\2\u02a2\u00b8\3\2\2\2\u02a3\u02a4\7t\2\2\u02a4\u02a5")
        buf.write("\7y\2\2\u02a5\u02a6\7g\2\2\u02a6\u02a7\7k\2\2\u02a7\u02a8")
        buf.write("\7d\2\2\u02a8\u02a9\7w\2\2\u02a9\u02aa\7n\2\2\u02aa\u02ab")
        buf.write("\7n\2\2\u02ab\u00ba\3\2\2\2\u02ac\u02ad\7t\2\2\u02ad\u02ae")
        buf.write("\7d\2\2\u02ae\u02af\7k\2\2\u02af\u02b0\7p\2\2\u02b0\u02b1")
        buf.write("\7q\2\2\u02b1\u02b2\7o\2\2\u02b2\u00bc\3\2\2\2\u02b3\u02b4")
        buf.write("\7t\2\2\u02b4\u02b5\7i\2\2\u02b5\u02b6\7g\2\2\u02b6\u02b7")
        buf.write("\7q\2\2\u02b7\u02b8\7o\2\2\u02b8\u00be\3\2\2\2\u02b9\u02ba")
        buf.write("\7t\2\2\u02ba\u02bb\7w\2\2\u02bb\u02bc\7p\2\2\u02bc\u02bd")
        buf.write("\7k\2\2\u02bd\u02be\7h\2\2\u02be\u00c0\3\2\2\2\u02bf\u02c0")
        buf.write("\7r\2\2\u02c0\u02c1\7g\2\2\u02c1\u02c2\7c\2\2\u02c2\u02c3")
        buf.write("\7t\2\2\u02c3\u02c4\7u\2\2\u02c4\u02c5\7q\2\2\u02c5\u02c6")
        buf.write("\7p\2\2\u02c6\u00c2\3\2\2\2\u02c7\u02c8\7m\2\2\u02c8\u02c9")
        buf.write("\7g\2\2\u02c9\u02ca\7p\2\2\u02ca\u02cb\7f\2\2\u02cb\u02cc")
        buf.write("\7c\2\2\u02cc\u02cd\7n\2\2\u02cd\u02ce\7n\2\2\u02ce\u00c4")
        buf.write("\3\2\2\2\u02cf\u02d0\7u\2\2\u02d0\u02d1\7r\2\2\u02d1\u02d2")
        buf.write("\7g\2\2\u02d2\u02d3\7c\2\2\u02d3\u02d4\7t\2\2\u02d4\u02d5")
        buf.write("\7o\2\2\u02d5\u02d6\7c\2\2\u02d6\u02d7\7p\2\2\u02d7\u00c6")
        buf.write("\3\2\2\2\u02d8\u02d9\t\5\2\2\u02d9\u02da\3\2\2\2\u02da")
        buf.write("\u02db\bd\2\2\u02db\u00c8\3\2\2\2\u02dc\u02de\7\17\2\2")
        buf.write("\u02dd\u02dc\3\2\2\2\u02dd\u02de\3\2\2\2\u02de\u02df\3")
        buf.write("\2\2\2\u02df\u02e2\7\f\2\2\u02e0\u02e2\7\17\2\2\u02e1")
        buf.write("\u02dd\3\2\2\2\u02e1\u02e0\3\2\2\2\u02e2\u02e3\3\2\2\2")
        buf.write("\u02e3\u02e4\be\2\2\u02e4\u00ca\3\2\2\2\u02e5\u02e9\7")
        buf.write("%\2\2\u02e6\u02e8\n\6\2\2\u02e7\u02e6\3\2\2\2\u02e8\u02eb")
        buf.write("\3\2\2\2\u02e9\u02e7\3\2\2\2\u02e9\u02ea\3\2\2\2\u02ea")
        buf.write("\u02ec\3\2\2\2\u02eb\u02e9\3\2\2\2\u02ec\u02ed\bf\2\2")
        buf.write("\u02ed\u00cc\3\2\2\2\u02ee\u02ef\7\61\2\2\u02ef\u02f0")
        buf.write("\7%\2\2\u02f0\u02f4\3\2\2\2\u02f1\u02f3\13\2\2\2\u02f2")
        buf.write("\u02f1\3\2\2\2\u02f3\u02f6\3\2\2\2\u02f4\u02f5\3\2\2\2")
        buf.write("\u02f4\u02f2\3\2\2\2\u02f5\u02f7\3\2\2\2\u02f6\u02f4\3")
        buf.write("\2\2\2\u02f7\u02f8\7%\2\2\u02f8\u02f9\7\61\2\2\u02f9\u02fa")
        buf.write("\3\2\2\2\u02fa\u02fb\bg\2\2\u02fb\u00ce\3\2\2\2\u02fc")
        buf.write("\u02fe\5S*\2\u02fd\u02fc\3\2\2\2\u02fd\u02fe\3\2\2\2\u02fe")
        buf.write("\u0300\3\2\2\2\u02ff\u0301\5\t\5\2\u0300\u02ff\3\2\2\2")
        buf.write("\u0301\u0302\3\2\2\2\u0302\u0300\3\2\2\2\u0302\u0303\3")
        buf.write("\2\2\2\u0303\u00d0\3\2\2\2\u0304\u0306\5S*\2\u0305\u0304")
        buf.write("\3\2\2\2\u0305\u0306\3\2\2\2\u0306\u0307\3\2\2\2\u0307")
        buf.write("\u030e\5\u00cfh\2\u0308\u030a\5\21\t\2\u0309\u030b\5\t")
        buf.write("\5\2\u030a\u0309\3\2\2\2\u030b\u030c\3\2\2\2\u030c\u030a")
        buf.write("\3\2\2\2\u030c\u030d\3\2\2\2\u030d\u030f\3\2\2\2\u030e")
        buf.write("\u0308\3\2\2\2\u030e\u030f\3\2\2\2\u030f\u00d2\3\2\2\2")
        buf.write("\u0310\u0312\7)\2\2\u0311\u0313\13\2\2\2\u0312\u0311\3")
        buf.write("\2\2\2\u0312\u0313\3\2\2\2\u0313\u0314\3\2\2\2\u0314\u0315")
        buf.write("\7)\2\2\u0315\u00d4\3\2\2\2\u0316\u031a\7$\2\2\u0317\u0319")
        buf.write("\13\2\2\2\u0318\u0317\3\2\2\2\u0319\u031c\3\2\2\2\u031a")
        buf.write("\u031b\3\2\2\2\u031a\u0318\3\2\2\2\u031b\u031d\3\2\2\2")
        buf.write("\u031c\u031a\3\2\2\2\u031d\u031e\7$\2\2\u031e\u00d6\3")
        buf.write("\2\2\2\u031f\u0324\5\5\3\2\u0320\u0324\5\7\4\2\u0321\u0324")
        buf.write("\5\t\5\2\u0322\u0324\7a\2\2\u0323\u031f\3\2\2\2\u0323")
        buf.write("\u0320\3\2\2\2\u0323\u0321\3\2\2\2\u0323\u0322\3\2\2\2")
        buf.write("\u0324\u0325\3\2\2\2\u0325\u0323\3\2\2\2\u0325\u0326\3")
        buf.write("\2\2\2\u0326\u00d8\3\2\2\2\u0327\u0328\7\62\2\2\u0328")
        buf.write("\u00da\3\2\2\2\u0329\u032a\7\63\2\2\u032a\u00dc\3\2\2")
        buf.write("\2\20\2\u02dd\u02e1\u02e9\u02f4\u02fd\u0302\u0305\u030c")
        buf.write("\u030e\u0312\u031a\u0323\u0325\3\b\2\2")
        return buf.getvalue()


class NmodLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    PROGRAM = 2
    MAIN = 3
    VARIABLES = 4
    PERIOD = 5
    SEMICOLON = 6
    COLON = 7
    COMMA = 8
    LBRACKET = 9
    RBRACKET = 10
    LPRACKET = 11
    RPRACKET = 12
    LCRACKET = 13
    RCRACKET = 14
    ISFUNCTION = 15
    FUNC = 16
    ERROR = 17
    NULL = 18
    VOID = 19
    INT = 20
    FLOAT = 21
    CHAR = 22
    IF = 23
    ELSE = 24
    WHILE = 25
    READ = 26
    PRINT = 27
    EQUALS = 28
    AND = 29
    OR = 30
    NOT = 31
    GREATERTHAN = 32
    GREATEROR = 33
    LESSERTHAN = 34
    LESSEROR = 35
    EQUAL = 36
    PLUS = 37
    MINUS = 38
    TIMES = 39
    DIVISION = 40
    MODULE = 41
    RETURN = 42
    RNOM = 43
    REXP = 44
    RGAMMA = 45
    POINTS = 46
    LINES = 47
    TEXT = 48
    BARPLOT = 49
    PIECHART = 50
    XYPLOT = 51
    DENSITYPLOT = 52
    HISTOGRAM = 53
    SIN = 54
    COS = 55
    TAN = 56
    ASIN = 57
    ACOS = 58
    ATAN = 59
    ATAN2 = 60
    LOG = 61
    LOG10 = 62
    EXPONENT = 63
    MAX = 64
    MIN = 65
    RANGE = 66
    SUM = 67
    DIFF = 68
    PROD = 69
    MEAN = 70
    MEDIAN = 71
    QUANTILE = 72
    WEIGHEDMEAN = 73
    RANK = 74
    VARIANCE = 75
    SD = 76
    COR = 77
    COV = 78
    ROUND = 79
    TRANSPOSE = 80
    DIAGONAL = 81
    GINV = 82
    ROWSUM = 83
    COLSUM = 84
    LOAD = 85
    DATA = 86
    LIBRARY = 87
    RPOIS = 88
    RWEIBULL = 89
    RBINOM = 90
    RGEOM = 91
    RUNIF = 92
    PEARSON = 93
    KENDALL = 94
    SPEARMAN = 95
    WHITESPACE = 96
    NEWLINE = 97
    LINECOMMENT = 98
    MULTICOMMENT = 99
    CTEI = 100
    CTEF = 101
    CTEC = 102
    STRING = 103
    ID = 104
    ZERO = 105
    ONE = 106

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'dotchart'", "'program'", "'main'", "'var'", "'.'", "';'", 
            "':'", "','", "'['", "']'", "'('", "')'", "'{'", "'}'", "'<-'", 
            "'func'", "'error'", "'null'", "'void'", "'int'", "'float'", 
            "'char'", "'if'", "'else'", "'while'", "'read'", "'print'", 
            "'='", "'and'", "'or'", "'not'", "'>'", "'>='", "'<'", "'<='", 
            "'equal'", "'+'", "'-'", "'*'", "'/'", "'%'", "'return'", "'rnom'", 
            "'rexp'", "'rgamma'", "'points'", "'lines'", "'text'", "'barplot'", 
            "'piechart'", "'xyplot'", "'densityplot'", "'histogram'", "'sin'", 
            "'cos'", "'tan'", "'asin'", "'acos'", "'atan'", "'atan2'", "'log'", 
            "'log10'", "'exp'", "'f_max'", "'f_min'", "'f_range'", "'f_sum'", 
            "'diff'", "'prod'", "'mean'", "'median'", "'quantile'", "'weighedmean'", 
            "'rank'", "'variance'", "'sd'", "'cor'", "'cov'", "'f_round'", 
            "'transpose'", "'diagonal'", "'ginv'", "'rowsum'", "'colsum'", 
            "'load'", "'data'", "'library'", "'rpois'", "'rweibull'", "'rbinom'", 
            "'rgeom'", "'runif'", "'pearson'", "'kendall'", "'spearman'", 
            "'0'", "'1'" ]

    symbolicNames = [ "<INVALID>",
            "PROGRAM", "MAIN", "VARIABLES", "PERIOD", "SEMICOLON", "COLON", 
            "COMMA", "LBRACKET", "RBRACKET", "LPRACKET", "RPRACKET", "LCRACKET", 
            "RCRACKET", "ISFUNCTION", "FUNC", "ERROR", "NULL", "VOID", "INT", 
            "FLOAT", "CHAR", "IF", "ELSE", "WHILE", "READ", "PRINT", "EQUALS", 
            "AND", "OR", "NOT", "GREATERTHAN", "GREATEROR", "LESSERTHAN", 
            "LESSEROR", "EQUAL", "PLUS", "MINUS", "TIMES", "DIVISION", "MODULE", 
            "RETURN", "RNOM", "REXP", "RGAMMA", "POINTS", "LINES", "TEXT", 
            "BARPLOT", "PIECHART", "XYPLOT", "DENSITYPLOT", "HISTOGRAM", 
            "SIN", "COS", "TAN", "ASIN", "ACOS", "ATAN", "ATAN2", "LOG", 
            "LOG10", "EXPONENT", "MAX", "MIN", "RANGE", "SUM", "DIFF", "PROD", 
            "MEAN", "MEDIAN", "QUANTILE", "WEIGHEDMEAN", "RANK", "VARIANCE", 
            "SD", "COR", "COV", "ROUND", "TRANSPOSE", "DIAGONAL", "GINV", 
            "ROWSUM", "COLSUM", "LOAD", "DATA", "LIBRARY", "RPOIS", "RWEIBULL", 
            "RBINOM", "RGEOM", "RUNIF", "PEARSON", "KENDALL", "SPEARMAN", 
            "WHITESPACE", "NEWLINE", "LINECOMMENT", "MULTICOMMENT", "CTEI", 
            "CTEF", "CTEC", "STRING", "ID", "ZERO", "ONE" ]

    ruleNames = [ "T__0", "LOWERCASE", "UPPERCASE", "DIGIT", "PROGRAM", 
                  "MAIN", "VARIABLES", "PERIOD", "SEMICOLON", "COLON", "COMMA", 
                  "LBRACKET", "RBRACKET", "LPRACKET", "RPRACKET", "LCRACKET", 
                  "RCRACKET", "ISFUNCTION", "FUNC", "ERROR", "NULL", "VOID", 
                  "INT", "FLOAT", "CHAR", "IF", "ELSE", "WHILE", "READ", 
                  "PRINT", "EQUALS", "AND", "OR", "NOT", "GREATERTHAN", 
                  "GREATEROR", "LESSERTHAN", "LESSEROR", "EQUAL", "PLUS", 
                  "MINUS", "TIMES", "DIVISION", "MODULE", "RETURN", "RNOM", 
                  "REXP", "RGAMMA", "POINTS", "LINES", "TEXT", "BARPLOT", 
                  "PIECHART", "XYPLOT", "DENSITYPLOT", "HISTOGRAM", "SIN", 
                  "COS", "TAN", "ASIN", "ACOS", "ATAN", "ATAN2", "LOG", 
                  "LOG10", "EXPONENT", "MAX", "MIN", "RANGE", "SUM", "DIFF", 
                  "PROD", "MEAN", "MEDIAN", "QUANTILE", "WEIGHEDMEAN", "RANK", 
                  "VARIANCE", "SD", "COR", "COV", "ROUND", "TRANSPOSE", 
                  "DIAGONAL", "GINV", "ROWSUM", "COLSUM", "LOAD", "DATA", 
                  "LIBRARY", "RPOIS", "RWEIBULL", "RBINOM", "RGEOM", "RUNIF", 
                  "PEARSON", "KENDALL", "SPEARMAN", "WHITESPACE", "NEWLINE", 
                  "LINECOMMENT", "MULTICOMMENT", "CTEI", "CTEF", "CTEC", 
                  "STRING", "ID", "ZERO", "ONE" ]

    grammarFileName = "Nmod.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


