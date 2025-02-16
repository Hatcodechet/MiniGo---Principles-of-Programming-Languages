# Generated from main/minigo/parser/MiniGo.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2D")
        buf.write("\u01f8\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\4F\tF\4G\tG\4H\tH\3\2\3\2\3\2\3\2\3\3\3")
        buf.write("\3\3\3\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\6\3\6\3\6")
        buf.write("\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3")
        buf.write("\b\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\n")
        buf.write("\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3")
        buf.write("\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r\3\16\3\16\3\16")
        buf.write("\3\16\3\16\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\17\3\17")
        buf.write("\3\20\3\20\3\20\3\20\3\21\3\21\3\21\3\21\3\21\3\21\3\21")
        buf.write("\3\21\3\21\3\22\3\22\3\22\3\22\3\22\3\22\3\23\3\23\3\23")
        buf.write("\3\23\3\23\3\23\3\24\3\24\3\24\3\24\3\25\3\25\3\25\3\25")
        buf.write("\3\25\3\26\3\26\3\26\3\26\3\26\3\26\3\27\3\27\3\30\3\30")
        buf.write("\3\31\3\31\3\32\3\32\3\33\3\33\3\34\3\34\3\34\3\35\3\35")
        buf.write("\3\35\3\36\3\36\3\37\3\37\3\37\3 \3 \3!\3!\3!\3\"\3\"")
        buf.write("\3\"\3#\3#\3#\3$\3$\3%\3%\3&\3&\3&\3\'\3\'\3\'\3(\3(\3")
        buf.write("(\3)\3)\3)\3*\3*\3*\3+\3+\3+\3,\3,\3-\3-\3.\3.\3/\3/\3")
        buf.write("\60\3\60\3\61\3\61\3\62\3\62\3\63\3\63\3\64\3\64\3\65")
        buf.write("\3\65\3\66\3\66\7\66\u0157\n\66\f\66\16\66\u015a\13\66")
        buf.write("\3\67\3\67\3\67\7\67\u015f\n\67\f\67\16\67\u0162\13\67")
        buf.write("\5\67\u0164\n\67\38\38\38\68\u0169\n8\r8\168\u016a\39")
        buf.write("\39\39\69\u0170\n9\r9\169\u0171\3:\3:\3:\6:\u0177\n:\r")
        buf.write(":\16:\u0178\3;\3;\3;\5;\u017e\n;\3;\5;\u0181\n;\3;\3;")
        buf.write("\3;\5;\u0186\n;\3;\5;\u0189\n;\5;\u018b\n;\3<\6<\u018e")
        buf.write("\n<\r<\16<\u018f\3=\3=\5=\u0194\n=\3=\3=\3>\3>\3>\3?\3")
        buf.write("?\3?\3@\3@\3@\3A\3A\3A\7A\u01a4\nA\fA\16A\u01a7\13A\3")
        buf.write("A\3A\3A\7A\u01ac\nA\fA\16A\u01af\13A\3A\3A\3A\3B\3B\3")
        buf.write("B\7B\u01b7\nB\fB\16B\u01ba\13B\3B\3B\3C\5C\u01bf\nC\3")
        buf.write("C\3C\3C\3D\6D\u01c5\nD\rD\16D\u01c6\3D\3D\3E\3E\3E\3E")
        buf.write("\3E\7E\u01d0\nE\fE\16E\u01d3\13E\3E\3E\3E\3E\3E\3F\3F")
        buf.write("\3F\3F\7F\u01de\nF\fF\16F\u01e1\13F\3F\3F\3G\3G\3G\7G")
        buf.write("\u01e8\nG\fG\16G\u01eb\13G\3G\5G\u01ee\nG\3G\3G\5G\u01f2")
        buf.write("\nG\3G\3G\3H\3H\3H\4\u01ad\u01d1\2I\3\3\5\4\7\5\t\6\13")
        buf.write("\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17\35\20\37")
        buf.write("\21!\22#\23%\24\'\25)\26+\27-\30/\31\61\32\63\33\65\34")
        buf.write("\67\359\36;\37= ?!A\"C#E$G%I&K\'M(O)Q*S+U,W-Y.[/]\60_")
        buf.write("\61a\62c\63e\64g\65i\66k\67m8o9q:s;u<w\2y\2{\2}\2\177")
        buf.write("\2\u0081=\u0083>\u0085?\u0087@\u0089A\u008bB\u008dC\u008f")
        buf.write("D\3\2\24\5\2C\\aac|\6\2\62;C\\aac|\3\2\63;\3\2\62;\4\2")
        buf.write("DDdd\3\2\62\63\4\2QQqq\3\2\629\4\2ZZzz\5\2\62;CHch\4\2")
        buf.write("GGgg\4\2--//\7\2$$^^ppttvv\6\2\f\f\17\17$$^^\t\2\f\f\17")
        buf.write("\17$$^^ppttvv\5\2\13\13\16\17\"\"\4\2\f\f\17\17\5\2\f")
        buf.write("\f$$^^\2\u020d\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t")
        buf.write("\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3")
        buf.write("\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2")
        buf.write("\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2")
        buf.write("\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2")
        buf.write("\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65")
        buf.write("\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2")
        buf.write("\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2")
        buf.write("\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2")
        buf.write("\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3")
        buf.write("\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e")
        buf.write("\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2")
        buf.write("o\3\2\2\2\2q\3\2\2\2\2s\3\2\2\2\2u\3\2\2\2\2\u0081\3\2")
        buf.write("\2\2\2\u0083\3\2\2\2\2\u0085\3\2\2\2\2\u0087\3\2\2\2\2")
        buf.write("\u0089\3\2\2\2\2\u008b\3\2\2\2\2\u008d\3\2\2\2\2\u008f")
        buf.write("\3\2\2\2\3\u0091\3\2\2\2\5\u0095\3\2\2\2\7\u0098\3\2\2")
        buf.write("\2\t\u009d\3\2\2\2\13\u00a1\3\2\2\2\r\u00a8\3\2\2\2\17")
        buf.write("\u00ad\3\2\2\2\21\u00b2\3\2\2\2\23\u00b9\3\2\2\2\25\u00c3")
        buf.write("\3\2\2\2\27\u00ca\3\2\2\2\31\u00ce\3\2\2\2\33\u00d4\3")
        buf.write("\2\2\2\35\u00dc\3\2\2\2\37\u00e2\3\2\2\2!\u00e6\3\2\2")
        buf.write("\2#\u00ef\3\2\2\2%\u00f5\3\2\2\2\'\u00fb\3\2\2\2)\u00ff")
        buf.write("\3\2\2\2+\u0104\3\2\2\2-\u010a\3\2\2\2/\u010c\3\2\2\2")
        buf.write("\61\u010e\3\2\2\2\63\u0110\3\2\2\2\65\u0112\3\2\2\2\67")
        buf.write("\u0114\3\2\2\29\u0117\3\2\2\2;\u011a\3\2\2\2=\u011c\3")
        buf.write("\2\2\2?\u011f\3\2\2\2A\u0121\3\2\2\2C\u0124\3\2\2\2E\u0127")
        buf.write("\3\2\2\2G\u012a\3\2\2\2I\u012c\3\2\2\2K\u012e\3\2\2\2")
        buf.write("M\u0131\3\2\2\2O\u0134\3\2\2\2Q\u0137\3\2\2\2S\u013a\3")
        buf.write("\2\2\2U\u013d\3\2\2\2W\u0140\3\2\2\2Y\u0142\3\2\2\2[\u0144")
        buf.write("\3\2\2\2]\u0146\3\2\2\2_\u0148\3\2\2\2a\u014a\3\2\2\2")
        buf.write("c\u014c\3\2\2\2e\u014e\3\2\2\2g\u0150\3\2\2\2i\u0152\3")
        buf.write("\2\2\2k\u0154\3\2\2\2m\u0163\3\2\2\2o\u0165\3\2\2\2q\u016c")
        buf.write("\3\2\2\2s\u0173\3\2\2\2u\u018a\3\2\2\2w\u018d\3\2\2\2")
        buf.write("y\u0191\3\2\2\2{\u0197\3\2\2\2}\u019a\3\2\2\2\177\u019d")
        buf.write("\3\2\2\2\u0081\u01a0\3\2\2\2\u0083\u01b3\3\2\2\2\u0085")
        buf.write("\u01be\3\2\2\2\u0087\u01c4\3\2\2\2\u0089\u01ca\3\2\2\2")
        buf.write("\u008b\u01d9\3\2\2\2\u008d\u01e4\3\2\2\2\u008f\u01f5\3")
        buf.write("\2\2\2\u0091\u0092\7u\2\2\u0092\u0093\7v\2\2\u0093\u0094")
        buf.write("\7t\2\2\u0094\4\3\2\2\2\u0095\u0096\7k\2\2\u0096\u0097")
        buf.write("\7h\2\2\u0097\6\3\2\2\2\u0098\u0099\7g\2\2\u0099\u009a")
        buf.write("\7n\2\2\u009a\u009b\7u\2\2\u009b\u009c\7g\2\2\u009c\b")
        buf.write("\3\2\2\2\u009d\u009e\7h\2\2\u009e\u009f\7q\2\2\u009f\u00a0")
        buf.write("\7t\2\2\u00a0\n\3\2\2\2\u00a1\u00a2\7t\2\2\u00a2\u00a3")
        buf.write("\7g\2\2\u00a3\u00a4\7v\2\2\u00a4\u00a5\7w\2\2\u00a5\u00a6")
        buf.write("\7t\2\2\u00a6\u00a7\7p\2\2\u00a7\f\3\2\2\2\u00a8\u00a9")
        buf.write("\7h\2\2\u00a9\u00aa\7w\2\2\u00aa\u00ab\7p\2\2\u00ab\u00ac")
        buf.write("\7e\2\2\u00ac\16\3\2\2\2\u00ad\u00ae\7v\2\2\u00ae\u00af")
        buf.write("\7{\2\2\u00af\u00b0\7r\2\2\u00b0\u00b1\7g\2\2\u00b1\20")
        buf.write("\3\2\2\2\u00b2\u00b3\7u\2\2\u00b3\u00b4\7v\2\2\u00b4\u00b5")
        buf.write("\7t\2\2\u00b5\u00b6\7w\2\2\u00b6\u00b7\7e\2\2\u00b7\u00b8")
        buf.write("\7v\2\2\u00b8\22\3\2\2\2\u00b9\u00ba\7k\2\2\u00ba\u00bb")
        buf.write("\7p\2\2\u00bb\u00bc\7v\2\2\u00bc\u00bd\7g\2\2\u00bd\u00be")
        buf.write("\7t\2\2\u00be\u00bf\7h\2\2\u00bf\u00c0\7c\2\2\u00c0\u00c1")
        buf.write("\7e\2\2\u00c1\u00c2\7g\2\2\u00c2\24\3\2\2\2\u00c3\u00c4")
        buf.write("\7u\2\2\u00c4\u00c5\7v\2\2\u00c5\u00c6\7t\2\2\u00c6\u00c7")
        buf.write("\7k\2\2\u00c7\u00c8\7p\2\2\u00c8\u00c9\7i\2\2\u00c9\26")
        buf.write("\3\2\2\2\u00ca\u00cb\7k\2\2\u00cb\u00cc\7p\2\2\u00cc\u00cd")
        buf.write("\7v\2\2\u00cd\30\3\2\2\2\u00ce\u00cf\7h\2\2\u00cf\u00d0")
        buf.write("\7n\2\2\u00d0\u00d1\7q\2\2\u00d1\u00d2\7c\2\2\u00d2\u00d3")
        buf.write("\7v\2\2\u00d3\32\3\2\2\2\u00d4\u00d5\7d\2\2\u00d5\u00d6")
        buf.write("\7q\2\2\u00d6\u00d7\7q\2\2\u00d7\u00d8\7n\2\2\u00d8\u00d9")
        buf.write("\7g\2\2\u00d9\u00da\7c\2\2\u00da\u00db\7p\2\2\u00db\34")
        buf.write("\3\2\2\2\u00dc\u00dd\7e\2\2\u00dd\u00de\7q\2\2\u00de\u00df")
        buf.write("\7p\2\2\u00df\u00e0\7u\2\2\u00e0\u00e1\7v\2\2\u00e1\36")
        buf.write("\3\2\2\2\u00e2\u00e3\7x\2\2\u00e3\u00e4\7c\2\2\u00e4\u00e5")
        buf.write("\7t\2\2\u00e5 \3\2\2\2\u00e6\u00e7\7e\2\2\u00e7\u00e8")
        buf.write("\7q\2\2\u00e8\u00e9\7p\2\2\u00e9\u00ea\7v\2\2\u00ea\u00eb")
        buf.write("\7k\2\2\u00eb\u00ec\7p\2\2\u00ec\u00ed\7w\2\2\u00ed\u00ee")
        buf.write("\7g\2\2\u00ee\"\3\2\2\2\u00ef\u00f0\7d\2\2\u00f0\u00f1")
        buf.write("\7t\2\2\u00f1\u00f2\7g\2\2\u00f2\u00f3\7c\2\2\u00f3\u00f4")
        buf.write("\7m\2\2\u00f4$\3\2\2\2\u00f5\u00f6\7t\2\2\u00f6\u00f7")
        buf.write("\7c\2\2\u00f7\u00f8\7p\2\2\u00f8\u00f9\7i\2\2\u00f9\u00fa")
        buf.write("\7g\2\2\u00fa&\3\2\2\2\u00fb\u00fc\7p\2\2\u00fc\u00fd")
        buf.write("\7k\2\2\u00fd\u00fe\7n\2\2\u00fe(\3\2\2\2\u00ff\u0100")
        buf.write("\7v\2\2\u0100\u0101\7t\2\2\u0101\u0102\7w\2\2\u0102\u0103")
        buf.write("\7g\2\2\u0103*\3\2\2\2\u0104\u0105\7h\2\2\u0105\u0106")
        buf.write("\7c\2\2\u0106\u0107\7n\2\2\u0107\u0108\7u\2\2\u0108\u0109")
        buf.write("\7g\2\2\u0109,\3\2\2\2\u010a\u010b\7-\2\2\u010b.\3\2\2")
        buf.write("\2\u010c\u010d\7/\2\2\u010d\60\3\2\2\2\u010e\u010f\7,")
        buf.write("\2\2\u010f\62\3\2\2\2\u0110\u0111\7\61\2\2\u0111\64\3")
        buf.write("\2\2\2\u0112\u0113\7\'\2\2\u0113\66\3\2\2\2\u0114\u0115")
        buf.write("\7?\2\2\u0115\u0116\7?\2\2\u01168\3\2\2\2\u0117\u0118")
        buf.write("\7#\2\2\u0118\u0119\7?\2\2\u0119:\3\2\2\2\u011a\u011b")
        buf.write("\7>\2\2\u011b<\3\2\2\2\u011c\u011d\7>\2\2\u011d\u011e")
        buf.write("\7?\2\2\u011e>\3\2\2\2\u011f\u0120\7@\2\2\u0120@\3\2\2")
        buf.write("\2\u0121\u0122\7@\2\2\u0122\u0123\7?\2\2\u0123B\3\2\2")
        buf.write("\2\u0124\u0125\7(\2\2\u0125\u0126\7(\2\2\u0126D\3\2\2")
        buf.write("\2\u0127\u0128\7~\2\2\u0128\u0129\7~\2\2\u0129F\3\2\2")
        buf.write("\2\u012a\u012b\7#\2\2\u012bH\3\2\2\2\u012c\u012d\7?\2")
        buf.write("\2\u012dJ\3\2\2\2\u012e\u012f\7-\2\2\u012f\u0130\7?\2")
        buf.write("\2\u0130L\3\2\2\2\u0131\u0132\7/\2\2\u0132\u0133\7?\2")
        buf.write("\2\u0133N\3\2\2\2\u0134\u0135\7,\2\2\u0135\u0136\7?\2")
        buf.write("\2\u0136P\3\2\2\2\u0137\u0138\7\61\2\2\u0138\u0139\7?")
        buf.write("\2\2\u0139R\3\2\2\2\u013a\u013b\7\'\2\2\u013b\u013c\7")
        buf.write("?\2\2\u013cT\3\2\2\2\u013d\u013e\7<\2\2\u013e\u013f\7")
        buf.write("?\2\2\u013fV\3\2\2\2\u0140\u0141\7\60\2\2\u0141X\3\2\2")
        buf.write("\2\u0142\u0143\7*\2\2\u0143Z\3\2\2\2\u0144\u0145\7+\2")
        buf.write("\2\u0145\\\3\2\2\2\u0146\u0147\7}\2\2\u0147^\3\2\2\2\u0148")
        buf.write("\u0149\7\177\2\2\u0149`\3\2\2\2\u014a\u014b\7]\2\2\u014b")
        buf.write("b\3\2\2\2\u014c\u014d\7_\2\2\u014dd\3\2\2\2\u014e\u014f")
        buf.write("\7=\2\2\u014ff\3\2\2\2\u0150\u0151\7<\2\2\u0151h\3\2\2")
        buf.write("\2\u0152\u0153\7.\2\2\u0153j\3\2\2\2\u0154\u0158\t\2\2")
        buf.write("\2\u0155\u0157\t\3\2\2\u0156\u0155\3\2\2\2\u0157\u015a")
        buf.write("\3\2\2\2\u0158\u0156\3\2\2\2\u0158\u0159\3\2\2\2\u0159")
        buf.write("l\3\2\2\2\u015a\u0158\3\2\2\2\u015b\u0164\7\62\2\2\u015c")
        buf.write("\u0160\t\4\2\2\u015d\u015f\t\5\2\2\u015e\u015d\3\2\2\2")
        buf.write("\u015f\u0162\3\2\2\2\u0160\u015e\3\2\2\2\u0160\u0161\3")
        buf.write("\2\2\2\u0161\u0164\3\2\2\2\u0162\u0160\3\2\2\2\u0163\u015b")
        buf.write("\3\2\2\2\u0163\u015c\3\2\2\2\u0164n\3\2\2\2\u0165\u0166")
        buf.write("\7\62\2\2\u0166\u0168\t\6\2\2\u0167\u0169\t\7\2\2\u0168")
        buf.write("\u0167\3\2\2\2\u0169\u016a\3\2\2\2\u016a\u0168\3\2\2\2")
        buf.write("\u016a\u016b\3\2\2\2\u016bp\3\2\2\2\u016c\u016d\7\62\2")
        buf.write("\2\u016d\u016f\t\b\2\2\u016e\u0170\t\t\2\2\u016f\u016e")
        buf.write("\3\2\2\2\u0170\u0171\3\2\2\2\u0171\u016f\3\2\2\2\u0171")
        buf.write("\u0172\3\2\2\2\u0172r\3\2\2\2\u0173\u0174\7\62\2\2\u0174")
        buf.write("\u0176\t\n\2\2\u0175\u0177\t\13\2\2\u0176\u0175\3\2\2")
        buf.write("\2\u0177\u0178\3\2\2\2\u0178\u0176\3\2\2\2\u0178\u0179")
        buf.write("\3\2\2\2\u0179t\3\2\2\2\u017a\u017b\5w<\2\u017b\u017d")
        buf.write("\7\60\2\2\u017c\u017e\5w<\2\u017d\u017c\3\2\2\2\u017d")
        buf.write("\u017e\3\2\2\2\u017e\u0180\3\2\2\2\u017f\u0181\5y=\2\u0180")
        buf.write("\u017f\3\2\2\2\u0180\u0181\3\2\2\2\u0181\u018b\3\2\2\2")
        buf.write("\u0182\u0183\7\62\2\2\u0183\u0185\7\60\2\2\u0184\u0186")
        buf.write("\5w<\2\u0185\u0184\3\2\2\2\u0185\u0186\3\2\2\2\u0186\u0188")
        buf.write("\3\2\2\2\u0187\u0189\5y=\2\u0188\u0187\3\2\2\2\u0188\u0189")
        buf.write("\3\2\2\2\u0189\u018b\3\2\2\2\u018a\u017a\3\2\2\2\u018a")
        buf.write("\u0182\3\2\2\2\u018bv\3\2\2\2\u018c\u018e\t\5\2\2\u018d")
        buf.write("\u018c\3\2\2\2\u018e\u018f\3\2\2\2\u018f\u018d\3\2\2\2")
        buf.write("\u018f\u0190\3\2\2\2\u0190x\3\2\2\2\u0191\u0193\t\f\2")
        buf.write("\2\u0192\u0194\t\r\2\2\u0193\u0192\3\2\2\2\u0193\u0194")
        buf.write("\3\2\2\2\u0194\u0195\3\2\2\2\u0195\u0196\5w<\2\u0196z")
        buf.write("\3\2\2\2\u0197\u0198\7^\2\2\u0198\u0199\t\16\2\2\u0199")
        buf.write("|\3\2\2\2\u019a\u019b\7^\2\2\u019b\u019c\t\16\2\2\u019c")
        buf.write("~\3\2\2\2\u019d\u019e\7^\2\2\u019e\u019f\n\16\2\2\u019f")
        buf.write("\u0080\3\2\2\2\u01a0\u01a5\7$\2\2\u01a1\u01a4\n\17\2\2")
        buf.write("\u01a2\u01a4\5{>\2\u01a3\u01a1\3\2\2\2\u01a3\u01a2\3\2")
        buf.write("\2\2\u01a4\u01a7\3\2\2\2\u01a5\u01a3\3\2\2\2\u01a5\u01a6")
        buf.write("\3\2\2\2\u01a6\u01a8\3\2\2\2\u01a7\u01a5\3\2\2\2\u01a8")
        buf.write("\u01a9\7^\2\2\u01a9\u01ad\n\20\2\2\u01aa\u01ac\13\2\2")
        buf.write("\2\u01ab\u01aa\3\2\2\2\u01ac\u01af\3\2\2\2\u01ad\u01ae")
        buf.write("\3\2\2\2\u01ad\u01ab\3\2\2\2\u01ae\u01b0\3\2\2\2\u01af")
        buf.write("\u01ad\3\2\2\2\u01b0\u01b1\7$\2\2\u01b1\u01b2\bA\2\2\u01b2")
        buf.write("\u0082\3\2\2\2\u01b3\u01b8\7$\2\2\u01b4\u01b7\n\17\2\2")
        buf.write("\u01b5\u01b7\5{>\2\u01b6\u01b4\3\2\2\2\u01b6\u01b5\3\2")
        buf.write("\2\2\u01b7\u01ba\3\2\2\2\u01b8\u01b6\3\2\2\2\u01b8\u01b9")
        buf.write("\3\2\2\2\u01b9\u01bb\3\2\2\2\u01ba\u01b8\3\2\2\2\u01bb")
        buf.write("\u01bc\7$\2\2\u01bc\u0084\3\2\2\2\u01bd\u01bf\7\17\2\2")
        buf.write("\u01be\u01bd\3\2\2\2\u01be\u01bf\3\2\2\2\u01bf\u01c0\3")
        buf.write("\2\2\2\u01c0\u01c1\7\f\2\2\u01c1\u01c2\bC\3\2\u01c2\u0086")
        buf.write("\3\2\2\2\u01c3\u01c5\t\21\2\2\u01c4\u01c3\3\2\2\2\u01c5")
        buf.write("\u01c6\3\2\2\2\u01c6\u01c4\3\2\2\2\u01c6\u01c7\3\2\2\2")
        buf.write("\u01c7\u01c8\3\2\2\2\u01c8\u01c9\bD\4\2\u01c9\u0088\3")
        buf.write("\2\2\2\u01ca\u01cb\7\61\2\2\u01cb\u01cc\7,\2\2\u01cc\u01d1")
        buf.write("\3\2\2\2\u01cd\u01d0\5\u0089E\2\u01ce\u01d0\13\2\2\2\u01cf")
        buf.write("\u01cd\3\2\2\2\u01cf\u01ce\3\2\2\2\u01d0\u01d3\3\2\2\2")
        buf.write("\u01d1\u01d2\3\2\2\2\u01d1\u01cf\3\2\2\2\u01d2\u01d4\3")
        buf.write("\2\2\2\u01d3\u01d1\3\2\2\2\u01d4\u01d5\7,\2\2\u01d5\u01d6")
        buf.write("\7\61\2\2\u01d6\u01d7\3\2\2\2\u01d7\u01d8\bE\4\2\u01d8")
        buf.write("\u008a\3\2\2\2\u01d9\u01da\7\61\2\2\u01da\u01db\7\61\2")
        buf.write("\2\u01db\u01df\3\2\2\2\u01dc\u01de\n\22\2\2\u01dd\u01dc")
        buf.write("\3\2\2\2\u01de\u01e1\3\2\2\2\u01df\u01dd\3\2\2\2\u01df")
        buf.write("\u01e0\3\2\2\2\u01e0\u01e2\3\2\2\2\u01e1\u01df\3\2\2\2")
        buf.write("\u01e2\u01e3\bF\4\2\u01e3\u008c\3\2\2\2\u01e4\u01e9\7")
        buf.write("$\2\2\u01e5\u01e8\n\23\2\2\u01e6\u01e8\5{>\2\u01e7\u01e5")
        buf.write("\3\2\2\2\u01e7\u01e6\3\2\2\2\u01e8\u01eb\3\2\2\2\u01e9")
        buf.write("\u01e7\3\2\2\2\u01e9\u01ea\3\2\2\2\u01ea\u01f1\3\2\2\2")
        buf.write("\u01eb\u01e9\3\2\2\2\u01ec\u01ee\7\17\2\2\u01ed\u01ec")
        buf.write("\3\2\2\2\u01ed\u01ee\3\2\2\2\u01ee\u01ef\3\2\2\2\u01ef")
        buf.write("\u01f2\7\f\2\2\u01f0\u01f2\7\2\2\3\u01f1\u01ed\3\2\2\2")
        buf.write("\u01f1\u01f0\3\2\2\2\u01f2\u01f3\3\2\2\2\u01f3\u01f4\b")
        buf.write("G\5\2\u01f4\u008e\3\2\2\2\u01f5\u01f6\13\2\2\2\u01f6\u01f7")
        buf.write("\bH\6\2\u01f7\u0090\3\2\2\2\36\2\u0158\u0160\u0163\u016a")
        buf.write("\u0171\u0178\u017d\u0180\u0185\u0188\u018a\u018f\u0193")
        buf.write("\u01a3\u01a5\u01ad\u01b6\u01b8\u01be\u01c6\u01cf\u01d1")
        buf.write("\u01df\u01e7\u01e9\u01ed\u01f1\7\3A\2\3C\3\b\2\2\3G\4")
        buf.write("\3H\5")
        return buf.getvalue()


class MiniGoLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    IF = 2
    ELSE = 3
    FOR = 4
    RETURN = 5
    FUNC = 6
    TYPE = 7
    STRUCT = 8
    INTERFACE = 9
    STRING = 10
    INT = 11
    FLOAT = 12
    BOOLEAN = 13
    CONST = 14
    VAR = 15
    CONTINUE = 16
    BREAK = 17
    RANGE = 18
    NIL = 19
    TRUE = 20
    FALSE = 21
    ADD = 22
    SUB = 23
    MUL = 24
    DIV = 25
    MOD = 26
    EQUAL = 27
    NOTEQUAL = 28
    LESS = 29
    LESSEQUAL = 30
    GREATER = 31
    GREATEREQUAL = 32
    AND = 33
    OR = 34
    NOT = 35
    ASSIGN = 36
    ADD_ASSIGN = 37
    SUB_ASSIGN = 38
    MUL_ASSIGN = 39
    DIV_ASSIGN = 40
    MOD_ASSIGN = 41
    COLON_ASSIGN = 42
    DOT = 43
    LPAREN = 44
    RPAREN = 45
    LBRACE = 46
    RBRACE = 47
    LBRACK = 48
    RBRACK = 49
    SEMI = 50
    COLON = 51
    COMMA = 52
    ID = 53
    INT_LIT = 54
    BIN_LIT = 55
    OCT_LIT = 56
    HEX_LIT = 57
    REAL = 58
    ILLEGAL_ESCAPE = 59
    STRING_LIT = 60
    NEWLINE = 61
    WS = 62
    MULTI_COMMENT = 63
    LINE_COMMENT = 64
    UNCLOSE_STRING = 65
    ERROR_CHAR = 66

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'str'", "'if'", "'else'", "'for'", "'return'", "'func'", "'type'", 
            "'struct'", "'interface'", "'string'", "'int'", "'float'", "'boolean'", 
            "'const'", "'var'", "'continue'", "'break'", "'range'", "'nil'", 
            "'true'", "'false'", "'+'", "'-'", "'*'", "'/'", "'%'", "'=='", 
            "'!='", "'<'", "'<='", "'>'", "'>='", "'&&'", "'||'", "'!'", 
            "'='", "'+='", "'-='", "'*='", "'/='", "'%='", "':='", "'.'", 
            "'('", "')'", "'{'", "'}'", "'['", "']'", "';'", "':'", "','" ]

    symbolicNames = [ "<INVALID>",
            "IF", "ELSE", "FOR", "RETURN", "FUNC", "TYPE", "STRUCT", "INTERFACE", 
            "STRING", "INT", "FLOAT", "BOOLEAN", "CONST", "VAR", "CONTINUE", 
            "BREAK", "RANGE", "NIL", "TRUE", "FALSE", "ADD", "SUB", "MUL", 
            "DIV", "MOD", "EQUAL", "NOTEQUAL", "LESS", "LESSEQUAL", "GREATER", 
            "GREATEREQUAL", "AND", "OR", "NOT", "ASSIGN", "ADD_ASSIGN", 
            "SUB_ASSIGN", "MUL_ASSIGN", "DIV_ASSIGN", "MOD_ASSIGN", "COLON_ASSIGN", 
            "DOT", "LPAREN", "RPAREN", "LBRACE", "RBRACE", "LBRACK", "RBRACK", 
            "SEMI", "COLON", "COMMA", "ID", "INT_LIT", "BIN_LIT", "OCT_LIT", 
            "HEX_LIT", "REAL", "ILLEGAL_ESCAPE", "STRING_LIT", "NEWLINE", 
            "WS", "MULTI_COMMENT", "LINE_COMMENT", "UNCLOSE_STRING", "ERROR_CHAR" ]

    ruleNames = [ "T__0", "IF", "ELSE", "FOR", "RETURN", "FUNC", "TYPE", 
                  "STRUCT", "INTERFACE", "STRING", "INT", "FLOAT", "BOOLEAN", 
                  "CONST", "VAR", "CONTINUE", "BREAK", "RANGE", "NIL", "TRUE", 
                  "FALSE", "ADD", "SUB", "MUL", "DIV", "MOD", "EQUAL", "NOTEQUAL", 
                  "LESS", "LESSEQUAL", "GREATER", "GREATEREQUAL", "AND", 
                  "OR", "NOT", "ASSIGN", "ADD_ASSIGN", "SUB_ASSIGN", "MUL_ASSIGN", 
                  "DIV_ASSIGN", "MOD_ASSIGN", "COLON_ASSIGN", "DOT", "LPAREN", 
                  "RPAREN", "LBRACE", "RBRACE", "LBRACK", "RBRACK", "SEMI", 
                  "COLON", "COMMA", "ID", "INT_LIT", "BIN_LIT", "OCT_LIT", 
                  "HEX_LIT", "REAL", "DIGITS", "EXPONENT", "VALID_ESC", 
                  "ESCAPE", "IL_ESCAPE", "ILLEGAL_ESCAPE", "STRING_LIT", 
                  "NEWLINE", "WS", "MULTI_COMMENT", "LINE_COMMENT", "UNCLOSE_STRING", 
                  "ERROR_CHAR" ]

    grammarFileName = "MiniGo.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None



    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None
        self.preType = None

    def emit(self):
        tk = self.type
        self.preType = tk;
        if tk == self.ILLEGAL_ESCAPE:
            escaped_text = self.text[1:-1]  
            raise IllegalEscape(escaped_text)
        elif tk == self.ERROR_CHAR:
            result = super().emit();
            raise ErrorToken(result.text); 
        else:
            return super().emit()


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[63] = self.ILLEGAL_ESCAPE_action 
            actions[65] = self.NEWLINE_action 
            actions[69] = self.UNCLOSE_STRING_action 
            actions[70] = self.ERROR_CHAR_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:

                  raise IllegalEscape("\"" + self.text[1:-1])  
                
     

    def NEWLINE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:

                approved = [self.RETURN, 
                            self.TYPE, self.STRUCT, self.INTERFACE, self.STRING, self.HEX_LIT, 
                            self.INT, self.FLOAT, self.BOOLEAN, self.CONST, self.VAR,
                            self.CONTINUE, self.BREAK, self.RANGE, self.NIL, self.TRUE,
                            self.COLON_ASSIGN, self.DOT,
                            self.LPAREN, self.RPAREN, self.LBRACE, self.RBRACE,
                            self.LBRACK, self.RBRACK, self.COMMA, self.SEMI,
                            self.ID, self.INT_LIT, self.REAL, self.STRING_LIT]
                if self.preType in approved:
                    self.text = ";"
                else:
                    self.skip() 
                
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:

                  if self.text[-1] == '\n':
                     raise UncloseString("\"" + self.text[1:-1])
                  else:
                     raise UncloseString("\"" + self.text[1:])
                
     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:
            raise ErrorToken(self.text)
     


