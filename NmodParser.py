# Generated from Nmod.g4 by ANTLR 4.7
# encoding: utf-8
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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3l")
        buf.write("\u03a6\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:\4;\t")
        buf.write(";\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\tC\4D\t")
        buf.write("D\4E\tE\4F\tF\4G\tG\4H\tH\4I\tI\4J\tJ\3\2\3\2\3\2\3\2")
        buf.write("\3\2\7\2\u009a\n\2\f\2\16\2\u009d\13\2\3\2\7\2\u00a0\n")
        buf.write("\2\f\2\16\2\u00a3\13\2\3\2\3\2\3\3\3\3\3\4\3\4\3\4\3\4")
        buf.write("\3\4\3\4\3\4\7\4\u00b0\n\4\f\4\16\4\u00b3\13\4\3\4\3\4")
        buf.write("\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\5\5\u00bf\n\5\3\6\3\6")
        buf.write("\3\6\3\6\3\6\5\6\u00c6\n\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6")
        buf.write("\3\6\3\6\7\6\u00d1\n\6\f\6\16\6\u00d4\13\6\5\6\u00d6\n")
        buf.write("\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\b\3\b\7\b\u00e3")
        buf.write("\n\b\f\b\16\b\u00e6\13\b\3\b\3\b\3\t\3\t\3\t\3\n\3\n\3")
        buf.write("\n\3\n\3\n\3\n\5\n\u00f3\n\n\3\13\3\13\3\13\3\13\3\13")
        buf.write("\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3")
        buf.write("\f\5\f\u0107\n\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3")
        buf.write("\r\3\16\3\16\3\16\3\16\3\16\3\16\7\16\u0119\n\16\f\16")
        buf.write("\16\16\u011c\13\16\5\16\u011e\n\16\3\16\3\16\3\16\3\17")
        buf.write("\3\17\3\17\3\17\3\17\3\17\3\17\7\17\u012a\n\17\f\17\16")
        buf.write("\17\u012d\13\17\5\17\u012f\n\17\3\17\3\17\3\17\3\20\3")
        buf.write("\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20")
        buf.write("\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20")
        buf.write("\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20")
        buf.write("\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20")
        buf.write("\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20")
        buf.write("\3\20\3\20\3\20\3\20\3\20\3\20\7\20\u0172\n\20\f\20\16")
        buf.write("\20\u0175\13\20\5\20\u0177\n\20\3\20\3\20\5\20\u017b\n")
        buf.write("\20\3\21\3\21\3\21\3\21\3\21\3\21\6\21\u0183\n\21\r\21")
        buf.write("\16\21\u0184\3\21\3\21\6\21\u0189\n\21\r\21\16\21\u018a")
        buf.write("\3\21\3\21\5\21\u018f\n\21\3\22\3\22\3\22\3\22\3\22\3")
        buf.write("\22\3\22\3\22\6\22\u0199\n\22\r\22\16\22\u019a\3\22\3")
        buf.write("\22\6\22\u019f\n\22\r\22\16\22\u01a0\3\22\3\22\5\22\u01a5")
        buf.write("\n\22\3\23\3\23\3\23\6\23\u01aa\n\23\r\23\16\23\u01ab")
        buf.write("\3\23\6\23\u01af\n\23\r\23\16\23\u01b0\3\23\3\23\5\23")
        buf.write("\u01b5\n\23\3\24\3\24\3\24\6\24\u01ba\n\24\r\24\16\24")
        buf.write("\u01bb\3\24\6\24\u01bf\n\24\r\24\16\24\u01c0\3\24\3\24")
        buf.write("\5\24\u01c5\n\24\3\25\3\25\3\25\3\25\3\25\5\25\u01cc\n")
        buf.write("\25\3\25\3\25\3\25\5\25\u01d1\n\25\3\26\3\26\3\26\3\26")
        buf.write("\3\26\3\26\3\26\5\26\u01da\n\26\3\27\3\27\3\27\3\27\3")
        buf.write("\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30")
        buf.write("\3\30\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\32\3\32")
        buf.write("\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\33\3\33\3\33")
        buf.write("\3\33\3\33\3\33\3\33\3\33\3\34\3\34\3\34\3\34\3\34\3\34")
        buf.write("\3\34\3\34\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35")
        buf.write("\3\35\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\36")
        buf.write("\3\36\3\36\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37")
        buf.write("\3\37\3\37\3\37\3 \3 \3 \3 \3 \3 \3 \3 \3 \3 \3 \3 \3")
        buf.write("!\3!\3!\3!\3!\3!\3!\3!\3!\3!\3!\3!\3\"\3\"\3\"\3\"\3\"")
        buf.write("\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3#\3#\3#\3#\3#\3#\3$\3$\3")
        buf.write("$\3$\3$\3$\3%\3%\3%\3%\3%\3%\3&\3&\3&\3&\3&\3&\3\'\3\'")
        buf.write("\3\'\3\'\3\'\3\'\3(\3(\3(\3(\3(\3(\3)\3)\3)\3)\3)\3)\3")
        buf.write("*\3*\3*\3*\3*\3*\3+\3+\3+\3+\3+\3+\3,\3,\3,\3,\3,\3,\3")
        buf.write("-\3-\3-\3-\3-\7-\u0295\n-\f-\16-\u0298\13-\3-\3-\3-\3")
        buf.write(".\3.\3.\3.\3.\7.\u02a2\n.\f.\16.\u02a5\13.\3.\3.\3.\3")
        buf.write("/\3/\3/\3/\3/\7/\u02af\n/\f/\16/\u02b2\13/\3/\3/\3/\3")
        buf.write("\60\3\60\3\60\3\60\3\60\7\60\u02bc\n\60\f\60\16\60\u02bf")
        buf.write("\13\60\3\60\3\60\3\60\3\61\3\61\3\61\3\61\3\61\3\61\3")
        buf.write("\61\3\61\3\62\3\62\3\62\3\62\3\62\7\62\u02d1\n\62\f\62")
        buf.write("\16\62\u02d4\13\62\3\62\3\62\3\62\3\63\3\63\3\63\3\63")
        buf.write("\3\63\3\63\3\64\3\64\3\64\3\64\3\64\3\64\3\65\3\65\3\65")
        buf.write("\3\65\3\65\7\65\u02ea\n\65\f\65\16\65\u02ed\13\65\3\65")
        buf.write("\3\65\3\65\3\66\3\66\3\66\3\66\3\66\7\66\u02f7\n\66\f")
        buf.write("\66\16\66\u02fa\13\66\3\66\3\66\3\66\3\67\3\67\3\67\3")
        buf.write("\67\3\67\3\67\3\67\3\67\3\67\3\67\3\67\3\67\3\67\3\67")
        buf.write("\3\67\3\67\5\67\u030f\n\67\38\38\38\38\38\38\38\38\39")
        buf.write("\39\39\39\39\39\3:\3:\3:\3:\3:\3:\3:\3:\3:\3:\3;\3;\3")
        buf.write(";\3;\3;\3;\3<\3<\3<\3<\3<\7<\u0334\n<\f<\16<\u0337\13")
        buf.write("<\3<\3<\3<\3=\3=\3=\3=\3=\3=\3>\3>\3>\3>\3>\3>\3?\3?\3")
        buf.write("?\3?\3?\3?\3@\3@\3@\3@\3@\3@\3A\3A\3A\3A\3A\3A\3B\3B\3")
        buf.write("B\3B\3B\7B\u035f\nB\fB\16B\u0362\13B\3B\3B\3B\3C\3C\3")
        buf.write("C\3C\3C\7C\u036c\nC\fC\16C\u036f\13C\3C\3C\3C\3D\3D\3")
        buf.write("D\3D\3D\3D\3E\3E\3E\3E\3E\3E\3E\3E\3E\3E\3F\3F\3F\3F\3")
        buf.write("F\3F\3G\3G\3G\3G\3G\3G\3G\3G\3G\3G\3H\3H\3H\3H\3H\3H\3")
        buf.write("H\3H\3I\3I\3I\3I\3I\3I\3I\3I\3J\3J\3J\2\2K\2\4\6\b\n\f")
        buf.write("\16\20\22\24\26\30\32\34\36 \"$&(*,.\60\62\64\668:<>@")
        buf.write("BDFHJLNPRTVXZ\\^`bdfhjlnprtvxz|~\u0080\u0082\u0084\u0086")
        buf.write("\u0088\u008a\u008c\u008e\u0090\u0092\2\6\3\2\30\32\3\2")
        buf.write("()\3\2*+\3\2eg\2\u03c7\2\u0094\3\2\2\2\4\u00a6\3\2\2\2")
        buf.write("\6\u00a8\3\2\2\2\b\u00b9\3\2\2\2\n\u00c0\3\2\2\2\f\u00db")
        buf.write("\3\2\2\2\16\u00e0\3\2\2\2\20\u00e9\3\2\2\2\22\u00f2\3")
        buf.write("\2\2\2\24\u00f4\3\2\2\2\26\u00fd\3\2\2\2\30\u010a\3\2")
        buf.write("\2\2\32\u0112\3\2\2\2\34\u0122\3\2\2\2\36\u017a\3\2\2")
        buf.write("\2 \u017c\3\2\2\2\"\u0190\3\2\2\2$\u01a6\3\2\2\2&\u01b6")
        buf.write("\3\2\2\2(\u01d0\3\2\2\2*\u01d9\3\2\2\2,\u01db\3\2\2\2")
        buf.write(".\u01df\3\2\2\2\60\u01eb\3\2\2\2\62\u01f3\3\2\2\2\64\u01fd")
        buf.write("\3\2\2\2\66\u0205\3\2\2\28\u020d\3\2\2\2:\u0217\3\2\2")
        buf.write("\2<\u0223\3\2\2\2>\u022f\3\2\2\2@\u023b\3\2\2\2B\u0247")
        buf.write("\3\2\2\2D\u0253\3\2\2\2F\u0259\3\2\2\2H\u025f\3\2\2\2")
        buf.write("J\u0265\3\2\2\2L\u026b\3\2\2\2N\u0271\3\2\2\2P\u0277\3")
        buf.write("\2\2\2R\u027d\3\2\2\2T\u0283\3\2\2\2V\u0289\3\2\2\2X\u028f")
        buf.write("\3\2\2\2Z\u029c\3\2\2\2\\\u02a9\3\2\2\2^\u02b6\3\2\2\2")
        buf.write("`\u02c3\3\2\2\2b\u02cb\3\2\2\2d\u02d8\3\2\2\2f\u02de\3")
        buf.write("\2\2\2h\u02e4\3\2\2\2j\u02f1\3\2\2\2l\u030e\3\2\2\2n\u0310")
        buf.write("\3\2\2\2p\u0318\3\2\2\2r\u031e\3\2\2\2t\u0328\3\2\2\2")
        buf.write("v\u032e\3\2\2\2x\u033b\3\2\2\2z\u0341\3\2\2\2|\u0347\3")
        buf.write("\2\2\2~\u034d\3\2\2\2\u0080\u0353\3\2\2\2\u0082\u0359")
        buf.write("\3\2\2\2\u0084\u0366\3\2\2\2\u0086\u0373\3\2\2\2\u0088")
        buf.write("\u0379\3\2\2\2\u008a\u0383\3\2\2\2\u008c\u0389\3\2\2\2")
        buf.write("\u008e\u0393\3\2\2\2\u0090\u039b\3\2\2\2\u0092\u03a3\3")
        buf.write("\2\2\2\u0094\u0095\7\4\2\2\u0095\u0096\7l\2\2\u0096\u0097")
        buf.write("\b\2\1\2\u0097\u009b\7\n\2\2\u0098\u009a\5\6\4\2\u0099")
        buf.write("\u0098\3\2\2\2\u009a\u009d\3\2\2\2\u009b\u0099\3\2\2\2")
        buf.write("\u009b\u009c\3\2\2\2\u009c\u00a1\3\2\2\2\u009d\u009b\3")
        buf.write("\2\2\2\u009e\u00a0\5\n\6\2\u009f\u009e\3\2\2\2\u00a0\u00a3")
        buf.write("\3\2\2\2\u00a1\u009f\3\2\2\2\u00a1\u00a2\3\2\2\2\u00a2")
        buf.write("\u00a4\3\2\2\2\u00a3\u00a1\3\2\2\2\u00a4\u00a5\5\f\7\2")
        buf.write("\u00a5\3\3\2\2\2\u00a6\u00a7\t\2\2\2\u00a7\5\3\2\2\2\u00a8")
        buf.write("\u00a9\7\6\2\2\u00a9\u00aa\5\b\5\2\u00aa\u00b1\b\4\1\2")
        buf.write("\u00ab\u00ac\7\13\2\2\u00ac\u00ad\5\b\5\2\u00ad\u00ae")
        buf.write("\b\4\1\2\u00ae\u00b0\3\2\2\2\u00af\u00ab\3\2\2\2\u00b0")
        buf.write("\u00b3\3\2\2\2\u00b1\u00af\3\2\2\2\u00b1\u00b2\3\2\2\2")
        buf.write("\u00b2\u00b4\3\2\2\2\u00b3\u00b1\3\2\2\2\u00b4\u00b5\7")
        buf.write("\n\2\2\u00b5\u00b6\5\4\3\2\u00b6\u00b7\7\t\2\2\u00b7\u00b8")
        buf.write("\b\4\1\2\u00b8\7\3\2\2\2\u00b9\u00be\7l\2\2\u00ba\u00bb")
        buf.write("\7\f\2\2\u00bb\u00bc\5 \21\2\u00bc\u00bd\7\r\2\2\u00bd")
        buf.write("\u00bf\3\2\2\2\u00be\u00ba\3\2\2\2\u00be\u00bf\3\2\2\2")
        buf.write("\u00bf\t\3\2\2\2\u00c0\u00c1\7l\2\2\u00c1\u00c2\b\6\1")
        buf.write("\2\u00c2\u00c5\7\22\2\2\u00c3\u00c6\7\27\2\2\u00c4\u00c6")
        buf.write("\5\4\3\2\u00c5\u00c3\3\2\2\2\u00c5\u00c4\3\2\2\2\u00c6")
        buf.write("\u00c7\3\2\2\2\u00c7\u00c8\7\24\2\2\u00c8\u00c9\b\6\1")
        buf.write("\2\u00c9\u00d5\7\16\2\2\u00ca\u00cb\5\20\t\2\u00cb\u00d2")
        buf.write("\b\6\1\2\u00cc\u00cd\7\13\2\2\u00cd\u00ce\5\20\t\2\u00ce")
        buf.write("\u00cf\b\6\1\2\u00cf\u00d1\3\2\2\2\u00d0\u00cc\3\2\2\2")
        buf.write("\u00d1\u00d4\3\2\2\2\u00d2\u00d0\3\2\2\2\u00d2\u00d3\3")
        buf.write("\2\2\2\u00d3\u00d6\3\2\2\2\u00d4\u00d2\3\2\2\2\u00d5\u00ca")
        buf.write("\3\2\2\2\u00d5\u00d6\3\2\2\2\u00d6\u00d7\3\2\2\2\u00d7")
        buf.write("\u00d8\b\6\1\2\u00d8\u00d9\7\17\2\2\u00d9\u00da\5\16\b")
        buf.write("\2\u00da\13\3\2\2\2\u00db\u00dc\7\5\2\2\u00dc\u00dd\7")
        buf.write("\16\2\2\u00dd\u00de\7\17\2\2\u00de\u00df\5\16\b\2\u00df")
        buf.write("\r\3\2\2\2\u00e0\u00e4\7\20\2\2\u00e1\u00e3\5\22\n\2\u00e2")
        buf.write("\u00e1\3\2\2\2\u00e3\u00e6\3\2\2\2\u00e4\u00e2\3\2\2\2")
        buf.write("\u00e4\u00e5\3\2\2\2\u00e5\u00e7\3\2\2\2\u00e6\u00e4\3")
        buf.write("\2\2\2\u00e7\u00e8\7\21\2\2\u00e8\17\3\2\2\2\u00e9\u00ea")
        buf.write("\5\4\3\2\u00ea\u00eb\5*\26\2\u00eb\21\3\2\2\2\u00ec\u00f3")
        buf.write("\5\24\13\2\u00ed\u00f3\5\26\f\2\u00ee\u00f3\5\32\16\2")
        buf.write("\u00ef\u00f3\5\34\17\2\u00f0\u00f3\5\30\r\2\u00f1\u00f3")
        buf.write("\5\36\20\2\u00f2\u00ec\3\2\2\2\u00f2\u00ed\3\2\2\2\u00f2")
        buf.write("\u00ee\3\2\2\2\u00f2\u00ef\3\2\2\2\u00f2\u00f0\3\2\2\2")
        buf.write("\u00f2\u00f1\3\2\2\2\u00f3\23\3\2\2\2\u00f4\u00f5\5\b")
        buf.write("\5\2\u00f5\u00f6\b\13\1\2\u00f6\u00f7\7\23\2\2\u00f7\u00f8")
        buf.write("\b\13\1\2\u00f8\u00f9\5 \21\2\u00f9\u00fa\b\13\1\2\u00fa")
        buf.write("\u00fb\7\t\2\2\u00fb\u00fc\b\13\1\2\u00fc\25\3\2\2\2\u00fd")
        buf.write("\u00fe\7\34\2\2\u00fe\u00ff\7\16\2\2\u00ff\u0100\5 \21")
        buf.write("\2\u0100\u0101\b\f\1\2\u0101\u0102\7\17\2\2\u0102\u0106")
        buf.write("\5\16\b\2\u0103\u0104\7\35\2\2\u0104\u0105\b\f\1\2\u0105")
        buf.write("\u0107\5\16\b\2\u0106\u0103\3\2\2\2\u0106\u0107\3\2\2")
        buf.write("\2\u0107\u0108\3\2\2\2\u0108\u0109\b\f\1\2\u0109\27\3")
        buf.write("\2\2\2\u010a\u010b\7\36\2\2\u010b\u010c\7\16\2\2\u010c")
        buf.write("\u010d\5 \21\2\u010d\u010e\b\r\1\2\u010e\u010f\7\17\2")
        buf.write("\2\u010f\u0110\5\16\b\2\u0110\u0111\b\r\1\2\u0111\31\3")
        buf.write("\2\2\2\u0112\u0113\7\37\2\2\u0113\u0114\b\16\1\2\u0114")
        buf.write("\u011d\7\16\2\2\u0115\u011a\5 \21\2\u0116\u0117\7\13\2")
        buf.write("\2\u0117\u0119\5 \21\2\u0118\u0116\3\2\2\2\u0119\u011c")
        buf.write("\3\2\2\2\u011a\u0118\3\2\2\2\u011a\u011b\3\2\2\2\u011b")
        buf.write("\u011e\3\2\2\2\u011c\u011a\3\2\2\2\u011d\u0115\3\2\2\2")
        buf.write("\u011d\u011e\3\2\2\2\u011e\u011f\3\2\2\2\u011f\u0120\7")
        buf.write("\17\2\2\u0120\u0121\7\t\2\2\u0121\33\3\2\2\2\u0122\u0123")
        buf.write("\7 \2\2\u0123\u0124\b\17\1\2\u0124\u012e\7\16\2\2\u0125")
        buf.write("\u0126\5 \21\2\u0126\u012b\b\17\1\2\u0127\u0128\7\13\2")
        buf.write("\2\u0128\u012a\5 \21\2\u0129\u0127\3\2\2\2\u012a\u012d")
        buf.write("\3\2\2\2\u012b\u0129\3\2\2\2\u012b\u012c\3\2\2\2\u012c")
        buf.write("\u012f\3\2\2\2\u012d\u012b\3\2\2\2\u012e\u0125\3\2\2\2")
        buf.write("\u012e\u012f\3\2\2\2\u012f\u0130\3\2\2\2\u0130\u0131\7")
        buf.write("\17\2\2\u0131\u0132\7\t\2\2\u0132\35\3\2\2\2\u0133\u017b")
        buf.write("\5,\27\2\u0134\u017b\5.\30\2\u0135\u017b\5\60\31\2\u0136")
        buf.write("\u017b\5\62\32\2\u0137\u017b\5\64\33\2\u0138\u017b\5\66")
        buf.write("\34\2\u0139\u017b\58\35\2\u013a\u017b\5:\36\2\u013b\u017b")
        buf.write("\5<\37\2\u013c\u017b\5> \2\u013d\u017b\5@!\2\u013e\u017b")
        buf.write("\5B\"\2\u013f\u017b\5D#\2\u0140\u017b\5F$\2\u0141\u017b")
        buf.write("\5H%\2\u0142\u017b\5J&\2\u0143\u017b\5L\'\2\u0144\u017b")
        buf.write("\5N(\2\u0145\u017b\5P)\2\u0146\u017b\5R*\2\u0147\u017b")
        buf.write("\5T+\2\u0148\u017b\5V,\2\u0149\u017b\5X-\2\u014a\u017b")
        buf.write("\5Z.\2\u014b\u017b\5\\/\2\u014c\u017b\5^\60\2\u014d\u017b")
        buf.write("\5`\61\2\u014e\u017b\5b\62\2\u014f\u017b\5d\63\2\u0150")
        buf.write("\u017b\5f\64\2\u0151\u017b\5h\65\2\u0152\u017b\5j\66\2")
        buf.write("\u0153\u017b\5l\67\2\u0154\u017b\5n8\2\u0155\u017b\5p")
        buf.write("9\2\u0156\u017b\5r:\2\u0157\u017b\5t;\2\u0158\u017b\5")
        buf.write("v<\2\u0159\u017b\5x=\2\u015a\u017b\5z>\2\u015b\u017b\5")
        buf.write("|?\2\u015c\u017b\5~@\2\u015d\u017b\5\u0080A\2\u015e\u017b")
        buf.write("\5\u0082B\2\u015f\u017b\5\u0084C\2\u0160\u017b\5\u0086")
        buf.write("D\2\u0161\u017b\5\u0088E\2\u0162\u017b\5\u008aF\2\u0163")
        buf.write("\u017b\5\u008cG\2\u0164\u017b\5\u008eH\2\u0165\u017b\5")
        buf.write("\u0090I\2\u0166\u0167\7l\2\2\u0167\u0168\b\20\1\2\u0168")
        buf.write("\u0169\7\16\2\2\u0169\u0176\b\20\1\2\u016a\u016b\5 \21")
        buf.write("\2\u016b\u0173\b\20\1\2\u016c\u016d\7\13\2\2\u016d\u016e")
        buf.write("\b\20\1\2\u016e\u016f\5 \21\2\u016f\u0170\b\20\1\2\u0170")
        buf.write("\u0172\3\2\2\2\u0171\u016c\3\2\2\2\u0172\u0175\3\2\2\2")
        buf.write("\u0173\u0171\3\2\2\2\u0173\u0174\3\2\2\2\u0174\u0177\3")
        buf.write("\2\2\2\u0175\u0173\3\2\2\2\u0176\u016a\3\2\2\2\u0176\u0177")
        buf.write("\3\2\2\2\u0177\u0178\3\2\2\2\u0178\u0179\7\17\2\2\u0179")
        buf.write("\u017b\b\20\1\2\u017a\u0133\3\2\2\2\u017a\u0134\3\2\2")
        buf.write("\2\u017a\u0135\3\2\2\2\u017a\u0136\3\2\2\2\u017a\u0137")
        buf.write("\3\2\2\2\u017a\u0138\3\2\2\2\u017a\u0139\3\2\2\2\u017a")
        buf.write("\u013a\3\2\2\2\u017a\u013b\3\2\2\2\u017a\u013c\3\2\2\2")
        buf.write("\u017a\u013d\3\2\2\2\u017a\u013e\3\2\2\2\u017a\u013f\3")
        buf.write("\2\2\2\u017a\u0140\3\2\2\2\u017a\u0141\3\2\2\2\u017a\u0142")
        buf.write("\3\2\2\2\u017a\u0143\3\2\2\2\u017a\u0144\3\2\2\2\u017a")
        buf.write("\u0145\3\2\2\2\u017a\u0146\3\2\2\2\u017a\u0147\3\2\2\2")
        buf.write("\u017a\u0148\3\2\2\2\u017a\u0149\3\2\2\2\u017a\u014a\3")
        buf.write("\2\2\2\u017a\u014b\3\2\2\2\u017a\u014c\3\2\2\2\u017a\u014d")
        buf.write("\3\2\2\2\u017a\u014e\3\2\2\2\u017a\u014f\3\2\2\2\u017a")
        buf.write("\u0150\3\2\2\2\u017a\u0151\3\2\2\2\u017a\u0152\3\2\2\2")
        buf.write("\u017a\u0153\3\2\2\2\u017a\u0154\3\2\2\2\u017a\u0155\3")
        buf.write("\2\2\2\u017a\u0156\3\2\2\2\u017a\u0157\3\2\2\2\u017a\u0158")
        buf.write("\3\2\2\2\u017a\u0159\3\2\2\2\u017a\u015a\3\2\2\2\u017a")
        buf.write("\u015b\3\2\2\2\u017a\u015c\3\2\2\2\u017a\u015d\3\2\2\2")
        buf.write("\u017a\u015e\3\2\2\2\u017a\u015f\3\2\2\2\u017a\u0160\3")
        buf.write("\2\2\2\u017a\u0161\3\2\2\2\u017a\u0162\3\2\2\2\u017a\u0163")
        buf.write("\3\2\2\2\u017a\u0164\3\2\2\2\u017a\u0165\3\2\2\2\u017a")
        buf.write("\u0166\3\2\2\2\u017b\37\3\2\2\2\u017c\u017d\5\"\22\2\u017d")
        buf.write("\u018e\b\21\1\2\u017e\u017f\7!\2\2\u017f\u0183\7!\2\2")
        buf.write("\u0180\u0181\7\"\2\2\u0181\u0183\7\"\2\2\u0182\u017e\3")
        buf.write("\2\2\2\u0182\u0180\3\2\2\2\u0183\u0184\3\2\2\2\u0184\u0182")
        buf.write("\3\2\2\2\u0184\u0185\3\2\2\2\u0185\u0186\3\2\2\2\u0186")
        buf.write("\u0188\b\21\1\2\u0187\u0189\5\"\22\2\u0188\u0187\3\2\2")
        buf.write("\2\u0189\u018a\3\2\2\2\u018a\u0188\3\2\2\2\u018a\u018b")
        buf.write("\3\2\2\2\u018b\u018c\3\2\2\2\u018c\u018d\b\21\1\2\u018d")
        buf.write("\u018f\3\2\2\2\u018e\u0182\3\2\2\2\u018e\u018f\3\2\2\2")
        buf.write("\u018f!\3\2\2\2\u0190\u0191\5$\23\2\u0191\u01a4\b\22\1")
        buf.write("\2\u0192\u0193\7\23\2\2\u0193\u0199\7\23\2\2\u0194\u0199")
        buf.write("\7%\2\2\u0195\u0199\7$\2\2\u0196\u0199\7\'\2\2\u0197\u0199")
        buf.write("\7&\2\2\u0198\u0192\3\2\2\2\u0198\u0194\3\2\2\2\u0198")
        buf.write("\u0195\3\2\2\2\u0198\u0196\3\2\2\2\u0198\u0197\3\2\2\2")
        buf.write("\u0199\u019a\3\2\2\2\u019a\u0198\3\2\2\2\u019a\u019b\3")
        buf.write("\2\2\2\u019b\u019c\3\2\2\2\u019c\u019e\b\22\1\2\u019d")
        buf.write("\u019f\5$\23\2\u019e\u019d\3\2\2\2\u019f\u01a0\3\2\2\2")
        buf.write("\u01a0\u019e\3\2\2\2\u01a0\u01a1\3\2\2\2\u01a1\u01a2\3")
        buf.write("\2\2\2\u01a2\u01a3\b\22\1\2\u01a3\u01a5\3\2\2\2\u01a4")
        buf.write("\u0198\3\2\2\2\u01a4\u01a5\3\2\2\2\u01a5#\3\2\2\2\u01a6")
        buf.write("\u01a7\5&\24\2\u01a7\u01b4\b\23\1\2\u01a8\u01aa\t\3\2")
        buf.write("\2\u01a9\u01a8\3\2\2\2\u01aa\u01ab\3\2\2\2\u01ab\u01a9")
        buf.write("\3\2\2\2\u01ab\u01ac\3\2\2\2\u01ac\u01ae\3\2\2\2\u01ad")
        buf.write("\u01af\5&\24\2\u01ae\u01ad\3\2\2\2\u01af\u01b0\3\2\2\2")
        buf.write("\u01b0\u01ae\3\2\2\2\u01b0\u01b1\3\2\2\2\u01b1\u01b2\3")
        buf.write("\2\2\2\u01b2\u01b3\b\23\1\2\u01b3\u01b5\3\2\2\2\u01b4")
        buf.write("\u01a9\3\2\2\2\u01b4\u01b5\3\2\2\2\u01b5%\3\2\2\2\u01b6")
        buf.write("\u01b7\5(\25\2\u01b7\u01c4\b\24\1\2\u01b8\u01ba\t\4\2")
        buf.write("\2\u01b9\u01b8\3\2\2\2\u01ba\u01bb\3\2\2\2\u01bb\u01b9")
        buf.write("\3\2\2\2\u01bb\u01bc\3\2\2\2\u01bc\u01be\3\2\2\2\u01bd")
        buf.write("\u01bf\5(\25\2\u01be\u01bd\3\2\2\2\u01bf\u01c0\3\2\2\2")
        buf.write("\u01c0\u01be\3\2\2\2\u01c0\u01c1\3\2\2\2\u01c1\u01c2\3")
        buf.write("\2\2\2\u01c2\u01c3\b\24\1\2\u01c3\u01c5\3\2\2\2\u01c4")
        buf.write("\u01b9\3\2\2\2\u01c4\u01c5\3\2\2\2\u01c5\'\3\2\2\2\u01c6")
        buf.write("\u01c7\7\16\2\2\u01c7\u01c8\5 \21\2\u01c8\u01c9\7\17\2")
        buf.write("\2\u01c9\u01d1\3\2\2\2\u01ca\u01cc\t\3\2\2\u01cb\u01ca")
        buf.write("\3\2\2\2\u01cb\u01cc\3\2\2\2\u01cc\u01cd\3\2\2\2\u01cd")
        buf.write("\u01ce\5*\26\2\u01ce\u01cf\b\25\1\2\u01cf\u01d1\3\2\2")
        buf.write("\2\u01d0\u01c6\3\2\2\2\u01d0\u01cb\3\2\2\2\u01d1)\3\2")
        buf.write("\2\2\u01d2\u01da\5\b\5\2\u01d3\u01da\7\7\2\2\u01d4\u01da")
        buf.write("\7\33\2\2\u01d5\u01da\7-\2\2\u01d6\u01da\7.\2\2\u01d7")
        buf.write("\u01da\7/\2\2\u01d8\u01da\5\36\20\2\u01d9\u01d2\3\2\2")
        buf.write("\2\u01d9\u01d3\3\2\2\2\u01d9\u01d4\3\2\2\2\u01d9\u01d5")
        buf.write("\3\2\2\2\u01d9\u01d6\3\2\2\2\u01d9\u01d7\3\2\2\2\u01d9")
        buf.write("\u01d8\3\2\2\2\u01da+\3\2\2\2\u01db\u01dc\7\60\2\2\u01dc")
        buf.write("\u01dd\5 \21\2\u01dd\u01de\7\t\2\2\u01de-\3\2\2\2\u01df")
        buf.write("\u01e0\7\61\2\2\u01e0\u01e1\7\16\2\2\u01e1\u01e2\5*\26")
        buf.write("\2\u01e2\u01e3\7\13\2\2\u01e3\u01e4\5*\26\2\u01e4\u01e5")
        buf.write("\7\13\2\2\u01e5\u01e6\5*\26\2\u01e6\u01e7\7\13\2\2\u01e7")
        buf.write("\u01e8\5*\26\2\u01e8\u01e9\7\17\2\2\u01e9\u01ea\7\t\2")
        buf.write("\2\u01ea/\3\2\2\2\u01eb\u01ec\7\62\2\2\u01ec\u01ed\7\16")
        buf.write("\2\2\u01ed\u01ee\5*\26\2\u01ee\u01ef\7\13\2\2\u01ef\u01f0")
        buf.write("\5*\26\2\u01f0\u01f1\7\17\2\2\u01f1\u01f2\7\t\2\2\u01f2")
        buf.write("\61\3\2\2\2\u01f3\u01f4\7\63\2\2\u01f4\u01f5\7\16\2\2")
        buf.write("\u01f5\u01f6\5*\26\2\u01f6\u01f7\7\13\2\2\u01f7\u01f8")
        buf.write("\5*\26\2\u01f8\u01f9\7\13\2\2\u01f9\u01fa\5*\26\2\u01fa")
        buf.write("\u01fb\7\17\2\2\u01fb\u01fc\7\t\2\2\u01fc\63\3\2\2\2\u01fd")
        buf.write("\u01fe\7\64\2\2\u01fe\u01ff\7\16\2\2\u01ff\u0200\5*\26")
        buf.write("\2\u0200\u0201\7\13\2\2\u0201\u0202\5*\26\2\u0202\u0203")
        buf.write("\7\17\2\2\u0203\u0204\7\t\2\2\u0204\65\3\2\2\2\u0205\u0206")
        buf.write("\7\65\2\2\u0206\u0207\7\16\2\2\u0207\u0208\5*\26\2\u0208")
        buf.write("\u0209\7\13\2\2\u0209\u020a\5*\26\2\u020a\u020b\7\17\2")
        buf.write("\2\u020b\u020c\7\t\2\2\u020c\67\3\2\2\2\u020d\u020e\7")
        buf.write("\66\2\2\u020e\u020f\7\16\2\2\u020f\u0210\7-\2\2\u0210")
        buf.write("\u0211\7\13\2\2\u0211\u0212\7-\2\2\u0212\u0213\7\13\2")
        buf.write("\2\u0213\u0214\5\b\5\2\u0214\u0215\7\17\2\2\u0215\u0216")
        buf.write("\7\t\2\2\u02169\3\2\2\2\u0217\u0218\7\67\2\2\u0218\u0219")
        buf.write("\7\16\2\2\u0219\u021a\5*\26\2\u021a\u021b\7\13\2\2\u021b")
        buf.write("\u021c\5*\26\2\u021c\u021d\7\13\2\2\u021d\u021e\5*\26")
        buf.write("\2\u021e\u021f\7\13\2\2\u021f\u0220\5*\26\2\u0220\u0221")
        buf.write("\7\17\2\2\u0221\u0222\7\t\2\2\u0222;\3\2\2\2\u0223\u0224")
        buf.write("\78\2\2\u0224\u0225\7\16\2\2\u0225\u0226\5*\26\2\u0226")
        buf.write("\u0227\7\13\2\2\u0227\u0228\5*\26\2\u0228\u0229\7\13\2")
        buf.write("\2\u0229\u022a\5*\26\2\u022a\u022b\7\13\2\2\u022b\u022c")
        buf.write("\5*\26\2\u022c\u022d\7\17\2\2\u022d\u022e\7\t\2\2\u022e")
        buf.write("=\3\2\2\2\u022f\u0230\79\2\2\u0230\u0231\7\16\2\2\u0231")
        buf.write("\u0232\5*\26\2\u0232\u0233\7\13\2\2\u0233\u0234\5*\26")
        buf.write("\2\u0234\u0235\7\13\2\2\u0235\u0236\5*\26\2\u0236\u0237")
        buf.write("\7\13\2\2\u0237\u0238\5*\26\2\u0238\u0239\7\17\2\2\u0239")
        buf.write("\u023a\7\t\2\2\u023a?\3\2\2\2\u023b\u023c\7:\2\2\u023c")
        buf.write("\u023d\7\16\2\2\u023d\u023e\5*\26\2\u023e\u023f\7\13\2")
        buf.write("\2\u023f\u0240\5*\26\2\u0240\u0241\7\13\2\2\u0241\u0242")
        buf.write("\5*\26\2\u0242\u0243\7\13\2\2\u0243\u0244\5*\26\2\u0244")
        buf.write("\u0245\7\17\2\2\u0245\u0246\7\t\2\2\u0246A\3\2\2\2\u0247")
        buf.write("\u0248\7;\2\2\u0248\u0249\7\16\2\2\u0249\u024a\5*\26\2")
        buf.write("\u024a\u024b\7\13\2\2\u024b\u024c\5*\26\2\u024c\u024d")
        buf.write("\7\13\2\2\u024d\u024e\5*\26\2\u024e\u024f\7\13\2\2\u024f")
        buf.write("\u0250\5*\26\2\u0250\u0251\7\17\2\2\u0251\u0252\7\t\2")
        buf.write("\2\u0252C\3\2\2\2\u0253\u0254\7<\2\2\u0254\u0255\7\16")
        buf.write("\2\2\u0255\u0256\5 \21\2\u0256\u0257\7\17\2\2\u0257\u0258")
        buf.write("\7\t\2\2\u0258E\3\2\2\2\u0259\u025a\7=\2\2\u025a\u025b")
        buf.write("\7\16\2\2\u025b\u025c\5 \21\2\u025c\u025d\7\17\2\2\u025d")
        buf.write("\u025e\7\t\2\2\u025eG\3\2\2\2\u025f\u0260\7>\2\2\u0260")
        buf.write("\u0261\7\16\2\2\u0261\u0262\5 \21\2\u0262\u0263\7\17\2")
        buf.write("\2\u0263\u0264\7\t\2\2\u0264I\3\2\2\2\u0265\u0266\7?\2")
        buf.write("\2\u0266\u0267\7\16\2\2\u0267\u0268\5 \21\2\u0268\u0269")
        buf.write("\7\17\2\2\u0269\u026a\7\t\2\2\u026aK\3\2\2\2\u026b\u026c")
        buf.write("\7@\2\2\u026c\u026d\7\16\2\2\u026d\u026e\5 \21\2\u026e")
        buf.write("\u026f\7\17\2\2\u026f\u0270\7\t\2\2\u0270M\3\2\2\2\u0271")
        buf.write("\u0272\7A\2\2\u0272\u0273\7\16\2\2\u0273\u0274\5 \21\2")
        buf.write("\u0274\u0275\7\17\2\2\u0275\u0276\7\t\2\2\u0276O\3\2\2")
        buf.write("\2\u0277\u0278\7B\2\2\u0278\u0279\7\16\2\2\u0279\u027a")
        buf.write("\5 \21\2\u027a\u027b\7\17\2\2\u027b\u027c\7\t\2\2\u027c")
        buf.write("Q\3\2\2\2\u027d\u027e\7C\2\2\u027e\u027f\7\16\2\2\u027f")
        buf.write("\u0280\5 \21\2\u0280\u0281\7\17\2\2\u0281\u0282\7\t\2")
        buf.write("\2\u0282S\3\2\2\2\u0283\u0284\7D\2\2\u0284\u0285\7\16")
        buf.write("\2\2\u0285\u0286\5 \21\2\u0286\u0287\7\17\2\2\u0287\u0288")
        buf.write("\7\t\2\2\u0288U\3\2\2\2\u0289\u028a\7E\2\2\u028a\u028b")
        buf.write("\7\16\2\2\u028b\u028c\5 \21\2\u028c\u028d\7\17\2\2\u028d")
        buf.write("\u028e\7\t\2\2\u028eW\3\2\2\2\u028f\u0290\7F\2\2\u0290")
        buf.write("\u0291\7\16\2\2\u0291\u0296\5 \21\2\u0292\u0293\7\13\2")
        buf.write("\2\u0293\u0295\5 \21\2\u0294\u0292\3\2\2\2\u0295\u0298")
        buf.write("\3\2\2\2\u0296\u0294\3\2\2\2\u0296\u0297\3\2\2\2\u0297")
        buf.write("\u0299\3\2\2\2\u0298\u0296\3\2\2\2\u0299\u029a\7\17\2")
        buf.write("\2\u029a\u029b\7\t\2\2\u029bY\3\2\2\2\u029c\u029d\7G\2")
        buf.write("\2\u029d\u029e\7\16\2\2\u029e\u02a3\5 \21\2\u029f\u02a0")
        buf.write("\7\13\2\2\u02a0\u02a2\5 \21\2\u02a1\u029f\3\2\2\2\u02a2")
        buf.write("\u02a5\3\2\2\2\u02a3\u02a1\3\2\2\2\u02a3\u02a4\3\2\2\2")
        buf.write("\u02a4\u02a6\3\2\2\2\u02a5\u02a3\3\2\2\2\u02a6\u02a7\7")
        buf.write("\17\2\2\u02a7\u02a8\7\t\2\2\u02a8[\3\2\2\2\u02a9\u02aa")
        buf.write("\7H\2\2\u02aa\u02ab\7\16\2\2\u02ab\u02b0\5 \21\2\u02ac")
        buf.write("\u02ad\7\13\2\2\u02ad\u02af\5 \21\2\u02ae\u02ac\3\2\2")
        buf.write("\2\u02af\u02b2\3\2\2\2\u02b0\u02ae\3\2\2\2\u02b0\u02b1")
        buf.write("\3\2\2\2\u02b1\u02b3\3\2\2\2\u02b2\u02b0\3\2\2\2\u02b3")
        buf.write("\u02b4\7\17\2\2\u02b4\u02b5\7\t\2\2\u02b5]\3\2\2\2\u02b6")
        buf.write("\u02b7\7I\2\2\u02b7\u02b8\7\16\2\2\u02b8\u02bd\5 \21\2")
        buf.write("\u02b9\u02ba\7\13\2\2\u02ba\u02bc\5 \21\2\u02bb\u02b9")
        buf.write("\3\2\2\2\u02bc\u02bf\3\2\2\2\u02bd\u02bb\3\2\2\2\u02bd")
        buf.write("\u02be\3\2\2\2\u02be\u02c0\3\2\2\2\u02bf\u02bd\3\2\2\2")
        buf.write("\u02c0\u02c1\7\17\2\2\u02c1\u02c2\7\t\2\2\u02c2_\3\2\2")
        buf.write("\2\u02c3\u02c4\7J\2\2\u02c4\u02c5\7\16\2\2\u02c5\u02c6")
        buf.write("\5\b\5\2\u02c6\u02c7\7\13\2\2\u02c7\u02c8\7-\2\2\u02c8")
        buf.write("\u02c9\7\17\2\2\u02c9\u02ca\7\t\2\2\u02caa\3\2\2\2\u02cb")
        buf.write("\u02cc\7K\2\2\u02cc\u02cd\7\16\2\2\u02cd\u02d2\5 \21\2")
        buf.write("\u02ce\u02cf\7\13\2\2\u02cf\u02d1\5 \21\2\u02d0\u02ce")
        buf.write("\3\2\2\2\u02d1\u02d4\3\2\2\2\u02d2\u02d0\3\2\2\2\u02d2")
        buf.write("\u02d3\3\2\2\2\u02d3\u02d5\3\2\2\2\u02d4\u02d2\3\2\2\2")
        buf.write("\u02d5\u02d6\7\17\2\2\u02d6\u02d7\7\t\2\2\u02d7c\3\2\2")
        buf.write("\2\u02d8\u02d9\7L\2\2\u02d9\u02da\7\16\2\2\u02da\u02db")
        buf.write("\5\b\5\2\u02db\u02dc\7\17\2\2\u02dc\u02dd\7\t\2\2\u02dd")
        buf.write("e\3\2\2\2\u02de\u02df\7M\2\2\u02df\u02e0\7\16\2\2\u02e0")
        buf.write("\u02e1\5\b\5\2\u02e1\u02e2\7\17\2\2\u02e2\u02e3\7\t\2")
        buf.write("\2\u02e3g\3\2\2\2\u02e4\u02e5\7N\2\2\u02e5\u02e6\7\16")
        buf.write("\2\2\u02e6\u02eb\5 \21\2\u02e7\u02e8\7\13\2\2\u02e8\u02ea")
        buf.write("\5 \21\2\u02e9\u02e7\3\2\2\2\u02ea\u02ed\3\2\2\2\u02eb")
        buf.write("\u02e9\3\2\2\2\u02eb\u02ec\3\2\2\2\u02ec\u02ee\3\2\2\2")
        buf.write("\u02ed\u02eb\3\2\2\2\u02ee\u02ef\7\17\2\2\u02ef\u02f0")
        buf.write("\7\t\2\2\u02f0i\3\2\2\2\u02f1\u02f2\7O\2\2\u02f2\u02f3")
        buf.write("\7\16\2\2\u02f3\u02f8\5 \21\2\u02f4\u02f5\7\13\2\2\u02f5")
        buf.write("\u02f7\5 \21\2\u02f6\u02f4\3\2\2\2\u02f7\u02fa\3\2\2\2")
        buf.write("\u02f8\u02f6\3\2\2\2\u02f8\u02f9\3\2\2\2\u02f9\u02fb\3")
        buf.write("\2\2\2\u02fa\u02f8\3\2\2\2\u02fb\u02fc\7\17\2\2\u02fc")
        buf.write("\u02fd\7\t\2\2\u02fdk\3\2\2\2\u02fe\u02ff\7P\2\2\u02ff")
        buf.write("\u0300\7\16\2\2\u0300\u0301\5\b\5\2\u0301\u0302\7\13\2")
        buf.write("\2\u0302\u0303\7c\2\2\u0303\u0304\7\17\2\2\u0304\u0305")
        buf.write("\7\t\2\2\u0305\u030f\3\2\2\2\u0306\u0307\7P\2\2\u0307")
        buf.write("\u0308\7\16\2\2\u0308\u0309\5\b\5\2\u0309\u030a\7\13\2")
        buf.write("\2\u030a\u030b\7d\2\2\u030b\u030c\7\17\2\2\u030c\u030d")
        buf.write("\7\t\2\2\u030d\u030f\3\2\2\2\u030e\u02fe\3\2\2\2\u030e")
        buf.write("\u0306\3\2\2\2\u030fm\3\2\2\2\u0310\u0311\7Q\2\2\u0311")
        buf.write("\u0312\7\16\2\2\u0312\u0313\5*\26\2\u0313\u0314\7\13\2")
        buf.write("\2\u0314\u0315\5*\26\2\u0315\u0316\7\17\2\2\u0316\u0317")
        buf.write("\7\t\2\2\u0317o\3\2\2\2\u0318\u0319\7R\2\2\u0319\u031a")
        buf.write("\7\16\2\2\u031a\u031b\5*\26\2\u031b\u031c\7\17\2\2\u031c")
        buf.write("\u031d\7\t\2\2\u031dq\3\2\2\2\u031e\u031f\7S\2\2\u031f")
        buf.write("\u0320\7\16\2\2\u0320\u0321\5*\26\2\u0321\u0322\7\13\2")
        buf.write("\2\u0322\u0323\5*\26\2\u0323\u0324\7\13\2\2\u0324\u0325")
        buf.write("\t\5\2\2\u0325\u0326\7\17\2\2\u0326\u0327\7\t\2\2\u0327")
        buf.write("s\3\2\2\2\u0328\u0329\7T\2\2\u0329\u032a\7\16\2\2\u032a")
        buf.write("\u032b\5*\26\2\u032b\u032c\7\17\2\2\u032c\u032d\7\t\2")
        buf.write("\2\u032du\3\2\2\2\u032e\u032f\7U\2\2\u032f\u0330\7\16")
        buf.write("\2\2\u0330\u0335\5*\26\2\u0331\u0332\7\13\2\2\u0332\u0334")
        buf.write("\5*\26\2\u0333\u0331\3\2\2\2\u0334\u0337\3\2\2\2\u0335")
        buf.write("\u0333\3\2\2\2\u0335\u0336\3\2\2\2\u0336\u0338\3\2\2\2")
        buf.write("\u0337\u0335\3\2\2\2\u0338\u0339\7\17\2\2\u0339\u033a")
        buf.write("\7\t\2\2\u033aw\3\2\2\2\u033b\u033c\7V\2\2\u033c\u033d")
        buf.write("\7\16\2\2\u033d\u033e\5*\26\2\u033e\u033f\7\17\2\2\u033f")
        buf.write("\u0340\7\t\2\2\u0340y\3\2\2\2\u0341\u0342\7W\2\2\u0342")
        buf.write("\u0343\7\16\2\2\u0343\u0344\5*\26\2\u0344\u0345\7\17\2")
        buf.write("\2\u0345\u0346\7\t\2\2\u0346{\3\2\2\2\u0347\u0348\7X\2")
        buf.write("\2\u0348\u0349\7\16\2\2\u0349\u034a\5*\26\2\u034a\u034b")
        buf.write("\7\17\2\2\u034b\u034c\7\t\2\2\u034c}\3\2\2\2\u034d\u034e")
        buf.write("\7Y\2\2\u034e\u034f\7\16\2\2\u034f\u0350\5*\26\2\u0350")
        buf.write("\u0351\7\17\2\2\u0351\u0352\7\t\2\2\u0352\177\3\2\2\2")
        buf.write("\u0353\u0354\7Z\2\2\u0354\u0355\7\16\2\2\u0355\u0356\5")
        buf.write("*\26\2\u0356\u0357\7\17\2\2\u0357\u0358\7\t\2\2\u0358")
        buf.write("\u0081\3\2\2\2\u0359\u035a\7[\2\2\u035a\u035b\7\16\2\2")
        buf.write("\u035b\u0360\5*\26\2\u035c\u035d\7\13\2\2\u035d\u035f")
        buf.write("\5*\26\2\u035e\u035c\3\2\2\2\u035f\u0362\3\2\2\2\u0360")
        buf.write("\u035e\3\2\2\2\u0360\u0361\3\2\2\2\u0361\u0363\3\2\2\2")
        buf.write("\u0362\u0360\3\2\2\2\u0363\u0364\7\17\2\2\u0364\u0365")
        buf.write("\7\t\2\2\u0365\u0083\3\2\2\2\u0366\u0367\7\\\2\2\u0367")
        buf.write("\u0368\7\16\2\2\u0368\u036d\5 \21\2\u0369\u036a\7\13\2")
        buf.write("\2\u036a\u036c\5 \21\2\u036b\u0369\3\2\2\2\u036c\u036f")
        buf.write("\3\2\2\2\u036d\u036b\3\2\2\2\u036d\u036e\3\2\2\2\u036e")
        buf.write("\u0370\3\2\2\2\u036f\u036d\3\2\2\2\u0370\u0371\7\17\2")
        buf.write("\2\u0371\u0372\7\t\2\2\u0372\u0085\3\2\2\2\u0373\u0374")
        buf.write("\7]\2\2\u0374\u0375\7\16\2\2\u0375\u0376\5*\26\2\u0376")
        buf.write("\u0377\7\17\2\2\u0377\u0378\7\t\2\2\u0378\u0087\3\2\2")
        buf.write("\2\u0379\u037a\7^\2\2\u037a\u037b\7\16\2\2\u037b\u037c")
        buf.write("\5*\26\2\u037c\u037d\7\13\2\2\u037d\u037e\5*\26\2\u037e")
        buf.write("\u037f\7\13\2\2\u037f\u0380\5*\26\2\u0380\u0381\7\17\2")
        buf.write("\2\u0381\u0382\7\t\2\2\u0382\u0089\3\2\2\2\u0383\u0384")
        buf.write("\7_\2\2\u0384\u0385\7\16\2\2\u0385\u0386\5*\26\2\u0386")
        buf.write("\u0387\7\17\2\2\u0387\u0388\7\t\2\2\u0388\u008b\3\2\2")
        buf.write("\2\u0389\u038a\7`\2\2\u038a\u038b\7\16\2\2\u038b\u038c")
        buf.write("\5*\26\2\u038c\u038d\7\13\2\2\u038d\u038e\5*\26\2\u038e")
        buf.write("\u038f\7\13\2\2\u038f\u0390\5*\26\2\u0390\u0391\7\17\2")
        buf.write("\2\u0391\u0392\7\t\2\2\u0392\u008d\3\2\2\2\u0393\u0394")
        buf.write("\7a\2\2\u0394\u0395\7\16\2\2\u0395\u0396\5*\26\2\u0396")
        buf.write("\u0397\7\13\2\2\u0397\u0398\5*\26\2\u0398\u0399\7\17\2")
        buf.write("\2\u0399\u039a\7\t\2\2\u039a\u008f\3\2\2\2\u039b\u039c")
        buf.write("\7b\2\2\u039c\u039d\7\16\2\2\u039d\u039e\5*\26\2\u039e")
        buf.write("\u039f\7\13\2\2\u039f\u03a0\5*\26\2\u03a0\u03a1\7\17\2")
        buf.write("\2\u03a1\u03a2\7\t\2\2\u03a2\u0091\3\2\2\2\u03a3\u03a4")
        buf.write("\7\3\2\2\u03a4\u0093\3\2\2\2/\u009b\u00a1\u00b1\u00be")
        buf.write("\u00c5\u00d2\u00d5\u00e4\u00f2\u0106\u011a\u011d\u012b")
        buf.write("\u012e\u0173\u0176\u017a\u0182\u0184\u018a\u018e\u0198")
        buf.write("\u019a\u01a0\u01a4\u01ab\u01b0\u01b4\u01bb\u01c0\u01c4")
        buf.write("\u01cb\u01d0\u01d9\u0296\u02a3\u02b0\u02bd\u02d2\u02eb")
        buf.write("\u02f8\u030e\u0335\u0360\u036d")
        return buf.getvalue()


