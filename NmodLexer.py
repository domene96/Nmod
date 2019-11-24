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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2k")
        buf.write("\u031a\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
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
        buf.write("g\tg\4h\th\4i\ti\4j\tj\4k\tk\4l\tl\4m\tm\3\2\3\2\3\3\3")
        buf.write("\3\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\7")
        buf.write("\3\7\3\7\3\7\3\b\3\b\3\t\3\t\3\n\3\n\3\13\3\13\3\f\3\f")
        buf.write("\3\r\3\r\3\16\3\16\3\17\3\17\3\20\3\20\3\21\3\21\3\22")
        buf.write("\3\22\3\22\3\23\3\23\3\23\3\23\3\23\3\24\3\24\3\24\3\24")
        buf.write("\3\24\3\24\3\25\3\25\3\25\3\25\3\25\3\26\3\26\3\26\3\26")
        buf.write("\3\26\3\27\3\27\3\27\3\27\3\30\3\30\3\30\3\30\3\30\3\30")
        buf.write("\3\31\3\31\3\31\3\31\3\31\3\32\3\32\3\32\3\33\3\33\3\33")
        buf.write("\3\33\3\33\3\34\3\34\3\34\3\34\3\34\3\34\3\35\3\35\3\35")
        buf.write("\3\35\3\35\3\36\3\36\3\36\3\36\3\36\3\36\3\37\3\37\3 ")
        buf.write("\3 \3 \3 \3!\3!\3!\3\"\3\"\3\"\3\"\3#\3#\3$\3$\3$\3%\3")
        buf.write("%\3&\3&\3&\3\'\3\'\3\'\3\'\3\'\3\'\3(\3(\3)\3)\3*\3*\3")
        buf.write("+\3+\3,\3,\3-\3-\3-\3-\3-\3-\3-\3.\3.\3.\3.\3.\3/\3/\3")
        buf.write("/\3/\3/\3\60\3\60\3\60\3\60\3\60\3\60\3\60\3\61\3\61\3")
        buf.write("\61\3\61\3\61\3\61\3\61\3\62\3\62\3\62\3\62\3\62\3\62")
        buf.write("\3\63\3\63\3\63\3\63\3\63\3\64\3\64\3\64\3\64\3\64\3\64")
        buf.write("\3\64\3\64\3\65\3\65\3\65\3\65\3\65\3\65\3\65\3\65\3\65")
        buf.write("\3\66\3\66\3\66\3\66\3\66\3\66\3\66\3\66\3\66\3\67\3\67")
        buf.write("\3\67\3\67\3\67\3\67\3\67\38\38\38\38\38\38\38\38\38\3")
        buf.write("8\38\38\39\39\39\39\39\39\39\39\39\39\3:\3:\3:\3:\3;\3")
        buf.write(";\3;\3;\3<\3<\3<\3<\3=\3=\3=\3=\3=\3>\3>\3>\3>\3>\3?\3")
        buf.write("?\3?\3?\3?\3@\3@\3@\3@\3@\3@\3A\3A\3A\3A\3B\3B\3B\3B\3")
        buf.write("B\3B\3C\3C\3C\3C\3D\3D\3D\3D\3D\3D\3E\3E\3E\3E\3E\3E\3")
        buf.write("F\3F\3F\3F\3F\3F\3F\3F\3G\3G\3G\3G\3G\3G\3H\3H\3H\3H\3")
        buf.write("H\3I\3I\3I\3I\3I\3J\3J\3J\3J\3J\3K\3K\3K\3K\3K\3K\3K\3")
        buf.write("L\3L\3L\3L\3L\3L\3L\3L\3L\3M\3M\3M\3M\3M\3N\3N\3N\3N\3")
        buf.write("N\3N\3N\3N\3N\3O\3O\3O\3P\3P\3P\3P\3Q\3Q\3Q\3Q\3R\3R\3")
        buf.write("R\3R\3R\3R\3R\3R\3S\3S\3S\3S\3S\3S\3S\3S\3S\3S\3T\3T\3")
        buf.write("T\3T\3T\3T\3T\3T\3T\3U\3U\3U\3U\3U\3V\3V\3V\3V\3V\3V\3")
        buf.write("V\3W\3W\3W\3W\3W\3W\3W\3X\3X\3X\3X\3X\3Y\3Y\3Y\3Y\3Y\3")
        buf.write("Z\3Z\3Z\3Z\3Z\3Z\3Z\3Z\3[\3[\3[\3[\3[\3[\3\\\3\\\3\\\3")
        buf.write("\\\3\\\3\\\3\\\3\\\3\\\3]\3]\3]\3]\3]\3]\3]\3^\3^\3^\3")
        buf.write("^\3^\3^\3_\3_\3_\3_\3_\3_\3`\3`\3`\3`\3`\3`\3`\3`\3a\3")
        buf.write("a\3a\3a\3a\3a\3a\3a\3b\3b\3b\3b\3b\3b\3b\3b\3b\3c\3c\3")
        buf.write("c\3c\3d\5d\u02cd\nd\3d\3d\5d\u02d1\nd\3d\3d\3e\3e\7e\u02d7")
        buf.write("\ne\fe\16e\u02da\13e\3e\3e\3f\3f\3f\3f\7f\u02e2\nf\ff")
        buf.write("\16f\u02e5\13f\3f\3f\3f\3f\3f\3g\5g\u02ed\ng\3g\6g\u02f0")
        buf.write("\ng\rg\16g\u02f1\3h\5h\u02f5\nh\3h\3h\3h\6h\u02fa\nh\r")
        buf.write("h\16h\u02fb\5h\u02fe\nh\3i\3i\5i\u0302\ni\3i\3i\3j\3j")
        buf.write("\7j\u0308\nj\fj\16j\u030b\13j\3j\3j\3k\3k\3k\3k\6k\u0313")
        buf.write("\nk\rk\16k\u0314\3l\3l\3m\3m\4\u02e3\u0309\2n\3\2\5\2")
        buf.write("\7\2\t\3\13\4\r\5\17\6\21\7\23\b\25\t\27\n\31\13\33\f")
        buf.write("\35\r\37\16!\17#\20%\21\'\22)\23+\24-\25/\26\61\27\63")
        buf.write("\30\65\31\67\329\33;\34=\35?\36A\37C E!G\"I#K$M%O&Q\'")
        buf.write("S(U)W*Y+[,]-_.a/c\60e\61g\62i\63k\64m\65o\66q\67s8u9w")
        buf.write(":y;{<}=\177>\u0081?\u0083@\u0085A\u0087B\u0089C\u008b")
        buf.write("D\u008dE\u008fF\u0091G\u0093H\u0095I\u0097J\u0099K\u009b")
        buf.write("L\u009dM\u009fN\u00a1O\u00a3P\u00a5Q\u00a7R\u00a9S\u00ab")
        buf.write("T\u00adU\u00afV\u00b1W\u00b3X\u00b5Y\u00b7Z\u00b9[\u00bb")
        buf.write("\\\u00bd]\u00bf^\u00c1_\u00c3`\u00c5a\u00c7b\u00c9c\u00cb")
        buf.write("d\u00cde\u00cff\u00d1g\u00d3h\u00d5i\u00d7j\u00d9k\3\2")
        buf.write("\7\3\2c|\3\2C\\\3\2\62;\4\2\13\13\"\"\4\2\f\f\17\17\2")
        buf.write("\u0325\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2")
        buf.write("\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2")
        buf.write("\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2")
        buf.write("!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2")
        buf.write("\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3")
        buf.write("\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2")
        buf.write("\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2")
        buf.write("\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2")
        buf.write("\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3")
        buf.write("\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2c")
        buf.write("\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2")
        buf.write("m\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2\2s\3\2\2\2\2u\3\2\2\2")
        buf.write("\2w\3\2\2\2\2y\3\2\2\2\2{\3\2\2\2\2}\3\2\2\2\2\177\3\2")
        buf.write("\2\2\2\u0081\3\2\2\2\2\u0083\3\2\2\2\2\u0085\3\2\2\2\2")
        buf.write("\u0087\3\2\2\2\2\u0089\3\2\2\2\2\u008b\3\2\2\2\2\u008d")
        buf.write("\3\2\2\2\2\u008f\3\2\2\2\2\u0091\3\2\2\2\2\u0093\3\2\2")
        buf.write("\2\2\u0095\3\2\2\2\2\u0097\3\2\2\2\2\u0099\3\2\2\2\2\u009b")
        buf.write("\3\2\2\2\2\u009d\3\2\2\2\2\u009f\3\2\2\2\2\u00a1\3\2\2")
        buf.write("\2\2\u00a3\3\2\2\2\2\u00a5\3\2\2\2\2\u00a7\3\2\2\2\2\u00a9")
        buf.write("\3\2\2\2\2\u00ab\3\2\2\2\2\u00ad\3\2\2\2\2\u00af\3\2\2")
        buf.write("\2\2\u00b1\3\2\2\2\2\u00b3\3\2\2\2\2\u00b5\3\2\2\2\2\u00b7")
        buf.write("\3\2\2\2\2\u00b9\3\2\2\2\2\u00bb\3\2\2\2\2\u00bd\3\2\2")
        buf.write("\2\2\u00bf\3\2\2\2\2\u00c1\3\2\2\2\2\u00c3\3\2\2\2\2\u00c5")
        buf.write("\3\2\2\2\2\u00c7\3\2\2\2\2\u00c9\3\2\2\2\2\u00cb\3\2\2")
        buf.write("\2\2\u00cd\3\2\2\2\2\u00cf\3\2\2\2\2\u00d1\3\2\2\2\2\u00d3")
        buf.write("\3\2\2\2\2\u00d5\3\2\2\2\2\u00d7\3\2\2\2\2\u00d9\3\2\2")
        buf.write("\2\3\u00db\3\2\2\2\5\u00dd\3\2\2\2\7\u00df\3\2\2\2\t\u00e1")
        buf.write("\3\2\2\2\13\u00e6\3\2\2\2\r\u00eb\3\2\2\2\17\u00ef\3\2")
        buf.write("\2\2\21\u00f1\3\2\2\2\23\u00f3\3\2\2\2\25\u00f5\3\2\2")
        buf.write("\2\27\u00f7\3\2\2\2\31\u00f9\3\2\2\2\33\u00fb\3\2\2\2")
        buf.write("\35\u00fd\3\2\2\2\37\u00ff\3\2\2\2!\u0101\3\2\2\2#\u0103")
        buf.write("\3\2\2\2%\u0106\3\2\2\2\'\u010b\3\2\2\2)\u0111\3\2\2\2")
        buf.write("+\u0116\3\2\2\2-\u011b\3\2\2\2/\u011f\3\2\2\2\61\u0125")
        buf.write("\3\2\2\2\63\u012a\3\2\2\2\65\u012d\3\2\2\2\67\u0132\3")
        buf.write("\2\2\29\u0138\3\2\2\2;\u013d\3\2\2\2=\u0143\3\2\2\2?\u0145")
        buf.write("\3\2\2\2A\u0149\3\2\2\2C\u014c\3\2\2\2E\u0150\3\2\2\2")
        buf.write("G\u0152\3\2\2\2I\u0155\3\2\2\2K\u0157\3\2\2\2M\u015a\3")
        buf.write("\2\2\2O\u0160\3\2\2\2Q\u0162\3\2\2\2S\u0164\3\2\2\2U\u0166")
        buf.write("\3\2\2\2W\u0168\3\2\2\2Y\u016a\3\2\2\2[\u0171\3\2\2\2")
        buf.write("]\u0176\3\2\2\2_\u017b\3\2\2\2a\u0182\3\2\2\2c\u0189\3")
        buf.write("\2\2\2e\u018f\3\2\2\2g\u0194\3\2\2\2i\u019c\3\2\2\2k\u01a5")
        buf.write("\3\2\2\2m\u01ae\3\2\2\2o\u01b5\3\2\2\2q\u01c1\3\2\2\2")
        buf.write("s\u01cb\3\2\2\2u\u01cf\3\2\2\2w\u01d3\3\2\2\2y\u01d7\3")
        buf.write("\2\2\2{\u01dc\3\2\2\2}\u01e1\3\2\2\2\177\u01e6\3\2\2\2")
        buf.write("\u0081\u01ec\3\2\2\2\u0083\u01f0\3\2\2\2\u0085\u01f6\3")
        buf.write("\2\2\2\u0087\u01fa\3\2\2\2\u0089\u0200\3\2\2\2\u008b\u0206")
        buf.write("\3\2\2\2\u008d\u020e\3\2\2\2\u008f\u0214\3\2\2\2\u0091")
        buf.write("\u0219\3\2\2\2\u0093\u021e\3\2\2\2\u0095\u0223\3\2\2\2")
        buf.write("\u0097\u022a\3\2\2\2\u0099\u0233\3\2\2\2\u009b\u0238\3")
        buf.write("\2\2\2\u009d\u0241\3\2\2\2\u009f\u0244\3\2\2\2\u00a1\u0248")
        buf.write("\3\2\2\2\u00a3\u024c\3\2\2\2\u00a5\u0254\3\2\2\2\u00a7")
        buf.write("\u025e\3\2\2\2\u00a9\u0267\3\2\2\2\u00ab\u026c\3\2\2\2")
        buf.write("\u00ad\u0273\3\2\2\2\u00af\u027a\3\2\2\2\u00b1\u027f\3")
        buf.write("\2\2\2\u00b3\u0284\3\2\2\2\u00b5\u028c\3\2\2\2\u00b7\u0292")
        buf.write("\3\2\2\2\u00b9\u029b\3\2\2\2\u00bb\u02a2\3\2\2\2\u00bd")
        buf.write("\u02a8\3\2\2\2\u00bf\u02ae\3\2\2\2\u00c1\u02b6\3\2\2\2")
        buf.write("\u00c3\u02be\3\2\2\2\u00c5\u02c7\3\2\2\2\u00c7\u02d0\3")
        buf.write("\2\2\2\u00c9\u02d4\3\2\2\2\u00cb\u02dd\3\2\2\2\u00cd\u02ec")
        buf.write("\3\2\2\2\u00cf\u02f4\3\2\2\2\u00d1\u02ff\3\2\2\2\u00d3")
        buf.write("\u0305\3\2\2\2\u00d5\u0312\3\2\2\2\u00d7\u0316\3\2\2\2")
        buf.write("\u00d9\u0318\3\2\2\2\u00db\u00dc\t\2\2\2\u00dc\4\3\2\2")
        buf.write("\2\u00dd\u00de\t\3\2\2\u00de\6\3\2\2\2\u00df\u00e0\t\4")
        buf.write("\2\2\u00e0\b\3\2\2\2\u00e1\u00e2\7p\2\2\u00e2\u00e3\7")
        buf.write("o\2\2\u00e3\u00e4\7q\2\2\u00e4\u00e5\7f\2\2\u00e5\n\3")
        buf.write("\2\2\2\u00e6\u00e7\7o\2\2\u00e7\u00e8\7c\2\2\u00e8\u00e9")
        buf.write("\7k\2\2\u00e9\u00ea\7p\2\2\u00ea\f\3\2\2\2\u00eb\u00ec")
        buf.write("\7x\2\2\u00ec\u00ed\7c\2\2\u00ed\u00ee\7t\2\2\u00ee\16")
        buf.write("\3\2\2\2\u00ef\u00f0\7\60\2\2\u00f0\20\3\2\2\2\u00f1\u00f2")
        buf.write("\7=\2\2\u00f2\22\3\2\2\2\u00f3\u00f4\7<\2\2\u00f4\24\3")
        buf.write("\2\2\2\u00f5\u00f6\7.\2\2\u00f6\26\3\2\2\2\u00f7\u00f8")
        buf.write("\7]\2\2\u00f8\30\3\2\2\2\u00f9\u00fa\7_\2\2\u00fa\32\3")
        buf.write("\2\2\2\u00fb\u00fc\7*\2\2\u00fc\34\3\2\2\2\u00fd\u00fe")
        buf.write("\7+\2\2\u00fe\36\3\2\2\2\u00ff\u0100\7}\2\2\u0100 \3\2")
        buf.write("\2\2\u0101\u0102\7\177\2\2\u0102\"\3\2\2\2\u0103\u0104")
        buf.write("\7>\2\2\u0104\u0105\7/\2\2\u0105$\3\2\2\2\u0106\u0107")
        buf.write("\7h\2\2\u0107\u0108\7w\2\2\u0108\u0109\7p\2\2\u0109\u010a")
        buf.write("\7e\2\2\u010a&\3\2\2\2\u010b\u010c\7g\2\2\u010c\u010d")
        buf.write("\7t\2\2\u010d\u010e\7t\2\2\u010e\u010f\7q\2\2\u010f\u0110")
        buf.write("\7t\2\2\u0110(\3\2\2\2\u0111\u0112\7p\2\2\u0112\u0113")
        buf.write("\7w\2\2\u0113\u0114\7n\2\2\u0114\u0115\7n\2\2\u0115*\3")
        buf.write("\2\2\2\u0116\u0117\7x\2\2\u0117\u0118\7q\2\2\u0118\u0119")
        buf.write("\7k\2\2\u0119\u011a\7f\2\2\u011a,\3\2\2\2\u011b\u011c")
        buf.write("\7k\2\2\u011c\u011d\7p\2\2\u011d\u011e\7v\2\2\u011e.\3")
        buf.write("\2\2\2\u011f\u0120\7h\2\2\u0120\u0121\7n\2\2\u0121\u0122")
        buf.write("\7q\2\2\u0122\u0123\7c\2\2\u0123\u0124\7v\2\2\u0124\60")
        buf.write("\3\2\2\2\u0125\u0126\7e\2\2\u0126\u0127\7j\2\2\u0127\u0128")
        buf.write("\7c\2\2\u0128\u0129\7t\2\2\u0129\62\3\2\2\2\u012a\u012b")
        buf.write("\7k\2\2\u012b\u012c\7h\2\2\u012c\64\3\2\2\2\u012d\u012e")
        buf.write("\7g\2\2\u012e\u012f\7n\2\2\u012f\u0130\7u\2\2\u0130\u0131")
        buf.write("\7g\2\2\u0131\66\3\2\2\2\u0132\u0133\7y\2\2\u0133\u0134")
        buf.write("\7j\2\2\u0134\u0135\7k\2\2\u0135\u0136\7n\2\2\u0136\u0137")
        buf.write("\7g\2\2\u01378\3\2\2\2\u0138\u0139\7t\2\2\u0139\u013a")
        buf.write("\7g\2\2\u013a\u013b\7c\2\2\u013b\u013c\7f\2\2\u013c:\3")
        buf.write("\2\2\2\u013d\u013e\7r\2\2\u013e\u013f\7t\2\2\u013f\u0140")
        buf.write("\7k\2\2\u0140\u0141\7p\2\2\u0141\u0142\7v\2\2\u0142<\3")
        buf.write("\2\2\2\u0143\u0144\7?\2\2\u0144>\3\2\2\2\u0145\u0146\7")
        buf.write("c\2\2\u0146\u0147\7p\2\2\u0147\u0148\7f\2\2\u0148@\3\2")
        buf.write("\2\2\u0149\u014a\7q\2\2\u014a\u014b\7t\2\2\u014bB\3\2")
        buf.write("\2\2\u014c\u014d\7p\2\2\u014d\u014e\7q\2\2\u014e\u014f")
        buf.write("\7v\2\2\u014fD\3\2\2\2\u0150\u0151\7@\2\2\u0151F\3\2\2")
        buf.write("\2\u0152\u0153\7@\2\2\u0153\u0154\7?\2\2\u0154H\3\2\2")
        buf.write("\2\u0155\u0156\7>\2\2\u0156J\3\2\2\2\u0157\u0158\7>\2")
        buf.write("\2\u0158\u0159\7?\2\2\u0159L\3\2\2\2\u015a\u015b\7g\2")
        buf.write("\2\u015b\u015c\7s\2\2\u015c\u015d\7w\2\2\u015d\u015e\7")
        buf.write("c\2\2\u015e\u015f\7n\2\2\u015fN\3\2\2\2\u0160\u0161\7")
        buf.write("-\2\2\u0161P\3\2\2\2\u0162\u0163\7/\2\2\u0163R\3\2\2\2")
        buf.write("\u0164\u0165\7,\2\2\u0165T\3\2\2\2\u0166\u0167\7\61\2")
        buf.write("\2\u0167V\3\2\2\2\u0168\u0169\7\'\2\2\u0169X\3\2\2\2\u016a")
        buf.write("\u016b\7t\2\2\u016b\u016c\7g\2\2\u016c\u016d\7v\2\2\u016d")
        buf.write("\u016e\7w\2\2\u016e\u016f\7t\2\2\u016f\u0170\7p\2\2\u0170")
        buf.write("Z\3\2\2\2\u0171\u0172\7t\2\2\u0172\u0173\7p\2\2\u0173")
        buf.write("\u0174\7q\2\2\u0174\u0175\7o\2\2\u0175\\\3\2\2\2\u0176")
        buf.write("\u0177\7t\2\2\u0177\u0178\7g\2\2\u0178\u0179\7z\2\2\u0179")
        buf.write("\u017a\7r\2\2\u017a^\3\2\2\2\u017b\u017c\7t\2\2\u017c")
        buf.write("\u017d\7i\2\2\u017d\u017e\7c\2\2\u017e\u017f\7o\2\2\u017f")
        buf.write("\u0180\7o\2\2\u0180\u0181\7c\2\2\u0181`\3\2\2\2\u0182")
        buf.write("\u0183\7r\2\2\u0183\u0184\7q\2\2\u0184\u0185\7k\2\2\u0185")
        buf.write("\u0186\7p\2\2\u0186\u0187\7v\2\2\u0187\u0188\7u\2\2\u0188")
        buf.write("b\3\2\2\2\u0189\u018a\7n\2\2\u018a\u018b\7k\2\2\u018b")
        buf.write("\u018c\7p\2\2\u018c\u018d\7g\2\2\u018d\u018e\7u\2\2\u018e")
        buf.write("d\3\2\2\2\u018f\u0190\7v\2\2\u0190\u0191\7g\2\2\u0191")
        buf.write("\u0192\7z\2\2\u0192\u0193\7v\2\2\u0193f\3\2\2\2\u0194")
        buf.write("\u0195\7d\2\2\u0195\u0196\7c\2\2\u0196\u0197\7t\2\2\u0197")
        buf.write("\u0198\7r\2\2\u0198\u0199\7n\2\2\u0199\u019a\7q\2\2\u019a")
        buf.write("\u019b\7v\2\2\u019bh\3\2\2\2\u019c\u019d\7f\2\2\u019d")
        buf.write("\u019e\7q\2\2\u019e\u019f\7v\2\2\u019f\u01a0\7e\2\2\u01a0")
        buf.write("\u01a1\7j\2\2\u01a1\u01a2\7c\2\2\u01a2\u01a3\7t\2\2\u01a3")
        buf.write("\u01a4\7v\2\2\u01a4j\3\2\2\2\u01a5\u01a6\7r\2\2\u01a6")
        buf.write("\u01a7\7k\2\2\u01a7\u01a8\7g\2\2\u01a8\u01a9\7e\2\2\u01a9")
        buf.write("\u01aa\7j\2\2\u01aa\u01ab\7c\2\2\u01ab\u01ac\7t\2\2\u01ac")
        buf.write("\u01ad\7v\2\2\u01adl\3\2\2\2\u01ae\u01af\7z\2\2\u01af")
        buf.write("\u01b0\7{\2\2\u01b0\u01b1\7r\2\2\u01b1\u01b2\7n\2\2\u01b2")
        buf.write("\u01b3\7q\2\2\u01b3\u01b4\7v\2\2\u01b4n\3\2\2\2\u01b5")
        buf.write("\u01b6\7f\2\2\u01b6\u01b7\7g\2\2\u01b7\u01b8\7p\2\2\u01b8")
        buf.write("\u01b9\7u\2\2\u01b9\u01ba\7k\2\2\u01ba\u01bb\7v\2\2\u01bb")
        buf.write("\u01bc\7{\2\2\u01bc\u01bd\7r\2\2\u01bd\u01be\7n\2\2\u01be")
        buf.write("\u01bf\7q\2\2\u01bf\u01c0\7v\2\2\u01c0p\3\2\2\2\u01c1")
        buf.write("\u01c2\7j\2\2\u01c2\u01c3\7k\2\2\u01c3\u01c4\7u\2\2\u01c4")
        buf.write("\u01c5\7v\2\2\u01c5\u01c6\7q\2\2\u01c6\u01c7\7i\2\2\u01c7")
        buf.write("\u01c8\7t\2\2\u01c8\u01c9\7c\2\2\u01c9\u01ca\7o\2\2\u01ca")
        buf.write("r\3\2\2\2\u01cb\u01cc\7u\2\2\u01cc\u01cd\7k\2\2\u01cd")
        buf.write("\u01ce\7p\2\2\u01cet\3\2\2\2\u01cf\u01d0\7e\2\2\u01d0")
        buf.write("\u01d1\7q\2\2\u01d1\u01d2\7u\2\2\u01d2v\3\2\2\2\u01d3")
        buf.write("\u01d4\7v\2\2\u01d4\u01d5\7c\2\2\u01d5\u01d6\7p\2\2\u01d6")
        buf.write("x\3\2\2\2\u01d7\u01d8\7c\2\2\u01d8\u01d9\7u\2\2\u01d9")
        buf.write("\u01da\7k\2\2\u01da\u01db\7p\2\2\u01dbz\3\2\2\2\u01dc")
        buf.write("\u01dd\7c\2\2\u01dd\u01de\7e\2\2\u01de\u01df\7q\2\2\u01df")
        buf.write("\u01e0\7u\2\2\u01e0|\3\2\2\2\u01e1\u01e2\7c\2\2\u01e2")
        buf.write("\u01e3\7v\2\2\u01e3\u01e4\7c\2\2\u01e4\u01e5\7p\2\2\u01e5")
        buf.write("~\3\2\2\2\u01e6\u01e7\7c\2\2\u01e7\u01e8\7v\2\2\u01e8")
        buf.write("\u01e9\7c\2\2\u01e9\u01ea\7p\2\2\u01ea\u01eb\7\64\2\2")
        buf.write("\u01eb\u0080\3\2\2\2\u01ec\u01ed\7n\2\2\u01ed\u01ee\7")
        buf.write("q\2\2\u01ee\u01ef\7i\2\2\u01ef\u0082\3\2\2\2\u01f0\u01f1")
        buf.write("\7n\2\2\u01f1\u01f2\7q\2\2\u01f2\u01f3\7i\2\2\u01f3\u01f4")
        buf.write("\7\63\2\2\u01f4\u01f5\7\62\2\2\u01f5\u0084\3\2\2\2\u01f6")
        buf.write("\u01f7\7g\2\2\u01f7\u01f8\7z\2\2\u01f8\u01f9\7r\2\2\u01f9")
        buf.write("\u0086\3\2\2\2\u01fa\u01fb\7h\2\2\u01fb\u01fc\7a\2\2\u01fc")
        buf.write("\u01fd\7o\2\2\u01fd\u01fe\7c\2\2\u01fe\u01ff\7z\2\2\u01ff")
        buf.write("\u0088\3\2\2\2\u0200\u0201\7h\2\2\u0201\u0202\7a\2\2\u0202")
        buf.write("\u0203\7o\2\2\u0203\u0204\7k\2\2\u0204\u0205\7p\2\2\u0205")
        buf.write("\u008a\3\2\2\2\u0206\u0207\7h\2\2\u0207\u0208\7a\2\2\u0208")
        buf.write("\u0209\7t\2\2\u0209\u020a\7c\2\2\u020a\u020b\7p\2\2\u020b")
        buf.write("\u020c\7i\2\2\u020c\u020d\7g\2\2\u020d\u008c\3\2\2\2\u020e")
        buf.write("\u020f\7h\2\2\u020f\u0210\7a\2\2\u0210\u0211\7u\2\2\u0211")
        buf.write("\u0212\7w\2\2\u0212\u0213\7o\2\2\u0213\u008e\3\2\2\2\u0214")
        buf.write("\u0215\7f\2\2\u0215\u0216\7k\2\2\u0216\u0217\7h\2\2\u0217")
        buf.write("\u0218\7h\2\2\u0218\u0090\3\2\2\2\u0219\u021a\7r\2\2\u021a")
        buf.write("\u021b\7t\2\2\u021b\u021c\7q\2\2\u021c\u021d\7f\2\2\u021d")
        buf.write("\u0092\3\2\2\2\u021e\u021f\7o\2\2\u021f\u0220\7g\2\2\u0220")
        buf.write("\u0221\7c\2\2\u0221\u0222\7p\2\2\u0222\u0094\3\2\2\2\u0223")
        buf.write("\u0224\7o\2\2\u0224\u0225\7g\2\2\u0225\u0226\7f\2\2\u0226")
        buf.write("\u0227\7k\2\2\u0227\u0228\7c\2\2\u0228\u0229\7p\2\2\u0229")
        buf.write("\u0096\3\2\2\2\u022a\u022b\7s\2\2\u022b\u022c\7w\2\2\u022c")
        buf.write("\u022d\7c\2\2\u022d\u022e\7p\2\2\u022e\u022f\7v\2\2\u022f")
        buf.write("\u0230\7k\2\2\u0230\u0231\7n\2\2\u0231\u0232\7g\2\2\u0232")
        buf.write("\u0098\3\2\2\2\u0233\u0234\7t\2\2\u0234\u0235\7c\2\2\u0235")
        buf.write("\u0236\7p\2\2\u0236\u0237\7m\2\2\u0237\u009a\3\2\2\2\u0238")
        buf.write("\u0239\7x\2\2\u0239\u023a\7c\2\2\u023a\u023b\7t\2\2\u023b")
        buf.write("\u023c\7k\2\2\u023c\u023d\7c\2\2\u023d\u023e\7p\2\2\u023e")
        buf.write("\u023f\7e\2\2\u023f\u0240\7g\2\2\u0240\u009c\3\2\2\2\u0241")
        buf.write("\u0242\7u\2\2\u0242\u0243\7f\2\2\u0243\u009e\3\2\2\2\u0244")
        buf.write("\u0245\7e\2\2\u0245\u0246\7q\2\2\u0246\u0247\7t\2\2\u0247")
        buf.write("\u00a0\3\2\2\2\u0248\u0249\7e\2\2\u0249\u024a\7q\2\2\u024a")
        buf.write("\u024b\7x\2\2\u024b\u00a2\3\2\2\2\u024c\u024d\7h\2\2\u024d")
        buf.write("\u024e\7a\2\2\u024e\u024f\7t\2\2\u024f\u0250\7q\2\2\u0250")
        buf.write("\u0251\7w\2\2\u0251\u0252\7p\2\2\u0252\u0253\7f\2\2\u0253")
        buf.write("\u00a4\3\2\2\2\u0254\u0255\7v\2\2\u0255\u0256\7t\2\2\u0256")
        buf.write("\u0257\7c\2\2\u0257\u0258\7p\2\2\u0258\u0259\7u\2\2\u0259")
        buf.write("\u025a\7r\2\2\u025a\u025b\7q\2\2\u025b\u025c\7u\2\2\u025c")
        buf.write("\u025d\7g\2\2\u025d\u00a6\3\2\2\2\u025e\u025f\7f\2\2\u025f")
        buf.write("\u0260\7k\2\2\u0260\u0261\7c\2\2\u0261\u0262\7i\2\2\u0262")
        buf.write("\u0263\7q\2\2\u0263\u0264\7p\2\2\u0264\u0265\7c\2\2\u0265")
        buf.write("\u0266\7n\2\2\u0266\u00a8\3\2\2\2\u0267\u0268\7i\2\2\u0268")
        buf.write("\u0269\7k\2\2\u0269\u026a\7p\2\2\u026a\u026b\7x\2\2\u026b")
        buf.write("\u00aa\3\2\2\2\u026c\u026d\7t\2\2\u026d\u026e\7q\2\2\u026e")
        buf.write("\u026f\7y\2\2\u026f\u0270\7u\2\2\u0270\u0271\7w\2\2\u0271")
        buf.write("\u0272\7o\2\2\u0272\u00ac\3\2\2\2\u0273\u0274\7e\2\2\u0274")
        buf.write("\u0275\7q\2\2\u0275\u0276\7n\2\2\u0276\u0277\7u\2\2\u0277")
        buf.write("\u0278\7w\2\2\u0278\u0279\7o\2\2\u0279\u00ae\3\2\2\2\u027a")
        buf.write("\u027b\7n\2\2\u027b\u027c\7q\2\2\u027c\u027d\7c\2\2\u027d")
        buf.write("\u027e\7f\2\2\u027e\u00b0\3\2\2\2\u027f\u0280\7f\2\2\u0280")
        buf.write("\u0281\7c\2\2\u0281\u0282\7v\2\2\u0282\u0283\7c\2\2\u0283")
        buf.write("\u00b2\3\2\2\2\u0284\u0285\7n\2\2\u0285\u0286\7k\2\2\u0286")
        buf.write("\u0287\7d\2\2\u0287\u0288\7t\2\2\u0288\u0289\7c\2\2\u0289")
        buf.write("\u028a\7t\2\2\u028a\u028b\7{\2\2\u028b\u00b4\3\2\2\2\u028c")
        buf.write("\u028d\7t\2\2\u028d\u028e\7r\2\2\u028e\u028f\7q\2\2\u028f")
        buf.write("\u0290\7k\2\2\u0290\u0291\7u\2\2\u0291\u00b6\3\2\2\2\u0292")
        buf.write("\u0293\7t\2\2\u0293\u0294\7y\2\2\u0294\u0295\7g\2\2\u0295")
        buf.write("\u0296\7k\2\2\u0296\u0297\7d\2\2\u0297\u0298\7w\2\2\u0298")
        buf.write("\u0299\7n\2\2\u0299\u029a\7n\2\2\u029a\u00b8\3\2\2\2\u029b")
        buf.write("\u029c\7t\2\2\u029c\u029d\7d\2\2\u029d\u029e\7k\2\2\u029e")
        buf.write("\u029f\7p\2\2\u029f\u02a0\7q\2\2\u02a0\u02a1\7o\2\2\u02a1")
        buf.write("\u00ba\3\2\2\2\u02a2\u02a3\7t\2\2\u02a3\u02a4\7i\2\2\u02a4")
        buf.write("\u02a5\7g\2\2\u02a5\u02a6\7q\2\2\u02a6\u02a7\7o\2\2\u02a7")
        buf.write("\u00bc\3\2\2\2\u02a8\u02a9\7t\2\2\u02a9\u02aa\7w\2\2\u02aa")
        buf.write("\u02ab\7p\2\2\u02ab\u02ac\7k\2\2\u02ac\u02ad\7h\2\2\u02ad")
        buf.write("\u00be\3\2\2\2\u02ae\u02af\7r\2\2\u02af\u02b0\7g\2\2\u02b0")
        buf.write("\u02b1\7c\2\2\u02b1\u02b2\7t\2\2\u02b2\u02b3\7u\2\2\u02b3")
        buf.write("\u02b4\7q\2\2\u02b4\u02b5\7p\2\2\u02b5\u00c0\3\2\2\2\u02b6")
        buf.write("\u02b7\7m\2\2\u02b7\u02b8\7g\2\2\u02b8\u02b9\7p\2\2\u02b9")
        buf.write("\u02ba\7f\2\2\u02ba\u02bb\7c\2\2\u02bb\u02bc\7n\2\2\u02bc")
        buf.write("\u02bd\7n\2\2\u02bd\u00c2\3\2\2\2\u02be\u02bf\7u\2\2\u02bf")
        buf.write("\u02c0\7r\2\2\u02c0\u02c1\7g\2\2\u02c1\u02c2\7c\2\2\u02c2")
        buf.write("\u02c3\7t\2\2\u02c3\u02c4\7o\2\2\u02c4\u02c5\7c\2\2\u02c5")
        buf.write("\u02c6\7p\2\2\u02c6\u00c4\3\2\2\2\u02c7\u02c8\t\5\2\2")
        buf.write("\u02c8\u02c9\3\2\2\2\u02c9\u02ca\bc\2\2\u02ca\u00c6\3")
        buf.write("\2\2\2\u02cb\u02cd\7\17\2\2\u02cc\u02cb\3\2\2\2\u02cc")
        buf.write("\u02cd\3\2\2\2\u02cd\u02ce\3\2\2\2\u02ce\u02d1\7\f\2\2")
        buf.write("\u02cf\u02d1\7\17\2\2\u02d0\u02cc\3\2\2\2\u02d0\u02cf")
        buf.write("\3\2\2\2\u02d1\u02d2\3\2\2\2\u02d2\u02d3\bd\2\2\u02d3")
        buf.write("\u00c8\3\2\2\2\u02d4\u02d8\7%\2\2\u02d5\u02d7\n\6\2\2")
        buf.write("\u02d6\u02d5\3\2\2\2\u02d7\u02da\3\2\2\2\u02d8\u02d6\3")
        buf.write("\2\2\2\u02d8\u02d9\3\2\2\2\u02d9\u02db\3\2\2\2\u02da\u02d8")
        buf.write("\3\2\2\2\u02db\u02dc\be\2\2\u02dc\u00ca\3\2\2\2\u02dd")
        buf.write("\u02de\7\61\2\2\u02de\u02df\7%\2\2\u02df\u02e3\3\2\2\2")
        buf.write("\u02e0\u02e2\13\2\2\2\u02e1\u02e0\3\2\2\2\u02e2\u02e5")
        buf.write("\3\2\2\2\u02e3\u02e4\3\2\2\2\u02e3\u02e1\3\2\2\2\u02e4")
        buf.write("\u02e6\3\2\2\2\u02e5\u02e3\3\2\2\2\u02e6\u02e7\7%\2\2")
        buf.write("\u02e7\u02e8\7\61\2\2\u02e8\u02e9\3\2\2\2\u02e9\u02ea")
        buf.write("\bf\2\2\u02ea\u00cc\3\2\2\2\u02eb\u02ed\5Q)\2\u02ec\u02eb")
        buf.write("\3\2\2\2\u02ec\u02ed\3\2\2\2\u02ed\u02ef\3\2\2\2\u02ee")
        buf.write("\u02f0\5\7\4\2\u02ef\u02ee\3\2\2\2\u02f0\u02f1\3\2\2\2")
        buf.write("\u02f1\u02ef\3\2\2\2\u02f1\u02f2\3\2\2\2\u02f2\u00ce\3")
        buf.write("\2\2\2\u02f3\u02f5\5Q)\2\u02f4\u02f3\3\2\2\2\u02f4\u02f5")
        buf.write("\3\2\2\2\u02f5\u02f6\3\2\2\2\u02f6\u02fd\5\u00cdg\2\u02f7")
        buf.write("\u02f9\5\17\b\2\u02f8\u02fa\5\7\4\2\u02f9\u02f8\3\2\2")
        buf.write("\2\u02fa\u02fb\3\2\2\2\u02fb\u02f9\3\2\2\2\u02fb\u02fc")
        buf.write("\3\2\2\2\u02fc\u02fe\3\2\2\2\u02fd\u02f7\3\2\2\2\u02fd")
        buf.write("\u02fe\3\2\2\2\u02fe\u00d0\3\2\2\2\u02ff\u0301\7)\2\2")
        buf.write("\u0300\u0302\13\2\2\2\u0301\u0300\3\2\2\2\u0301\u0302")
        buf.write("\3\2\2\2\u0302\u0303\3\2\2\2\u0303\u0304\7)\2\2\u0304")
        buf.write("\u00d2\3\2\2\2\u0305\u0309\7$\2\2\u0306\u0308\13\2\2\2")
        buf.write("\u0307\u0306\3\2\2\2\u0308\u030b\3\2\2\2\u0309\u030a\3")
        buf.write("\2\2\2\u0309\u0307\3\2\2\2\u030a\u030c\3\2\2\2\u030b\u0309")
        buf.write("\3\2\2\2\u030c\u030d\7$\2\2\u030d\u00d4\3\2\2\2\u030e")
        buf.write("\u0313\5\3\2\2\u030f\u0313\5\5\3\2\u0310\u0313\5\7\4\2")
        buf.write("\u0311\u0313\7a\2\2\u0312\u030e\3\2\2\2\u0312\u030f\3")
        buf.write("\2\2\2\u0312\u0310\3\2\2\2\u0312\u0311\3\2\2\2\u0313\u0314")
        buf.write("\3\2\2\2\u0314\u0312\3\2\2\2\u0314\u0315\3\2\2\2\u0315")
        buf.write("\u00d6\3\2\2\2\u0316\u0317\7\62\2\2\u0317\u00d8\3\2\2")
        buf.write("\2\u0318\u0319\7\63\2\2\u0319\u00da\3\2\2\2\20\2\u02cc")
        buf.write("\u02d0\u02d8\u02e3\u02ec\u02f1\u02f4\u02fb\u02fd\u0301")
        buf.write("\u0309\u0312\u0314\3\b\2\2")
        return buf.getvalue()


class NmodLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    PROGRAM = 1
    MAIN = 2
    VARIABLES = 3
    PERIOD = 4
    SEMICOLON = 5
    COLON = 6
    COMMA = 7
    LBRACKET = 8
    RBRACKET = 9
    LPRACKET = 10
    RPRACKET = 11
    LCRACKET = 12
    RCRACKET = 13
    ISFUNCTION = 14
    FUNC = 15
    ERROR = 16
    NULL = 17
    VOID = 18
    INT = 19
    FLOAT = 20
    CHAR = 21
    IF = 22
    ELSE = 23
    WHILE = 24
    READ = 25
    PRINT = 26
    EQUALS = 27
    AND = 28
    OR = 29
    NOT = 30
    GREATERTHAN = 31
    GREATEROR = 32
    LESSERTHAN = 33
    LESSEROR = 34
    EQUAL = 35
    PLUS = 36
    MINUS = 37
    TIMES = 38
    DIVISION = 39
    MODULE = 40
    RETURN = 41
    RNOM = 42
    REXP = 43
    RGAMMA = 44
    POINTS = 45
    LINES = 46
    TEXT = 47
    BARPLOT = 48
    DOTCHART = 49
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
    RANK = 73
    VARIANCE = 74
    SD = 75
    COR = 76
    COV = 77
    ROUND = 78
    TRANSPOSE = 79
    DIAGONAL = 80
    GINV = 81
    ROWSUM = 82
    COLSUM = 83
    LOAD = 84
    DATA = 85
    LIBRARY = 86
    RPOIS = 87
    RWEIBULL = 88
    RBINOM = 89
    RGEOM = 90
    RUNIF = 91
    PEARSON = 92
    KENDALL = 93
    SPEARMAN = 94
    WHITESPACE = 95
    NEWLINE = 96
    LINECOMMENT = 97
    MULTICOMMENT = 98
    CTEI = 99
    CTEF = 100
    CTEC = 101
    STRING = 102
    ID = 103
    ZERO = 104
    ONE = 105

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'nmod'", "'main'", "'var'", "'.'", "';'", "':'", "','", "'['", 
            "']'", "'('", "')'", "'{'", "'}'", "'<-'", "'func'", "'error'", 
            "'null'", "'void'", "'int'", "'float'", "'char'", "'if'", "'else'", 
            "'while'", "'read'", "'print'", "'='", "'and'", "'or'", "'not'", 
            "'>'", "'>='", "'<'", "'<='", "'equal'", "'+'", "'-'", "'*'", 
            "'/'", "'%'", "'return'", "'rnom'", "'rexp'", "'rgamma'", "'points'", 
            "'lines'", "'text'", "'barplot'", "'dotchart'", "'piechart'", 
            "'xyplot'", "'densityplot'", "'histogram'", "'sin'", "'cos'", 
            "'tan'", "'asin'", "'acos'", "'atan'", "'atan2'", "'log'", "'log10'", 
            "'exp'", "'f_max'", "'f_min'", "'f_range'", "'f_sum'", "'diff'", 
            "'prod'", "'mean'", "'median'", "'quantile'", "'rank'", "'variance'", 
            "'sd'", "'cor'", "'cov'", "'f_round'", "'transpose'", "'diagonal'", 
            "'ginv'", "'rowsum'", "'colsum'", "'load'", "'data'", "'library'", 
            "'rpois'", "'rweibull'", "'rbinom'", "'rgeom'", "'runif'", "'pearson'", 
            "'kendall'", "'spearman'", "'0'", "'1'" ]

    symbolicNames = [ "<INVALID>",
            "PROGRAM", "MAIN", "VARIABLES", "PERIOD", "SEMICOLON", "COLON", 
            "COMMA", "LBRACKET", "RBRACKET", "LPRACKET", "RPRACKET", "LCRACKET", 
            "RCRACKET", "ISFUNCTION", "FUNC", "ERROR", "NULL", "VOID", "INT", 
            "FLOAT", "CHAR", "IF", "ELSE", "WHILE", "READ", "PRINT", "EQUALS", 
            "AND", "OR", "NOT", "GREATERTHAN", "GREATEROR", "LESSERTHAN", 
            "LESSEROR", "EQUAL", "PLUS", "MINUS", "TIMES", "DIVISION", "MODULE", 
            "RETURN", "RNOM", "REXP", "RGAMMA", "POINTS", "LINES", "TEXT", 
            "BARPLOT", "DOTCHART", "PIECHART", "XYPLOT", "DENSITYPLOT", 
            "HISTOGRAM", "SIN", "COS", "TAN", "ASIN", "ACOS", "ATAN", "ATAN2", 
            "LOG", "LOG10", "EXPONENT", "MAX", "MIN", "RANGE", "SUM", "DIFF", 
            "PROD", "MEAN", "MEDIAN", "QUANTILE", "RANK", "VARIANCE", "SD", 
            "COR", "COV", "ROUND", "TRANSPOSE", "DIAGONAL", "GINV", "ROWSUM", 
            "COLSUM", "LOAD", "DATA", "LIBRARY", "RPOIS", "RWEIBULL", "RBINOM", 
            "RGEOM", "RUNIF", "PEARSON", "KENDALL", "SPEARMAN", "WHITESPACE", 
            "NEWLINE", "LINECOMMENT", "MULTICOMMENT", "CTEI", "CTEF", "CTEC", 
            "STRING", "ID", "ZERO", "ONE" ]

    ruleNames = [ "LOWERCASE", "UPPERCASE", "DIGIT", "PROGRAM", "MAIN", 
                  "VARIABLES", "PERIOD", "SEMICOLON", "COLON", "COMMA", 
                  "LBRACKET", "RBRACKET", "LPRACKET", "RPRACKET", "LCRACKET", 
                  "RCRACKET", "ISFUNCTION", "FUNC", "ERROR", "NULL", "VOID", 
                  "INT", "FLOAT", "CHAR", "IF", "ELSE", "WHILE", "READ", 
                  "PRINT", "EQUALS", "AND", "OR", "NOT", "GREATERTHAN", 
                  "GREATEROR", "LESSERTHAN", "LESSEROR", "EQUAL", "PLUS", 
                  "MINUS", "TIMES", "DIVISION", "MODULE", "RETURN", "RNOM", 
                  "REXP", "RGAMMA", "POINTS", "LINES", "TEXT", "BARPLOT", 
                  "DOTCHART", "PIECHART", "XYPLOT", "DENSITYPLOT", "HISTOGRAM", 
                  "SIN", "COS", "TAN", "ASIN", "ACOS", "ATAN", "ATAN2", 
                  "LOG", "LOG10", "EXPONENT", "MAX", "MIN", "RANGE", "SUM", 
                  "DIFF", "PROD", "MEAN", "MEDIAN", "QUANTILE", "RANK", 
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