class NmodParser ( Parser ):

    grammarFileName = "Nmod.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'dotchart'", "'program'", "'main'", "'var'", 
                     "<INVALID>", "'.'", "';'", "':'", "','", "'['", "']'", 
                     "'('", "')'", "'{'", "'}'", "'<-'", "'='", "'func'", 
                     "'error'", "'null'", "'void'", "'int'", "'float'", 
                     "'char'", "<INVALID>", "'if'", "'else'", "'while'", 
                     "'read'", "'print'", "'&'", "'|'", "'!'", "'>'", "'>='", 
                     "'<'", "'<='", "'+'", "'-'", "'*'", "'/'", "'%'", "'ctei'", 
                     "'ctef'", "'ctec'", "'return'", "'rnom'", "'rexp'", 
                     "'rgamma'", "'points'", "'lines'", "'text'", "'barplot'", 
                     "'piechart'", "'xyplot'", "'densityplot'", "'histogram'", 
                     "'sin'", "'cos'", "'tan'", "'asin'", "'acos'", "'atan'", 
                     "'atan2'", "'log'", "'log10'", "'exp'", "'f_max'", 
                     "'f_min'", "'f_range'", "'f_sum'", "'diff'", "'prod'", 
                     "'mean'", "'median'", "'quantile'", "'weighedmean'", 
                     "'rank'", "'variance'", "'sd'", "'cor'", "'cov'", "'f_round'", 
                     "'transpose'", "'diagonal'", "'ginv'", "'rowsum'", 
                     "'colsum'", "'load'", "'data'", "'library'", "'rpois'", 
                     "'rweibull'", "'rbinom'", "'rgeom'", "'runif'", "'0'", 
                     "'1'", "'pearson'", "'kendall'", "'spearman'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "PROGRAM", "MAIN", "VARIABLES", 
                      "NUMBER", "PERIOD", "SEMICOLON", "COLON", "COMMA", 
                      "LBRACKET", "RBRACKET", "LPRACKET", "RPRACKET", "LCRACKET", 
                      "RCRACKET", "ISFUNCTION", "EQUALS", "FUNC", "ERROR", 
                      "NULL", "VOID", "INT", "FLOAT", "CHAR", "STRING", 
                      "IF", "ELSE", "WHILE", "READ", "PRINT", "AND", "OR", 
                      "NOT", "GREATERTHAN", "GREATEROR", "LESSERTHAN", "LESSEROR", 
                      "PLUS", "MINUS", "TIMES", "DIVISION", "MODULE", "CTEI", 
                      "CTEF", "CTEC", "RETURN", "RNOM", "REXP", "RGAMMA", 
                      "POINTS", "LINES", "TEXT", "BARPLOT", "PIECHART", 
                      "XYPLOT", "DENSITYPLOT", "HISTOGRAM", "SIN", "COS", 
                      "TAN", "ASIN", "ACOS", "ATAN", "ATAN2", "LOG", "LOG10", 
                      "EXPONENT", "MAX", "MIN", "RANGE", "SUM", "DIFF", 
                      "PROD", "MEAN", "MEDIAN", "QUANTILE", "WEIGHEDMEAN", 
                      "RANK", "VARIANCE", "SD", "COR", "COV", "ROUND", "TRANSPOSE", 
                      "DIAGONAL", "GINV", "ROWSUM", "COLSUM", "LOAD", "DATA", 
                      "LIBRARY", "RPOIS", "RWEIBULL", "RBINOM", "RGEOM", 
                      "RUNIF", "ZERO", "ONE", "PEARSON", "KENDALL", "SPEARMAN", 
                      "WHITESPACE", "NEWLINE", "LINECOMMENT", "MULTICOMMENT", 
                      "ID" ]

    RULE_program = 0
    RULE_f_type = 1
    RULE_variables = 2
    RULE_f_id = 3
    RULE_modules = 4
    RULE_main = 5
    RULE_block = 6
    RULE_parameter = 7
    RULE_statute = 8
    RULE_assignment = 9
    RULE_condition = 10
    RULE_cicle = 11
    RULE_reading = 12
    RULE_writing = 13
    RULE_call_module = 14
    RULE_expression = 15
    RULE_sub_exp = 16
    RULE_exp = 17
    RULE_term = 18
    RULE_factor = 19
    RULE_var_cte = 20
    RULE_r_return = 21
    RULE_rnom = 22
    RULE_rexp = 23
    RULE_rgamma = 24
    RULE_points = 25
    RULE_lines = 26
    RULE_text = 27
    RULE_barplot = 28
    RULE_piechart = 29
    RULE_xyplot = 30
    RULE_densityplot = 31
    RULE_histogram = 32
    RULE_sin = 33
    RULE_cos = 34
    RULE_tan = 35
    RULE_asin = 36
    RULE_acos = 37
    RULE_atan = 38
    RULE_atan2 = 39
    RULE_log = 40
    RULE_log10 = 41
    RULE_exponent = 42
    RULE_f_max = 43
    RULE_f_min = 44
    RULE_f_range = 45
    RULE_f_sum = 46
    RULE_diff = 47
    RULE_prod = 48
    RULE_mean = 49
    RULE_median = 50
    RULE_quantile = 51
    RULE_weighedmean = 52
    RULE_rank = 53
    RULE_var = 54
    RULE_sd = 55
    RULE_cor = 56
    RULE_cov = 57
    RULE_f_round = 58
    RULE_transpose = 59
    RULE_diagonal = 60
    RULE_ginv = 61
    RULE_rowsum = 62
    RULE_colsum = 63
    RULE_load = 64
    RULE_data = 65
    RULE_library = 66
    RULE_rpois = 67
    RULE_rweibull = 68
    RULE_rbinom = 69
    RULE_rgeom = 70
    RULE_runif = 71
    RULE_dotchart = 72

    ruleNames =  [ "program", "f_type", "variables", "f_id", "modules", 
                   "main", "block", "parameter", "statute", "assignment", 
                   "condition", "cicle", "reading", "writing", "call_module", 
                   "expression", "sub_exp", "exp", "term", "factor", "var_cte", 
                   "r_return", "rnom", "rexp", "rgamma", "points", "lines", 
                   "text", "barplot", "piechart", "xyplot", "densityplot", 
                   "histogram", "sin", "cos", "tan", "asin", "acos", "atan", 
                   "atan2", "log", "log10", "exponent", "f_max", "f_min", 
                   "f_range", "f_sum", "diff", "prod", "mean", "median", 
                   "quantile", "weighedmean", "rank", "var", "sd", "cor", 
                   "cov", "f_round", "transpose", "diagonal", "ginv", "rowsum", 
                   "colsum", "load", "data", "library", "rpois", "rweibull", 
                   "rbinom", "rgeom", "runif", "dotchart" ]

    EOF = Token.EOF
    T__0=1
    PROGRAM=2
    MAIN=3
    VARIABLES=4
    NUMBER=5
    PERIOD=6
    SEMICOLON=7
    COLON=8
    COMMA=9
    LBRACKET=10
    RBRACKET=11
    LPRACKET=12
    RPRACKET=13
    LCRACKET=14
    RCRACKET=15
    ISFUNCTION=16
    EQUALS=17
    FUNC=18
    ERROR=19
    NULL=20
    VOID=21
    INT=22
    FLOAT=23
    CHAR=24
    STRING=25
    IF=26
    ELSE=27
    WHILE=28
    READ=29
    PRINT=30
    AND=31
    OR=32
    NOT=33
    GREATERTHAN=34
    GREATEROR=35
    LESSERTHAN=36
    LESSEROR=37
    PLUS=38
    MINUS=39
    TIMES=40
    DIVISION=41
    MODULE=42
    CTEI=43
    CTEF=44
    CTEC=45
    RETURN=46
    RNOM=47
    REXP=48
    RGAMMA=49
    POINTS=50
    LINES=51
    TEXT=52
    BARPLOT=53
    PIECHART=54
    XYPLOT=55
    DENSITYPLOT=56
    HISTOGRAM=57
    SIN=58
    COS=59
    TAN=60
    ASIN=61
    ACOS=62
    ATAN=63
    ATAN2=64
    LOG=65
    LOG10=66
    EXPONENT=67
    MAX=68
    MIN=69
    RANGE=70
    SUM=71
    DIFF=72
    PROD=73
    MEAN=74
    MEDIAN=75
    QUANTILE=76
    WEIGHEDMEAN=77
    RANK=78
    VARIANCE=79
    SD=80
    COR=81
    COV=82
    ROUND=83
    TRANSPOSE=84
    DIAGONAL=85
    GINV=86
    ROWSUM=87
    COLSUM=88
    LOAD=89
    DATA=90
    LIBRARY=91
    RPOIS=92
    RWEIBULL=93
    RBINOM=94
    RGEOM=95
    RUNIF=96
    ZERO=97
    ONE=98
    PEARSON=99
    KENDALL=100
    SPEARMAN=101
    WHITESPACE=102
    NEWLINE=103
    LINECOMMENT=104
    MULTICOMMENT=105
    ID=106

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class ProgramContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._ID = None # Token

        def PROGRAM(self):
            return self.getToken(NmodParser.PROGRAM, 0)

        def ID(self):
            return self.getToken(NmodParser.ID, 0)

        def COLON(self):
            return self.getToken(NmodParser.COLON, 0)

        def main(self):
            return self.getTypedRuleContext(NmodParser.MainContext,0)


        def variables(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(NmodParser.VariablesContext)
            else:
                return self.getTypedRuleContext(NmodParser.VariablesContext,i)


        def modules(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(NmodParser.ModulesContext)
            else:
                return self.getTypedRuleContext(NmodParser.ModulesContext,i)


        def getRuleIndex(self):
            return NmodParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)




    def program(self):

        localctx = NmodParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 146
            self.match(NmodParser.PROGRAM)
            self.state = 147
            localctx._ID = self.match(NmodParser.ID)
            c.insertFunctionDirectory((None if localctx._ID is None else localctx._ID.text),"void")
            self.state = 149
            self.match(NmodParser.COLON)
            self.state = 153
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==NmodParser.VARIABLES:
                self.state = 150
                self.variables()
                self.state = 155
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 159
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==NmodParser.ID:
                self.state = 156
                self.modules()
                self.state = 161
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 162
            self.main()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class F_typeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(NmodParser.INT, 0)

        def FLOAT(self):
            return self.getToken(NmodParser.FLOAT, 0)

        def CHAR(self):
            return self.getToken(NmodParser.CHAR, 0)

        def getRuleIndex(self):
            return NmodParser.RULE_f_type

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterF_type" ):
                listener.enterF_type(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitF_type" ):
                listener.exitF_type(self)




    def f_type(self):

        localctx = NmodParser.F_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_f_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 164
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << NmodParser.INT) | (1 << NmodParser.FLOAT) | (1 << NmodParser.CHAR))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class VariablesContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._f_id = None # F_idContext
            self._f_type = None # F_typeContext

        def VARIABLES(self):
            return self.getToken(NmodParser.VARIABLES, 0)

        def f_id(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(NmodParser.F_idContext)
            else:
                return self.getTypedRuleContext(NmodParser.F_idContext,i)


        def COLON(self):
            return self.getToken(NmodParser.COLON, 0)

        def f_type(self):
            return self.getTypedRuleContext(NmodParser.F_typeContext,0)


        def SEMICOLON(self):
            return self.getToken(NmodParser.SEMICOLON, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(NmodParser.COMMA)
            else:
                return self.getToken(NmodParser.COMMA, i)

        def getRuleIndex(self):
            return NmodParser.RULE_variables

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariables" ):
                listener.enterVariables(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariables" ):
                listener.exitVariables(self)




    def variables(self):

        localctx = NmodParser.VariablesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_variables)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 166
            self.match(NmodParser.VARIABLES)
            self.state = 167
            localctx._f_id = self.f_id()
            c.storeVariable((None if localctx._f_id is None else self._input.getText((localctx._f_id.start,localctx._f_id.stop))))
            self.state = 175
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==NmodParser.COMMA:
                self.state = 169
                self.match(NmodParser.COMMA)
                self.state = 170
                localctx._f_id = self.f_id()
                c.storeVariable((None if localctx._f_id is None else self._input.getText((localctx._f_id.start,localctx._f_id.stop))))
                self.state = 177
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 178
            self.match(NmodParser.COLON)
            self.state = 179
            localctx._f_type = self.f_type()
            self.state = 180
            self.match(NmodParser.SEMICOLON)
            c.declareVariables(c.getStoredVariables(),(None if localctx._f_type is None else self._input.getText((localctx._f_type.start,localctx._f_type.stop))))
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class F_idContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(NmodParser.ID, 0)

        def LBRACKET(self):
            return self.getToken(NmodParser.LBRACKET, 0)

        def expression(self):
            return self.getTypedRuleContext(NmodParser.ExpressionContext,0)


        def RBRACKET(self):
            return self.getToken(NmodParser.RBRACKET, 0)

        def getRuleIndex(self):
            return NmodParser.RULE_f_id

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterF_id" ):
                listener.enterF_id(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitF_id" ):
                listener.exitF_id(self)




    def f_id(self):

        localctx = NmodParser.F_idContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_f_id)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 183
            self.match(NmodParser.ID)
            self.state = 188
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==NmodParser.LBRACKET:
                self.state = 184
                self.match(NmodParser.LBRACKET)
                self.state = 185
                self.expression()
                self.state = 186
                self.match(NmodParser.RBRACKET)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ModulesContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._ID = None # Token
            self._parameter = None # ParameterContext

        def ID(self):
            return self.getToken(NmodParser.ID, 0)

        def ISFUNCTION(self):
            return self.getToken(NmodParser.ISFUNCTION, 0)

        def FUNC(self):
            return self.getToken(NmodParser.FUNC, 0)

        def LPRACKET(self):
            return self.getToken(NmodParser.LPRACKET, 0)

        def RPRACKET(self):
            return self.getToken(NmodParser.RPRACKET, 0)

        def block(self):
            return self.getTypedRuleContext(NmodParser.BlockContext,0)


        def VOID(self):
            return self.getToken(NmodParser.VOID, 0)

        def f_type(self):
            return self.getTypedRuleContext(NmodParser.F_typeContext,0)


        def parameter(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(NmodParser.ParameterContext)
            else:
                return self.getTypedRuleContext(NmodParser.ParameterContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(NmodParser.COMMA)
            else:
                return self.getToken(NmodParser.COMMA, i)

        def getRuleIndex(self):
            return NmodParser.RULE_modules

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterModules" ):
                listener.enterModules(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitModules" ):
                listener.exitModules(self)




    def modules(self):

        localctx = NmodParser.ModulesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_modules)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 190
            localctx._ID = self.match(NmodParser.ID)
            c.storeVariable((None if localctx._ID is None else localctx._ID.text))
            self.state = 192
            self.match(NmodParser.ISFUNCTION)
            self.state = 195
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [NmodParser.VOID]:
                self.state = 193
                self.match(NmodParser.VOID)
                pass
            elif token in [NmodParser.INT, NmodParser.FLOAT, NmodParser.CHAR]:
                self.state = 194
                self.f_type()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 197
            self.match(NmodParser.FUNC)
            c.declareModule((None if localctx._ID is None else localctx._ID.text))
            self.state = 199
            self.match(NmodParser.LPRACKET)
            self.state = 211
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << NmodParser.INT) | (1 << NmodParser.FLOAT) | (1 << NmodParser.CHAR))) != 0):
                self.state = 200
                localctx._parameter = self.parameter()
                c.storeParameter((None if localctx._parameter is None else self._input.getText((localctx._parameter.start,localctx._parameter.stop))))
                self.state = 208
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==NmodParser.COMMA:
                    self.state = 202
                    self.match(NmodParser.COMMA)
                    self.state = 203
                    localctx._parameter = self.parameter()
                    c.storeParameter((None if localctx._parameter is None else self._input.getText((localctx._parameter.start,localctx._parameter.stop))))
                    self.state = 210
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            c.validateParameters()
            self.state = 214
            self.match(NmodParser.RPRACKET)
            self.state = 215
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class MainContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MAIN(self):
            return self.getToken(NmodParser.MAIN, 0)

        def LPRACKET(self):
            return self.getToken(NmodParser.LPRACKET, 0)

        def RPRACKET(self):
            return self.getToken(NmodParser.RPRACKET, 0)

        def block(self):
            return self.getTypedRuleContext(NmodParser.BlockContext,0)


        def getRuleIndex(self):
            return NmodParser.RULE_main

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMain" ):
                listener.enterMain(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMain" ):
                listener.exitMain(self)




    def main(self):

        localctx = NmodParser.MainContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_main)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 217
            self.match(NmodParser.MAIN)
            self.state = 218
            self.match(NmodParser.LPRACKET)
            self.state = 219
            self.match(NmodParser.RPRACKET)
            self.state = 220
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class BlockContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LCRACKET(self):
            return self.getToken(NmodParser.LCRACKET, 0)

        def RCRACKET(self):
            return self.getToken(NmodParser.RCRACKET, 0)

        def statute(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(NmodParser.StatuteContext)
            else:
                return self.getTypedRuleContext(NmodParser.StatuteContext,i)


        def getRuleIndex(self):
            return NmodParser.RULE_block

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlock" ):
                listener.enterBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlock" ):
                listener.exitBlock(self)




    def block(self):

        localctx = NmodParser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 222
            self.match(NmodParser.LCRACKET)
            self.state = 226
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << NmodParser.IF) | (1 << NmodParser.WHILE) | (1 << NmodParser.READ) | (1 << NmodParser.PRINT) | (1 << NmodParser.RETURN) | (1 << NmodParser.RNOM) | (1 << NmodParser.REXP) | (1 << NmodParser.RGAMMA) | (1 << NmodParser.POINTS) | (1 << NmodParser.LINES) | (1 << NmodParser.TEXT) | (1 << NmodParser.BARPLOT) | (1 << NmodParser.PIECHART) | (1 << NmodParser.XYPLOT) | (1 << NmodParser.DENSITYPLOT) | (1 << NmodParser.HISTOGRAM) | (1 << NmodParser.SIN) | (1 << NmodParser.COS) | (1 << NmodParser.TAN) | (1 << NmodParser.ASIN) | (1 << NmodParser.ACOS) | (1 << NmodParser.ATAN))) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & ((1 << (NmodParser.ATAN2 - 64)) | (1 << (NmodParser.LOG - 64)) | (1 << (NmodParser.LOG10 - 64)) | (1 << (NmodParser.EXPONENT - 64)) | (1 << (NmodParser.MAX - 64)) | (1 << (NmodParser.MIN - 64)) | (1 << (NmodParser.RANGE - 64)) | (1 << (NmodParser.SUM - 64)) | (1 << (NmodParser.DIFF - 64)) | (1 << (NmodParser.PROD - 64)) | (1 << (NmodParser.MEAN - 64)) | (1 << (NmodParser.MEDIAN - 64)) | (1 << (NmodParser.QUANTILE - 64)) | (1 << (NmodParser.WEIGHEDMEAN - 64)) | (1 << (NmodParser.RANK - 64)) | (1 << (NmodParser.VARIANCE - 64)) | (1 << (NmodParser.SD - 64)) | (1 << (NmodParser.COR - 64)) | (1 << (NmodParser.COV - 64)) | (1 << (NmodParser.ROUND - 64)) | (1 << (NmodParser.TRANSPOSE - 64)) | (1 << (NmodParser.DIAGONAL - 64)) | (1 << (NmodParser.GINV - 64)) | (1 << (NmodParser.ROWSUM - 64)) | (1 << (NmodParser.COLSUM - 64)) | (1 << (NmodParser.LOAD - 64)) | (1 << (NmodParser.DATA - 64)) | (1 << (NmodParser.LIBRARY - 64)) | (1 << (NmodParser.RPOIS - 64)) | (1 << (NmodParser.RWEIBULL - 64)) | (1 << (NmodParser.RBINOM - 64)) | (1 << (NmodParser.RGEOM - 64)) | (1 << (NmodParser.RUNIF - 64)) | (1 << (NmodParser.ID - 64)))) != 0):
                self.state = 223
                self.statute()
                self.state = 228
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 229
            self.match(NmodParser.RCRACKET)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ParameterContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def f_type(self):
            return self.getTypedRuleContext(NmodParser.F_typeContext,0)


        def var_cte(self):
            return self.getTypedRuleContext(NmodParser.Var_cteContext,0)


        def getRuleIndex(self):
            return NmodParser.RULE_parameter

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParameter" ):
                listener.enterParameter(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParameter" ):
                listener.exitParameter(self)




    def parameter(self):

        localctx = NmodParser.ParameterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_parameter)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 231
            self.f_type()
            self.state = 232
            self.var_cte()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class StatuteContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assignment(self):
            return self.getTypedRuleContext(NmodParser.AssignmentContext,0)


        def condition(self):
            return self.getTypedRuleContext(NmodParser.ConditionContext,0)


        def reading(self):
            return self.getTypedRuleContext(NmodParser.ReadingContext,0)


        def writing(self):
            return self.getTypedRuleContext(NmodParser.WritingContext,0)


        def cicle(self):
            return self.getTypedRuleContext(NmodParser.CicleContext,0)


        def call_module(self):
            return self.getTypedRuleContext(NmodParser.Call_moduleContext,0)


        def getRuleIndex(self):
            return NmodParser.RULE_statute

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatute" ):
                listener.enterStatute(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatute" ):
                listener.exitStatute(self)




    def statute(self):

        localctx = NmodParser.StatuteContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_statute)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 240
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.state = 234
                self.assignment()
                pass

            elif la_ == 2:
                self.state = 235
                self.condition()
                pass

            elif la_ == 3:
                self.state = 236
                self.reading()
                pass

            elif la_ == 4:
                self.state = 237
                self.writing()
                pass

            elif la_ == 5:
                self.state = 238
                self.cicle()
                pass

            elif la_ == 6:
                self.state = 239
                self.call_module()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class AssignmentContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._f_id = None # F_idContext
            self._EQUALS = None # Token

        def f_id(self):
            return self.getTypedRuleContext(NmodParser.F_idContext,0)


        def EQUALS(self):
            return self.getToken(NmodParser.EQUALS, 0)

        def expression(self):
            return self.getTypedRuleContext(NmodParser.ExpressionContext,0)


        def SEMICOLON(self):
            return self.getToken(NmodParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return NmodParser.RULE_assignment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignment" ):
                listener.enterAssignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignment" ):
                listener.exitAssignment(self)




    def assignment(self):

        localctx = NmodParser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 242
            localctx._f_id = self.f_id()
            c.insertStackOperand((None if localctx._f_id is None else self._input.getText((localctx._f_id.start,localctx._f_id.stop))))
            self.state = 244
            localctx._EQUALS = self.match(NmodParser.EQUALS)
            c.insertStackOperator((None if localctx._EQUALS is None else localctx._EQUALS.text))
            self.state = 246
            self.expression()
            c.validateExpression()
            self.state = 248
            self.match(NmodParser.SEMICOLON)
            c.generateAssignmentQuadruples()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ConditionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(NmodParser.IF, 0)

        def LPRACKET(self):
            return self.getToken(NmodParser.LPRACKET, 0)

        def expression(self):
            return self.getTypedRuleContext(NmodParser.ExpressionContext,0)


        def RPRACKET(self):
            return self.getToken(NmodParser.RPRACKET, 0)

        def block(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(NmodParser.BlockContext)
            else:
                return self.getTypedRuleContext(NmodParser.BlockContext,i)


        def ELSE(self):
            return self.getToken(NmodParser.ELSE, 0)

        def getRuleIndex(self):
            return NmodParser.RULE_condition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCondition" ):
                listener.enterCondition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCondition" ):
                listener.exitCondition(self)




    def condition(self):

        localctx = NmodParser.ConditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_condition)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 251
            self.match(NmodParser.IF)
            self.state = 252
            self.match(NmodParser.LPRACKET)
            self.state = 253
            self.expression()
            c.validateExpression(), c.insertStackJump(quadPlace), c.generateGotoFQuadruples()
            self.state = 255
            self.match(NmodParser.RPRACKET)
            self.state = 256
            self.block()
            self.state = 260
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==NmodParser.ELSE:
                self.state = 257
                self.match(NmodParser.ELSE)
                c.popStackJump(), c.generateGotoQuadruples()
                self.state = 259
                self.block()


            c.popStackJump()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class CicleContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHILE(self):
            return self.getToken(NmodParser.WHILE, 0)

        def LPRACKET(self):
            return self.getToken(NmodParser.LPRACKET, 0)

        def expression(self):
            return self.getTypedRuleContext(NmodParser.ExpressionContext,0)


        def RPRACKET(self):
            return self.getToken(NmodParser.RPRACKET, 0)

        def block(self):
            return self.getTypedRuleContext(NmodParser.BlockContext,0)


        def getRuleIndex(self):
            return NmodParser.RULE_cicle

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCicle" ):
                listener.enterCicle(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCicle" ):
                listener.exitCicle(self)




    def cicle(self):

        localctx = NmodParser.CicleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_cicle)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 264
            self.match(NmodParser.WHILE)
            self.state = 265
            self.match(NmodParser.LPRACKET)
            self.state = 266
            self.expression()
            c.validateExpression(), c.insertStackJump(quadPlace), c.generateGotoFQuadruples()
            self.state = 268
            self.match(NmodParser.RPRACKET)
            self.state = 269
            self.block()
            c.popStackJump(), c.generateGotoQuadruples(), c.popStackJump()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ReadingContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def READ(self):
            return self.getToken(NmodParser.READ, 0)

        def LPRACKET(self):
            return self.getToken(NmodParser.LPRACKET, 0)

        def RPRACKET(self):
            return self.getToken(NmodParser.RPRACKET, 0)

        def SEMICOLON(self):
            return self.getToken(NmodParser.SEMICOLON, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(NmodParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(NmodParser.ExpressionContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(NmodParser.COMMA)
            else:
                return self.getToken(NmodParser.COMMA, i)

        def getRuleIndex(self):
            return NmodParser.RULE_reading

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReading" ):
                listener.enterReading(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReading" ):
                listener.exitReading(self)




    def reading(self):

        localctx = NmodParser.ReadingContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_reading)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 272
            self.match(NmodParser.READ)
            c.insertFunctionDirectory(READ,VOID)
            self.state = 274
            self.match(NmodParser.LPRACKET)
            self.state = 283
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << NmodParser.NUMBER) | (1 << NmodParser.LPRACKET) | (1 << NmodParser.STRING) | (1 << NmodParser.PLUS) | (1 << NmodParser.MINUS) | (1 << NmodParser.CTEI) | (1 << NmodParser.CTEF) | (1 << NmodParser.CTEC) | (1 << NmodParser.RETURN) | (1 << NmodParser.RNOM) | (1 << NmodParser.REXP) | (1 << NmodParser.RGAMMA) | (1 << NmodParser.POINTS) | (1 << NmodParser.LINES) | (1 << NmodParser.TEXT) | (1 << NmodParser.BARPLOT) | (1 << NmodParser.PIECHART) | (1 << NmodParser.XYPLOT) | (1 << NmodParser.DENSITYPLOT) | (1 << NmodParser.HISTOGRAM) | (1 << NmodParser.SIN) | (1 << NmodParser.COS) | (1 << NmodParser.TAN) | (1 << NmodParser.ASIN) | (1 << NmodParser.ACOS) | (1 << NmodParser.ATAN))) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & ((1 << (NmodParser.ATAN2 - 64)) | (1 << (NmodParser.LOG - 64)) | (1 << (NmodParser.LOG10 - 64)) | (1 << (NmodParser.EXPONENT - 64)) | (1 << (NmodParser.MAX - 64)) | (1 << (NmodParser.MIN - 64)) | (1 << (NmodParser.RANGE - 64)) | (1 << (NmodParser.SUM - 64)) | (1 << (NmodParser.DIFF - 64)) | (1 << (NmodParser.PROD - 64)) | (1 << (NmodParser.MEAN - 64)) | (1 << (NmodParser.MEDIAN - 64)) | (1 << (NmodParser.QUANTILE - 64)) | (1 << (NmodParser.WEIGHEDMEAN - 64)) | (1 << (NmodParser.RANK - 64)) | (1 << (NmodParser.VARIANCE - 64)) | (1 << (NmodParser.SD - 64)) | (1 << (NmodParser.COR - 64)) | (1 << (NmodParser.COV - 64)) | (1 << (NmodParser.ROUND - 64)) | (1 << (NmodParser.TRANSPOSE - 64)) | (1 << (NmodParser.DIAGONAL - 64)) | (1 << (NmodParser.GINV - 64)) | (1 << (NmodParser.ROWSUM - 64)) | (1 << (NmodParser.COLSUM - 64)) | (1 << (NmodParser.LOAD - 64)) | (1 << (NmodParser.DATA - 64)) | (1 << (NmodParser.LIBRARY - 64)) | (1 << (NmodParser.RPOIS - 64)) | (1 << (NmodParser.RWEIBULL - 64)) | (1 << (NmodParser.RBINOM - 64)) | (1 << (NmodParser.RGEOM - 64)) | (1 << (NmodParser.RUNIF - 64)) | (1 << (NmodParser.ID - 64)))) != 0):
                self.state = 275
                self.expression()
                self.state = 280
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==NmodParser.COMMA:
                    self.state = 276
                    self.match(NmodParser.COMMA)
                    self.state = 277
                    self.expression()
                    self.state = 282
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 285
            self.match(NmodParser.RPRACKET)
            self.state = 286
            self.match(NmodParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class WritingContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PRINT(self):
            return self.getToken(NmodParser.PRINT, 0)

        def LPRACKET(self):
            return self.getToken(NmodParser.LPRACKET, 0)

        def RPRACKET(self):
            return self.getToken(NmodParser.RPRACKET, 0)

        def SEMICOLON(self):
            return self.getToken(NmodParser.SEMICOLON, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(NmodParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(NmodParser.ExpressionContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(NmodParser.COMMA)
            else:
                return self.getToken(NmodParser.COMMA, i)

        def getRuleIndex(self):
            return NmodParser.RULE_writing

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWriting" ):
                listener.enterWriting(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWriting" ):
                listener.exitWriting(self)




    def writing(self):

        localctx = NmodParser.WritingContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_writing)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 288
            self.match(NmodParser.PRINT)
            c.insertFunctionDirectory(PRINT,VOID)
            self.state = 290
            self.match(NmodParser.LPRACKET)
            self.state = 300
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << NmodParser.NUMBER) | (1 << NmodParser.LPRACKET) | (1 << NmodParser.STRING) | (1 << NmodParser.PLUS) | (1 << NmodParser.MINUS) | (1 << NmodParser.CTEI) | (1 << NmodParser.CTEF) | (1 << NmodParser.CTEC) | (1 << NmodParser.RETURN) | (1 << NmodParser.RNOM) | (1 << NmodParser.REXP) | (1 << NmodParser.RGAMMA) | (1 << NmodParser.POINTS) | (1 << NmodParser.LINES) | (1 << NmodParser.TEXT) | (1 << NmodParser.BARPLOT) | (1 << NmodParser.PIECHART) | (1 << NmodParser.XYPLOT) | (1 << NmodParser.DENSITYPLOT) | (1 << NmodParser.HISTOGRAM) | (1 << NmodParser.SIN) | (1 << NmodParser.COS) | (1 << NmodParser.TAN) | (1 << NmodParser.ASIN) | (1 << NmodParser.ACOS) | (1 << NmodParser.ATAN))) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & ((1 << (NmodParser.ATAN2 - 64)) | (1 << (NmodParser.LOG - 64)) | (1 << (NmodParser.LOG10 - 64)) | (1 << (NmodParser.EXPONENT - 64)) | (1 << (NmodParser.MAX - 64)) | (1 << (NmodParser.MIN - 64)) | (1 << (NmodParser.RANGE - 64)) | (1 << (NmodParser.SUM - 64)) | (1 << (NmodParser.DIFF - 64)) | (1 << (NmodParser.PROD - 64)) | (1 << (NmodParser.MEAN - 64)) | (1 << (NmodParser.MEDIAN - 64)) | (1 << (NmodParser.QUANTILE - 64)) | (1 << (NmodParser.WEIGHEDMEAN - 64)) | (1 << (NmodParser.RANK - 64)) | (1 << (NmodParser.VARIANCE - 64)) | (1 << (NmodParser.SD - 64)) | (1 << (NmodParser.COR - 64)) | (1 << (NmodParser.COV - 64)) | (1 << (NmodParser.ROUND - 64)) | (1 << (NmodParser.TRANSPOSE - 64)) | (1 << (NmodParser.DIAGONAL - 64)) | (1 << (NmodParser.GINV - 64)) | (1 << (NmodParser.ROWSUM - 64)) | (1 << (NmodParser.COLSUM - 64)) | (1 << (NmodParser.LOAD - 64)) | (1 << (NmodParser.DATA - 64)) | (1 << (NmodParser.LIBRARY - 64)) | (1 << (NmodParser.RPOIS - 64)) | (1 << (NmodParser.RWEIBULL - 64)) | (1 << (NmodParser.RBINOM - 64)) | (1 << (NmodParser.RGEOM - 64)) | (1 << (NmodParser.RUNIF - 64)) | (1 << (NmodParser.ID - 64)))) != 0):
                self.state = 291
                self.expression()
                c.validateExpression()
                self.state = 297
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==NmodParser.COMMA:
                    self.state = 293
                    self.match(NmodParser.COMMA)
                    self.state = 294
                    self.expression()
                    self.state = 299
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 302
            self.match(NmodParser.RPRACKET)
            self.state = 303
            self.match(NmodParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Call_moduleContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def r_return(self):
            return self.getTypedRuleContext(NmodParser.R_returnContext,0)


        def rnom(self):
            return self.getTypedRuleContext(NmodParser.RnomContext,0)


        def rexp(self):
            return self.getTypedRuleContext(NmodParser.RexpContext,0)


        def rgamma(self):
            return self.getTypedRuleContext(NmodParser.RgammaContext,0)


        def points(self):
            return self.getTypedRuleContext(NmodParser.PointsContext,0)


        def lines(self):
            return self.getTypedRuleContext(NmodParser.LinesContext,0)


        def text(self):
            return self.getTypedRuleContext(NmodParser.TextContext,0)


        def barplot(self):
            return self.getTypedRuleContext(NmodParser.BarplotContext,0)


        def piechart(self):
            return self.getTypedRuleContext(NmodParser.PiechartContext,0)


        def xyplot(self):
            return self.getTypedRuleContext(NmodParser.XyplotContext,0)


        def densityplot(self):
            return self.getTypedRuleContext(NmodParser.DensityplotContext,0)


        def histogram(self):
            return self.getTypedRuleContext(NmodParser.HistogramContext,0)


        def sin(self):
            return self.getTypedRuleContext(NmodParser.SinContext,0)


        def cos(self):
            return self.getTypedRuleContext(NmodParser.CosContext,0)


        def tan(self):
            return self.getTypedRuleContext(NmodParser.TanContext,0)


        def asin(self):
            return self.getTypedRuleContext(NmodParser.AsinContext,0)


        def acos(self):
            return self.getTypedRuleContext(NmodParser.AcosContext,0)


        def atan(self):
            return self.getTypedRuleContext(NmodParser.AtanContext,0)


        def atan2(self):
            return self.getTypedRuleContext(NmodParser.Atan2Context,0)


        def log(self):
            return self.getTypedRuleContext(NmodParser.LogContext,0)


        def log10(self):
            return self.getTypedRuleContext(NmodParser.Log10Context,0)


        def exponent(self):
            return self.getTypedRuleContext(NmodParser.ExponentContext,0)


        def f_max(self):
            return self.getTypedRuleContext(NmodParser.F_maxContext,0)


        def f_min(self):
            return self.getTypedRuleContext(NmodParser.F_minContext,0)


        def f_range(self):
            return self.getTypedRuleContext(NmodParser.F_rangeContext,0)


        def f_sum(self):
            return self.getTypedRuleContext(NmodParser.F_sumContext,0)


        def diff(self):
            return self.getTypedRuleContext(NmodParser.DiffContext,0)


        def prod(self):
            return self.getTypedRuleContext(NmodParser.ProdContext,0)


        def mean(self):
            return self.getTypedRuleContext(NmodParser.MeanContext,0)


        def median(self):
            return self.getTypedRuleContext(NmodParser.MedianContext,0)


        def quantile(self):
            return self.getTypedRuleContext(NmodParser.QuantileContext,0)


        def weighedmean(self):
            return self.getTypedRuleContext(NmodParser.WeighedmeanContext,0)


        def rank(self):
            return self.getTypedRuleContext(NmodParser.RankContext,0)


        def var(self):
            return self.getTypedRuleContext(NmodParser.VarContext,0)


        def sd(self):
            return self.getTypedRuleContext(NmodParser.SdContext,0)


        def cor(self):
            return self.getTypedRuleContext(NmodParser.CorContext,0)


        def cov(self):
            return self.getTypedRuleContext(NmodParser.CovContext,0)


        def f_round(self):
            return self.getTypedRuleContext(NmodParser.F_roundContext,0)


        def transpose(self):
            return self.getTypedRuleContext(NmodParser.TransposeContext,0)


        def diagonal(self):
            return self.getTypedRuleContext(NmodParser.DiagonalContext,0)


        def ginv(self):
            return self.getTypedRuleContext(NmodParser.GinvContext,0)


        def rowsum(self):
            return self.getTypedRuleContext(NmodParser.RowsumContext,0)


        def colsum(self):
            return self.getTypedRuleContext(NmodParser.ColsumContext,0)


        def load(self):
            return self.getTypedRuleContext(NmodParser.LoadContext,0)


        def data(self):
            return self.getTypedRuleContext(NmodParser.DataContext,0)


        def library(self):
            return self.getTypedRuleContext(NmodParser.LibraryContext,0)


        def rpois(self):
            return self.getTypedRuleContext(NmodParser.RpoisContext,0)


        def rweibull(self):
            return self.getTypedRuleContext(NmodParser.RweibullContext,0)


        def rbinom(self):
            return self.getTypedRuleContext(NmodParser.RbinomContext,0)


        def rgeom(self):
            return self.getTypedRuleContext(NmodParser.RgeomContext,0)


        def runif(self):
            return self.getTypedRuleContext(NmodParser.RunifContext,0)


        def ID(self):
            return self.getToken(NmodParser.ID, 0)

        def LPRACKET(self):
            return self.getToken(NmodParser.LPRACKET, 0)

        def RPRACKET(self):
            return self.getToken(NmodParser.RPRACKET, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(NmodParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(NmodParser.ExpressionContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(NmodParser.COMMA)
            else:
                return self.getToken(NmodParser.COMMA, i)

        def getRuleIndex(self):
            return NmodParser.RULE_call_module

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCall_module" ):
                listener.enterCall_module(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCall_module" ):
                listener.exitCall_module(self)




    def call_module(self):

        localctx = NmodParser.Call_moduleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_call_module)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 376
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [NmodParser.RETURN]:
                self.state = 305
                self.r_return()
                pass
            elif token in [NmodParser.RNOM]:
                self.state = 306
                self.rnom()
                pass
            elif token in [NmodParser.REXP]:
                self.state = 307
                self.rexp()
                pass
            elif token in [NmodParser.RGAMMA]:
                self.state = 308
                self.rgamma()
                pass
            elif token in [NmodParser.POINTS]:
                self.state = 309
                self.points()
                pass
            elif token in [NmodParser.LINES]:
                self.state = 310
                self.lines()
                pass
            elif token in [NmodParser.TEXT]:
                self.state = 311
                self.text()
                pass
            elif token in [NmodParser.BARPLOT]:
                self.state = 312
                self.barplot()
                pass
            elif token in [NmodParser.PIECHART]:
                self.state = 313
                self.piechart()
                pass
            elif token in [NmodParser.XYPLOT]:
                self.state = 314
                self.xyplot()
                pass
            elif token in [NmodParser.DENSITYPLOT]:
                self.state = 315
                self.densityplot()
                pass
            elif token in [NmodParser.HISTOGRAM]:
                self.state = 316
                self.histogram()
                pass
            elif token in [NmodParser.SIN]:
                self.state = 317
                self.sin()
                pass
            elif token in [NmodParser.COS]:
                self.state = 318
                self.cos()
                pass
            elif token in [NmodParser.TAN]:
                self.state = 319
                self.tan()
                pass
            elif token in [NmodParser.ASIN]:
                self.state = 320
                self.asin()
                pass
            elif token in [NmodParser.ACOS]:
                self.state = 321
                self.acos()
                pass
            elif token in [NmodParser.ATAN]:
                self.state = 322
                self.atan()
                pass
            elif token in [NmodParser.ATAN2]:
                self.state = 323
                self.atan2()
                pass
            elif token in [NmodParser.LOG]:
                self.state = 324
                self.log()
                pass
            elif token in [NmodParser.LOG10]:
                self.state = 325
                self.log10()
                pass
            elif token in [NmodParser.EXPONENT]:
                self.state = 326
                self.exponent()
                pass
            elif token in [NmodParser.MAX]:
                self.state = 327
                self.f_max()
                pass
            elif token in [NmodParser.MIN]:
                self.state = 328
                self.f_min()
                pass
            elif token in [NmodParser.RANGE]:
                self.state = 329
                self.f_range()
                pass
            elif token in [NmodParser.SUM]:
                self.state = 330
                self.f_sum()
                pass
            elif token in [NmodParser.DIFF]:
                self.state = 331
                self.diff()
                pass
            elif token in [NmodParser.PROD]:
                self.state = 332
                self.prod()
                pass
            elif token in [NmodParser.MEAN]:
                self.state = 333
                self.mean()
                pass
            elif token in [NmodParser.MEDIAN]:
                self.state = 334
                self.median()
                pass
            elif token in [NmodParser.QUANTILE]:
                self.state = 335
                self.quantile()
                pass
            elif token in [NmodParser.WEIGHEDMEAN]:
                self.state = 336
                self.weighedmean()
                pass
            elif token in [NmodParser.RANK]:
                self.state = 337
                self.rank()
                pass
            elif token in [NmodParser.VARIANCE]:
                self.state = 338
                self.var()
                pass
            elif token in [NmodParser.SD]:
                self.state = 339
                self.sd()
                pass
            elif token in [NmodParser.COR]:
                self.state = 340
                self.cor()
                pass
            elif token in [NmodParser.COV]:
                self.state = 341
                self.cov()
                pass
            elif token in [NmodParser.ROUND]:
                self.state = 342
                self.f_round()
                pass
            elif token in [NmodParser.TRANSPOSE]:
                self.state = 343
                self.transpose()
                pass
            elif token in [NmodParser.DIAGONAL]:
                self.state = 344
                self.diagonal()
                pass
            elif token in [NmodParser.GINV]:
                self.state = 345
                self.ginv()
                pass
            elif token in [NmodParser.ROWSUM]:
                self.state = 346
                self.rowsum()
                pass
            elif token in [NmodParser.COLSUM]:
                self.state = 347
                self.colsum()
                pass
            elif token in [NmodParser.LOAD]:
                self.state = 348
                self.load()
                pass
            elif token in [NmodParser.DATA]:
                self.state = 349
                self.data()
                pass
            elif token in [NmodParser.LIBRARY]:
                self.state = 350
                self.library()
                pass
            elif token in [NmodParser.RPOIS]:
                self.state = 351
                self.rpois()
                pass
            elif token in [NmodParser.RWEIBULL]:
                self.state = 352
                self.rweibull()
                pass
            elif token in [NmodParser.RBINOM]:
                self.state = 353
                self.rbinom()
                pass
            elif token in [NmodParser.RGEOM]:
                self.state = 354
                self.rgeom()
                pass
            elif token in [NmodParser.RUNIF]:
                self.state = 355
                self.runif()
                pass
            elif token in [NmodParser.ID]:
                self.state = 356
                self.match(NmodParser.ID)
                c.procedureExists(ID)
                self.state = 358
                self.match(NmodParser.LPRACKET)
                c.generateERA()
                self.state = 372
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << NmodParser.NUMBER) | (1 << NmodParser.LPRACKET) | (1 << NmodParser.STRING) | (1 << NmodParser.PLUS) | (1 << NmodParser.MINUS) | (1 << NmodParser.CTEI) | (1 << NmodParser.CTEF) | (1 << NmodParser.CTEC) | (1 << NmodParser.RETURN) | (1 << NmodParser.RNOM) | (1 << NmodParser.REXP) | (1 << NmodParser.RGAMMA) | (1 << NmodParser.POINTS) | (1 << NmodParser.LINES) | (1 << NmodParser.TEXT) | (1 << NmodParser.BARPLOT) | (1 << NmodParser.PIECHART) | (1 << NmodParser.XYPLOT) | (1 << NmodParser.DENSITYPLOT) | (1 << NmodParser.HISTOGRAM) | (1 << NmodParser.SIN) | (1 << NmodParser.COS) | (1 << NmodParser.TAN) | (1 << NmodParser.ASIN) | (1 << NmodParser.ACOS) | (1 << NmodParser.ATAN))) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & ((1 << (NmodParser.ATAN2 - 64)) | (1 << (NmodParser.LOG - 64)) | (1 << (NmodParser.LOG10 - 64)) | (1 << (NmodParser.EXPONENT - 64)) | (1 << (NmodParser.MAX - 64)) | (1 << (NmodParser.MIN - 64)) | (1 << (NmodParser.RANGE - 64)) | (1 << (NmodParser.SUM - 64)) | (1 << (NmodParser.DIFF - 64)) | (1 << (NmodParser.PROD - 64)) | (1 << (NmodParser.MEAN - 64)) | (1 << (NmodParser.MEDIAN - 64)) | (1 << (NmodParser.QUANTILE - 64)) | (1 << (NmodParser.WEIGHEDMEAN - 64)) | (1 << (NmodParser.RANK - 64)) | (1 << (NmodParser.VARIANCE - 64)) | (1 << (NmodParser.SD - 64)) | (1 << (NmodParser.COR - 64)) | (1 << (NmodParser.COV - 64)) | (1 << (NmodParser.ROUND - 64)) | (1 << (NmodParser.TRANSPOSE - 64)) | (1 << (NmodParser.DIAGONAL - 64)) | (1 << (NmodParser.GINV - 64)) | (1 << (NmodParser.ROWSUM - 64)) | (1 << (NmodParser.COLSUM - 64)) | (1 << (NmodParser.LOAD - 64)) | (1 << (NmodParser.DATA - 64)) | (1 << (NmodParser.LIBRARY - 64)) | (1 << (NmodParser.RPOIS - 64)) | (1 << (NmodParser.RWEIBULL - 64)) | (1 << (NmodParser.RBINOM - 64)) | (1 << (NmodParser.RGEOM - 64)) | (1 << (NmodParser.RUNIF - 64)) | (1 << (NmodParser.ID - 64)))) != 0):
                    self.state = 360
                    self.expression()
                    c.validateExpression()
                    self.state = 369
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==NmodParser.COMMA:
                        self.state = 362
                        self.match(NmodParser.COMMA)
                        c.raiseParamCounter()
                        self.state = 364
                        self.expression()
                        c.validateExpression()
                        self.state = 371
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)



                self.state = 374
                self.match(NmodParser.RPRACKET)
                c.generateGoSub()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ExpressionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def sub_exp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(NmodParser.Sub_expContext)
            else:
                return self.getTypedRuleContext(NmodParser.Sub_expContext,i)


        def AND(self, i:int=None):
            if i is None:
                return self.getTokens(NmodParser.AND)
            else:
                return self.getToken(NmodParser.AND, i)

        def OR(self, i:int=None):
            if i is None:
                return self.getTokens(NmodParser.OR)
            else:
                return self.getToken(NmodParser.OR, i)

        def getRuleIndex(self):
            return NmodParser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)




    def expression(self):

        localctx = NmodParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 378
            self.sub_exp()
            c.validateSubExp(), c.topStackOperatorLogical()
            self.state = 396
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==NmodParser.AND or _la==NmodParser.OR:
                self.state = 384 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 384
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [NmodParser.AND]:
                        self.state = 380
                        self.match(NmodParser.AND)
                        self.state = 381
                        self.match(NmodParser.AND)
                        pass
                    elif token in [NmodParser.OR]:
                        self.state = 382
                        self.match(NmodParser.OR)
                        self.state = 383
                        self.match(NmodParser.OR)
                        pass
                    else:
                        raise NoViableAltException(self)

                    self.state = 386 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==NmodParser.AND or _la==NmodParser.OR):
                        break

                c.insertStackOperator()
                self.state = 390 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 389
                    self.sub_exp()
                    self.state = 392 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << NmodParser.NUMBER) | (1 << NmodParser.LPRACKET) | (1 << NmodParser.STRING) | (1 << NmodParser.PLUS) | (1 << NmodParser.MINUS) | (1 << NmodParser.CTEI) | (1 << NmodParser.CTEF) | (1 << NmodParser.CTEC) | (1 << NmodParser.RETURN) | (1 << NmodParser.RNOM) | (1 << NmodParser.REXP) | (1 << NmodParser.RGAMMA) | (1 << NmodParser.POINTS) | (1 << NmodParser.LINES) | (1 << NmodParser.TEXT) | (1 << NmodParser.BARPLOT) | (1 << NmodParser.PIECHART) | (1 << NmodParser.XYPLOT) | (1 << NmodParser.DENSITYPLOT) | (1 << NmodParser.HISTOGRAM) | (1 << NmodParser.SIN) | (1 << NmodParser.COS) | (1 << NmodParser.TAN) | (1 << NmodParser.ASIN) | (1 << NmodParser.ACOS) | (1 << NmodParser.ATAN))) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & ((1 << (NmodParser.ATAN2 - 64)) | (1 << (NmodParser.LOG - 64)) | (1 << (NmodParser.LOG10 - 64)) | (1 << (NmodParser.EXPONENT - 64)) | (1 << (NmodParser.MAX - 64)) | (1 << (NmodParser.MIN - 64)) | (1 << (NmodParser.RANGE - 64)) | (1 << (NmodParser.SUM - 64)) | (1 << (NmodParser.DIFF - 64)) | (1 << (NmodParser.PROD - 64)) | (1 << (NmodParser.MEAN - 64)) | (1 << (NmodParser.MEDIAN - 64)) | (1 << (NmodParser.QUANTILE - 64)) | (1 << (NmodParser.WEIGHEDMEAN - 64)) | (1 << (NmodParser.RANK - 64)) | (1 << (NmodParser.VARIANCE - 64)) | (1 << (NmodParser.SD - 64)) | (1 << (NmodParser.COR - 64)) | (1 << (NmodParser.COV - 64)) | (1 << (NmodParser.ROUND - 64)) | (1 << (NmodParser.TRANSPOSE - 64)) | (1 << (NmodParser.DIAGONAL - 64)) | (1 << (NmodParser.GINV - 64)) | (1 << (NmodParser.ROWSUM - 64)) | (1 << (NmodParser.COLSUM - 64)) | (1 << (NmodParser.LOAD - 64)) | (1 << (NmodParser.DATA - 64)) | (1 << (NmodParser.LIBRARY - 64)) | (1 << (NmodParser.RPOIS - 64)) | (1 << (NmodParser.RWEIBULL - 64)) | (1 << (NmodParser.RBINOM - 64)) | (1 << (NmodParser.RGEOM - 64)) | (1 << (NmodParser.RUNIF - 64)) | (1 << (NmodParser.ID - 64)))) != 0)):
                        break

                c.validateSubExp()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Sub_expContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(NmodParser.ExpContext)
            else:
                return self.getTypedRuleContext(NmodParser.ExpContext,i)


        def EQUALS(self, i:int=None):
            if i is None:
                return self.getTokens(NmodParser.EQUALS)
            else:
                return self.getToken(NmodParser.EQUALS, i)

        def GREATEROR(self, i:int=None):
            if i is None:
                return self.getTokens(NmodParser.GREATEROR)
            else:
                return self.getToken(NmodParser.GREATEROR, i)

        def GREATERTHAN(self, i:int=None):
            if i is None:
                return self.getTokens(NmodParser.GREATERTHAN)
            else:
                return self.getToken(NmodParser.GREATERTHAN, i)

        def LESSEROR(self, i:int=None):
            if i is None:
                return self.getTokens(NmodParser.LESSEROR)
            else:
                return self.getToken(NmodParser.LESSEROR, i)

        def LESSERTHAN(self, i:int=None):
            if i is None:
                return self.getTokens(NmodParser.LESSERTHAN)
            else:
                return self.getToken(NmodParser.LESSERTHAN, i)

        def getRuleIndex(self):
            return NmodParser.RULE_sub_exp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSub_exp" ):
                listener.enterSub_exp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSub_exp" ):
                listener.exitSub_exp(self)




    def sub_exp(self):

        localctx = NmodParser.Sub_expContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_sub_exp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 398
            self.exp()
            c.validateExp(), c.topStackOperatorComparative()
            self.state = 418
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << NmodParser.EQUALS) | (1 << NmodParser.GREATERTHAN) | (1 << NmodParser.GREATEROR) | (1 << NmodParser.LESSERTHAN) | (1 << NmodParser.LESSEROR))) != 0):
                self.state = 406 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 406
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [NmodParser.EQUALS]:
                        self.state = 400
                        self.match(NmodParser.EQUALS)
                        self.state = 401
                        self.match(NmodParser.EQUALS)
                        pass
                    elif token in [NmodParser.GREATEROR]:
                        self.state = 402
                        self.match(NmodParser.GREATEROR)
                        pass
                    elif token in [NmodParser.GREATERTHAN]:
                        self.state = 403
                        self.match(NmodParser.GREATERTHAN)
                        pass
                    elif token in [NmodParser.LESSEROR]:
                        self.state = 404
                        self.match(NmodParser.LESSEROR)
                        pass
                    elif token in [NmodParser.LESSERTHAN]:
                        self.state = 405
                        self.match(NmodParser.LESSERTHAN)
                        pass
                    else:
                        raise NoViableAltException(self)

                    self.state = 408 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << NmodParser.EQUALS) | (1 << NmodParser.GREATERTHAN) | (1 << NmodParser.GREATEROR) | (1 << NmodParser.LESSERTHAN) | (1 << NmodParser.LESSEROR))) != 0)):
                        break

                c.insertStackOperator()
                self.state = 412 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 411
                        self.exp()

                    else:
                        raise NoViableAltException(self)
                    self.state = 414 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,23,self._ctx)

                c.validateExp()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ExpContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def term(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(NmodParser.TermContext)
            else:
                return self.getTypedRuleContext(NmodParser.TermContext,i)


        def MINUS(self, i:int=None):
            if i is None:
                return self.getTokens(NmodParser.MINUS)
            else:
                return self.getToken(NmodParser.MINUS, i)

        def PLUS(self, i:int=None):
            if i is None:
                return self.getTokens(NmodParser.PLUS)
            else:
                return self.getToken(NmodParser.PLUS, i)

        def getRuleIndex(self):
            return NmodParser.RULE_exp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExp" ):
                listener.enterExp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExp" ):
                listener.exitExp(self)




    def exp(self):

        localctx = NmodParser.ExpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_exp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 420
            self.term()
            c.validateTerm(), c.topStackOperatorTerms()
            self.state = 434
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
            if la_ == 1:
                self.state = 423 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 422
                        _la = self._input.LA(1)
                        if not(_la==NmodParser.PLUS or _la==NmodParser.MINUS):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()

                    else:
                        raise NoViableAltException(self)
                    self.state = 425 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,25,self._ctx)

                self.state = 428 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 427
                        self.term()

                    else:
                        raise NoViableAltException(self)
                    self.state = 430 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,26,self._ctx)

                c.validateTerm()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class TermContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def factor(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(NmodParser.FactorContext)
            else:
                return self.getTypedRuleContext(NmodParser.FactorContext,i)


        def DIVISION(self, i:int=None):
            if i is None:
                return self.getTokens(NmodParser.DIVISION)
            else:
                return self.getToken(NmodParser.DIVISION, i)

        def TIMES(self, i:int=None):
            if i is None:
                return self.getTokens(NmodParser.TIMES)
            else:
                return self.getToken(NmodParser.TIMES, i)

        def getRuleIndex(self):
            return NmodParser.RULE_term

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTerm" ):
                listener.enterTerm(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTerm" ):
                listener.exitTerm(self)




    def term(self):

        localctx = NmodParser.TermContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_term)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 436
            self.factor()
            c.validateFactor(), c.topStackOperatorFactors()
            self.state = 450
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==NmodParser.TIMES or _la==NmodParser.DIVISION:
                self.state = 439 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 438
                    _la = self._input.LA(1)
                    if not(_la==NmodParser.TIMES or _la==NmodParser.DIVISION):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 441 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==NmodParser.TIMES or _la==NmodParser.DIVISION):
                        break

                self.state = 444 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 443
                        self.factor()

                    else:
                        raise NoViableAltException(self)
                    self.state = 446 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,29,self._ctx)

                c.validateFactor()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class FactorContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LPRACKET(self):
            return self.getToken(NmodParser.LPRACKET, 0)

        def expression(self):
            return self.getTypedRuleContext(NmodParser.ExpressionContext,0)


        def RPRACKET(self):
            return self.getToken(NmodParser.RPRACKET, 0)

        def var_cte(self):
            return self.getTypedRuleContext(NmodParser.Var_cteContext,0)


        def PLUS(self):
            return self.getToken(NmodParser.PLUS, 0)

        def MINUS(self):
            return self.getToken(NmodParser.MINUS, 0)

        def getRuleIndex(self):
            return NmodParser.RULE_factor

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFactor" ):
                listener.enterFactor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFactor" ):
                listener.exitFactor(self)




    def factor(self):

        localctx = NmodParser.FactorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_factor)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 462
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [NmodParser.LPRACKET]:
                self.state = 452
                self.match(NmodParser.LPRACKET)
                self.state = 453
                self.expression()
                self.state = 454
                self.match(NmodParser.RPRACKET)
                pass
            elif token in [NmodParser.NUMBER, NmodParser.STRING, NmodParser.PLUS, NmodParser.MINUS, NmodParser.CTEI, NmodParser.CTEF, NmodParser.CTEC, NmodParser.RETURN, NmodParser.RNOM, NmodParser.REXP, NmodParser.RGAMMA, NmodParser.POINTS, NmodParser.LINES, NmodParser.TEXT, NmodParser.BARPLOT, NmodParser.PIECHART, NmodParser.XYPLOT, NmodParser.DENSITYPLOT, NmodParser.HISTOGRAM, NmodParser.SIN, NmodParser.COS, NmodParser.TAN, NmodParser.ASIN, NmodParser.ACOS, NmodParser.ATAN, NmodParser.ATAN2, NmodParser.LOG, NmodParser.LOG10, NmodParser.EXPONENT, NmodParser.MAX, NmodParser.MIN, NmodParser.RANGE, NmodParser.SUM, NmodParser.DIFF, NmodParser.PROD, NmodParser.MEAN, NmodParser.MEDIAN, NmodParser.QUANTILE, NmodParser.WEIGHEDMEAN, NmodParser.RANK, NmodParser.VARIANCE, NmodParser.SD, NmodParser.COR, NmodParser.COV, NmodParser.ROUND, NmodParser.TRANSPOSE, NmodParser.DIAGONAL, NmodParser.GINV, NmodParser.ROWSUM, NmodParser.COLSUM, NmodParser.LOAD, NmodParser.DATA, NmodParser.LIBRARY, NmodParser.RPOIS, NmodParser.RWEIBULL, NmodParser.RBINOM, NmodParser.RGEOM, NmodParser.RUNIF, NmodParser.ID]:
                self.state = 457
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==NmodParser.PLUS or _la==NmodParser.MINUS:
                    self.state = 456
                    _la = self._input.LA(1)
                    if not(_la==NmodParser.PLUS or _la==NmodParser.MINUS):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()


                self.state = 459
                self.var_cte()
                c.insertStackType(), c.popStackOperand()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Var_cteContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def f_id(self):
            return self.getTypedRuleContext(NmodParser.F_idContext,0)


        def NUMBER(self):
            return self.getToken(NmodParser.NUMBER, 0)

        def STRING(self):
            return self.getToken(NmodParser.STRING, 0)

        def CTEI(self):
            return self.getToken(NmodParser.CTEI, 0)

        def CTEF(self):
            return self.getToken(NmodParser.CTEF, 0)

        def CTEC(self):
            return self.getToken(NmodParser.CTEC, 0)

        def call_module(self):
            return self.getTypedRuleContext(NmodParser.Call_moduleContext,0)


        def getRuleIndex(self):
            return NmodParser.RULE_var_cte

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVar_cte" ):
                listener.enterVar_cte(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVar_cte" ):
                listener.exitVar_cte(self)




    def var_cte(self):

        localctx = NmodParser.Var_cteContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_var_cte)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 471
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,33,self._ctx)
            if la_ == 1:
                self.state = 464
                self.f_id()
                pass

            elif la_ == 2:
                self.state = 465
                self.match(NmodParser.NUMBER)
                pass

            elif la_ == 3:
                self.state = 466
                self.match(NmodParser.STRING)
                pass

            elif la_ == 4:
                self.state = 467
                self.match(NmodParser.CTEI)
                pass

            elif la_ == 5:
                self.state = 468
                self.match(NmodParser.CTEF)
                pass

            elif la_ == 6:
                self.state = 469
                self.match(NmodParser.CTEC)
                pass

            elif la_ == 7:
                self.state = 470
                self.call_module()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class R_returnContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(NmodParser.RETURN, 0)

        def expression(self):
            return self.getTypedRuleContext(NmodParser.ExpressionContext,0)


        def SEMICOLON(self):
            return self.getToken(NmodParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return NmodParser.RULE_r_return

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterR_return" ):
                listener.enterR_return(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitR_return" ):
                listener.exitR_return(self)




    def r_return(self):

        localctx = NmodParser.R_returnContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_r_return)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 473
            self.match(NmodParser.RETURN)
            self.state = 474
            self.expression()
            self.state = 475
            self.match(NmodParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class RnomContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RNOM(self):
            return self.getToken(NmodParser.RNOM, 0)

        def LPRACKET(self):
            return self.getToken(NmodParser.LPRACKET, 0)

        def var_cte(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(NmodParser.Var_cteContext)
            else:
                return self.getTypedRuleContext(NmodParser.Var_cteContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(NmodParser.COMMA)
            else:
                return self.getToken(NmodParser.COMMA, i)

        def RPRACKET(self):
            return self.getToken(NmodParser.RPRACKET, 0)

        def SEMICOLON(self):
            return self.getToken(NmodParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return NmodParser.RULE_rnom

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRnom" ):
                listener.enterRnom(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRnom" ):
                listener.exitRnom(self)




    def rnom(self):

        localctx = NmodParser.RnomContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_rnom)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 477
            self.match(NmodParser.RNOM)
            self.state = 478
            self.match(NmodParser.LPRACKET)
            self.state = 479
            self.var_cte()
            self.state = 480
            self.match(NmodParser.COMMA)
            self.state = 481
            self.var_cte()
            self.state = 482
            self.match(NmodParser.COMMA)
            self.state = 483
            self.var_cte()
            self.state = 484
            self.match(NmodParser.COMMA)
            self.state = 485
            self.var_cte()
            self.state = 486
            self.match(NmodParser.RPRACKET)
            self.state = 487
            self.match(NmodParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class RexpContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def REXP(self):
            return self.getToken(NmodParser.REXP, 0)

        def LPRACKET(self):
            return self.getToken(NmodParser.LPRACKET, 0)

        def var_cte(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(NmodParser.Var_cteContext)
            else:
                return self.getTypedRuleContext(NmodParser.Var_cteContext,i)


        def COMMA(self):
            return self.getToken(NmodParser.COMMA, 0)

        def RPRACKET(self):
            return self.getToken(NmodParser.RPRACKET, 0)

        def SEMICOLON(self):
            return self.getToken(NmodParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return NmodParser.RULE_rexp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRexp" ):
                listener.enterRexp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRexp" ):
                listener.exitRexp(self)




    def rexp(self):

        localctx = NmodParser.RexpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_rexp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 489
            self.match(NmodParser.REXP)
            self.state = 490
            self.match(NmodParser.LPRACKET)
            self.state = 491
            self.var_cte()
            self.state = 492
            self.match(NmodParser.COMMA)
            self.state = 493
            self.var_cte()
            self.state = 494
            self.match(NmodParser.RPRACKET)
            self.state = 495
            self.match(NmodParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class RgammaContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RGAMMA(self):
            return self.getToken(NmodParser.RGAMMA, 0)

        def LPRACKET(self):
            return self.getToken(NmodParser.LPRACKET, 0)

        def var_cte(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(NmodParser.Var_cteContext)
            else:
                return self.getTypedRuleContext(NmodParser.Var_cteContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(NmodParser.COMMA)
            else:
                return self.getToken(NmodParser.COMMA, i)

        def RPRACKET(self):
            return self.getToken(NmodParser.RPRACKET, 0)

        def SEMICOLON(self):
            return self.getToken(NmodParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return NmodParser.RULE_rgamma

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRgamma" ):
                listener.enterRgamma(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRgamma" ):
                listener.exitRgamma(self)




    def rgamma(self):

        localctx = NmodParser.RgammaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_rgamma)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 497
            self.match(NmodParser.RGAMMA)
            self.state = 498
            self.match(NmodParser.LPRACKET)
            self.state = 499
            self.var_cte()
            self.state = 500
            self.match(NmodParser.COMMA)
            self.state = 501
            self.var_cte()
            self.state = 502
            self.match(NmodParser.COMMA)
            self.state = 503
            self.var_cte()
            self.state = 504
            self.match(NmodParser.RPRACKET)
            self.state = 505
            self.match(NmodParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class PointsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def POINTS(self):
            return self.getToken(NmodParser.POINTS, 0)

        def LPRACKET(self):
            return self.getToken(NmodParser.LPRACKET, 0)

        def var_cte(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(NmodParser.Var_cteContext)
            else:
                return self.getTypedRuleContext(NmodParser.Var_cteContext,i)


        def COMMA(self):
            return self.getToken(NmodParser.COMMA, 0)

        def RPRACKET(self):
            return self.getToken(NmodParser.RPRACKET, 0)

        def SEMICOLON(self):
            return self.getToken(NmodParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return NmodParser.RULE_points

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPoints" ):
                listener.enterPoints(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPoints" ):
                listener.exitPoints(self)




    def points(self):

        localctx = NmodParser.PointsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_points)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 507
            self.match(NmodParser.POINTS)
            self.state = 508
            self.match(NmodParser.LPRACKET)
            self.state = 509
            self.var_cte()
            self.state = 510
            self.match(NmodParser.COMMA)
            self.state = 511
            self.var_cte()
            self.state = 512
            self.match(NmodParser.RPRACKET)
            self.state = 513
            self.match(NmodParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class LinesContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LINES(self):
            return self.getToken(NmodParser.LINES, 0)

        def LPRACKET(self):
            return self.getToken(NmodParser.LPRACKET, 0)

        def var_cte(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(NmodParser.Var_cteContext)
            else:
                return self.getTypedRuleContext(NmodParser.Var_cteContext,i)


        def COMMA(self):
            return self.getToken(NmodParser.COMMA, 0)

        def RPRACKET(self):
            return self.getToken(NmodParser.RPRACKET, 0)

        def SEMICOLON(self):
            return self.getToken(NmodParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return NmodParser.RULE_lines

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLines" ):
                listener.enterLines(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLines" ):
                listener.exitLines(self)




    def lines(self):

        localctx = NmodParser.LinesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_lines)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 515
            self.match(NmodParser.LINES)
            self.state = 516
            self.match(NmodParser.LPRACKET)
            self.state = 517
            self.var_cte()
            self.state = 518
            self.match(NmodParser.COMMA)
            self.state = 519
            self.var_cte()
            self.state = 520
            self.match(NmodParser.RPRACKET)
            self.state = 521
            self.match(NmodParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class TextContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TEXT(self):
            return self.getToken(NmodParser.TEXT, 0)

        def LPRACKET(self):
            return self.getToken(NmodParser.LPRACKET, 0)

        def CTEI(self, i:int=None):
            if i is None:
                return self.getTokens(NmodParser.CTEI)
            else:
                return self.getToken(NmodParser.CTEI, i)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(NmodParser.COMMA)
            else:
                return self.getToken(NmodParser.COMMA, i)

        def f_id(self):
            return self.getTypedRuleContext(NmodParser.F_idContext,0)


        def RPRACKET(self):
            return self.getToken(NmodParser.RPRACKET, 0)

        def SEMICOLON(self):
            return self.getToken(NmodParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return NmodParser.RULE_text

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterText" ):
                listener.enterText(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitText" ):
                listener.exitText(self)




    def text(self):

        localctx = NmodParser.TextContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_text)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 523
            self.match(NmodParser.TEXT)
            self.state = 524
            self.match(NmodParser.LPRACKET)
            self.state = 525
            self.match(NmodParser.CTEI)
            self.state = 526
            self.match(NmodParser.COMMA)
            self.state = 527
            self.match(NmodParser.CTEI)
            self.state = 528
            self.match(NmodParser.COMMA)
            self.state = 529
            self.f_id()
            self.state = 530
            self.match(NmodParser.RPRACKET)
            self.state = 531
            self.match(NmodParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class BarplotContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BARPLOT(self):
            return self.getToken(NmodParser.BARPLOT, 0)

        def LPRACKET(self):
            return self.getToken(NmodParser.LPRACKET, 0)

        def var_cte(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(NmodParser.Var_cteContext)
            else:
                return self.getTypedRuleContext(NmodParser.Var_cteContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(NmodParser.COMMA)
            else:
                return self.getToken(NmodParser.COMMA, i)

        def RPRACKET(self):
            return self.getToken(NmodParser.RPRACKET, 0)

        def SEMICOLON(self):
            return self.getToken(NmodParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return NmodParser.RULE_barplot

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBarplot" ):
                listener.enterBarplot(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBarplot" ):
                listener.exitBarplot(self)




    def barplot(self):

        localctx = NmodParser.BarplotContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_barplot)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 533
            self.match(NmodParser.BARPLOT)
            self.state = 534
            self.match(NmodParser.LPRACKET)
            self.state = 535
            self.var_cte()
            self.state = 536
            self.match(NmodParser.COMMA)
            self.state = 537
            self.var_cte()
            self.state = 538
            self.match(NmodParser.COMMA)
            self.state = 539
            self.var_cte()
            self.state = 540
            self.match(NmodParser.COMMA)
            self.state = 541
            self.var_cte()
            self.state = 542
            self.match(NmodParser.RPRACKET)
            self.state = 543
            self.match(NmodParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class PiechartContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PIECHART(self):
            return self.getToken(NmodParser.PIECHART, 0)

        def LPRACKET(self):
            return self.getToken(NmodParser.LPRACKET, 0)

        def var_cte(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(NmodParser.Var_cteContext)
            else:
                return self.getTypedRuleContext(NmodParser.Var_cteContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(NmodParser.COMMA)
            else:
                return self.getToken(NmodParser.COMMA, i)

        def RPRACKET(self):
            return self.getToken(NmodParser.RPRACKET, 0)

        def SEMICOLON(self):
            return self.getToken(NmodParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return NmodParser.RULE_piechart

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPiechart" ):
                listener.enterPiechart(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPiechart" ):
                listener.exitPiechart(self)




    def piechart(self):

        localctx = NmodParser.PiechartContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_piechart)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 545
            self.match(NmodParser.PIECHART)
            self.state = 546
            self.match(NmodParser.LPRACKET)
            self.state = 547
            self.var_cte()
            self.state = 548
            self.match(NmodParser.COMMA)
            self.state = 549
            self.var_cte()
            self.state = 550
            self.match(NmodParser.COMMA)
            self.state = 551
            self.var_cte()
            self.state = 552
            self.match(NmodParser.COMMA)
            self.state = 553
            self.var_cte()
            self.state = 554
            self.match(NmodParser.RPRACKET)
            self.state = 555
            self.match(NmodParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class XyplotContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def XYPLOT(self):
            return self.getToken(NmodParser.XYPLOT, 0)

        def LPRACKET(self):
            return self.getToken(NmodParser.LPRACKET, 0)

        def var_cte(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(NmodParser.Var_cteContext)
            else:
                return self.getTypedRuleContext(NmodParser.Var_cteContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(NmodParser.COMMA)
            else:
                return self.getToken(NmodParser.COMMA, i)

        def RPRACKET(self):
            return self.getToken(NmodParser.RPRACKET, 0)

        def SEMICOLON(self):
            return self.getToken(NmodParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return NmodParser.RULE_xyplot

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterXyplot" ):
                listener.enterXyplot(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitXyplot" ):
                listener.exitXyplot(self)




    def xyplot(self):

        localctx = NmodParser.XyplotContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_xyplot)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 557
            self.match(NmodParser.XYPLOT)
            self.state = 558
            self.match(NmodParser.LPRACKET)
            self.state = 559
            self.var_cte()
            self.state = 560
            self.match(NmodParser.COMMA)
            self.state = 561
            self.var_cte()
            self.state = 562
            self.match(NmodParser.COMMA)
            self.state = 563
            self.var_cte()
            self.state = 564
            self.match(NmodParser.COMMA)
            self.state = 565
            self.var_cte()
            self.state = 566
            self.match(NmodParser.RPRACKET)
            self.state = 567
            self.match(NmodParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class DensityplotContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DENSITYPLOT(self):
            return self.getToken(NmodParser.DENSITYPLOT, 0)

        def LPRACKET(self):
            return self.getToken(NmodParser.LPRACKET, 0)

        def var_cte(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(NmodParser.Var_cteContext)
            else:
                return self.getTypedRuleContext(NmodParser.Var_cteContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(NmodParser.COMMA)
            else:
                return self.getToken(NmodParser.COMMA, i)

        def RPRACKET(self):
            return self.getToken(NmodParser.RPRACKET, 0)

        def SEMICOLON(self):
            return self.getToken(NmodParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return NmodParser.RULE_densityplot

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDensityplot" ):
                listener.enterDensityplot(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDensityplot" ):
                listener.exitDensityplot(self)




    def densityplot(self):

        localctx = NmodParser.DensityplotContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_densityplot)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 569
            self.match(NmodParser.DENSITYPLOT)
            self.state = 570
            self.match(NmodParser.LPRACKET)
            self.state = 571
            self.var_cte()
            self.state = 572
            self.match(NmodParser.COMMA)
            self.state = 573
            self.var_cte()
            self.state = 574
            self.match(NmodParser.COMMA)
            self.state = 575
            self.var_cte()
            self.state = 576
            self.match(NmodParser.COMMA)
            self.state = 577
            self.var_cte()
            self.state = 578
            self.match(NmodParser.RPRACKET)
            self.state = 579
            self.match(NmodParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class HistogramContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def HISTOGRAM(self):
            return self.getToken(NmodParser.HISTOGRAM, 0)

        def LPRACKET(self):
            return self.getToken(NmodParser.LPRACKET, 0)

        def var_cte(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(NmodParser.Var_cteContext)
            else:
                return self.getTypedRuleContext(NmodParser.Var_cteContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(NmodParser.COMMA)
            else:
                return self.getToken(NmodParser.COMMA, i)

        def RPRACKET(self):
            return self.getToken(NmodParser.RPRACKET, 0)

        def SEMICOLON(self):
            return self.getToken(NmodParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return NmodParser.RULE_histogram

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterHistogram" ):
                listener.enterHistogram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitHistogram" ):
                listener.exitHistogram(self)




    def histogram(self):

        localctx = NmodParser.HistogramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_histogram)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 581
            self.match(NmodParser.HISTOGRAM)
            self.state = 582
            self.match(NmodParser.LPRACKET)
            self.state = 583
            self.var_cte()
            self.state = 584
            self.match(NmodParser.COMMA)
            self.state = 585
            self.var_cte()
            self.state = 586
            self.match(NmodParser.COMMA)
            self.state = 587
            self.var_cte()
            self.state = 588
            self.match(NmodParser.COMMA)
            self.state = 589
            self.var_cte()
            self.state = 590
            self.match(NmodParser.RPRACKET)
            self.state = 591
            self.match(NmodParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class SinContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SIN(self):
            return self.getToken(NmodParser.SIN, 0)

        def LPRACKET(self):
            return self.getToken(NmodParser.LPRACKET, 0)

        def expression(self):
            return self.getTypedRuleContext(NmodParser.ExpressionContext,0)


        def RPRACKET(self):
            return self.getToken(NmodParser.RPRACKET, 0)

        def SEMICOLON(self):
            return self.getToken(NmodParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return NmodParser.RULE_sin

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSin" ):
                listener.enterSin(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSin" ):
                listener.exitSin(self)




    def sin(self):

        localctx = NmodParser.SinContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_sin)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 593
            self.match(NmodParser.SIN)
            self.state = 594
            self.match(NmodParser.LPRACKET)
            self.state = 595
            self.expression()
            self.state = 596
            self.match(NmodParser.RPRACKET)
            self.state = 597
            self.match(NmodParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class CosContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COS(self):
            return self.getToken(NmodParser.COS, 0)

        def LPRACKET(self):
            return self.getToken(NmodParser.LPRACKET, 0)

        def expression(self):
            return self.getTypedRuleContext(NmodParser.ExpressionContext,0)


        def RPRACKET(self):
            return self.getToken(NmodParser.RPRACKET, 0)

        def SEMICOLON(self):
            return self.getToken(NmodParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return NmodParser.RULE_cos

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCos" ):
                listener.enterCos(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCos" ):
                listener.exitCos(self)




    def cos(self):

        localctx = NmodParser.CosContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_cos)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 599
            self.match(NmodParser.COS)
            self.state = 600
            self.match(NmodParser.LPRACKET)
            self.state = 601
            self.expression()
            self.state = 602
            self.match(NmodParser.RPRACKET)
            self.state = 603
            self.match(NmodParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class TanContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TAN(self):
            return self.getToken(NmodParser.TAN, 0)

        def LPRACKET(self):
            return self.getToken(NmodParser.LPRACKET, 0)

        def expression(self):
            return self.getTypedRuleContext(NmodParser.ExpressionContext,0)


        def RPRACKET(self):
            return self.getToken(NmodParser.RPRACKET, 0)

        def SEMICOLON(self):
            return self.getToken(NmodParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return NmodParser.RULE_tan

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTan" ):
                listener.enterTan(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTan" ):
                listener.exitTan(self)




    def tan(self):

        localctx = NmodParser.TanContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_tan)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 605
            self.match(NmodParser.TAN)
            self.state = 606
            self.match(NmodParser.LPRACKET)
            self.state = 607
            self.expression()
            self.state = 608
            self.match(NmodParser.RPRACKET)
            self.state = 609
            self.match(NmodParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class AsinContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ASIN(self):
            return self.getToken(NmodParser.ASIN, 0)

        def LPRACKET(self):
            return self.getToken(NmodParser.LPRACKET, 0)

        def expression(self):
            return self.getTypedRuleContext(NmodParser.ExpressionContext,0)


        def RPRACKET(self):
            return self.getToken(NmodParser.RPRACKET, 0)

        def SEMICOLON(self):
            return self.getToken(NmodParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return NmodParser.RULE_asin

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAsin" ):
                listener.enterAsin(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAsin" ):
                listener.exitAsin(self)




    def asin(self):

        localctx = NmodParser.AsinContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_asin)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 611
            self.match(NmodParser.ASIN)
            self.state = 612
            self.match(NmodParser.LPRACKET)
            self.state = 613
            self.expression()
            self.state = 614
            self.match(NmodParser.RPRACKET)
            self.state = 615
            self.match(NmodParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class AcosContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ACOS(self):
            return self.getToken(NmodParser.ACOS, 0)

        def LPRACKET(self):
            return self.getToken(NmodParser.LPRACKET, 0)

        def expression(self):
            return self.getTypedRuleContext(NmodParser.ExpressionContext,0)


        def RPRACKET(self):
            return self.getToken(NmodParser.RPRACKET, 0)

        def SEMICOLON(self):
            return self.getToken(NmodParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return NmodParser.RULE_acos

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAcos" ):
                listener.enterAcos(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAcos" ):
                listener.exitAcos(self)




    def acos(self):

        localctx = NmodParser.AcosContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_acos)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 617
            self.match(NmodParser.ACOS)
            self.state = 618
            self.match(NmodParser.LPRACKET)
            self.state = 619
            self.expression()
            self.state = 620
            self.match(NmodParser.RPRACKET)
            self.state = 621
            self.match(NmodParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class AtanContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ATAN(self):
            return self.getToken(NmodParser.ATAN, 0)

        def LPRACKET(self):
            return self.getToken(NmodParser.LPRACKET, 0)

        def expression(self):
            return self.getTypedRuleContext(NmodParser.ExpressionContext,0)


        def RPRACKET(self):
            return self.getToken(NmodParser.RPRACKET, 0)

        def SEMICOLON(self):
            return self.getToken(NmodParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return NmodParser.RULE_atan

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAtan" ):
                listener.enterAtan(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAtan" ):
                listener.exitAtan(self)




    def atan(self):

        localctx = NmodParser.AtanContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_atan)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 623
            self.match(NmodParser.ATAN)
            self.state = 624
            self.match(NmodParser.LPRACKET)
            self.state = 625
            self.expression()
            self.state = 626
            self.match(NmodParser.RPRACKET)
            self.state = 627
            self.match(NmodParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Atan2Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ATAN2(self):
            return self.getToken(NmodParser.ATAN2, 0)

        def LPRACKET(self):
            return self.getToken(NmodParser.LPRACKET, 0)

        def expression(self):
            return self.getTypedRuleContext(NmodParser.ExpressionContext,0)


        def RPRACKET(self):
            return self.getToken(NmodParser.RPRACKET, 0)

        def SEMICOLON(self):
            return self.getToken(NmodParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return NmodParser.RULE_atan2

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAtan2" ):
                listener.enterAtan2(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAtan2" ):
                listener.exitAtan2(self)




    def atan2(self):

        localctx = NmodParser.Atan2Context(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_atan2)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 629
            self.match(NmodParser.ATAN2)
            self.state = 630
            self.match(NmodParser.LPRACKET)
            self.state = 631
            self.expression()
            self.state = 632
            self.match(NmodParser.RPRACKET)
            self.state = 633
            self.match(NmodParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class LogContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LOG(self):
            return self.getToken(NmodParser.LOG, 0)

        def LPRACKET(self):
            return self.getToken(NmodParser.LPRACKET, 0)

        def expression(self):
            return self.getTypedRuleContext(NmodParser.ExpressionContext,0)


        def RPRACKET(self):
            return self.getToken(NmodParser.RPRACKET, 0)

        def SEMICOLON(self):
            return self.getToken(NmodParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return NmodParser.RULE_log

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLog" ):
                listener.enterLog(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLog" ):
                listener.exitLog(self)




    def log(self):

        localctx = NmodParser.LogContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_log)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 635
            self.match(NmodParser.LOG)
            self.state = 636
            self.match(NmodParser.LPRACKET)
            self.state = 637
            self.expression()
            self.state = 638
            self.match(NmodParser.RPRACKET)
            self.state = 639
            self.match(NmodParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Log10Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LOG10(self):
            return self.getToken(NmodParser.LOG10, 0)

        def LPRACKET(self):
            return self.getToken(NmodParser.LPRACKET, 0)

        def expression(self):
            return self.getTypedRuleContext(NmodParser.ExpressionContext,0)


        def RPRACKET(self):
            return self.getToken(NmodParser.RPRACKET, 0)

        def SEMICOLON(self):
            return self.getToken(NmodParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return NmodParser.RULE_log10

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLog10" ):
                listener.enterLog10(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLog10" ):
                listener.exitLog10(self)




    def log10(self):

        localctx = NmodParser.Log10Context(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_log10)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 641
            self.match(NmodParser.LOG10)
            self.state = 642
            self.match(NmodParser.LPRACKET)
            self.state = 643
            self.expression()
            self.state = 644
            self.match(NmodParser.RPRACKET)
            self.state = 645
            self.match(NmodParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ExponentContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EXPONENT(self):
            return self.getToken(NmodParser.EXPONENT, 0)

        def LPRACKET(self):
            return self.getToken(NmodParser.LPRACKET, 0)

        def expression(self):
            return self.getTypedRuleContext(NmodParser.ExpressionContext,0)


        def RPRACKET(self):
            return self.getToken(NmodParser.RPRACKET, 0)

        def SEMICOLON(self):
            return self.getToken(NmodParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return NmodParser.RULE_exponent

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExponent" ):
                listener.enterExponent(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExponent" ):
                listener.exitExponent(self)




    def exponent(self):

        localctx = NmodParser.ExponentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_exponent)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 647
            self.match(NmodParser.EXPONENT)
            self.state = 648
            self.match(NmodParser.LPRACKET)
            self.state = 649
            self.expression()
            self.state = 650
            self.match(NmodParser.RPRACKET)
            self.state = 651
            self.match(NmodParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class F_maxContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MAX(self):
            return self.getToken(NmodParser.MAX, 0)

        def LPRACKET(self):
            return self.getToken(NmodParser.LPRACKET, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(NmodParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(NmodParser.ExpressionContext,i)


        def RPRACKET(self):
            return self.getToken(NmodParser.RPRACKET, 0)

        def SEMICOLON(self):
            return self.getToken(NmodParser.SEMICOLON, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(NmodParser.COMMA)
            else:
                return self.getToken(NmodParser.COMMA, i)

        def getRuleIndex(self):
            return NmodParser.RULE_f_max

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterF_max" ):
                listener.enterF_max(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitF_max" ):
                listener.exitF_max(self)




    def f_max(self):

        localctx = NmodParser.F_maxContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_f_max)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 653
            self.match(NmodParser.MAX)
            self.state = 654
            self.match(NmodParser.LPRACKET)
            self.state = 655
            self.expression()
            self.state = 660
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==NmodParser.COMMA:
                self.state = 656
                self.match(NmodParser.COMMA)
                self.state = 657
                self.expression()
                self.state = 662
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 663
            self.match(NmodParser.RPRACKET)
            self.state = 664
            self.match(NmodParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class F_minContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MIN(self):
            return self.getToken(NmodParser.MIN, 0)

        def LPRACKET(self):
            return self.getToken(NmodParser.LPRACKET, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(NmodParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(NmodParser.ExpressionContext,i)


        def RPRACKET(self):
            return self.getToken(NmodParser.RPRACKET, 0)

        def SEMICOLON(self):
            return self.getToken(NmodParser.SEMICOLON, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(NmodParser.COMMA)
            else:
                return self.getToken(NmodParser.COMMA, i)

        def getRuleIndex(self):
            return NmodParser.RULE_f_min

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterF_min" ):
                listener.enterF_min(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitF_min" ):
                listener.exitF_min(self)




    def f_min(self):

        localctx = NmodParser.F_minContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_f_min)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 666
            self.match(NmodParser.MIN)
            self.state = 667
            self.match(NmodParser.LPRACKET)
            self.state = 668
            self.expression()
            self.state = 673
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==NmodParser.COMMA:
                self.state = 669
                self.match(NmodParser.COMMA)
                self.state = 670
                self.expression()
                self.state = 675
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 676
            self.match(NmodParser.RPRACKET)
            self.state = 677
            self.match(NmodParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class F_rangeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RANGE(self):
            return self.getToken(NmodParser.RANGE, 0)

        def LPRACKET(self):
            return self.getToken(NmodParser.LPRACKET, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(NmodParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(NmodParser.ExpressionContext,i)


        def RPRACKET(self):
            return self.getToken(NmodParser.RPRACKET, 0)

        def SEMICOLON(self):
            return self.getToken(NmodParser.SEMICOLON, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(NmodParser.COMMA)
            else:
                return self.getToken(NmodParser.COMMA, i)

        def getRuleIndex(self):
            return NmodParser.RULE_f_range

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterF_range" ):
                listener.enterF_range(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitF_range" ):
                listener.exitF_range(self)




    def f_range(self):

        localctx = NmodParser.F_rangeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_f_range)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 679
            self.match(NmodParser.RANGE)
            self.state = 680
            self.match(NmodParser.LPRACKET)
            self.state = 681
            self.expression()
            self.state = 686
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==NmodParser.COMMA:
                self.state = 682
                self.match(NmodParser.COMMA)
                self.state = 683
                self.expression()
                self.state = 688
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 689
            self.match(NmodParser.RPRACKET)
            self.state = 690
            self.match(NmodParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class F_sumContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SUM(self):
            return self.getToken(NmodParser.SUM, 0)

        def LPRACKET(self):
            return self.getToken(NmodParser.LPRACKET, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(NmodParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(NmodParser.ExpressionContext,i)


        def RPRACKET(self):
            return self.getToken(NmodParser.RPRACKET, 0)

        def SEMICOLON(self):
            return self.getToken(NmodParser.SEMICOLON, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(NmodParser.COMMA)
            else:
                return self.getToken(NmodParser.COMMA, i)

        def getRuleIndex(self):
            return NmodParser.RULE_f_sum

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterF_sum" ):
                listener.enterF_sum(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitF_sum" ):
                listener.exitF_sum(self)




    def f_sum(self):

        localctx = NmodParser.F_sumContext(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_f_sum)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 692
            self.match(NmodParser.SUM)
            self.state = 693
            self.match(NmodParser.LPRACKET)
            self.state = 694
            self.expression()
            self.state = 699
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==NmodParser.COMMA:
                self.state = 695
                self.match(NmodParser.COMMA)
                self.state = 696
                self.expression()
                self.state = 701
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 702
            self.match(NmodParser.RPRACKET)
            self.state = 703
            self.match(NmodParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class DiffContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DIFF(self):
            return self.getToken(NmodParser.DIFF, 0)

        def LPRACKET(self):
            return self.getToken(NmodParser.LPRACKET, 0)

        def f_id(self):
            return self.getTypedRuleContext(NmodParser.F_idContext,0)


        def COMMA(self):
            return self.getToken(NmodParser.COMMA, 0)

        def CTEI(self):
            return self.getToken(NmodParser.CTEI, 0)

        def RPRACKET(self):
            return self.getToken(NmodParser.RPRACKET, 0)

        def SEMICOLON(self):
            return self.getToken(NmodParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return NmodParser.RULE_diff

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDiff" ):
                listener.enterDiff(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDiff" ):
                listener.exitDiff(self)




    def diff(self):

        localctx = NmodParser.DiffContext(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_diff)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 705
            self.match(NmodParser.DIFF)
            self.state = 706
            self.match(NmodParser.LPRACKET)
            self.state = 707
            self.f_id()
            self.state = 708
            self.match(NmodParser.COMMA)
            self.state = 709
            self.match(NmodParser.CTEI)
            self.state = 710
            self.match(NmodParser.RPRACKET)
            self.state = 711
            self.match(NmodParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ProdContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PROD(self):
            return self.getToken(NmodParser.PROD, 0)

        def LPRACKET(self):
            return self.getToken(NmodParser.LPRACKET, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(NmodParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(NmodParser.ExpressionContext,i)


        def RPRACKET(self):
            return self.getToken(NmodParser.RPRACKET, 0)

        def SEMICOLON(self):
            return self.getToken(NmodParser.SEMICOLON, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(NmodParser.COMMA)
            else:
                return self.getToken(NmodParser.COMMA, i)

        def getRuleIndex(self):
            return NmodParser.RULE_prod

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProd" ):
                listener.enterProd(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProd" ):
                listener.exitProd(self)




    def prod(self):

        localctx = NmodParser.ProdContext(self, self._ctx, self.state)
        self.enterRule(localctx, 96, self.RULE_prod)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 713
            self.match(NmodParser.PROD)
            self.state = 714
            self.match(NmodParser.LPRACKET)
            self.state = 715
            self.expression()
            self.state = 720
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==NmodParser.COMMA:
                self.state = 716
                self.match(NmodParser.COMMA)
                self.state = 717
                self.expression()
                self.state = 722
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 723
            self.match(NmodParser.RPRACKET)
            self.state = 724
            self.match(NmodParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class MeanContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MEAN(self):
            return self.getToken(NmodParser.MEAN, 0)

        def LPRACKET(self):
            return self.getToken(NmodParser.LPRACKET, 0)

        def f_id(self):
            return self.getTypedRuleContext(NmodParser.F_idContext,0)


        def RPRACKET(self):
            return self.getToken(NmodParser.RPRACKET, 0)

        def SEMICOLON(self):
            return self.getToken(NmodParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return NmodParser.RULE_mean

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMean" ):
                listener.enterMean(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMean" ):
                listener.exitMean(self)




    def mean(self):

        localctx = NmodParser.MeanContext(self, self._ctx, self.state)
        self.enterRule(localctx, 98, self.RULE_mean)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 726
            self.match(NmodParser.MEAN)
            self.state = 727
            self.match(NmodParser.LPRACKET)
            self.state = 728
            self.f_id()
            self.state = 729
            self.match(NmodParser.RPRACKET)
            self.state = 730
            self.match(NmodParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class MedianContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MEDIAN(self):
            return self.getToken(NmodParser.MEDIAN, 0)

        def LPRACKET(self):
            return self.getToken(NmodParser.LPRACKET, 0)

        def f_id(self):
            return self.getTypedRuleContext(NmodParser.F_idContext,0)


        def RPRACKET(self):
            return self.getToken(NmodParser.RPRACKET, 0)

        def SEMICOLON(self):
            return self.getToken(NmodParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return NmodParser.RULE_median

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMedian" ):
                listener.enterMedian(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMedian" ):
                listener.exitMedian(self)




    def median(self):

        localctx = NmodParser.MedianContext(self, self._ctx, self.state)
        self.enterRule(localctx, 100, self.RULE_median)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 732
            self.match(NmodParser.MEDIAN)
            self.state = 733
            self.match(NmodParser.LPRACKET)
            self.state = 734
            self.f_id()
            self.state = 735
            self.match(NmodParser.RPRACKET)
            self.state = 736
            self.match(NmodParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class QuantileContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def QUANTILE(self):
            return self.getToken(NmodParser.QUANTILE, 0)

        def LPRACKET(self):
            return self.getToken(NmodParser.LPRACKET, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(NmodParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(NmodParser.ExpressionContext,i)


        def RPRACKET(self):
            return self.getToken(NmodParser.RPRACKET, 0)

        def SEMICOLON(self):
            return self.getToken(NmodParser.SEMICOLON, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(NmodParser.COMMA)
            else:
                return self.getToken(NmodParser.COMMA, i)

        def getRuleIndex(self):
            return NmodParser.RULE_quantile

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterQuantile" ):
                listener.enterQuantile(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitQuantile" ):
                listener.exitQuantile(self)




    def quantile(self):

        localctx = NmodParser.QuantileContext(self, self._ctx, self.state)
        self.enterRule(localctx, 102, self.RULE_quantile)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 738
            self.match(NmodParser.QUANTILE)
            self.state = 739
            self.match(NmodParser.LPRACKET)
            self.state = 740
            self.expression()
            self.state = 745
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==NmodParser.COMMA:
                self.state = 741
                self.match(NmodParser.COMMA)
                self.state = 742
                self.expression()
                self.state = 747
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 748
            self.match(NmodParser.RPRACKET)
            self.state = 749
            self.match(NmodParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class WeighedmeanContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WEIGHEDMEAN(self):
            return self.getToken(NmodParser.WEIGHEDMEAN, 0)

        def LPRACKET(self):
            return self.getToken(NmodParser.LPRACKET, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(NmodParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(NmodParser.ExpressionContext,i)


        def RPRACKET(self):
            return self.getToken(NmodParser.RPRACKET, 0)

        def SEMICOLON(self):
            return self.getToken(NmodParser.SEMICOLON, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(NmodParser.COMMA)
            else:
                return self.getToken(NmodParser.COMMA, i)

        def getRuleIndex(self):
            return NmodParser.RULE_weighedmean

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWeighedmean" ):
                listener.enterWeighedmean(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWeighedmean" ):
                listener.exitWeighedmean(self)




    def weighedmean(self):

        localctx = NmodParser.WeighedmeanContext(self, self._ctx, self.state)
        self.enterRule(localctx, 104, self.RULE_weighedmean)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 751
            self.match(NmodParser.WEIGHEDMEAN)
            self.state = 752
            self.match(NmodParser.LPRACKET)
            self.state = 753
            self.expression()
            self.state = 758
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==NmodParser.COMMA:
                self.state = 754
                self.match(NmodParser.COMMA)
                self.state = 755
                self.expression()
                self.state = 760
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 761
            self.match(NmodParser.RPRACKET)
            self.state = 762
            self.match(NmodParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class RankContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RANK(self):
            return self.getToken(NmodParser.RANK, 0)

        def LPRACKET(self):
            return self.getToken(NmodParser.LPRACKET, 0)

        def f_id(self):
            return self.getTypedRuleContext(NmodParser.F_idContext,0)


        def COMMA(self):
            return self.getToken(NmodParser.COMMA, 0)

        def ZERO(self):
            return self.getToken(NmodParser.ZERO, 0)

        def RPRACKET(self):
            return self.getToken(NmodParser.RPRACKET, 0)

        def SEMICOLON(self):
            return self.getToken(NmodParser.SEMICOLON, 0)

        def ONE(self):
            return self.getToken(NmodParser.ONE, 0)

        def getRuleIndex(self):
            return NmodParser.RULE_rank

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRank" ):
                listener.enterRank(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRank" ):
                listener.exitRank(self)




    def rank(self):

        localctx = NmodParser.RankContext(self, self._ctx, self.state)
        self.enterRule(localctx, 106, self.RULE_rank)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 780
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,41,self._ctx)
            if la_ == 1:
                self.state = 764
                self.match(NmodParser.RANK)
                self.state = 765
                self.match(NmodParser.LPRACKET)
                self.state = 766
                self.f_id()
                self.state = 767
                self.match(NmodParser.COMMA)
                self.state = 768
                self.match(NmodParser.ZERO)
                self.state = 769
                self.match(NmodParser.RPRACKET)
                self.state = 770
                self.match(NmodParser.SEMICOLON)
                pass

            elif la_ == 2:
                self.state = 772
                self.match(NmodParser.RANK)
                self.state = 773
                self.match(NmodParser.LPRACKET)
                self.state = 774
                self.f_id()
                self.state = 775
                self.match(NmodParser.COMMA)
                self.state = 776
                self.match(NmodParser.ONE)
                self.state = 777
                self.match(NmodParser.RPRACKET)
                self.state = 778
                self.match(NmodParser.SEMICOLON)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class VarContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VARIANCE(self):
            return self.getToken(NmodParser.VARIANCE, 0)

        def LPRACKET(self):
            return self.getToken(NmodParser.LPRACKET, 0)

        def var_cte(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(NmodParser.Var_cteContext)
            else:
                return self.getTypedRuleContext(NmodParser.Var_cteContext,i)


        def COMMA(self):
            return self.getToken(NmodParser.COMMA, 0)

        def RPRACKET(self):
            return self.getToken(NmodParser.RPRACKET, 0)

        def SEMICOLON(self):
            return self.getToken(NmodParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return NmodParser.RULE_var

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVar" ):
                listener.enterVar(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVar" ):
                listener.exitVar(self)




    def var(self):

        localctx = NmodParser.VarContext(self, self._ctx, self.state)
        self.enterRule(localctx, 108, self.RULE_var)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 782
            self.match(NmodParser.VARIANCE)
            self.state = 783
            self.match(NmodParser.LPRACKET)
            self.state = 784
            self.var_cte()
            self.state = 785
            self.match(NmodParser.COMMA)
            self.state = 786
            self.var_cte()
            self.state = 787
            self.match(NmodParser.RPRACKET)
            self.state = 788
            self.match(NmodParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class SdContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SD(self):
            return self.getToken(NmodParser.SD, 0)

        def LPRACKET(self):
            return self.getToken(NmodParser.LPRACKET, 0)

        def var_cte(self):
            return self.getTypedRuleContext(NmodParser.Var_cteContext,0)


        def RPRACKET(self):
            return self.getToken(NmodParser.RPRACKET, 0)

        def SEMICOLON(self):
            return self.getToken(NmodParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return NmodParser.RULE_sd

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSd" ):
                listener.enterSd(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSd" ):
                listener.exitSd(self)




    def sd(self):

        localctx = NmodParser.SdContext(self, self._ctx, self.state)
        self.enterRule(localctx, 110, self.RULE_sd)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 790
            self.match(NmodParser.SD)
            self.state = 791
            self.match(NmodParser.LPRACKET)
            self.state = 792
            self.var_cte()
            self.state = 793
            self.match(NmodParser.RPRACKET)
            self.state = 794
            self.match(NmodParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class CorContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COR(self):
            return self.getToken(NmodParser.COR, 0)

        def LPRACKET(self):
            return self.getToken(NmodParser.LPRACKET, 0)

        def var_cte(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(NmodParser.Var_cteContext)
            else:
                return self.getTypedRuleContext(NmodParser.Var_cteContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(NmodParser.COMMA)
            else:
                return self.getToken(NmodParser.COMMA, i)

        def RPRACKET(self):
            return self.getToken(NmodParser.RPRACKET, 0)

        def SEMICOLON(self):
            return self.getToken(NmodParser.SEMICOLON, 0)

        def PEARSON(self):
            return self.getToken(NmodParser.PEARSON, 0)

        def KENDALL(self):
            return self.getToken(NmodParser.KENDALL, 0)

        def SPEARMAN(self):
            return self.getToken(NmodParser.SPEARMAN, 0)

        def getRuleIndex(self):
            return NmodParser.RULE_cor

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCor" ):
                listener.enterCor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCor" ):
                listener.exitCor(self)




    def cor(self):

        localctx = NmodParser.CorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 112, self.RULE_cor)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 796
            self.match(NmodParser.COR)
            self.state = 797
            self.match(NmodParser.LPRACKET)
            self.state = 798
            self.var_cte()
            self.state = 799
            self.match(NmodParser.COMMA)
            self.state = 800
            self.var_cte()
            self.state = 801
            self.match(NmodParser.COMMA)
            self.state = 802
            _la = self._input.LA(1)
            if not(((((_la - 99)) & ~0x3f) == 0 and ((1 << (_la - 99)) & ((1 << (NmodParser.PEARSON - 99)) | (1 << (NmodParser.KENDALL - 99)) | (1 << (NmodParser.SPEARMAN - 99)))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 803
            self.match(NmodParser.RPRACKET)
            self.state = 804
            self.match(NmodParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class CovContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COV(self):
            return self.getToken(NmodParser.COV, 0)

        def LPRACKET(self):
            return self.getToken(NmodParser.LPRACKET, 0)

        def var_cte(self):
            return self.getTypedRuleContext(NmodParser.Var_cteContext,0)


        def RPRACKET(self):
            return self.getToken(NmodParser.RPRACKET, 0)

        def SEMICOLON(self):
            return self.getToken(NmodParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return NmodParser.RULE_cov

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCov" ):
                listener.enterCov(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCov" ):
                listener.exitCov(self)




    def cov(self):

        localctx = NmodParser.CovContext(self, self._ctx, self.state)
        self.enterRule(localctx, 114, self.RULE_cov)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 806
            self.match(NmodParser.COV)
            self.state = 807
            self.match(NmodParser.LPRACKET)
            self.state = 808
            self.var_cte()
            self.state = 809
            self.match(NmodParser.RPRACKET)
            self.state = 810
            self.match(NmodParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class F_roundContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ROUND(self):
            return self.getToken(NmodParser.ROUND, 0)

        def LPRACKET(self):
            return self.getToken(NmodParser.LPRACKET, 0)

        def var_cte(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(NmodParser.Var_cteContext)
            else:
                return self.getTypedRuleContext(NmodParser.Var_cteContext,i)


        def RPRACKET(self):
            return self.getToken(NmodParser.RPRACKET, 0)

        def SEMICOLON(self):
            return self.getToken(NmodParser.SEMICOLON, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(NmodParser.COMMA)
            else:
                return self.getToken(NmodParser.COMMA, i)

        def getRuleIndex(self):
            return NmodParser.RULE_f_round

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterF_round" ):
                listener.enterF_round(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitF_round" ):
                listener.exitF_round(self)




    def f_round(self):

        localctx = NmodParser.F_roundContext(self, self._ctx, self.state)
        self.enterRule(localctx, 116, self.RULE_f_round)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 812
            self.match(NmodParser.ROUND)
            self.state = 813
            self.match(NmodParser.LPRACKET)
            self.state = 814
            self.var_cte()
            self.state = 819
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==NmodParser.COMMA:
                self.state = 815
                self.match(NmodParser.COMMA)
                self.state = 816
                self.var_cte()
                self.state = 821
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 822
            self.match(NmodParser.RPRACKET)
            self.state = 823
            self.match(NmodParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class TransposeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TRANSPOSE(self):
            return self.getToken(NmodParser.TRANSPOSE, 0)

        def LPRACKET(self):
            return self.getToken(NmodParser.LPRACKET, 0)

        def var_cte(self):
            return self.getTypedRuleContext(NmodParser.Var_cteContext,0)


        def RPRACKET(self):
            return self.getToken(NmodParser.RPRACKET, 0)

        def SEMICOLON(self):
            return self.getToken(NmodParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return NmodParser.RULE_transpose

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTranspose" ):
                listener.enterTranspose(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTranspose" ):
                listener.exitTranspose(self)




    def transpose(self):

        localctx = NmodParser.TransposeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 118, self.RULE_transpose)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 825
            self.match(NmodParser.TRANSPOSE)
            self.state = 826
            self.match(NmodParser.LPRACKET)
            self.state = 827
            self.var_cte()
            self.state = 828
            self.match(NmodParser.RPRACKET)
            self.state = 829
            self.match(NmodParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class DiagonalContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DIAGONAL(self):
            return self.getToken(NmodParser.DIAGONAL, 0)

        def LPRACKET(self):
            return self.getToken(NmodParser.LPRACKET, 0)

        def var_cte(self):
            return self.getTypedRuleContext(NmodParser.Var_cteContext,0)


        def RPRACKET(self):
            return self.getToken(NmodParser.RPRACKET, 0)

        def SEMICOLON(self):
            return self.getToken(NmodParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return NmodParser.RULE_diagonal

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDiagonal" ):
                listener.enterDiagonal(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDiagonal" ):
                listener.exitDiagonal(self)




    def diagonal(self):

        localctx = NmodParser.DiagonalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 120, self.RULE_diagonal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 831
            self.match(NmodParser.DIAGONAL)
            self.state = 832
            self.match(NmodParser.LPRACKET)
            self.state = 833
            self.var_cte()
            self.state = 834
            self.match(NmodParser.RPRACKET)
            self.state = 835
            self.match(NmodParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class GinvContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def GINV(self):
            return self.getToken(NmodParser.GINV, 0)

        def LPRACKET(self):
            return self.getToken(NmodParser.LPRACKET, 0)

        def var_cte(self):
            return self.getTypedRuleContext(NmodParser.Var_cteContext,0)


        def RPRACKET(self):
            return self.getToken(NmodParser.RPRACKET, 0)

        def SEMICOLON(self):
            return self.getToken(NmodParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return NmodParser.RULE_ginv

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGinv" ):
                listener.enterGinv(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGinv" ):
                listener.exitGinv(self)




    def ginv(self):

        localctx = NmodParser.GinvContext(self, self._ctx, self.state)
        self.enterRule(localctx, 122, self.RULE_ginv)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 837
            self.match(NmodParser.GINV)
            self.state = 838
            self.match(NmodParser.LPRACKET)
            self.state = 839
            self.var_cte()
            self.state = 840
            self.match(NmodParser.RPRACKET)
            self.state = 841
            self.match(NmodParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class RowsumContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ROWSUM(self):
            return self.getToken(NmodParser.ROWSUM, 0)

        def LPRACKET(self):
            return self.getToken(NmodParser.LPRACKET, 0)

        def var_cte(self):
            return self.getTypedRuleContext(NmodParser.Var_cteContext,0)


        def RPRACKET(self):
            return self.getToken(NmodParser.RPRACKET, 0)

        def SEMICOLON(self):
            return self.getToken(NmodParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return NmodParser.RULE_rowsum

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRowsum" ):
                listener.enterRowsum(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRowsum" ):
                listener.exitRowsum(self)




    def rowsum(self):

        localctx = NmodParser.RowsumContext(self, self._ctx, self.state)
        self.enterRule(localctx, 124, self.RULE_rowsum)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 843
            self.match(NmodParser.ROWSUM)
            self.state = 844
            self.match(NmodParser.LPRACKET)
            self.state = 845
            self.var_cte()
            self.state = 846
            self.match(NmodParser.RPRACKET)
            self.state = 847
            self.match(NmodParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ColsumContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COLSUM(self):
            return self.getToken(NmodParser.COLSUM, 0)

        def LPRACKET(self):
            return self.getToken(NmodParser.LPRACKET, 0)

        def var_cte(self):
            return self.getTypedRuleContext(NmodParser.Var_cteContext,0)


        def RPRACKET(self):
            return self.getToken(NmodParser.RPRACKET, 0)

        def SEMICOLON(self):
            return self.getToken(NmodParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return NmodParser.RULE_colsum

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterColsum" ):
                listener.enterColsum(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitColsum" ):
                listener.exitColsum(self)




    def colsum(self):

        localctx = NmodParser.ColsumContext(self, self._ctx, self.state)
        self.enterRule(localctx, 126, self.RULE_colsum)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 849
            self.match(NmodParser.COLSUM)
            self.state = 850
            self.match(NmodParser.LPRACKET)
            self.state = 851
            self.var_cte()
            self.state = 852
            self.match(NmodParser.RPRACKET)
            self.state = 853
            self.match(NmodParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class LoadContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LOAD(self):
            return self.getToken(NmodParser.LOAD, 0)

        def LPRACKET(self):
            return self.getToken(NmodParser.LPRACKET, 0)

        def var_cte(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(NmodParser.Var_cteContext)
            else:
                return self.getTypedRuleContext(NmodParser.Var_cteContext,i)


        def RPRACKET(self):
            return self.getToken(NmodParser.RPRACKET, 0)

        def SEMICOLON(self):
            return self.getToken(NmodParser.SEMICOLON, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(NmodParser.COMMA)
            else:
                return self.getToken(NmodParser.COMMA, i)

        def getRuleIndex(self):
            return NmodParser.RULE_load

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLoad" ):
                listener.enterLoad(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLoad" ):
                listener.exitLoad(self)




    def load(self):

        localctx = NmodParser.LoadContext(self, self._ctx, self.state)
        self.enterRule(localctx, 128, self.RULE_load)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 855
            self.match(NmodParser.LOAD)
            self.state = 856
            self.match(NmodParser.LPRACKET)
            self.state = 857
            self.var_cte()
            self.state = 862
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==NmodParser.COMMA:
                self.state = 858
                self.match(NmodParser.COMMA)
                self.state = 859
                self.var_cte()
                self.state = 864
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 865
            self.match(NmodParser.RPRACKET)
            self.state = 866
            self.match(NmodParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class DataContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DATA(self):
            return self.getToken(NmodParser.DATA, 0)

        def LPRACKET(self):
            return self.getToken(NmodParser.LPRACKET, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(NmodParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(NmodParser.ExpressionContext,i)


        def RPRACKET(self):
            return self.getToken(NmodParser.RPRACKET, 0)

        def SEMICOLON(self):
            return self.getToken(NmodParser.SEMICOLON, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(NmodParser.COMMA)
            else:
                return self.getToken(NmodParser.COMMA, i)

        def getRuleIndex(self):
            return NmodParser.RULE_data

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterData" ):
                listener.enterData(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitData" ):
                listener.exitData(self)




    def data(self):

        localctx = NmodParser.DataContext(self, self._ctx, self.state)
        self.enterRule(localctx, 130, self.RULE_data)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 868
            self.match(NmodParser.DATA)
            self.state = 869
            self.match(NmodParser.LPRACKET)
            self.state = 870
            self.expression()
            self.state = 875
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==NmodParser.COMMA:
                self.state = 871
                self.match(NmodParser.COMMA)
                self.state = 872
                self.expression()
                self.state = 877
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 878
            self.match(NmodParser.RPRACKET)
            self.state = 879
            self.match(NmodParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class LibraryContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LIBRARY(self):
            return self.getToken(NmodParser.LIBRARY, 0)

        def LPRACKET(self):
            return self.getToken(NmodParser.LPRACKET, 0)

        def var_cte(self):
            return self.getTypedRuleContext(NmodParser.Var_cteContext,0)


        def RPRACKET(self):
            return self.getToken(NmodParser.RPRACKET, 0)

        def SEMICOLON(self):
            return self.getToken(NmodParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return NmodParser.RULE_library

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLibrary" ):
                listener.enterLibrary(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLibrary" ):
                listener.exitLibrary(self)




    def library(self):

        localctx = NmodParser.LibraryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 132, self.RULE_library)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 881
            self.match(NmodParser.LIBRARY)
            self.state = 882
            self.match(NmodParser.LPRACKET)
            self.state = 883
            self.var_cte()
            self.state = 884
            self.match(NmodParser.RPRACKET)
            self.state = 885
            self.match(NmodParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class RpoisContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RPOIS(self):
            return self.getToken(NmodParser.RPOIS, 0)

        def LPRACKET(self):
            return self.getToken(NmodParser.LPRACKET, 0)

        def var_cte(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(NmodParser.Var_cteContext)
            else:
                return self.getTypedRuleContext(NmodParser.Var_cteContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(NmodParser.COMMA)
            else:
                return self.getToken(NmodParser.COMMA, i)

        def RPRACKET(self):
            return self.getToken(NmodParser.RPRACKET, 0)

        def SEMICOLON(self):
            return self.getToken(NmodParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return NmodParser.RULE_rpois

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRpois" ):
                listener.enterRpois(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRpois" ):
                listener.exitRpois(self)




    def rpois(self):

        localctx = NmodParser.RpoisContext(self, self._ctx, self.state)
        self.enterRule(localctx, 134, self.RULE_rpois)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 887
            self.match(NmodParser.RPOIS)
            self.state = 888
            self.match(NmodParser.LPRACKET)
            self.state = 889
            self.var_cte()
            self.state = 890
            self.match(NmodParser.COMMA)
            self.state = 891
            self.var_cte()
            self.state = 892
            self.match(NmodParser.COMMA)
            self.state = 893
            self.var_cte()
            self.state = 894
            self.match(NmodParser.RPRACKET)
            self.state = 895
            self.match(NmodParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class RweibullContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RWEIBULL(self):
            return self.getToken(NmodParser.RWEIBULL, 0)

        def LPRACKET(self):
            return self.getToken(NmodParser.LPRACKET, 0)

        def var_cte(self):
            return self.getTypedRuleContext(NmodParser.Var_cteContext,0)


        def RPRACKET(self):
            return self.getToken(NmodParser.RPRACKET, 0)

        def SEMICOLON(self):
            return self.getToken(NmodParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return NmodParser.RULE_rweibull

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRweibull" ):
                listener.enterRweibull(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRweibull" ):
                listener.exitRweibull(self)




    def rweibull(self):

        localctx = NmodParser.RweibullContext(self, self._ctx, self.state)
        self.enterRule(localctx, 136, self.RULE_rweibull)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 897
            self.match(NmodParser.RWEIBULL)
            self.state = 898
            self.match(NmodParser.LPRACKET)
            self.state = 899
            self.var_cte()
            self.state = 900
            self.match(NmodParser.RPRACKET)
            self.state = 901
            self.match(NmodParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class RbinomContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RBINOM(self):
            return self.getToken(NmodParser.RBINOM, 0)

        def LPRACKET(self):
            return self.getToken(NmodParser.LPRACKET, 0)

        def var_cte(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(NmodParser.Var_cteContext)
            else:
                return self.getTypedRuleContext(NmodParser.Var_cteContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(NmodParser.COMMA)
            else:
                return self.getToken(NmodParser.COMMA, i)

        def RPRACKET(self):
            return self.getToken(NmodParser.RPRACKET, 0)

        def SEMICOLON(self):
            return self.getToken(NmodParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return NmodParser.RULE_rbinom

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRbinom" ):
                listener.enterRbinom(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRbinom" ):
                listener.exitRbinom(self)




    def rbinom(self):

        localctx = NmodParser.RbinomContext(self, self._ctx, self.state)
        self.enterRule(localctx, 138, self.RULE_rbinom)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 903
            self.match(NmodParser.RBINOM)
            self.state = 904
            self.match(NmodParser.LPRACKET)
            self.state = 905
            self.var_cte()
            self.state = 906
            self.match(NmodParser.COMMA)
            self.state = 907
            self.var_cte()
            self.state = 908
            self.match(NmodParser.COMMA)
            self.state = 909
            self.var_cte()
            self.state = 910
            self.match(NmodParser.RPRACKET)
            self.state = 911
            self.match(NmodParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class RgeomContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RGEOM(self):
            return self.getToken(NmodParser.RGEOM, 0)

        def LPRACKET(self):
            return self.getToken(NmodParser.LPRACKET, 0)

        def var_cte(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(NmodParser.Var_cteContext)
            else:
                return self.getTypedRuleContext(NmodParser.Var_cteContext,i)


        def COMMA(self):
            return self.getToken(NmodParser.COMMA, 0)

        def RPRACKET(self):
            return self.getToken(NmodParser.RPRACKET, 0)

        def SEMICOLON(self):
            return self.getToken(NmodParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return NmodParser.RULE_rgeom

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRgeom" ):
                listener.enterRgeom(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRgeom" ):
                listener.exitRgeom(self)




    def rgeom(self):

        localctx = NmodParser.RgeomContext(self, self._ctx, self.state)
        self.enterRule(localctx, 140, self.RULE_rgeom)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 913
            self.match(NmodParser.RGEOM)
            self.state = 914
            self.match(NmodParser.LPRACKET)
            self.state = 915
            self.var_cte()
            self.state = 916
            self.match(NmodParser.COMMA)
            self.state = 917
            self.var_cte()
            self.state = 918
            self.match(NmodParser.RPRACKET)
            self.state = 919
            self.match(NmodParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class RunifContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RUNIF(self):
            return self.getToken(NmodParser.RUNIF, 0)

        def LPRACKET(self):
            return self.getToken(NmodParser.LPRACKET, 0)

        def var_cte(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(NmodParser.Var_cteContext)
            else:
                return self.getTypedRuleContext(NmodParser.Var_cteContext,i)


        def COMMA(self):
            return self.getToken(NmodParser.COMMA, 0)

        def RPRACKET(self):
            return self.getToken(NmodParser.RPRACKET, 0)

        def SEMICOLON(self):
            return self.getToken(NmodParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return NmodParser.RULE_runif

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRunif" ):
                listener.enterRunif(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRunif" ):
                listener.exitRunif(self)




    def runif(self):

        localctx = NmodParser.RunifContext(self, self._ctx, self.state)
        self.enterRule(localctx, 142, self.RULE_runif)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 921
            self.match(NmodParser.RUNIF)
            self.state = 922
            self.match(NmodParser.LPRACKET)
            self.state = 923
            self.var_cte()
            self.state = 924
            self.match(NmodParser.COMMA)
            self.state = 925
            self.var_cte()
            self.state = 926
            self.match(NmodParser.RPRACKET)
            self.state = 927
            self.match(NmodParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class DotchartContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return NmodParser.RULE_dotchart

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDotchart" ):
                listener.enterDotchart(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDotchart" ):
                listener.exitDotchart(self)




    def dotchart(self):

        localctx = NmodParser.DotchartContext(self, self._ctx, self.state)
        self.enterRule(localctx, 144, self.RULE_dotchart)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 929
            self.match(NmodParser.T__0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





