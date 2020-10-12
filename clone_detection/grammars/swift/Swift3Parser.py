# Generated from ../clone_detection/grammars/swift/Swift3.g4 by ANTLR 4.7.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys

from clone_detection.grammars.grammars_registry import PARSERS


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\u00ad")
        buf.write("\u0ad0\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:\4;\t")
        buf.write(";\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\tC\4D\t")
        buf.write("D\4E\tE\4F\tF\4G\tG\4H\tH\4I\tI\4J\tJ\4K\tK\4L\tL\4M\t")
        buf.write("M\4N\tN\4O\tO\4P\tP\4Q\tQ\4R\tR\4S\tS\4T\tT\4U\tU\4V\t")
        buf.write("V\4W\tW\4X\tX\4Y\tY\4Z\tZ\4[\t[\4\\\t\\\4]\t]\4^\t^\4")
        buf.write("_\t_\4`\t`\4a\ta\4b\tb\4c\tc\4d\td\4e\te\4f\tf\4g\tg\4")
        buf.write("h\th\4i\ti\4j\tj\4k\tk\4l\tl\4m\tm\4n\tn\4o\to\4p\tp\4")
        buf.write("q\tq\4r\tr\4s\ts\4t\tt\4u\tu\4v\tv\4w\tw\4x\tx\4y\ty\4")
        buf.write("z\tz\4{\t{\4|\t|\4}\t}\4~\t~\4\177\t\177\4\u0080\t\u0080")
        buf.write("\4\u0081\t\u0081\4\u0082\t\u0082\4\u0083\t\u0083\4\u0084")
        buf.write("\t\u0084\4\u0085\t\u0085\4\u0086\t\u0086\4\u0087\t\u0087")
        buf.write("\4\u0088\t\u0088\4\u0089\t\u0089\4\u008a\t\u008a\4\u008b")
        buf.write("\t\u008b\4\u008c\t\u008c\4\u008d\t\u008d\4\u008e\t\u008e")
        buf.write("\4\u008f\t\u008f\4\u0090\t\u0090\4\u0091\t\u0091\4\u0092")
        buf.write("\t\u0092\4\u0093\t\u0093\4\u0094\t\u0094\4\u0095\t\u0095")
        buf.write("\4\u0096\t\u0096\4\u0097\t\u0097\4\u0098\t\u0098\4\u0099")
        buf.write("\t\u0099\4\u009a\t\u009a\4\u009b\t\u009b\4\u009c\t\u009c")
        buf.write("\4\u009d\t\u009d\4\u009e\t\u009e\4\u009f\t\u009f\4\u00a0")
        buf.write("\t\u00a0\4\u00a1\t\u00a1\4\u00a2\t\u00a2\4\u00a3\t\u00a3")
        buf.write("\4\u00a4\t\u00a4\4\u00a5\t\u00a5\4\u00a6\t\u00a6\4\u00a7")
        buf.write("\t\u00a7\4\u00a8\t\u00a8\4\u00a9\t\u00a9\4\u00aa\t\u00aa")
        buf.write("\4\u00ab\t\u00ab\4\u00ac\t\u00ac\4\u00ad\t\u00ad\4\u00ae")
        buf.write("\t\u00ae\4\u00af\t\u00af\4\u00b0\t\u00b0\4\u00b1\t\u00b1")
        buf.write("\4\u00b2\t\u00b2\4\u00b3\t\u00b3\4\u00b4\t\u00b4\4\u00b5")
        buf.write("\t\u00b5\4\u00b6\t\u00b6\4\u00b7\t\u00b7\4\u00b8\t\u00b8")
        buf.write("\4\u00b9\t\u00b9\4\u00ba\t\u00ba\4\u00bb\t\u00bb\4\u00bc")
        buf.write("\t\u00bc\4\u00bd\t\u00bd\4\u00be\t\u00be\4\u00bf\t\u00bf")
        buf.write("\4\u00c0\t\u00c0\4\u00c1\t\u00c1\4\u00c2\t\u00c2\4\u00c3")
        buf.write("\t\u00c3\4\u00c4\t\u00c4\4\u00c5\t\u00c5\4\u00c6\t\u00c6")
        buf.write("\4\u00c7\t\u00c7\4\u00c8\t\u00c8\4\u00c9\t\u00c9\4\u00ca")
        buf.write("\t\u00ca\4\u00cb\t\u00cb\4\u00cc\t\u00cc\4\u00cd\t\u00cd")
        buf.write("\4\u00ce\t\u00ce\4\u00cf\t\u00cf\4\u00d0\t\u00d0\4\u00d1")
        buf.write("\t\u00d1\4\u00d2\t\u00d2\4\u00d3\t\u00d3\4\u00d4\t\u00d4")
        buf.write("\4\u00d5\t\u00d5\4\u00d6\t\u00d6\4\u00d7\t\u00d7\4\u00d8")
        buf.write("\t\u00d8\4\u00d9\t\u00d9\4\u00da\t\u00da\4\u00db\t\u00db")
        buf.write("\4\u00dc\t\u00dc\4\u00dd\t\u00dd\4\u00de\t\u00de\4\u00df")
        buf.write("\t\u00df\4\u00e0\t\u00e0\4\u00e1\t\u00e1\4\u00e2\t\u00e2")
        buf.write("\4\u00e3\t\u00e3\4\u00e4\t\u00e4\4\u00e5\t\u00e5\4\u00e6")
        buf.write("\t\u00e6\4\u00e7\t\u00e7\4\u00e8\t\u00e8\4\u00e9\t\u00e9")
        buf.write("\4\u00ea\t\u00ea\4\u00eb\t\u00eb\4\u00ec\t\u00ec\4\u00ed")
        buf.write("\t\u00ed\4\u00ee\t\u00ee\4\u00ef\t\u00ef\4\u00f0\t\u00f0")
        buf.write("\4\u00f1\t\u00f1\4\u00f2\t\u00f2\4\u00f3\t\u00f3\4\u00f4")
        buf.write("\t\u00f4\4\u00f5\t\u00f5\4\u00f6\t\u00f6\4\u00f7\t\u00f7")
        buf.write("\4\u00f8\t\u00f8\4\u00f9\t\u00f9\4\u00fa\t\u00fa\4\u00fb")
        buf.write("\t\u00fb\4\u00fc\t\u00fc\4\u00fd\t\u00fd\4\u00fe\t\u00fe")
        buf.write("\4\u00ff\t\u00ff\4\u0100\t\u0100\4\u0101\t\u0101\4\u0102")
        buf.write("\t\u0102\4\u0103\t\u0103\4\u0104\t\u0104\4\u0105\t\u0105")
        buf.write("\4\u0106\t\u0106\4\u0107\t\u0107\4\u0108\t\u0108\4\u0109")
        buf.write("\t\u0109\4\u010a\t\u010a\4\u010b\t\u010b\4\u010c\t\u010c")
        buf.write("\4\u010d\t\u010d\4\u010e\t\u010e\4\u010f\t\u010f\4\u0110")
        buf.write("\t\u0110\4\u0111\t\u0111\4\u0112\t\u0112\4\u0113\t\u0113")
        buf.write("\4\u0114\t\u0114\4\u0115\t\u0115\4\u0116\t\u0116\4\u0117")
        buf.write("\t\u0117\4\u0118\t\u0118\4\u0119\t\u0119\4\u011a\t\u011a")
        buf.write("\4\u011b\t\u011b\4\u011c\t\u011c\4\u011d\t\u011d\4\u011e")
        buf.write("\t\u011e\3\2\5\2\u023e\n\2\3\2\3\2\3\3\3\3\5\3\u0244\n")
        buf.write("\3\3\3\3\3\5\3\u0248\n\3\3\3\3\3\5\3\u024c\n\3\3\3\3\3")
        buf.write("\5\3\u0250\n\3\3\3\3\3\5\3\u0254\n\3\3\3\3\3\5\3\u0258")
        buf.write("\n\3\3\3\3\3\5\3\u025c\n\3\3\3\3\3\5\3\u0260\n\3\3\3\3")
        buf.write("\3\5\3\u0264\n\3\5\3\u0266\n\3\3\4\3\4\3\5\3\5\3\5\3\5")
        buf.write("\5\5\u026e\n\5\3\6\3\6\3\6\3\6\5\6\u0274\n\6\3\7\3\7\5")
        buf.write("\7\u0278\n\7\3\7\3\7\5\7\u027c\n\7\3\7\3\7\5\7\u0280\n")
        buf.write("\7\3\7\3\7\3\7\3\7\5\7\u0286\n\7\3\7\3\7\5\7\u028a\n\7")
        buf.write("\3\7\3\7\5\7\u028e\n\7\3\7\3\7\5\7\u0292\n\7\3\b\3\b\5")
        buf.write("\b\u0296\n\b\3\t\3\t\5\t\u029a\n\t\3\t\3\t\3\t\3\t\5\t")
        buf.write("\u02a0\n\t\3\t\3\t\3\n\3\n\3\n\3\n\3\13\3\13\3\13\7\13")
        buf.write("\u02ab\n\13\f\13\16\13\u02ae\13\13\3\f\3\f\3\f\3\f\5\f")
        buf.write("\u02b4\n\f\3\r\3\r\3\r\3\r\5\r\u02ba\n\r\3\16\3\16\3\16")
        buf.write("\3\16\3\16\3\16\3\16\3\16\5\16\u02c4\n\16\3\17\3\17\3")
        buf.write("\17\3\17\3\17\3\20\3\20\3\20\5\20\u02ce\n\20\3\21\3\21")
        buf.write("\3\21\3\21\5\21\u02d4\n\21\3\22\3\22\3\22\3\22\5\22\u02da")
        buf.write("\n\22\3\23\3\23\3\23\3\23\3\23\3\24\3\24\3\24\3\24\5\24")
        buf.write("\u02e5\n\24\3\24\3\24\3\25\3\25\5\25\u02eb\n\25\3\26\3")
        buf.write("\26\3\26\3\26\3\26\3\26\5\26\u02f3\n\26\3\27\3\27\3\27")
        buf.write("\3\27\3\30\3\30\5\30\u02fb\n\30\3\30\3\30\5\30\u02ff\n")
        buf.write("\30\3\30\3\30\3\30\5\30\u0304\n\30\3\31\3\31\3\31\3\32")
        buf.write("\3\32\3\32\3\33\3\33\3\34\3\34\3\34\3\34\3\34\3\34\3\34")
        buf.write("\3\34\3\34\3\34\3\34\3\34\5\34\u031a\n\34\3\35\3\35\3")
        buf.write("\35\3\36\3\36\3\37\3\37\3\37\3\37\3\37\5\37\u0326\n\37")
        buf.write("\3 \3 \5 \u032a\n \3!\3!\5!\u032e\n!\3\"\3\"\3#\3#\5#")
        buf.write("\u0334\n#\3$\3$\3$\3%\3%\3%\3&\3&\3&\5&\u033f\n&\3\'\3")
        buf.write("\'\5\'\u0343\n\'\3(\3(\5(\u0347\n(\3(\5(\u034a\n(\3(\3")
        buf.write("(\3)\3)\5)\u0350\n)\3*\3*\5*\u0354\n*\3*\5*\u0357\n*\3")
        buf.write("*\3*\3+\3+\3+\5+\u035e\n+\3,\6,\u0361\n,\r,\16,\u0362")
        buf.write("\3-\3-\3-\5-\u0368\n-\3.\3.\5.\u036c\n.\3/\3/\3\60\3\60")
        buf.write("\3\61\3\61\3\62\3\62\3\63\3\63\3\63\3\63\3\63\3\63\3\63")
        buf.write("\3\63\3\63\3\63\5\63\u0380\n\63\3\63\3\63\3\63\3\63\3")
        buf.write("\63\3\63\3\63\3\63\7\63\u038a\n\63\f\63\16\63\u038d\13")
        buf.write("\63\3\64\3\64\3\64\3\64\3\64\3\64\3\64\3\64\3\64\3\64")
        buf.write("\3\64\3\64\3\64\3\64\3\64\3\64\5\64\u039f\n\64\3\65\3")
        buf.write("\65\3\65\3\65\3\66\3\66\3\67\3\67\38\38\38\38\38\38\3")
        buf.write("8\38\38\38\38\38\38\38\58\u03b7\n8\39\39\3:\3:\3;\3;\3")
        buf.write(";\3;\3;\3<\3<\3<\7<\u03c5\n<\f<\16<\u03c8\13<\3=\3=\3")
        buf.write(">\3>\3>\3>\3?\3?\3?\7?\u03d3\n?\f?\16?\u03d6\13?\3@\3")
        buf.write("@\3@\3@\3@\3@\3@\3@\3@\5@\u03e1\n@\3A\3A\3A\3B\3B\3B\7")
        buf.write("B\u03e9\nB\fB\16B\u03ec\13B\3C\3C\5C\u03f0\nC\3D\3D\3")
        buf.write("D\3D\3D\3D\3D\3D\5D\u03fa\nD\3E\3E\3E\3E\3F\3F\3F\3F\3")
        buf.write("G\3G\3G\7G\u0407\nG\fG\16G\u040a\13G\3H\3H\3I\3I\3I\3")
        buf.write("I\3I\3I\3I\3I\3I\3I\3I\3I\3I\3I\3I\3I\5I\u041e\nI\3J\6")
        buf.write("J\u0421\nJ\rJ\16J\u0422\3K\5K\u0426\nK\3L\3L\5L\u042a")
        buf.write("\nL\3L\3L\3M\5M\u042f\nM\3M\3M\5M\u0433\nM\3M\3M\3N\3")
        buf.write("N\3O\3O\3O\7O\u043c\nO\fO\16O\u043f\13O\3P\3P\5P\u0443")
        buf.write("\nP\3Q\5Q\u0446\nQ\3Q\5Q\u0449\nQ\3Q\3Q\3Q\3R\3R\3R\7")
        buf.write("R\u0451\nR\fR\16R\u0454\13R\3S\3S\5S\u0458\nS\3T\3T\3")
        buf.write("T\3U\3U\3U\3U\3U\3U\3U\3U\3U\3U\3U\3U\3U\3U\3U\3U\3U\3")
        buf.write("U\3U\5U\u0470\nU\3U\3U\3U\3U\3U\3U\3U\5U\u0479\nU\3U\3")
        buf.write("U\3U\3U\3U\5U\u0480\nU\3V\5V\u0483\nV\3V\5V\u0486\nV\3")
        buf.write("V\3V\3W\3W\3X\3X\3X\5X\u048f\nX\3X\3X\3X\3X\3X\3X\3X\5")
        buf.write("X\u0498\nX\3Y\5Y\u049b\nY\3Y\5Y\u049e\nY\3Y\3Y\3Y\3Z\5")
        buf.write("Z\u04a4\nZ\3Z\5Z\u04a7\nZ\3Z\3Z\5Z\u04ab\nZ\3Z\3Z\3[\3")
        buf.write("[\3[\3[\3\\\3\\\3\\\5\\\u04b6\n\\\3\\\3\\\3\\\3\\\3\\")
        buf.write("\3\\\3\\\5\\\u04bf\n\\\3]\5]\u04c2\n]\3]\5]\u04c5\n]\3")
        buf.write("]\3]\3^\5^\u04ca\n^\3^\5^\u04cd\n^\3^\3^\3_\3_\3_\5_\u04d4")
        buf.write("\n_\3_\3_\3_\3_\3_\3_\3_\5_\u04dd\n_\3`\5`\u04e0\n`\3")
        buf.write("`\3`\5`\u04e4\n`\3`\3`\3a\5a\u04e9\na\3a\3a\5a\u04ed\n")
        buf.write("a\3a\3a\3b\5b\u04f2\nb\3b\5b\u04f5\nb\3b\3b\3b\5b\u04fa")
        buf.write("\nb\3b\3b\3c\3c\3d\3d\3d\3e\3e\3e\5e\u0506\ne\3e\3e\5")
        buf.write("e\u050a\ne\3e\5e\u050d\ne\3f\5f\u0510\nf\3f\5f\u0513\n")
        buf.write("f\3f\3f\3g\3g\5g\u0519\ng\3h\3h\5h\u051d\nh\3h\5h\u0520")
        buf.write("\nh\3h\3h\3h\5h\u0525\nh\5h\u0527\nh\3i\3i\5i\u052b\n")
        buf.write("i\3i\3i\3j\3j\3k\3k\3k\3k\3k\3k\5k\u0537\nk\3l\3l\3l\7")
        buf.write("l\u053c\nl\fl\16l\u053f\13l\3m\5m\u0542\nm\3m\3m\3m\5")
        buf.write("m\u0547\nm\3m\5m\u054a\nm\3m\3m\3m\3m\5m\u0550\nm\3m\3")
        buf.write("m\3m\3m\5m\u0556\nm\3n\3n\3o\3o\3p\3p\3p\3q\5q\u0560\n")
        buf.write("q\3q\5q\u0563\nq\3q\3q\5q\u0567\nq\3q\5q\u056a\nq\3q\5")
        buf.write("q\u056d\nq\3r\5r\u0570\nr\3r\3r\3r\5r\u0575\nr\3r\5r\u0578")
        buf.write("\nr\3r\5r\u057b\nr\3r\3r\5r\u057f\nr\3r\3r\3s\3s\5s\u0585")
        buf.write("\ns\3t\3t\3t\5t\u058a\nt\3u\5u\u058d\nu\3u\5u\u0590\n")
        buf.write("u\3u\3u\3u\3v\3v\3v\3v\3v\5v\u059a\nv\3w\3w\5w\u059e\n")
        buf.write("w\3x\3x\3y\3y\3z\3z\3z\5z\u05a7\nz\3z\3z\5z\u05ab\nz\3")
        buf.write("z\3z\3z\3z\3{\3{\5{\u05b3\n{\3|\3|\3|\5|\u05b8\n|\3}\5")
        buf.write("}\u05bb\n}\3}\3}\3}\3~\3~\3~\3~\3~\5~\u05c5\n~\3\177\3")
        buf.write("\177\5\177\u05c9\n\177\3\u0080\3\u0080\3\u0080\3\u0081")
        buf.write("\3\u0081\3\u0081\5\u0081\u05d1\n\u0081\3\u0082\5\u0082")
        buf.write("\u05d4\n\u0082\3\u0082\5\u0082\u05d7\n\u0082\3\u0082\3")
        buf.write("\u0082\3\u0082\5\u0082\u05dc\n\u0082\3\u0082\5\u0082\u05df")
        buf.write("\n\u0082\3\u0082\5\u0082\u05e2\n\u0082\3\u0082\3\u0082")
        buf.write("\3\u0083\3\u0083\3\u0084\3\u0084\7\u0084\u05ea\n\u0084")
        buf.write("\f\u0084\16\u0084\u05ed\13\u0084\3\u0084\3\u0084\3\u0085")
        buf.write("\3\u0085\5\u0085\u05f3\n\u0085\3\u0086\5\u0086\u05f6\n")
        buf.write("\u0086\3\u0086\5\u0086\u05f9\n\u0086\3\u0086\5\u0086\u05fc")
        buf.write("\n\u0086\3\u0086\3\u0086\3\u0086\5\u0086\u0601\n\u0086")
        buf.write("\3\u0086\5\u0086\u0604\n\u0086\3\u0086\5\u0086\u0607\n")
        buf.write("\u0086\3\u0086\3\u0086\3\u0086\5\u0086\u060c\n\u0086\3")
        buf.write("\u0086\5\u0086\u060f\n\u0086\3\u0086\3\u0086\5\u0086\u0613")
        buf.write("\n\u0086\3\u0086\3\u0086\3\u0086\5\u0086\u0618\n\u0086")
        buf.write("\3\u0086\5\u0086\u061b\n\u0086\3\u0086\5\u0086\u061e\n")
        buf.write("\u0086\3\u0086\3\u0086\5\u0086\u0622\n\u0086\3\u0087\3")
        buf.write("\u0087\3\u0088\3\u0088\7\u0088\u0628\n\u0088\f\u0088\16")
        buf.write("\u0088\u062b\13\u0088\3\u0088\3\u0088\3\u0089\3\u0089")
        buf.write("\5\u0089\u0631\n\u0089\3\u008a\5\u008a\u0634\n\u008a\3")
        buf.write("\u008a\5\u008a\u0637\n\u008a\3\u008a\3\u008a\3\u008a\5")
        buf.write("\u008a\u063c\n\u008a\3\u008a\3\u008a\3\u008b\3\u008b\3")
        buf.write("\u008c\3\u008c\7\u008c\u0644\n\u008c\f\u008c\16\u008c")
        buf.write("\u0647\13\u008c\3\u008c\3\u008c\3\u008d\3\u008d\5\u008d")
        buf.write("\u064d\n\u008d\3\u008e\3\u008e\3\u008e\3\u008e\3\u008e")
        buf.write("\3\u008e\5\u008e\u0655\n\u008e\3\u008f\3\u008f\3\u008f")
        buf.write("\3\u008f\3\u008f\3\u0090\3\u0090\3\u0090\5\u0090\u065f")
        buf.write("\n\u0090\3\u0090\3\u0090\5\u0090\u0663\n\u0090\3\u0091")
        buf.write("\3\u0091\5\u0091\u0667\n\u0091\3\u0091\3\u0091\5\u0091")
        buf.write("\u066b\n\u0091\3\u0091\5\u0091\u066e\n\u0091\3\u0091\3")
        buf.write("\u0091\5\u0091\u0672\n\u0091\3\u0091\3\u0091\3\u0091\5")
        buf.write("\u0091\u0677\n\u0091\5\u0091\u0679\n\u0091\3\u0092\3\u0092")
        buf.write("\3\u0092\3\u0092\3\u0093\5\u0093\u0680\n\u0093\3\u0093")
        buf.write("\5\u0093\u0683\n\u0093\3\u0093\3\u0093\3\u0093\5\u0093")
        buf.write("\u0688\n\u0093\3\u0093\5\u0093\u068b\n\u0093\3\u0094\3")
        buf.write("\u0094\5\u0094\u068f\n\u0094\3\u0094\3\u0094\5\u0094\u0693")
        buf.write("\n\u0094\3\u0094\5\u0094\u0696\n\u0094\3\u0094\3\u0094")
        buf.write("\3\u0094\3\u0094\5\u0094\u069c\n\u0094\3\u0094\3\u0094")
        buf.write("\3\u0094\5\u0094\u06a1\n\u0094\3\u0094\3\u0094\5\u0094")
        buf.write("\u06a5\n\u0094\3\u0095\5\u0095\u06a8\n\u0095\3\u0095\5")
        buf.write("\u0095\u06ab\n\u0095\3\u0095\3\u0095\5\u0095\u06af\n\u0095")
        buf.write("\3\u0095\5\u0095\u06b2\n\u0095\3\u0095\3\u0095\3\u0095")
        buf.write("\5\u0095\u06b7\n\u0095\3\u0095\5\u0095\u06ba\n\u0095\3")
        buf.write("\u0095\3\u0095\5\u0095\u06be\n\u0095\3\u0096\3\u0096\3")
        buf.write("\u0097\5\u0097\u06c3\n\u0097\3\u0097\3\u0097\3\u0097\3")
        buf.write("\u0098\5\u0098\u06c9\n\u0098\3\u0098\5\u0098\u06cc\n\u0098")
        buf.write("\3\u0098\3\u0098\3\u0098\5\u0098\u06d1\n\u0098\3\u0098")
        buf.write("\3\u0098\3\u0098\5\u0098\u06d6\n\u0098\3\u0098\5\u0098")
        buf.write("\u06d9\n\u0098\3\u0098\3\u0098\3\u0098\3\u0098\3\u0098")
        buf.write("\5\u0098\u06e0\n\u0098\3\u0099\3\u0099\7\u0099\u06e4\n")
        buf.write("\u0099\f\u0099\16\u0099\u06e7\13\u0099\3\u0099\3\u0099")
        buf.write("\3\u009a\3\u009a\5\u009a\u06ed\n\u009a\3\u009b\3\u009b")
        buf.write("\3\u009b\3\u009b\3\u009b\3\u009b\3\u009b\3\u009b\3\u009b")
        buf.write("\3\u009b\3\u009b\3\u009b\5\u009b\u06fb\n\u009b\3\u009c")
        buf.write("\5\u009c\u06fe\n\u009c\3\u009c\5\u009c\u0701\n\u009c\3")
        buf.write("\u009c\3\u009c\3\u009c\3\u009d\3\u009d\5\u009d\u0708\n")
        buf.write("\u009d\3\u009d\3\u009d\3\u009e\3\u009e\3\u009e\5\u009e")
        buf.write("\u070f\n\u009e\3\u009f\3\u009f\3\u009f\3\u009f\3\u00a0")
        buf.write("\3\u00a0\3\u00a0\3\u00a0\3\u00a1\3\u00a1\3\u00a1\3\u00a1")
        buf.write("\5\u00a1\u071d\n\u00a1\3\u00a2\3\u00a2\3\u00a2\3\u00a3")
        buf.write("\3\u00a3\3\u00a3\3\u00a3\7\u00a3\u0726\n\u00a3\f\u00a3")
        buf.write("\16\u00a3\u0729\13\u00a3\3\u00a3\3\u00a3\3\u00a4\3\u00a4")
        buf.write("\3\u00a4\5\u00a4\u0730\n\u00a4\3\u00a5\3\u00a5\3\u00a5")
        buf.write("\3\u00a5\3\u00a5\3\u00a5\5\u00a5\u0738\n\u00a5\3\u00a6")
        buf.write("\3\u00a6\3\u00a6\3\u00a6\3\u00a7\3\u00a7\3\u00a7\3\u00a7")
        buf.write("\3\u00a8\3\u00a8\3\u00a9\3\u00a9\3\u00a9\7\u00a9\u0747")
        buf.write("\n\u00a9\f\u00a9\16\u00a9\u074a\13\u00a9\3\u00aa\3\u00aa")
        buf.write("\3\u00ab\3\u00ab\3\u00ab\3\u00ab\3\u00ab\3\u00ab\3\u00ab")
        buf.write("\3\u00ab\3\u00ab\3\u00ab\3\u00ab\3\u00ab\3\u00ab\3\u00ab")
        buf.write("\3\u00ab\3\u00ab\3\u00ab\3\u00ab\3\u00ab\3\u00ab\3\u00ab")
        buf.write("\3\u00ab\3\u00ab\3\u00ab\5\u00ab\u0766\n\u00ab\3\u00ac")
        buf.write("\6\u00ac\u0769\n\u00ac\r\u00ac\16\u00ac\u076a\3\u00ad")
        buf.write("\3\u00ad\3\u00ad\3\u00ad\3\u00ad\3\u00ad\3\u00ad\3\u00ad")
        buf.write("\3\u00ad\3\u00ad\3\u00ad\3\u00ad\3\u00ad\3\u00ad\3\u00ad")
        buf.write("\3\u00ad\3\u00ad\3\u00ad\3\u00ad\3\u00ad\3\u00ad\3\u00ad")
        buf.write("\3\u00ad\3\u00ad\3\u00ad\5\u00ad\u0786\n\u00ad\3\u00ae")
        buf.write("\3\u00ae\3\u00af\3\u00af\3\u00af\5\u00af\u078d\n\u00af")
        buf.write("\3\u00af\3\u00af\5\u00af\u0791\n\u00af\3\u00af\3\u00af")
        buf.write("\3\u00af\5\u00af\u0796\n\u00af\3\u00af\3\u00af\3\u00af")
        buf.write("\3\u00af\3\u00af\5\u00af\u079d\n\u00af\3\u00af\3\u00af")
        buf.write("\3\u00af\7\u00af\u07a2\n\u00af\f\u00af\16\u00af\u07a5")
        buf.write("\13\u00af\3\u00b0\3\u00b0\3\u00b1\3\u00b1\3\u00b2\3\u00b2")
        buf.write("\3\u00b2\3\u00b2\5\u00b2\u07af\n\u00b2\3\u00b3\3\u00b3")
        buf.write("\5\u00b3\u07b3\n\u00b3\3\u00b3\3\u00b3\3\u00b4\3\u00b4")
        buf.write("\3\u00b4\7\u00b4\u07ba\n\u00b4\f\u00b4\16\u00b4\u07bd")
        buf.write("\13\u00b4\3\u00b5\3\u00b5\3\u00b6\5\u00b6\u07c2\n\u00b6")
        buf.write("\3\u00b6\3\u00b6\3\u00b6\5\u00b6\u07c7\n\u00b6\3\u00b7")
        buf.write("\3\u00b7\3\u00b7\3\u00b8\3\u00b8\3\u00b9\3\u00b9\3\u00b9")
        buf.write("\5\u00b9\u07d1\n\u00b9\3\u00ba\3\u00ba\3\u00bb\3\u00bb")
        buf.write("\3\u00bb\3\u00bb\3\u00bc\6\u00bc\u07da\n\u00bc\r\u00bc")
        buf.write("\16\u00bc\u07db\3\u00bd\7\u00bd\u07df\n\u00bd\f\u00bd")
        buf.write("\16\u00bd\u07e2\13\u00bd\3\u00be\3\u00be\3\u00be\3\u00be")
        buf.write("\3\u00be\3\u00be\3\u00be\3\u00be\3\u00be\3\u00be\3\u00be")
        buf.write("\3\u00be\3\u00be\3\u00be\3\u00be\3\u00be\3\u00be\5\u00be")
        buf.write("\u07f5\n\u00be\3\u00bf\3\u00bf\3\u00bf\3\u00bf\3\u00bf")
        buf.write("\3\u00bf\5\u00bf\u07fd\n\u00bf\3\u00c0\5\u00c0\u0800\n")
        buf.write("\u00c0\3\u00c0\3\u00c0\5\u00c0\u0804\n\u00c0\3\u00c1\3")
        buf.write("\u00c1\3\u00c1\7\u00c1\u0809\n\u00c1\f\u00c1\16\u00c1")
        buf.write("\u080c\13\u00c1\3\u00c2\3\u00c2\3\u00c2\3\u00c2\3\u00c2")
        buf.write("\5\u00c2\u0813\n\u00c2\3\u00c3\3\u00c3\3\u00c3\3\u00c4")
        buf.write("\3\u00c4\3\u00c4\3\u00c4\3\u00c4\5\u00c4\u081d\n\u00c4")
        buf.write("\3\u00c5\3\u00c5\3\u00c5\3\u00c5\3\u00c5\5\u00c5\u0824")
        buf.write("\n\u00c5\3\u00c5\3\u00c5\3\u00c5\3\u00c5\5\u00c5\u082a")
        buf.write("\n\u00c5\3\u00c5\3\u00c5\3\u00c5\5\u00c5\u082f\n\u00c5")
        buf.write("\3\u00c6\6\u00c6\u0832\n\u00c6\r\u00c6\16\u00c6\u0833")
        buf.write("\3\u00c7\3\u00c7\5\u00c7\u0838\n\u00c7\3\u00c7\3\u00c7")
        buf.write("\3\u00c7\3\u00c8\3\u00c8\3\u00c8\3\u00c8\3\u00c8\3\u00c8")
        buf.write("\3\u00c8\3\u00c8\3\u00c8\3\u00c8\5\u00c8\u0847\n\u00c8")
        buf.write("\3\u00c9\3\u00c9\5\u00c9\u084b\n\u00c9\3\u00c9\3\u00c9")
        buf.write("\3\u00c9\3\u00c9\3\u00c9\3\u00c9\3\u00c9\3\u00c9\3\u00c9")
        buf.write("\3\u00c9\5\u00c9\u0857\n\u00c9\3\u00ca\3\u00ca\3\u00ca")
        buf.write("\3\u00ca\3\u00ca\3\u00ca\3\u00ca\3\u00ca\5\u00ca\u0861")
        buf.write("\n\u00ca\3\u00cb\3\u00cb\5\u00cb\u0865\n\u00cb\3\u00cb")
        buf.write("\3\u00cb\3\u00cc\3\u00cc\5\u00cc\u086b\n\u00cc\3\u00cc")
        buf.write("\3\u00cc\3\u00cc\3\u00cc\5\u00cc\u0871\n\u00cc\3\u00cd")
        buf.write("\3\u00cd\3\u00ce\3\u00ce\3\u00ce\3\u00ce\3\u00ce\3\u00ce")
        buf.write("\3\u00ce\5\u00ce\u087c\n\u00ce\3\u00cf\3\u00cf\5\u00cf")
        buf.write("\u0880\n\u00cf\3\u00cf\3\u00cf\3\u00cf\3\u00cf\5\u00cf")
        buf.write("\u0886\n\u00cf\3\u00d0\3\u00d0\3\u00d0\3\u00d0\3\u00d1")
        buf.write("\3\u00d1\3\u00d1\3\u00d1\3\u00d1\3\u00d1\3\u00d1\3\u00d1")
        buf.write("\3\u00d1\3\u00d1\3\u00d1\3\u00d1\3\u00d1\3\u00d1\3\u00d1")
        buf.write("\3\u00d1\3\u00d1\3\u00d1\3\u00d1\3\u00d1\3\u00d1\3\u00d1")
        buf.write("\3\u00d1\3\u00d1\3\u00d1\3\u00d1\3\u00d1\3\u00d1\3\u00d1")
        buf.write("\3\u00d1\3\u00d1\3\u00d1\3\u00d1\5\u00d1\u08ad\n\u00d1")
        buf.write("\3\u00d2\3\u00d2\3\u00d2\3\u00d2\3\u00d2\3\u00d2\3\u00d2")
        buf.write("\3\u00d2\3\u00d2\3\u00d2\3\u00d2\3\u00d2\3\u00d2\3\u00d2")
        buf.write("\3\u00d2\3\u00d2\3\u00d2\3\u00d2\3\u00d2\5\u00d2\u08c2")
        buf.write("\n\u00d2\3\u00d3\3\u00d3\3\u00d3\5\u00d3\u08c7\n\u00d3")
        buf.write("\3\u00d4\3\u00d4\3\u00d4\3\u00d4\3\u00d5\3\u00d5\3\u00d5")
        buf.write("\3\u00d5\3\u00d5\3\u00d6\3\u00d6\3\u00d6\3\u00d6\3\u00d7")
        buf.write("\3\u00d7\5\u00d7\u08d8\n\u00d7\3\u00d7\5\u00d7\u08db\n")
        buf.write("\u00d7\3\u00d7\3\u00d7\3\u00d8\5\u00d8\u08e0\n\u00d8\3")
        buf.write("\u00d8\3\u00d8\5\u00d8\u08e4\n\u00d8\3\u00d8\5\u00d8\u08e7")
        buf.write("\n\u00d8\3\u00d8\3\u00d8\3\u00d8\3\u00d8\3\u00d8\5\u00d8")
        buf.write("\u08ee\n\u00d8\3\u00d9\3\u00d9\3\u00d9\3\u00d9\3\u00d9")
        buf.write("\3\u00d9\3\u00d9\5\u00d9\u08f7\n\u00d9\3\u00da\3\u00da")
        buf.write("\3\u00da\7\u00da\u08fc\n\u00da\f\u00da\16\u00da\u08ff")
        buf.write("\13\u00da\3\u00db\3\u00db\3\u00db\7\u00db\u0904\n\u00db")
        buf.write("\f\u00db\16\u00db\u0907\13\u00db\3\u00dc\3\u00dc\5\u00dc")
        buf.write("\u090b\n\u00dc\3\u00dc\3\u00dc\3\u00dc\3\u00dc\5\u00dc")
        buf.write("\u0911\n\u00dc\3\u00dd\3\u00dd\3\u00de\3\u00de\3\u00de")
        buf.write("\3\u00de\3\u00df\3\u00df\3\u00df\7\u00df\u091c\n\u00df")
        buf.write("\f\u00df\16\u00df\u091f\13\u00df\3\u00e0\5\u00e0\u0922")
        buf.write("\n\u00e0\3\u00e0\3\u00e0\3\u00e1\3\u00e1\3\u00e2\3\u00e2")
        buf.write("\3\u00e2\3\u00e3\3\u00e3\3\u00e3\3\u00e3\3\u00e4\3\u00e4")
        buf.write("\3\u00e4\3\u00e4\3\u00e4\3\u00e4\6\u00e4\u0935\n\u00e4")
        buf.write("\r\u00e4\16\u00e4\u0936\3\u00e4\3\u00e4\5\u00e4\u093b")
        buf.write("\n\u00e4\3\u00e5\3\u00e5\3\u00e5\3\u00e5\3\u00e5\5\u00e5")
        buf.write("\u0942\n\u00e5\3\u00e6\3\u00e6\3\u00e7\3\u00e7\3\u00e7")
        buf.write("\3\u00e7\3\u00e7\3\u00e7\3\u00e7\3\u00e7\3\u00e7\3\u00e7")
        buf.write("\3\u00e7\3\u00e7\3\u00e7\3\u00e7\3\u00e7\3\u00e7\3\u00e7")
        buf.write("\5\u00e7\u0957\n\u00e7\3\u00e8\3\u00e8\3\u00e8\3\u00e8")
        buf.write("\3\u00e8\3\u00e9\3\u00e9\3\u00e9\5\u00e9\u0961\n\u00e9")
        buf.write("\3\u00e9\3\u00e9\3\u00e9\3\u00e9\3\u00e9\3\u00e9\5\u00e9")
        buf.write("\u0969\n\u00e9\3\u00e9\3\u00e9\3\u00e9\3\u00e9\3\u00e9")
        buf.write("\3\u00e9\3\u00e9\3\u00e9\3\u00e9\3\u00e9\3\u00e9\3\u00e9")
        buf.write("\3\u00e9\3\u00e9\3\u00e9\3\u00e9\3\u00e9\3\u00e9\5\u00e9")
        buf.write("\u097d\n\u00e9\3\u00e9\3\u00e9\3\u00e9\3\u00e9\3\u00e9")
        buf.write("\3\u00e9\3\u00e9\3\u00e9\3\u00e9\3\u00e9\3\u00e9\3\u00e9")
        buf.write("\3\u00e9\3\u00e9\3\u00e9\3\u00e9\3\u00e9\3\u00e9\3\u00e9")
        buf.write("\3\u00e9\7\u00e9\u0993\n\u00e9\f\u00e9\16\u00e9\u0996")
        buf.write("\13\u00e9\3\u00ea\3\u00ea\3\u00ea\3\u00ea\3\u00ea\3\u00ea")
        buf.write("\5\u00ea\u099e\n\u00ea\3\u00eb\3\u00eb\3\u00eb\7\u00eb")
        buf.write("\u09a3\n\u00eb\f\u00eb\16\u00eb\u09a6\13\u00eb\3\u00ec")
        buf.write("\3\u00ec\3\u00ec\3\u00ec\3\u00ec\3\u00ec\3\u00ec\3\u00ec")
        buf.write("\3\u00ec\3\u00ec\5\u00ec\u09b2\n\u00ec\3\u00ed\3\u00ed")
        buf.write("\3\u00ee\3\u00ee\7\u00ee\u09b8\n\u00ee\f\u00ee\16\u00ee")
        buf.write("\u09bb\13\u00ee\3\u00ef\3\u00ef\3\u00ef\3\u00f0\3\u00f0")
        buf.write("\3\u00f0\3\u00f0\3\u00f0\3\u00f0\3\u00f0\3\u00f1\3\u00f1")
        buf.write("\3\u00f1\3\u00f1\3\u00f1\3\u00f1\3\u00f1\3\u00f1\3\u00f1")
        buf.write("\5\u00f1\u09d0\n\u00f1\3\u00f1\3\u00f1\3\u00f1\3\u00f1")
        buf.write("\3\u00f1\3\u00f1\3\u00f1\3\u00f1\3\u00f1\3\u00f1\7\u00f1")
        buf.write("\u09dc\n\u00f1\f\u00f1\16\u00f1\u09df\13\u00f1\3\u00f2")
        buf.write("\3\u00f2\5\u00f2\u09e3\n\u00f2\3\u00f2\5\u00f2\u09e6\n")
        buf.write("\u00f2\3\u00f2\3\u00f2\3\u00f3\3\u00f3\5\u00f3\u09ec\n")
        buf.write("\u00f3\3\u00f3\3\u00f3\5\u00f3\u09f0\n\u00f3\3\u00f4\3")
        buf.write("\u00f4\3\u00f5\3\u00f5\5\u00f5\u09f6\n\u00f5\3\u00f5\3")
        buf.write("\u00f5\3\u00f6\3\u00f6\3\u00f6\3\u00f6\3\u00f6\5\u00f6")
        buf.write("\u09ff\n\u00f6\3\u00f7\3\u00f7\3\u00f7\3\u00f7\5\u00f7")
        buf.write("\u0a05\n\u00f7\3\u00f8\3\u00f8\3\u00f9\5\u00f9\u0a0a\n")
        buf.write("\u00f9\3\u00f9\3\u00f9\5\u00f9\u0a0e\n\u00f9\3\u00f9\3")
        buf.write("\u00f9\3\u00f9\3\u00f9\5\u00f9\u0a14\n\u00f9\3\u00f9\3")
        buf.write("\u00f9\3\u00f9\3\u00f9\3\u00f9\5\u00f9\u0a1b\n\u00f9\3")
        buf.write("\u00fa\3\u00fa\3\u00fa\3\u00fa\3\u00fa\5\u00fa\u0a22\n")
        buf.write("\u00fa\3\u00fa\3\u00fa\5\u00fa\u0a26\n\u00fa\3\u00fb\3")
        buf.write("\u00fb\3\u00fb\3\u00fb\3\u00fb\5\u00fb\u0a2d\n\u00fb\3")
        buf.write("\u00fc\5\u00fc\u0a30\n\u00fc\3\u00fc\5\u00fc\u0a33\n\u00fc")
        buf.write("\3\u00fc\3\u00fc\3\u00fc\3\u00fc\5\u00fc\u0a39\n\u00fc")
        buf.write("\3\u00fd\3\u00fd\3\u00fe\3\u00fe\3\u00fe\3\u00fe\3\u00ff")
        buf.write("\3\u00ff\3\u00ff\3\u00ff\3\u00ff\3\u00ff\3\u0100\3\u0100")
        buf.write("\3\u0100\6\u0100\u0a4a\n\u0100\r\u0100\16\u0100\u0a4b")
        buf.write("\3\u0101\3\u0101\3\u0102\3\u0102\3\u0102\3\u0102\3\u0102")
        buf.write("\3\u0102\3\u0102\3\u0102\3\u0102\5\u0102\u0a59\n\u0102")
        buf.write("\3\u0103\3\u0103\3\u0103\3\u0103\3\u0103\5\u0103\u0a60")
        buf.write("\n\u0103\3\u0104\3\u0104\3\u0105\3\u0105\5\u0105\u0a66")
        buf.write("\n\u0105\3\u0106\3\u0106\5\u0106\u0a6a\n\u0106\3\u0107")
        buf.write("\3\u0107\3\u0108\3\u0108\3\u0109\3\u0109\3\u0109\3\u010a")
        buf.write("\3\u010a\3\u010a\3\u010b\3\u010b\3\u010b\3\u010b\3\u010c")
        buf.write("\3\u010c\3\u010c\3\u010c\3\u010d\3\u010d\3\u010d\3\u010d")
        buf.write("\3\u010e\3\u010e\3\u010e\3\u010e\3\u010f\3\u010f\3\u010f")
        buf.write("\3\u010f\3\u010f\3\u0110\3\u0110\3\u0110\3\u0110\3\u0111")
        buf.write("\3\u0111\3\u0111\3\u0112\3\u0112\3\u0112\3\u0113\3\u0113")
        buf.write("\3\u0113\3\u0114\3\u0114\3\u0114\7\u0114\u0a9b\n\u0114")
        buf.write("\f\u0114\16\u0114\u0a9e\13\u0114\3\u0114\3\u0114\3\u0114")
        buf.write("\7\u0114\u0aa3\n\u0114\f\u0114\16\u0114\u0aa6\13\u0114")
        buf.write("\5\u0114\u0aa8\n\u0114\3\u0115\3\u0115\5\u0115\u0aac\n")
        buf.write("\u0115\3\u0116\3\u0116\5\u0116\u0ab0\n\u0116\3\u0117\3")
        buf.write("\u0117\3\u0118\3\u0118\5\u0118\u0ab6\n\u0118\3\u0119\3")
        buf.write("\u0119\3\u0119\3\u0119\5\u0119\u0abc\n\u0119\3\u011a\5")
        buf.write("\u011a\u0abf\n\u011a\3\u011a\3\u011a\5\u011a\u0ac3\n\u011a")
        buf.write("\3\u011a\5\u011a\u0ac6\n\u011a\3\u011b\3\u011b\3\u011c")
        buf.write("\3\u011c\3\u011d\3\u011d\3\u011e\3\u011e\3\u011e\2\6d")
        buf.write("\u015c\u01d0\u01e0\u011f\2\4\6\b\n\f\16\20\22\24\26\30")
        buf.write("\32\34\36 \"$&(*,.\60\62\64\668:<>@BDFHJLNPRTVXZ\\^`b")
        buf.write("dfhjlnprtvxz|~\u0080\u0082\u0084\u0086\u0088\u008a\u008c")
        buf.write("\u008e\u0090\u0092\u0094\u0096\u0098\u009a\u009c\u009e")
        buf.write("\u00a0\u00a2\u00a4\u00a6\u00a8\u00aa\u00ac\u00ae\u00b0")
        buf.write("\u00b2\u00b4\u00b6\u00b8\u00ba\u00bc\u00be\u00c0\u00c2")
        buf.write("\u00c4\u00c6\u00c8\u00ca\u00cc\u00ce\u00d0\u00d2\u00d4")
        buf.write("\u00d6\u00d8\u00da\u00dc\u00de\u00e0\u00e2\u00e4\u00e6")
        buf.write("\u00e8\u00ea\u00ec\u00ee\u00f0\u00f2\u00f4\u00f6\u00f8")
        buf.write("\u00fa\u00fc\u00fe\u0100\u0102\u0104\u0106\u0108\u010a")
        buf.write("\u010c\u010e\u0110\u0112\u0114\u0116\u0118\u011a\u011c")
        buf.write("\u011e\u0120\u0122\u0124\u0126\u0128\u012a\u012c\u012e")
        buf.write("\u0130\u0132\u0134\u0136\u0138\u013a\u013c\u013e\u0140")
        buf.write("\u0142\u0144\u0146\u0148\u014a\u014c\u014e\u0150\u0152")
        buf.write("\u0154\u0156\u0158\u015a\u015c\u015e\u0160\u0162\u0164")
        buf.write("\u0166\u0168\u016a\u016c\u016e\u0170\u0172\u0174\u0176")
        buf.write("\u0178\u017a\u017c\u017e\u0180\u0182\u0184\u0186\u0188")
        buf.write("\u018a\u018c\u018e\u0190\u0192\u0194\u0196\u0198\u019a")
        buf.write("\u019c\u019e\u01a0\u01a2\u01a4\u01a6\u01a8\u01aa\u01ac")
        buf.write("\u01ae\u01b0\u01b2\u01b4\u01b6\u01b8\u01ba\u01bc\u01be")
        buf.write("\u01c0\u01c2\u01c4\u01c6\u01c8\u01ca\u01cc\u01ce\u01d0")
        buf.write("\u01d2\u01d4\u01d6\u01d8\u01da\u01dc\u01de\u01e0\u01e2")
        buf.write("\u01e4\u01e6\u01e8\u01ea\u01ec\u01ee\u01f0\u01f2\u01f4")
        buf.write("\u01f6\u01f8\u01fa\u01fc\u01fe\u0200\u0202\u0204\u0206")
        buf.write("\u0208\u020a\u020c\u020e\u0210\u0212\u0214\u0216\u0218")
        buf.write("\u021a\u021c\u021e\u0220\u0222\u0224\u0226\u0228\u022a")
        buf.write("\u022c\u022e\u0230\u0232\u0234\u0236\u0238\u023a\2\16")
        buf.write("\4\2\u0084\u0084\u009c\u009c\4\2\b\b$)\3\2@B\3\2ST\7\2")
        buf.write("WX\u0086\u0086\u008d\u008f\u0094\u0095\u0098\u0098\5\2")
        buf.write("JJMMjk\17\2\34\36 !*-\60\61\67\679:<HJMRT`ceepsv\u0080")
        buf.write("\r\2\3\6\t\27\34\36 !#VYY`ceegiptv\u0083\5\2\u0090\u0091")
        buf.write("\u0093\u0094\u0096\u009f\4\2\u0081\u0081\u0083\u0083\3")
        buf.write("\2\u00a3\u00a7\3\2\u00a9\u00aa\2\u0b7f\2\u023d\3\2\2\2")
        buf.write("\4\u0265\3\2\2\2\6\u0267\3\2\2\2\b\u0269\3\2\2\2\n\u0273")
        buf.write("\3\2\2\2\f\u0291\3\2\2\2\16\u0295\3\2\2\2\20\u0297\3\2")
        buf.write("\2\2\22\u02a3\3\2\2\2\24\u02a7\3\2\2\2\26\u02b3\3\2\2")
        buf.write("\2\30\u02b5\3\2\2\2\32\u02c3\3\2\2\2\34\u02c5\3\2\2\2")
        buf.write("\36\u02cd\3\2\2\2 \u02cf\3\2\2\2\"\u02d9\3\2\2\2$\u02db")
        buf.write("\3\2\2\2&\u02e0\3\2\2\2(\u02e8\3\2\2\2*\u02f2\3\2\2\2")
        buf.write(",\u02f4\3\2\2\2.\u0303\3\2\2\2\60\u0305\3\2\2\2\62\u0308")
        buf.write("\3\2\2\2\64\u030b\3\2\2\2\66\u0319\3\2\2\28\u031b\3\2")
        buf.write("\2\2:\u031e\3\2\2\2<\u0325\3\2\2\2>\u0327\3\2\2\2@\u032b")
        buf.write("\3\2\2\2B\u032f\3\2\2\2D\u0331\3\2\2\2F\u0335\3\2\2\2")
        buf.write("H\u0338\3\2\2\2J\u033b\3\2\2\2L\u0340\3\2\2\2N\u0344\3")
        buf.write("\2\2\2P\u034f\3\2\2\2R\u0351\3\2\2\2T\u035a\3\2\2\2V\u0360")
        buf.write("\3\2\2\2X\u0364\3\2\2\2Z\u0369\3\2\2\2\\\u036d\3\2\2\2")
        buf.write("^\u036f\3\2\2\2`\u0371\3\2\2\2b\u0373\3\2\2\2d\u037f\3")
        buf.write("\2\2\2f\u039e\3\2\2\2h\u03a0\3\2\2\2j\u03a4\3\2\2\2l\u03a6")
        buf.write("\3\2\2\2n\u03b6\3\2\2\2p\u03b8\3\2\2\2r\u03ba\3\2\2\2")
        buf.write("t\u03bc\3\2\2\2v\u03c1\3\2\2\2x\u03c9\3\2\2\2z\u03cb\3")
        buf.write("\2\2\2|\u03cf\3\2\2\2~\u03e0\3\2\2\2\u0080\u03e2\3\2\2")
        buf.write("\2\u0082\u03e5\3\2\2\2\u0084\u03ef\3\2\2\2\u0086\u03f9")
        buf.write("\3\2\2\2\u0088\u03fb\3\2\2\2\u008a\u03ff\3\2\2\2\u008c")
        buf.write("\u0403\3\2\2\2\u008e\u040b\3\2\2\2\u0090\u041d\3\2\2\2")
        buf.write("\u0092\u0420\3\2\2\2\u0094\u0425\3\2\2\2\u0096\u0427\3")
        buf.write("\2\2\2\u0098\u042e\3\2\2\2\u009a\u0436\3\2\2\2\u009c\u0438")
        buf.write("\3\2\2\2\u009e\u0442\3\2\2\2\u00a0\u0445\3\2\2\2\u00a2")
        buf.write("\u044d\3\2\2\2\u00a4\u0455\3\2\2\2\u00a6\u0459\3\2\2\2")
        buf.write("\u00a8\u047f\3\2\2\2\u00aa\u0482\3\2\2\2\u00ac\u0489\3")
        buf.write("\2\2\2\u00ae\u0497\3\2\2\2\u00b0\u049a\3\2\2\2\u00b2\u04a3")
        buf.write("\3\2\2\2\u00b4\u04ae\3\2\2\2\u00b6\u04be\3\2\2\2\u00b8")
        buf.write("\u04c1\3\2\2\2\u00ba\u04c9\3\2\2\2\u00bc\u04dc\3\2\2\2")
        buf.write("\u00be\u04df\3\2\2\2\u00c0\u04e8\3\2\2\2\u00c2\u04f1\3")
        buf.write("\2\2\2\u00c4\u04fd\3\2\2\2\u00c6\u04ff\3\2\2\2\u00c8\u0502")
        buf.write("\3\2\2\2\u00ca\u050f\3\2\2\2\u00cc\u0518\3\2\2\2\u00ce")
        buf.write("\u0526\3\2\2\2\u00d0\u0528\3\2\2\2\u00d2\u052e\3\2\2\2")
        buf.write("\u00d4\u0536\3\2\2\2\u00d6\u0538\3\2\2\2\u00d8\u0555\3")
        buf.write("\2\2\2\u00da\u0557\3\2\2\2\u00dc\u0559\3\2\2\2\u00de\u055b")
        buf.write("\3\2\2\2\u00e0\u056c\3\2\2\2\u00e2\u056f\3\2\2\2\u00e4")
        buf.write("\u0582\3\2\2\2\u00e6\u0589\3\2\2\2\u00e8\u058c\3\2\2\2")
        buf.write("\u00ea\u0599\3\2\2\2\u00ec\u059b\3\2\2\2\u00ee\u059f\3")
        buf.write("\2\2\2\u00f0\u05a1\3\2\2\2\u00f2\u05a3\3\2\2\2\u00f4\u05b0")
        buf.write("\3\2\2\2\u00f6\u05b7\3\2\2\2\u00f8\u05ba\3\2\2\2\u00fa")
        buf.write("\u05c4\3\2\2\2\u00fc\u05c6\3\2\2\2\u00fe\u05ca\3\2\2\2")
        buf.write("\u0100\u05d0\3\2\2\2\u0102\u05d3\3\2\2\2\u0104\u05e5\3")
        buf.write("\2\2\2\u0106\u05e7\3\2\2\2\u0108\u05f2\3\2\2\2\u010a\u0621")
        buf.write("\3\2\2\2\u010c\u0623\3\2\2\2\u010e\u0625\3\2\2\2\u0110")
        buf.write("\u0630\3\2\2\2\u0112\u0633\3\2\2\2\u0114\u063f\3\2\2\2")
        buf.write("\u0116\u0641\3\2\2\2\u0118\u064c\3\2\2\2\u011a\u0654\3")
        buf.write("\2\2\2\u011c\u0656\3\2\2\2\u011e\u065b\3\2\2\2\u0120\u0678")
        buf.write("\3\2\2\2\u0122\u067a\3\2\2\2\u0124\u067f\3\2\2\2\u0126")
        buf.write("\u06a4\3\2\2\2\u0128\u06bd\3\2\2\2\u012a\u06bf\3\2\2\2")
        buf.write("\u012c\u06c2\3\2\2\2\u012e\u06df\3\2\2\2\u0130\u06e1\3")
        buf.write("\2\2\2\u0132\u06ec\3\2\2\2\u0134\u06fa\3\2\2\2\u0136\u06fd")
        buf.write("\3\2\2\2\u0138\u0705\3\2\2\2\u013a\u070e\3\2\2\2\u013c")
        buf.write("\u0710\3\2\2\2\u013e\u0714\3\2\2\2\u0140\u0718\3\2\2\2")
        buf.write("\u0142\u071e\3\2\2\2\u0144\u0721\3\2\2\2\u0146\u072f\3")
        buf.write("\2\2\2\u0148\u0737\3\2\2\2\u014a\u0739\3\2\2\2\u014c\u073d")
        buf.write("\3\2\2\2\u014e\u0741\3\2\2\2\u0150\u0743\3\2\2\2\u0152")
        buf.write("\u074b\3\2\2\2\u0154\u0765\3\2\2\2\u0156\u0768\3\2\2\2")
        buf.write("\u0158\u0785\3\2\2\2\u015a\u0787\3\2\2\2\u015c\u079c\3")
        buf.write("\2\2\2\u015e\u07a6\3\2\2\2\u0160\u07a8\3\2\2\2\u0162\u07ae")
        buf.write("\3\2\2\2\u0164\u07b0\3\2\2\2\u0166\u07b6\3\2\2\2\u0168")
        buf.write("\u07be\3\2\2\2\u016a\u07c1\3\2\2\2\u016c\u07c8\3\2\2\2")
        buf.write("\u016e\u07cb\3\2\2\2\u0170\u07cd\3\2\2\2\u0172\u07d2\3")
        buf.write("\2\2\2\u0174\u07d4\3\2\2\2\u0176\u07d9\3\2\2\2\u0178\u07e0")
        buf.write("\3\2\2\2\u017a\u07f4\3\2\2\2\u017c\u07fc\3\2\2\2\u017e")
        buf.write("\u07ff\3\2\2\2\u0180\u0805\3\2\2\2\u0182\u0812\3\2\2\2")
        buf.write("\u0184\u0814\3\2\2\2\u0186\u081c\3\2\2\2\u0188\u082e\3")
        buf.write("\2\2\2\u018a\u0831\3\2\2\2\u018c\u0835\3\2\2\2\u018e\u0846")
        buf.write("\3\2\2\2\u0190\u0856\3\2\2\2\u0192\u0860\3\2\2\2\u0194")
        buf.write("\u0862\3\2\2\2\u0196\u0870\3\2\2\2\u0198\u0872\3\2\2\2")
        buf.write("\u019a\u087b\3\2\2\2\u019c\u0885\3\2\2\2\u019e\u0887\3")
        buf.write("\2\2\2\u01a0\u08ac\3\2\2\2\u01a2\u08c1\3\2\2\2\u01a4\u08c6")
        buf.write("\3\2\2\2\u01a6\u08c8\3\2\2\2\u01a8\u08cc\3\2\2\2\u01aa")
        buf.write("\u08d1\3\2\2\2\u01ac\u08d5\3\2\2\2\u01ae\u08ed\3\2\2\2")
        buf.write("\u01b0\u08f6\3\2\2\2\u01b2\u08f8\3\2\2\2\u01b4\u0900\3")
        buf.write("\2\2\2\u01b6\u0910\3\2\2\2\u01b8\u0912\3\2\2\2\u01ba\u0914")
        buf.write("\3\2\2\2\u01bc\u0918\3\2\2\2\u01be\u0921\3\2\2\2\u01c0")
        buf.write("\u0925\3\2\2\2\u01c2\u0927\3\2\2\2\u01c4\u092a\3\2\2\2")
        buf.write("\u01c6\u093a\3\2\2\2\u01c8\u0941\3\2\2\2\u01ca\u0943\3")
        buf.write("\2\2\2\u01cc\u0956\3\2\2\2\u01ce\u0958\3\2\2\2\u01d0\u0960")
        buf.write("\3\2\2\2\u01d2\u099d\3\2\2\2\u01d4\u099f\3\2\2\2\u01d6")
        buf.write("\u09b1\3\2\2\2\u01d8\u09b3\3\2\2\2\u01da\u09b5\3\2\2\2")
        buf.write("\u01dc\u09bc\3\2\2\2\u01de\u09bf\3\2\2\2\u01e0\u09cf\3")
        buf.write("\2\2\2\u01e2\u09e0\3\2\2\2\u01e4\u09e9\3\2\2\2\u01e6\u09f1")
        buf.write("\3\2\2\2\u01e8\u09f3\3\2\2\2\u01ea\u09fe\3\2\2\2\u01ec")
        buf.write("\u0a04\3\2\2\2\u01ee\u0a06\3\2\2\2\u01f0\u0a1a\3\2\2\2")
        buf.write("\u01f2\u0a25\3\2\2\2\u01f4\u0a2c\3\2\2\2\u01f6\u0a38\3")
        buf.write("\2\2\2\u01f8\u0a3a\3\2\2\2\u01fa\u0a3c\3\2\2\2\u01fc\u0a40")
        buf.write("\3\2\2\2\u01fe\u0a46\3\2\2\2\u0200\u0a4d\3\2\2\2\u0202")
        buf.write("\u0a58\3\2\2\2\u0204\u0a5f\3\2\2\2\u0206\u0a61\3\2\2\2")
        buf.write("\u0208\u0a65\3\2\2\2\u020a\u0a69\3\2\2\2\u020c\u0a6b\3")
        buf.write("\2\2\2\u020e\u0a6d\3\2\2\2\u0210\u0a6f\3\2\2\2\u0212\u0a72")
        buf.write("\3\2\2\2\u0214\u0a75\3\2\2\2\u0216\u0a79\3\2\2\2\u0218")
        buf.write("\u0a7d\3\2\2\2\u021a\u0a81\3\2\2\2\u021c\u0a85\3\2\2\2")
        buf.write("\u021e\u0a8a\3\2\2\2\u0220\u0a8e\3\2\2\2\u0222\u0a91\3")
        buf.write("\2\2\2\u0224\u0a94\3\2\2\2\u0226\u0aa7\3\2\2\2\u0228\u0aab")
        buf.write("\3\2\2\2\u022a\u0aaf\3\2\2\2\u022c\u0ab1\3\2\2\2\u022e")
        buf.write("\u0ab5\3\2\2\2\u0230\u0abb\3\2\2\2\u0232\u0ac5\3\2\2\2")
        buf.write("\u0234\u0ac7\3\2\2\2\u0236\u0ac9\3\2\2\2\u0238\u0acb\3")
        buf.write("\2\2\2\u023a\u0acd\3\2\2\2\u023c\u023e\5\6\4\2\u023d\u023c")
        buf.write("\3\2\2\2\u023d\u023e\3\2\2\2\u023e\u023f\3\2\2\2\u023f")
        buf.write("\u0240\7\2\2\3\u0240\3\3\2\2\2\u0241\u0243\5\u017e\u00c0")
        buf.write("\2\u0242\u0244\7\u008f\2\2\u0243\u0242\3\2\2\2\u0243\u0244")
        buf.write("\3\2\2\2\u0244\u0266\3\2\2\2\u0245\u0247\5\u0090I\2\u0246")
        buf.write("\u0248\7\u008f\2\2\u0247\u0246\3\2\2\2\u0247\u0248\3\2")
        buf.write("\2\2\u0248\u0266\3\2\2\2\u0249\u024b\5\n\6\2\u024a\u024c")
        buf.write("\7\u008f\2\2\u024b\u024a\3\2\2\2\u024b\u024c\3\2\2\2\u024c")
        buf.write("\u0266\3\2\2\2\u024d\u024f\5\36\20\2\u024e\u0250\7\u008f")
        buf.write("\2\2\u024f\u024e\3\2\2\2\u024f\u0250\3\2\2\2\u0250\u0266")
        buf.write("\3\2\2\2\u0251\u0253\5\66\34\2\u0252\u0254\7\u008f\2\2")
        buf.write("\u0253\u0252\3\2\2\2\u0253\u0254\3\2\2\2\u0254\u0266\3")
        buf.write("\2\2\2\u0255\u0257\5<\37\2\u0256\u0258\7\u008f\2\2\u0257")
        buf.write("\u0256\3\2\2\2\u0257\u0258\3\2\2\2\u0258\u0266\3\2\2\2")
        buf.write("\u0259\u025b\5H%\2\u025a\u025c\7\u008f\2\2\u025b\u025a")
        buf.write("\3\2\2\2\u025b\u025c\3\2\2\2\u025c\u0266\3\2\2\2\u025d")
        buf.write("\u025f\5J&\2\u025e\u0260\7\u008f\2\2\u025f\u025e\3\2\2")
        buf.write("\2\u025f\u0260\3\2\2\2\u0260\u0266\3\2\2\2\u0261\u0263")
        buf.write("\5P)\2\u0262\u0264\7\u008f\2\2\u0263\u0262\3\2\2\2\u0263")
        buf.write("\u0264\3\2\2\2\u0264\u0266\3\2\2\2\u0265\u0241\3\2\2\2")
        buf.write("\u0265\u0245\3\2\2\2\u0265\u0249\3\2\2\2\u0265\u024d\3")
        buf.write("\2\2\2\u0265\u0251\3\2\2\2\u0265\u0255\3\2\2\2\u0265\u0259")
        buf.write("\3\2\2\2\u0265\u025d\3\2\2\2\u0265\u0261\3\2\2\2\u0266")
        buf.write("\5\3\2\2\2\u0267\u0268\5\b\5\2\u0268\7\3\2\2\2\u0269\u026a")
        buf.write("\6\5\2\3\u026a\u026b\5\4\3\2\u026b\u026d\b\5\1\2\u026c")
        buf.write("\u026e\5\b\5\2\u026d\u026c\3\2\2\2\u026d\u026e\3\2\2\2")
        buf.write("\u026e\t\3\2\2\2\u026f\u0274\5\f\7\2\u0270\u0274\5\20")
        buf.write("\t\2\u0271\u0274\5\22\n\2\u0272\u0274\5\34\17\2\u0273")
        buf.write("\u026f\3\2\2\2\u0273\u0270\3\2\2\2\u0273\u0271\3\2\2\2")
        buf.write("\u0273\u0272\3\2\2\2\u0274\13\3\2\2\2\u0275\u0277\7\3")
        buf.write("\2\2\u0276\u0278\5\16\b\2\u0277\u0276\3\2\2\2\u0277\u0278")
        buf.write("\3\2\2\2\u0278\u0279\3\2\2\2\u0279\u027b\7\u008f\2\2\u027a")
        buf.write("\u027c\5\u017e\u00c0\2\u027b\u027a\3\2\2\2\u027b\u027c")
        buf.write("\3\2\2\2\u027c\u027d\3\2\2\2\u027d\u027f\7\u008f\2\2\u027e")
        buf.write("\u0280\5\u017e\u00c0\2\u027f\u027e\3\2\2\2\u027f\u0280")
        buf.write("\3\2\2\2\u0280\u0281\3\2\2\2\u0281\u0292\5\u0096L\2\u0282")
        buf.write("\u0283\7\3\2\2\u0283\u0285\7\u0088\2\2\u0284\u0286\5\16")
        buf.write("\b\2\u0285\u0284\3\2\2\2\u0285\u0286\3\2\2\2\u0286\u0287")
        buf.write("\3\2\2\2\u0287\u0289\7\u008f\2\2\u0288\u028a\5\u017e\u00c0")
        buf.write("\2\u0289\u0288\3\2\2\2\u0289\u028a\3\2\2\2\u028a\u028b")
        buf.write("\3\2\2\2\u028b\u028d\7\u008f\2\2\u028c\u028e\5\u017e\u00c0")
        buf.write("\2\u028d\u028c\3\2\2\2\u028d\u028e\3\2\2\2\u028e\u028f")
        buf.write("\3\2\2\2\u028f\u0290\7\u008b\2\2\u0290\u0292\5\u0096L")
        buf.write("\2\u0291\u0275\3\2\2\2\u0291\u0282\3\2\2\2\u0292\r\3\2")
        buf.write("\2\2\u0293\u0296\5\u00a8U\2\u0294\u0296\5\u0180\u00c1")
        buf.write("\2\u0295\u0293\3\2\2\2\u0295\u0294\3\2\2\2\u0296\17\3")
        buf.write("\2\2\2\u0297\u0299\7\3\2\2\u0298\u029a\7\4\2\2\u0299\u0298")
        buf.write("\3\2\2\2\u0299\u029a\3\2\2\2\u029a\u029b\3\2\2\2\u029b")
        buf.write("\u029c\5\u015c\u00af\2\u029c\u029d\7\5\2\2\u029d\u029f")
        buf.write("\5\u017e\u00c0\2\u029e\u02a0\5\62\32\2\u029f\u029e\3\2")
        buf.write("\2\2\u029f\u02a0\3\2\2\2\u02a0\u02a1\3\2\2\2\u02a1\u02a2")
        buf.write("\5\u0096L\2\u02a2\21\3\2\2\2\u02a3\u02a4\7\6\2\2\u02a4")
        buf.write("\u02a5\5\24\13\2\u02a5\u02a6\5\u0096L\2\u02a6\23\3\2\2")
        buf.write("\2\u02a7\u02ac\5\26\f\2\u02a8\u02a9\7\u008d\2\2\u02a9")
        buf.write("\u02ab\5\26\f\2\u02aa\u02a8\3\2\2\2\u02ab\u02ae\3\2\2")
        buf.write("\2\u02ac\u02aa\3\2\2\2\u02ac\u02ad\3\2\2\2\u02ad\25\3")
        buf.write("\2\2\2\u02ae\u02ac\3\2\2\2\u02af\u02b4\5\u017e\u00c0\2")
        buf.write("\u02b0\u02b4\5t;\2\u02b1\u02b4\5\30\r\2\u02b2\u02b4\5")
        buf.write("\32\16\2\u02b3\u02af\3\2\2\2\u02b3\u02b0\3\2\2\2\u02b3")
        buf.write("\u02b1\3\2\2\2\u02b3\u02b2\3\2\2\2\u02b4\27\3\2\2\2\u02b5")
        buf.write("\u02b6\7\4\2\2\u02b6\u02b7\5\u015c\u00af\2\u02b7\u02b9")
        buf.write("\5\u00a6T\2\u02b8\u02ba\5\62\32\2\u02b9\u02b8\3\2\2\2")
        buf.write("\u02b9\u02ba\3\2\2\2\u02ba\31\3\2\2\2\u02bb\u02bc\7\7")
        buf.write("\2\2\u02bc\u02bd\5\u015c\u00af\2\u02bd\u02be\5\u00a6T")
        buf.write("\2\u02be\u02c4\3\2\2\2\u02bf\u02c0\7\b\2\2\u02c0\u02c1")
        buf.write("\5\u015c\u00af\2\u02c1\u02c2\5\u00a6T\2\u02c2\u02c4\3")
        buf.write("\2\2\2\u02c3\u02bb\3\2\2\2\u02c3\u02bf\3\2\2\2\u02c4\33")
        buf.write("\3\2\2\2\u02c5\u02c6\7\t\2\2\u02c6\u02c7\5\u0096L\2\u02c7")
        buf.write("\u02c8\7\6\2\2\u02c8\u02c9\5\u017e\u00c0\2\u02c9\35\3")
        buf.write("\2\2\2\u02ca\u02ce\5 \21\2\u02cb\u02ce\5$\23\2\u02cc\u02ce")
        buf.write("\5&\24\2\u02cd\u02ca\3\2\2\2\u02cd\u02cb\3\2\2\2\u02cd")
        buf.write("\u02cc\3\2\2\2\u02ce\37\3\2\2\2\u02cf\u02d0\7\n\2\2\u02d0")
        buf.write("\u02d1\5\24\13\2\u02d1\u02d3\5\u0096L\2\u02d2\u02d4\5")
        buf.write("\"\22\2\u02d3\u02d2\3\2\2\2\u02d3\u02d4\3\2\2\2\u02d4")
        buf.write("!\3\2\2\2\u02d5\u02d6\7\13\2\2\u02d6\u02da\5\u0096L\2")
        buf.write("\u02d7\u02d8\7\13\2\2\u02d8\u02da\5 \21\2\u02d9\u02d5")
        buf.write("\3\2\2\2\u02d9\u02d7\3\2\2\2\u02da#\3\2\2\2\u02db\u02dc")
        buf.write("\7\f\2\2\u02dc\u02dd\5\24\13\2\u02dd\u02de\7\13\2\2\u02de")
        buf.write("\u02df\5\u0096L\2\u02df%\3\2\2\2\u02e0\u02e1\7\r\2\2\u02e1")
        buf.write("\u02e2\5\u017e\u00c0\2\u02e2\u02e4\7\u0087\2\2\u02e3\u02e5")
        buf.write("\5(\25\2\u02e4\u02e3\3\2\2\2\u02e4\u02e5\3\2\2\2\u02e5")
        buf.write("\u02e6\3\2\2\2\u02e6\u02e7\7\u008a\2\2\u02e7\'\3\2\2\2")
        buf.write("\u02e8\u02ea\5*\26\2\u02e9\u02eb\5(\25\2\u02ea\u02e9\3")
        buf.write("\2\2\2\u02ea\u02eb\3\2\2\2\u02eb)\3\2\2\2\u02ec\u02ed")
        buf.write("\5,\27\2\u02ed\u02ee\5\6\4\2\u02ee\u02f3\3\2\2\2\u02ef")
        buf.write("\u02f0\5\60\31\2\u02f0\u02f1\5\6\4\2\u02f1\u02f3\3\2\2")
        buf.write("\2\u02f2\u02ec\3\2\2\2\u02f2\u02ef\3\2\2\2\u02f3+\3\2")
        buf.write("\2\2\u02f4\u02f5\7\4\2\2\u02f5\u02f6\5.\30\2\u02f6\u02f7")
        buf.write("\7\u008e\2\2\u02f7-\3\2\2\2\u02f8\u02fa\5\u015c\u00af")
        buf.write("\2\u02f9\u02fb\5\62\32\2\u02fa\u02f9\3\2\2\2\u02fa\u02fb")
        buf.write("\3\2\2\2\u02fb\u0304\3\2\2\2\u02fc\u02fe\5\u015c\u00af")
        buf.write("\2\u02fd\u02ff\5\62\32\2\u02fe\u02fd\3\2\2\2\u02fe\u02ff")
        buf.write("\3\2\2\2\u02ff\u0300\3\2\2\2\u0300\u0301\7\u008d\2\2\u0301")
        buf.write("\u0302\5.\30\2\u0302\u0304\3\2\2\2\u0303\u02f8\3\2\2\2")
        buf.write("\u0303\u02fc\3\2\2\2\u0304/\3\2\2\2\u0305\u0306\7\16\2")
        buf.write("\2\u0306\u0307\7\u008e\2\2\u0307\61\3\2\2\2\u0308\u0309")
        buf.write("\7\17\2\2\u0309\u030a\5\64\33\2\u030a\63\3\2\2\2\u030b")
        buf.write("\u030c\5\u017e\u00c0\2\u030c\65\3\2\2\2\u030d\u030e\5")
        buf.write("8\35\2\u030e\u030f\5\n\6\2\u030f\u031a\3\2\2\2\u0310\u0311")
        buf.write("\58\35\2\u0311\u0312\5 \21\2\u0312\u031a\3\2\2\2\u0313")
        buf.write("\u0314\58\35\2\u0314\u0315\5&\24\2\u0315\u031a\3\2\2\2")
        buf.write("\u0316\u0317\58\35\2\u0317\u0318\5J&\2\u0318\u031a\3\2")
        buf.write("\2\2\u0319\u030d\3\2\2\2\u0319\u0310\3\2\2\2\u0319\u0313")
        buf.write("\3\2\2\2\u0319\u0316\3\2\2\2\u031a\67\3\2\2\2\u031b\u031c")
        buf.write("\5:\36\2\u031c\u031d\7\u008e\2\2\u031d9\3\2\2\2\u031e")
        buf.write("\u031f\5\u0208\u0105\2\u031f;\3\2\2\2\u0320\u0326\5> ")
        buf.write("\2\u0321\u0326\5@!\2\u0322\u0326\5B\"\2\u0323\u0326\5")
        buf.write("D#\2\u0324\u0326\5F$\2\u0325\u0320\3\2\2\2\u0325\u0321")
        buf.write("\3\2\2\2\u0325\u0322\3\2\2\2\u0325\u0323\3\2\2\2\u0325")
        buf.write("\u0324\3\2\2\2\u0326=\3\2\2\2\u0327\u0329\7\20\2\2\u0328")
        buf.write("\u032a\5:\36\2\u0329\u0328\3\2\2\2\u0329\u032a\3\2\2\2")
        buf.write("\u032a?\3\2\2\2\u032b\u032d\7\21\2\2\u032c\u032e\5:\36")
        buf.write("\2\u032d\u032c\3\2\2\2\u032d\u032e\3\2\2\2\u032eA\3\2")
        buf.write("\2\2\u032f\u0330\7\22\2\2\u0330C\3\2\2\2\u0331\u0333\7")
        buf.write("\23\2\2\u0332\u0334\5\u017e\u00c0\2\u0333\u0332\3\2\2")
        buf.write("\2\u0333\u0334\3\2\2\2\u0334E\3\2\2\2\u0335\u0336\7\24")
        buf.write("\2\2\u0336\u0337\5\u017e\u00c0\2\u0337G\3\2\2\2\u0338")
        buf.write("\u0339\7\25\2\2\u0339\u033a\5\u0096L\2\u033aI\3\2\2\2")
        buf.write("\u033b\u033c\7\26\2\2\u033c\u033e\5\u0096L\2\u033d\u033f")
        buf.write("\5L\'\2\u033e\u033d\3\2\2\2\u033e\u033f\3\2\2\2\u033f")
        buf.write("K\3\2\2\2\u0340\u0342\5N(\2\u0341\u0343\5L\'\2\u0342\u0341")
        buf.write("\3\2\2\2\u0342\u0343\3\2\2\2\u0343M\3\2\2\2\u0344\u0346")
        buf.write("\7\27\2\2\u0345\u0347\5\u015c\u00af\2\u0346\u0345\3\2")
        buf.write("\2\2\u0346\u0347\3\2\2\2\u0347\u0349\3\2\2\2\u0348\u034a")
        buf.write("\5\62\32\2\u0349\u0348\3\2\2\2\u0349\u034a\3\2\2\2\u034a")
        buf.write("\u034b\3\2\2\2\u034b\u034c\5\u0096L\2\u034cO\3\2\2\2\u034d")
        buf.write("\u0350\5R*\2\u034e\u0350\5n8\2\u034f\u034d\3\2\2\2\u034f")
        buf.write("\u034e\3\2\2\2\u0350Q\3\2\2\2\u0351\u0353\5T+\2\u0352")
        buf.write("\u0354\5V,\2\u0353\u0352\3\2\2\2\u0353\u0354\3\2\2\2\u0354")
        buf.write("\u0356\3\2\2\2\u0355\u0357\5Z.\2\u0356\u0355\3\2\2\2\u0356")
        buf.write("\u0357\3\2\2\2\u0357\u0358\3\2\2\2\u0358\u0359\5b\62\2")
        buf.write("\u0359S\3\2\2\2\u035a\u035b\5\\/\2\u035b\u035d\5d\63\2")
        buf.write("\u035c\u035e\5\6\4\2\u035d\u035c\3\2\2\2\u035d\u035e\3")
        buf.write("\2\2\2\u035eU\3\2\2\2\u035f\u0361\5X-\2\u0360\u035f\3")
        buf.write("\2\2\2\u0361\u0362\3\2\2\2\u0362\u0360\3\2\2\2\u0362\u0363")
        buf.write("\3\2\2\2\u0363W\3\2\2\2\u0364\u0365\5^\60\2\u0365\u0367")
        buf.write("\5d\63\2\u0366\u0368\5\6\4\2\u0367\u0366\3\2\2\2\u0367")
        buf.write("\u0368\3\2\2\2\u0368Y\3\2\2\2\u0369\u036b\5`\61\2\u036a")
        buf.write("\u036c\5\6\4\2\u036b\u036a\3\2\2\2\u036b\u036c\3\2\2\2")
        buf.write("\u036c[\3\2\2\2\u036d\u036e\7\30\2\2\u036e]\3\2\2\2\u036f")
        buf.write("\u0370\7\31\2\2\u0370_\3\2\2\2\u0371\u0372\7\32\2\2\u0372")
        buf.write("a\3\2\2\2\u0373\u0374\7\33\2\2\u0374c\3\2\2\2\u0375\u0376")
        buf.write("\b\63\1\2\u0376\u0380\5f\64\2\u0377\u0380\5\u020a\u0106")
        buf.write("\2\u0378\u0380\5\u0234\u011b\2\u0379\u037a\7\u0088\2\2")
        buf.write("\u037a\u037b\5d\63\2\u037b\u037c\7\u008b\2\2\u037c\u0380")
        buf.write("\3\2\2\2\u037d\u037e\7\u0093\2\2\u037e\u0380\5d\63\5\u037f")
        buf.write("\u0375\3\2\2\2\u037f\u0377\3\2\2\2\u037f\u0378\3\2\2\2")
        buf.write("\u037f\u0379\3\2\2\2\u037f\u037d\3\2\2\2\u0380\u038b\3")
        buf.write("\2\2\2\u0381\u0382\f\4\2\2\u0382\u0383\5\u0214\u010b\2")
        buf.write("\u0383\u0384\5d\63\5\u0384\u038a\3\2\2\2\u0385\u0386\f")
        buf.write("\3\2\2\u0386\u0387\5\u0216\u010c\2\u0387\u0388\5d\63\4")
        buf.write("\u0388\u038a\3\2\2\2\u0389\u0381\3\2\2\2\u0389\u0385\3")
        buf.write("\2\2\2\u038a\u038d\3\2\2\2\u038b\u0389\3\2\2\2\u038b\u038c")
        buf.write("\3\2\2\2\u038ce\3\2\2\2\u038d\u038b\3\2\2\2\u038e\u038f")
        buf.write("\7\34\2\2\u038f\u0390\7\u0088\2\2\u0390\u0391\5j\66\2")
        buf.write("\u0391\u0392\7\u008b\2\2\u0392\u039f\3\2\2\2\u0393\u0394")
        buf.write("\7\35\2\2\u0394\u0395\7\u0088\2\2\u0395\u0396\5l\67\2")
        buf.write("\u0396\u0397\7\u008b\2\2\u0397\u039f\3\2\2\2\u0398\u0399")
        buf.write("\7\36\2\2\u0399\u039a\7\u0088\2\2\u039a\u039b\5\u0218")
        buf.write("\u010d\2\u039b\u039c\5h\65\2\u039c\u039d\7\u008b\2\2\u039d")
        buf.write("\u039f\3\2\2\2\u039e\u038e\3\2\2\2\u039e\u0393\3\2\2\2")
        buf.write("\u039e\u0398\3\2\2\2\u039fg\3\2\2\2\u03a0\u03a1\7\u00a6")
        buf.write("\2\2\u03a1\u03a2\7\u0086\2\2\u03a2\u03a3\7\u00a6\2\2\u03a3")
        buf.write("i\3\2\2\2\u03a4\u03a5\5\u0208\u0105\2\u03a5k\3\2\2\2\u03a6")
        buf.write("\u03a7\5\u0208\u0105\2\u03a7m\3\2\2\2\u03a8\u03a9\7\37")
        buf.write("\2\2\u03a9\u03aa\7\u0088\2\2\u03aa\u03ab\7 \2\2\u03ab")
        buf.write("\u03ac\7\u008e\2\2\u03ac\u03ad\5r:\2\u03ad\u03ae\7\u008d")
        buf.write("\2\2\u03ae\u03af\7!\2\2\u03af\u03b0\7\u008e\2\2\u03b0")
        buf.write("\u03b1\5p9\2\u03b1\u03b2\7\u008b\2\2\u03b2\u03b7\3\2\2")
        buf.write("\2\u03b3\u03b4\7\37\2\2\u03b4\u03b5\7\u0088\2\2\u03b5")
        buf.write("\u03b7\7\u008b\2\2\u03b6\u03a8\3\2\2\2\u03b6\u03b3\3\2")
        buf.write("\2\2\u03b7o\3\2\2\2\u03b8\u03b9\5\u0238\u011d\2\u03b9")
        buf.write("q\3\2\2\2\u03ba\u03bb\7\u00a9\2\2\u03bbs\3\2\2\2\u03bc")
        buf.write("\u03bd\7\"\2\2\u03bd\u03be\7\u0088\2\2\u03be\u03bf\5v")
        buf.write("<\2\u03bf\u03c0\7\u008b\2\2\u03c0u\3\2\2\2\u03c1\u03c6")
        buf.write("\5x=\2\u03c2\u03c3\7\u008d\2\2\u03c3\u03c5\5x=\2\u03c4")
        buf.write("\u03c2\3\2\2\2\u03c5\u03c8\3\2\2\2\u03c6\u03c4\3\2\2\2")
        buf.write("\u03c6\u03c7\3\2\2\2\u03c7w\3\2\2\2\u03c8\u03c6\3\2\2")
        buf.write("\2\u03c9\u03ca\t\2\2\2\u03cay\3\2\2\2\u03cb\u03cc\7\u0090")
        buf.write("\2\2\u03cc\u03cd\5|?\2\u03cd\u03ce\7\u0091\2\2\u03ce{")
        buf.write("\3\2\2\2\u03cf\u03d4\5~@\2\u03d0\u03d1\7\u008d\2\2\u03d1")
        buf.write("\u03d3\5~@\2\u03d2\u03d0\3\2\2\2\u03d3\u03d6\3\2\2\2\u03d4")
        buf.write("\u03d2\3\2\2\2\u03d4\u03d5\3\2\2\2\u03d5}\3\2\2\2\u03d6")
        buf.write("\u03d4\3\2\2\2\u03d7\u03e1\5\u01e6\u00f4\2\u03d8\u03d9")
        buf.write("\5\u01e6\u00f4\2\u03d9\u03da\7\u008e\2\2\u03da\u03db\5")
        buf.write("\u01e4\u00f3\2\u03db\u03e1\3\2\2\2\u03dc\u03dd\5\u01e6")
        buf.write("\u00f4\2\u03dd\u03de\7\u008e\2\2\u03de\u03df\5\u01fe\u0100")
        buf.write("\2\u03df\u03e1\3\2\2\2\u03e0\u03d7\3\2\2\2\u03e0\u03d8")
        buf.write("\3\2\2\2\u03e0\u03dc\3\2\2\2\u03e1\177\3\2\2\2\u03e2\u03e3")
        buf.write("\7\17\2\2\u03e3\u03e4\5\u0082B\2\u03e4\u0081\3\2\2\2\u03e5")
        buf.write("\u03ea\5\u0084C\2\u03e6\u03e7\7\u008d\2\2\u03e7\u03e9")
        buf.write("\5\u0084C\2\u03e8\u03e6\3\2\2\2\u03e9\u03ec\3\2\2\2\u03ea")
        buf.write("\u03e8\3\2\2\2\u03ea\u03eb\3\2\2\2\u03eb\u0083\3\2\2\2")
        buf.write("\u03ec\u03ea\3\2\2\2\u03ed\u03f0\5\u0086D\2\u03ee\u03f0")
        buf.write("\5\u0088E\2\u03ef\u03ed\3\2\2\2\u03ef\u03ee\3\2\2\2\u03f0")
        buf.write("\u0085\3\2\2\2\u03f1\u03f2\5\u01e4\u00f3\2\u03f2\u03f3")
        buf.write("\7\u008e\2\2\u03f3\u03f4\5\u01e4\u00f3\2\u03f4\u03fa\3")
        buf.write("\2\2\2\u03f5\u03f6\5\u01e4\u00f3\2\u03f6\u03f7\7\u008e")
        buf.write("\2\2\u03f7\u03f8\5\u01fe\u0100\2\u03f8\u03fa\3\2\2\2\u03f9")
        buf.write("\u03f1\3\2\2\2\u03f9\u03f5\3\2\2\2\u03fa\u0087\3\2\2\2")
        buf.write("\u03fb\u03fc\5\u01e4\u00f3\2\u03fc\u03fd\5\u021e\u0110")
        buf.write("\2\u03fd\u03fe\5\u01e0\u00f1\2\u03fe\u0089\3\2\2\2\u03ff")
        buf.write("\u0400\7\u0090\2\2\u0400\u0401\5\u008cG\2\u0401\u0402")
        buf.write("\7\u0091\2\2\u0402\u008b\3\2\2\2\u0403\u0408\5\u008eH")
        buf.write("\2\u0404\u0405\7\u008d\2\2\u0405\u0407\5\u008eH\2\u0406")
        buf.write("\u0404\3\2\2\2\u0407\u040a\3\2\2\2\u0408\u0406\3\2\2\2")
        buf.write("\u0408\u0409\3\2\2\2\u0409\u008d\3\2\2\2\u040a\u0408\3")
        buf.write("\2\2\2\u040b\u040c\5\u01e0\u00f1\2\u040c\u008f\3\2\2\2")
        buf.write("\u040d\u041e\5\u0098M\2\u040e\u041e\5\u00a0Q\2\u040f\u041e")
        buf.write("\5\u00a8U\2\u0410\u041e\5\u00c2b\2\u0411\u041e\5\u00c8")
        buf.write("e\2\u0412\u041e\5\u00e0q\2\u0413\u041e\5\u0102\u0082\2")
        buf.write("\u0414\u041e\5\u010a\u0086\2\u0415\u041e\5\u0112\u008a")
        buf.write("\2\u0416\u041e\5\u0126\u0094\2\u0417\u041e\5\u012c\u0097")
        buf.write("\2\u0418\u041e\5\u012e\u0098\2\u0419\u041e\5\u0134\u009b")
        buf.write("\2\u041a\u041e\5\u013a\u009e\2\u041b\u041e\5\u013a\u009e")
        buf.write("\2\u041c\u041e\5\u0144\u00a3\2\u041d\u040d\3\2\2\2\u041d")
        buf.write("\u040e\3\2\2\2\u041d\u040f\3\2\2\2\u041d\u0410\3\2\2\2")
        buf.write("\u041d\u0411\3\2\2\2\u041d\u0412\3\2\2\2\u041d\u0413\3")
        buf.write("\2\2\2\u041d\u0414\3\2\2\2\u041d\u0415\3\2\2\2\u041d\u0416")
        buf.write("\3\2\2\2\u041d\u0417\3\2\2\2\u041d\u0418\3\2\2\2\u041d")
        buf.write("\u0419\3\2\2\2\u041d\u041a\3\2\2\2\u041d\u041b\3\2\2\2")
        buf.write("\u041d\u041c\3\2\2\2\u041e\u0091\3\2\2\2\u041f\u0421\5")
        buf.write("\u0090I\2\u0420\u041f\3\2\2\2\u0421\u0422\3\2\2\2\u0422")
        buf.write("\u0420\3\2\2\2\u0422\u0423\3\2\2\2\u0423\u0093\3\2\2\2")
        buf.write("\u0424\u0426\5\6\4\2\u0425\u0424\3\2\2\2\u0425\u0426\3")
        buf.write("\2\2\2\u0426\u0095\3\2\2\2\u0427\u0429\7\u0087\2\2\u0428")
        buf.write("\u042a\5\6\4\2\u0429\u0428\3\2\2\2\u0429\u042a\3\2\2\2")
        buf.write("\u042a\u042b\3\2\2\2\u042b\u042c\7\u008a\2\2\u042c\u0097")
        buf.write("\3\2\2\2\u042d\u042f\5\u0176\u00bc\2\u042e\u042d\3\2\2")
        buf.write("\2\u042e\u042f\3\2\2\2\u042f\u0430\3\2\2\2\u0430\u0432")
        buf.write("\7#\2\2\u0431\u0433\5\u009aN\2\u0432\u0431\3\2\2\2\u0432")
        buf.write("\u0433\3\2\2\2\u0433\u0434\3\2\2\2\u0434\u0435\5\u009c")
        buf.write("O\2\u0435\u0099\3\2\2\2\u0436\u0437\t\3\2\2\u0437\u009b")
        buf.write("\3\2\2\2\u0438\u043d\5\u009eP\2\u0439\u043a\7\u0086\2")
        buf.write("\2\u043a\u043c\5\u009eP\2\u043b\u0439\3\2\2\2\u043c\u043f")
        buf.write("\3\2\2\2\u043d\u043b\3\2\2\2\u043d\u043e\3\2\2\2\u043e")
        buf.write("\u009d\3\2\2\2\u043f\u043d\3\2\2\2\u0440\u0443\5\u0208")
        buf.write("\u0105\2\u0441\u0443\5\u0226\u0114\2\u0442\u0440\3\2\2")
        buf.write("\2\u0442\u0441\3\2\2\2\u0443\u009f\3\2\2\2\u0444\u0446")
        buf.write("\5\u0176\u00bc\2\u0445\u0444\3\2\2\2\u0445\u0446\3\2\2")
        buf.write("\2\u0446\u0448\3\2\2\2\u0447\u0449\5\u0156\u00ac\2\u0448")
        buf.write("\u0447\3\2\2\2\u0448\u0449\3\2\2\2\u0449\u044a\3\2\2\2")
        buf.write("\u044a\u044b\7\7\2\2\u044b\u044c\5\u00a2R\2\u044c\u00a1")
        buf.write("\3\2\2\2\u044d\u0452\5\u00a4S\2\u044e\u044f\7\u008d\2")
        buf.write("\2\u044f\u0451\5\u00a4S\2\u0450\u044e\3\2\2\2\u0451\u0454")
        buf.write("\3\2\2\2\u0452\u0450\3\2\2\2\u0452\u0453\3\2\2\2\u0453")
        buf.write("\u00a3\3\2\2\2\u0454\u0452\3\2\2\2\u0455\u0457\5\u015c")
        buf.write("\u00af\2\u0456\u0458\5\u00a6T\2\u0457\u0456\3\2\2\2\u0457")
        buf.write("\u0458\3\2\2\2\u0458\u00a5\3\2\2\2\u0459\u045a\5\u0210")
        buf.write("\u0109\2\u045a\u045b\5\u017e\u00c0\2\u045b\u00a7\3\2\2")
        buf.write("\2\u045c\u045d\5\u00aaV\2\u045d\u045e\5\u00acW\2\u045e")
        buf.write("\u045f\5\u01e2\u00f2\2\u045f\u0460\5\u0096L\2\u0460\u0480")
        buf.write("\3\2\2\2\u0461\u0462\5\u00aaV\2\u0462\u0463\5\u00acW\2")
        buf.write("\u0463\u0464\5\u01e2\u00f2\2\u0464\u0465\5\u00aeX\2\u0465")
        buf.write("\u0480\3\2\2\2\u0466\u0467\5\u00aaV\2\u0467\u0468\5\u00ac")
        buf.write("W\2\u0468\u0469\5\u01e2\u00f2\2\u0469\u046a\5\u00b6\\")
        buf.write("\2\u046a\u0480\3\2\2\2\u046b\u046c\5\u00aaV\2\u046c\u046d")
        buf.write("\5\u00acW\2\u046d\u046f\5\u01e2\u00f2\2\u046e\u0470\5")
        buf.write("\u00a6T\2\u046f\u046e\3\2\2\2\u046f\u0470\3\2\2\2\u0470")
        buf.write("\u0471\3\2\2\2\u0471\u0472\5\u00bc_\2\u0472\u0480\3\2")
        buf.write("\2\2\u0473\u0474\5\u00aaV\2\u0474\u0475\5\u00acW\2\u0475")
        buf.write("\u0476\5\u01e2\u00f2\2\u0476\u0478\5\u01e2\u00f2\2\u0477")
        buf.write("\u0479\5\u00a6T\2\u0478\u0477\3\2\2\2\u0478\u0479\3\2")
        buf.write("\2\2\u0479\u047a\3\2\2\2\u047a\u047b\5\u00bc_\2\u047b")
        buf.write("\u0480\3\2\2\2\u047c\u047d\5\u00aaV\2\u047d\u047e\5\u00a2")
        buf.write("R\2\u047e\u0480\3\2\2\2\u047f\u045c\3\2\2\2\u047f\u0461")
        buf.write("\3\2\2\2\u047f\u0466\3\2\2\2\u047f\u046b\3\2\2\2\u047f")
        buf.write("\u0473\3\2\2\2\u047f\u047c\3\2\2\2\u0480\u00a9\3\2\2\2")
        buf.write("\u0481\u0483\5\u0176\u00bc\2\u0482\u0481\3\2\2\2\u0482")
        buf.write("\u0483\3\2\2\2\u0483\u0485\3\2\2\2\u0484\u0486\5\u0156")
        buf.write("\u00ac\2\u0485\u0484\3\2\2\2\u0485\u0486\3\2\2\2\u0486")
        buf.write("\u0487\3\2\2\2\u0487\u0488\7\b\2\2\u0488\u00ab\3\2\2\2")
        buf.write("\u0489\u048a\5\u0208\u0105\2\u048a\u00ad\3\2\2\2\u048b")
        buf.write("\u048c\7\u0087\2\2\u048c\u048e\5\u00b0Y\2\u048d\u048f")
        buf.write("\5\u00b2Z\2\u048e\u048d\3\2\2\2\u048e\u048f\3\2\2\2\u048f")
        buf.write("\u0490\3\2\2\2\u0490\u0491\7\u008a\2\2\u0491\u0498\3\2")
        buf.write("\2\2\u0492\u0493\7\u0087\2\2\u0493\u0494\5\u00b2Z\2\u0494")
        buf.write("\u0495\5\u00b0Y\2\u0495\u0496\7\u008a\2\2\u0496\u0498")
        buf.write("\3\2\2\2\u0497\u048b\3\2\2\2\u0497\u0492\3\2\2\2\u0498")
        buf.write("\u00af\3\2\2\2\u0499\u049b\5\u0176\u00bc\2\u049a\u0499")
        buf.write("\3\2\2\2\u049a\u049b\3\2\2\2\u049b\u049d\3\2\2\2\u049c")
        buf.write("\u049e\5\u015a\u00ae\2\u049d\u049c\3\2\2\2\u049d\u049e")
        buf.write("\3\2\2\2\u049e\u049f\3\2\2\2\u049f\u04a0\7*\2\2\u04a0")
        buf.write("\u04a1\5\u0096L\2\u04a1\u00b1\3\2\2\2\u04a2\u04a4\5\u0176")
        buf.write("\u00bc\2\u04a3\u04a2\3\2\2\2\u04a3\u04a4\3\2\2\2\u04a4")
        buf.write("\u04a6\3\2\2\2\u04a5\u04a7\5\u015a\u00ae\2\u04a6\u04a5")
        buf.write("\3\2\2\2\u04a6\u04a7\3\2\2\2\u04a7\u04a8\3\2\2\2\u04a8")
        buf.write("\u04aa\7+\2\2\u04a9\u04ab\5\u00b4[\2\u04aa\u04a9\3\2\2")
        buf.write("\2\u04aa\u04ab\3\2\2\2\u04ab\u04ac\3\2\2\2\u04ac\u04ad")
        buf.write("\5\u0096L\2\u04ad\u00b3\3\2\2\2\u04ae\u04af\7\u0088\2")
        buf.write("\2\u04af\u04b0\5\u0208\u0105\2\u04b0\u04b1\7\u008b\2\2")
        buf.write("\u04b1\u00b5\3\2\2\2\u04b2\u04b3\7\u0087\2\2\u04b3\u04b5")
        buf.write("\5\u00b8]\2\u04b4\u04b6\5\u00ba^\2\u04b5\u04b4\3\2\2\2")
        buf.write("\u04b5\u04b6\3\2\2\2\u04b6\u04b7\3\2\2\2\u04b7\u04b8\7")
        buf.write("\u008a\2\2\u04b8\u04bf\3\2\2\2\u04b9\u04ba\7\u0087\2\2")
        buf.write("\u04ba\u04bb\5\u00ba^\2\u04bb\u04bc\5\u00b8]\2\u04bc\u04bd")
        buf.write("\7\u008a\2\2\u04bd\u04bf\3\2\2\2\u04be\u04b2\3\2\2\2\u04be")
        buf.write("\u04b9\3\2\2\2\u04bf\u00b7\3\2\2\2\u04c0\u04c2\5\u0176")
        buf.write("\u00bc\2\u04c1\u04c0\3\2\2\2\u04c1\u04c2\3\2\2\2\u04c2")
        buf.write("\u04c4\3\2\2\2\u04c3\u04c5\5\u015a\u00ae\2\u04c4\u04c3")
        buf.write("\3\2\2\2\u04c4\u04c5\3\2\2\2\u04c5\u04c6\3\2\2\2\u04c6")
        buf.write("\u04c7\7*\2\2\u04c7\u00b9\3\2\2\2\u04c8\u04ca\5\u0176")
        buf.write("\u00bc\2\u04c9\u04c8\3\2\2\2\u04c9\u04ca\3\2\2\2\u04ca")
        buf.write("\u04cc\3\2\2\2\u04cb\u04cd\5\u015a\u00ae\2\u04cc\u04cb")
        buf.write("\3\2\2\2\u04cc\u04cd\3\2\2\2\u04cd\u04ce\3\2\2\2\u04ce")
        buf.write("\u04cf\7+\2\2\u04cf\u00bb\3\2\2\2\u04d0\u04d1\7\u0087")
        buf.write("\2\2\u04d1\u04d3\5\u00be`\2\u04d2\u04d4\5\u00c0a\2\u04d3")
        buf.write("\u04d2\3\2\2\2\u04d3\u04d4\3\2\2\2\u04d4\u04d5\3\2\2\2")
        buf.write("\u04d5\u04d6\7\u008a\2\2\u04d6\u04dd\3\2\2\2\u04d7\u04d8")
        buf.write("\7\u0087\2\2\u04d8\u04d9\5\u00c0a\2\u04d9\u04da\5\u00be")
        buf.write("`\2\u04da\u04db\7\u008a\2\2\u04db\u04dd\3\2\2\2\u04dc")
        buf.write("\u04d0\3\2\2\2\u04dc\u04d7\3\2\2\2\u04dd\u00bd\3\2\2\2")
        buf.write("\u04de\u04e0\5\u0176\u00bc\2\u04df\u04de\3\2\2\2\u04df")
        buf.write("\u04e0\3\2\2\2\u04e0\u04e1\3\2\2\2\u04e1\u04e3\7,\2\2")
        buf.write("\u04e2\u04e4\5\u00b4[\2\u04e3\u04e2\3\2\2\2\u04e3\u04e4")
        buf.write("\3\2\2\2\u04e4\u04e5\3\2\2\2\u04e5\u04e6\5\u0096L\2\u04e6")
        buf.write("\u00bf\3\2\2\2\u04e7\u04e9\5\u0176\u00bc\2\u04e8\u04e7")
        buf.write("\3\2\2\2\u04e8\u04e9\3\2\2\2\u04e9\u04ea\3\2\2\2\u04ea")
        buf.write("\u04ec\7-\2\2\u04eb\u04ed\5\u00b4[\2\u04ec\u04eb\3\2\2")
        buf.write("\2\u04ec\u04ed\3\2\2\2\u04ed\u04ee\3\2\2\2\u04ee\u04ef")
        buf.write("\5\u0096L\2\u04ef\u00c1\3\2\2\2\u04f0\u04f2\5\u0176\u00bc")
        buf.write("\2\u04f1\u04f0\3\2\2\2\u04f1\u04f2\3\2\2\2\u04f2\u04f4")
        buf.write("\3\2\2\2\u04f3\u04f5\5\u0158\u00ad\2\u04f4\u04f3\3\2\2")
        buf.write("\2\u04f4\u04f5\3\2\2\2\u04f5\u04f6\3\2\2\2\u04f6\u04f7")
        buf.write("\7$\2\2\u04f7\u04f9\5\u00c4c\2\u04f8\u04fa\5z>\2\u04f9")
        buf.write("\u04f8\3\2\2\2\u04f9\u04fa\3\2\2\2\u04fa\u04fb\3\2\2\2")
        buf.write("\u04fb\u04fc\5\u00c6d\2\u04fc\u00c3\3\2\2\2\u04fd\u04fe")
        buf.write("\5\u0208\u0105\2\u04fe\u00c5\3\2\2\2\u04ff\u0500\5\u0210")
        buf.write("\u0109\2\u0500\u0501\5\u01e0\u00f1\2\u0501\u00c7\3\2\2")
        buf.write("\2\u0502\u0503\5\u00caf\2\u0503\u0505\5\u00ccg\2\u0504")
        buf.write("\u0506\5z>\2\u0505\u0504\3\2\2\2\u0505\u0506\3\2\2\2\u0506")
        buf.write("\u0507\3\2\2\2\u0507\u0509\5\u00ceh\2\u0508\u050a\5\u0080")
        buf.write("A\2\u0509\u0508\3\2\2\2\u0509\u050a\3\2\2\2\u050a\u050c")
        buf.write("\3\2\2\2\u050b\u050d\5\u00d2j\2\u050c\u050b\3\2\2\2\u050c")
        buf.write("\u050d\3\2\2\2\u050d\u00c9\3\2\2\2\u050e\u0510\5\u0176")
        buf.write("\u00bc\2\u050f\u050e\3\2\2\2\u050f\u0510\3\2\2\2\u0510")
        buf.write("\u0512\3\2\2\2\u0511\u0513\5\u0156\u00ac\2\u0512\u0511")
        buf.write("\3\2\2\2\u0512\u0513\3\2\2\2\u0513\u0514\3\2\2\2\u0514")
        buf.write("\u0515\7)\2\2\u0515\u00cb\3\2\2\2\u0516\u0519\5\u0208")
        buf.write("\u0105\2\u0517\u0519\5\u0226\u0114\2\u0518\u0516\3\2\2")
        buf.write("\2\u0518\u0517\3\2\2\2\u0519\u00cd\3\2\2\2\u051a\u051c")
        buf.write("\5\u00d4k\2\u051b\u051d\7.\2\2\u051c\u051b\3\2\2\2\u051c")
        buf.write("\u051d\3\2\2\2\u051d\u051f\3\2\2\2\u051e\u0520\5\u00d0")
        buf.write("i\2\u051f\u051e\3\2\2\2\u051f\u0520\3\2\2\2\u0520\u0527")
        buf.write("\3\2\2\2\u0521\u0522\5\u00d4k\2\u0522\u0524\7/\2\2\u0523")
        buf.write("\u0525\5\u00d0i\2\u0524\u0523\3\2\2\2\u0524\u0525\3\2")
        buf.write("\2\2\u0525\u0527\3\2\2\2\u0526\u051a\3\2\2\2\u0526\u0521")
        buf.write("\3\2\2\2\u0527\u00cf\3\2\2\2\u0528\u052a\5\u021a\u010e")
        buf.write("\2\u0529\u052b\5\u0176\u00bc\2\u052a\u0529\3\2\2\2\u052a")
        buf.write("\u052b\3\2\2\2\u052b\u052c\3\2\2\2\u052c\u052d\5\u01e0")
        buf.write("\u00f1\2\u052d\u00d1\3\2\2\2\u052e\u052f\5\u0096L\2\u052f")
        buf.write("\u00d3\3\2\2\2\u0530\u0531\7\u0088\2\2\u0531\u0537\7\u008b")
        buf.write("\2\2\u0532\u0533\7\u0088\2\2\u0533\u0534\5\u00d6l\2\u0534")
        buf.write("\u0535\7\u008b\2\2\u0535\u0537\3\2\2\2\u0536\u0530\3\2")
        buf.write("\2\2\u0536\u0532\3\2\2\2\u0537\u00d5\3\2\2\2\u0538\u053d")
        buf.write("\5\u00d8m\2\u0539\u053a\7\u008d\2\2\u053a\u053c\5\u00d8")
        buf.write("m\2\u053b\u0539\3\2\2\2\u053c\u053f\3\2\2\2\u053d\u053b")
        buf.write("\3\2\2\2\u053d\u053e\3\2\2\2\u053e\u00d7\3\2\2\2\u053f")
        buf.write("\u053d\3\2\2\2\u0540\u0542\5\u00dan\2\u0541\u0540\3\2")
        buf.write("\2\2\u0541\u0542\3\2\2\2\u0542\u0543\3\2\2\2\u0543\u0544")
        buf.write("\5\u00dco\2\u0544\u0546\5\u01e2\u00f2\2\u0545\u0547\5")
        buf.write("\u00dep\2\u0546\u0545\3\2\2\2\u0546\u0547\3\2\2\2\u0547")
        buf.write("\u0556\3\2\2\2\u0548\u054a\5\u00dan\2\u0549\u0548\3\2")
        buf.write("\2\2\u0549\u054a\3\2\2\2\u054a\u054b\3\2\2\2\u054b\u054c")
        buf.write("\5\u00dco\2\u054c\u054d\5\u01e2\u00f2\2\u054d\u0556\3")
        buf.write("\2\2\2\u054e\u0550\5\u00dan\2\u054f\u054e\3\2\2\2\u054f")
        buf.write("\u0550\3\2\2\2\u0550\u0551\3\2\2\2\u0551\u0552\5\u00dc")
        buf.write("o\2\u0552\u0553\5\u01e2\u00f2\2\u0553\u0554\5\u021c\u010f")
        buf.write("\2\u0554\u0556\3\2\2\2\u0555\u0541\3\2\2\2\u0555\u0549")
        buf.write("\3\2\2\2\u0555\u054f\3\2\2\2\u0556\u00d9\3\2\2\2\u0557")
        buf.write("\u0558\5\u020a\u0106\2\u0558\u00db\3\2\2\2\u0559\u055a")
        buf.write("\5\u020a\u0106\2\u055a\u00dd\3\2\2\2\u055b\u055c\5\u0210")
        buf.write("\u0109\2\u055c\u055d\5\u017e\u00c0\2\u055d\u00df\3\2\2")
        buf.write("\2\u055e\u0560\5\u0176\u00bc\2\u055f\u055e\3\2\2\2\u055f")
        buf.write("\u0560\3\2\2\2\u0560\u0562\3\2\2\2\u0561\u0563\5\u0158")
        buf.write("\u00ad\2\u0562\u0561\3\2\2\2\u0562\u0563\3\2\2\2\u0563")
        buf.write("\u0564\3\2\2\2\u0564\u056d\5\u00e2r\2\u0565\u0567\5\u0176")
        buf.write("\u00bc\2\u0566\u0565\3\2\2\2\u0566\u0567\3\2\2\2\u0567")
        buf.write("\u0569\3\2\2\2\u0568\u056a\5\u0158\u00ad\2\u0569\u0568")
        buf.write("\3\2\2\2\u0569\u056a\3\2\2\2\u056a\u056b\3\2\2\2\u056b")
        buf.write("\u056d\5\u00f2z\2\u056c\u055f\3\2\2\2\u056c\u0566\3\2")
        buf.write("\2\2\u056d\u00e1\3\2\2\2\u056e\u0570\7\60\2\2\u056f\u056e")
        buf.write("\3\2\2\2\u056f\u0570\3\2\2\2\u0570\u0571\3\2\2\2\u0571")
        buf.write("\u0572\7\'\2\2\u0572\u0574\5\u00eex\2\u0573\u0575\5z>")
        buf.write("\2\u0574\u0573\3\2\2\2\u0574\u0575\3\2\2\2\u0575\u0577")
        buf.write("\3\2\2\2\u0576\u0578\5\u0202\u0102\2\u0577\u0576\3\2\2")
        buf.write("\2\u0577\u0578\3\2\2\2\u0578\u057a\3\2\2\2\u0579\u057b")
        buf.write("\5\u0080A\2\u057a\u0579\3\2\2\2\u057a\u057b\3\2\2\2\u057b")
        buf.write("\u057c\3\2\2\2\u057c\u057e\7\u0087\2\2\u057d\u057f\5\u00e4")
        buf.write("s\2\u057e\u057d\3\2\2\2\u057e\u057f\3\2\2\2\u057f\u0580")
        buf.write("\3\2\2\2\u0580\u0581\7\u008a\2\2\u0581\u00e3\3\2\2\2\u0582")
        buf.write("\u0584\5\u00e6t\2\u0583\u0585\5\u00e4s\2\u0584\u0583\3")
        buf.write("\2\2\2\u0584\u0585\3\2\2\2\u0585\u00e5\3\2\2\2\u0586\u058a")
        buf.write("\5\u0090I\2\u0587\u058a\5\u00e8u\2\u0588\u058a\5P)\2\u0589")
        buf.write("\u0586\3\2\2\2\u0589\u0587\3\2\2\2\u0589\u0588\3\2\2\2")
        buf.write("\u058a\u00e7\3\2\2\2\u058b\u058d\5\u0176\u00bc\2\u058c")
        buf.write("\u058b\3\2\2\2\u058c\u058d\3\2\2\2\u058d\u058f\3\2\2\2")
        buf.write("\u058e\u0590\7\60\2\2\u058f\u058e\3\2\2\2\u058f\u0590")
        buf.write("\3\2\2\2\u0590\u0591\3\2\2\2\u0591\u0592\7\4\2\2\u0592")
        buf.write("\u0593\5\u00eav\2\u0593\u00e9\3\2\2\2\u0594\u059a\5\u00ec")
        buf.write("w\2\u0595\u0596\5\u00ecw\2\u0596\u0597\7\u008d\2\2\u0597")
        buf.write("\u0598\5\u00eav\2\u0598\u059a\3\2\2\2\u0599\u0594\3\2")
        buf.write("\2\2\u0599\u0595\3\2\2\2\u059a\u00eb\3\2\2\2\u059b\u059d")
        buf.write("\5\u00f0y\2\u059c\u059e\5\u01e8\u00f5\2\u059d\u059c\3")
        buf.write("\2\2\2\u059d\u059e\3\2\2\2\u059e\u00ed\3\2\2\2\u059f\u05a0")
        buf.write("\5\u0208\u0105\2\u05a0\u00ef\3\2\2\2\u05a1\u05a2\5\u0208")
        buf.write("\u0105\2\u05a2\u00f1\3\2\2\2\u05a3\u05a4\7\'\2\2\u05a4")
        buf.write("\u05a6\5\u00eex\2\u05a5\u05a7\5z>\2\u05a6\u05a5\3\2\2")
        buf.write("\2\u05a6\u05a7\3\2\2\2\u05a7\u05a8\3\2\2\2\u05a8\u05aa")
        buf.write("\5\u0202\u0102\2\u05a9\u05ab\5\u0080A\2\u05aa\u05a9\3")
        buf.write("\2\2\2\u05aa\u05ab\3\2\2\2\u05ab\u05ac\3\2\2\2\u05ac\u05ad")
        buf.write("\7\u0087\2\2\u05ad\u05ae\5\u00f4{\2\u05ae\u05af\7\u008a")
        buf.write("\2\2\u05af\u00f3\3\2\2\2\u05b0\u05b2\5\u00f6|\2\u05b1")
        buf.write("\u05b3\5\u00f4{\2\u05b2\u05b1\3\2\2\2\u05b2\u05b3\3\2")
        buf.write("\2\2\u05b3\u00f5\3\2\2\2\u05b4\u05b8\5\u0090I\2\u05b5")
        buf.write("\u05b8\5\u00f8}\2\u05b6\u05b8\5P)\2\u05b7\u05b4\3\2\2")
        buf.write("\2\u05b7\u05b5\3\2\2\2\u05b7\u05b6\3\2\2\2\u05b8\u00f7")
        buf.write("\3\2\2\2\u05b9\u05bb\5\u0176\u00bc\2\u05ba\u05b9\3\2\2")
        buf.write("\2\u05ba\u05bb\3\2\2\2\u05bb\u05bc\3\2\2\2\u05bc\u05bd")
        buf.write("\7\4\2\2\u05bd\u05be\5\u00fa~\2\u05be\u00f9\3\2\2\2\u05bf")
        buf.write("\u05c5\5\u00fc\177\2\u05c0\u05c1\5\u00fc\177\2\u05c1\u05c2")
        buf.write("\7\u008d\2\2\u05c2\u05c3\5\u00fa~\2\u05c3\u05c5\3\2\2")
        buf.write("\2\u05c4\u05bf\3\2\2\2\u05c4\u05c0\3\2\2\2\u05c5\u00fb")
        buf.write("\3\2\2\2\u05c6\u05c8\5\u00f0y\2\u05c7\u05c9\5\u00fe\u0080")
        buf.write("\2\u05c8\u05c7\3\2\2\2\u05c8\u05c9\3\2\2\2\u05c9\u00fd")
        buf.write("\3\2\2\2\u05ca\u05cb\5\u0210\u0109\2\u05cb\u05cc\5\u0100")
        buf.write("\u0081\2\u05cc\u00ff\3\2\2\2\u05cd\u05d1\5\u0232\u011a")
        buf.write("\2\u05ce\u05d1\7\u00a9\2\2\u05cf\u05d1\5\u0234\u011b\2")
        buf.write("\u05d0\u05cd\3\2\2\2\u05d0\u05ce\3\2\2\2\u05d0\u05cf\3")
        buf.write("\2\2\2\u05d1\u0101\3\2\2\2\u05d2\u05d4\5\u0176\u00bc\2")
        buf.write("\u05d3\u05d2\3\2\2\2\u05d3\u05d4\3\2\2\2\u05d4\u05d6\3")
        buf.write("\2\2\2\u05d5\u05d7\5\u0158\u00ad\2\u05d6\u05d5\3\2\2\2")
        buf.write("\u05d6\u05d7\3\2\2\2\u05d7\u05d8\3\2\2\2\u05d8\u05d9\7")
        buf.write("%\2\2\u05d9\u05db\5\u0104\u0083\2\u05da\u05dc\5z>\2\u05db")
        buf.write("\u05da\3\2\2\2\u05db\u05dc\3\2\2\2\u05dc\u05de\3\2\2\2")
        buf.write("\u05dd\u05df\5\u0202\u0102\2\u05de\u05dd\3\2\2\2\u05de")
        buf.write("\u05df\3\2\2\2\u05df\u05e1\3\2\2\2\u05e0\u05e2\5\u0080")
        buf.write("A\2\u05e1\u05e0\3\2\2\2\u05e1\u05e2\3\2\2\2\u05e2\u05e3")
        buf.write("\3\2\2\2\u05e3\u05e4\5\u0106\u0084\2\u05e4\u0103\3\2\2")
        buf.write("\2\u05e5\u05e6\5\u0208\u0105\2\u05e6\u0105\3\2\2\2\u05e7")
        buf.write("\u05eb\7\u0087\2\2\u05e8\u05ea\5\u0108\u0085\2\u05e9\u05e8")
        buf.write("\3\2\2\2\u05ea\u05ed\3\2\2\2\u05eb\u05e9\3\2\2\2\u05eb")
        buf.write("\u05ec\3\2\2\2\u05ec\u05ee\3\2\2\2\u05ed\u05eb\3\2\2\2")
        buf.write("\u05ee\u05ef\7\u008a\2\2\u05ef\u0107\3\2\2\2\u05f0\u05f3")
        buf.write("\5\u0090I\2\u05f1\u05f3\5P)\2\u05f2\u05f0\3\2\2\2\u05f2")
        buf.write("\u05f1\3\2\2\2\u05f3\u0109\3\2\2\2\u05f4\u05f6\5\u0176")
        buf.write("\u00bc\2\u05f5\u05f4\3\2\2\2\u05f5\u05f6\3\2\2\2\u05f6")
        buf.write("\u05f8\3\2\2\2\u05f7\u05f9\5\u0158\u00ad\2\u05f8\u05f7")
        buf.write("\3\2\2\2\u05f8\u05f9\3\2\2\2\u05f9\u05fb\3\2\2\2\u05fa")
        buf.write("\u05fc\7\61\2\2\u05fb\u05fa\3\2\2\2\u05fb\u05fc\3\2\2")
        buf.write("\2\u05fc\u05fd\3\2\2\2\u05fd\u05fe\7&\2\2\u05fe\u0600")
        buf.write("\5\u010c\u0087\2\u05ff\u0601\5z>\2\u0600\u05ff\3\2\2\2")
        buf.write("\u0600\u0601\3\2\2\2\u0601\u0603\3\2\2\2\u0602\u0604\5")
        buf.write("\u0202\u0102\2\u0603\u0602\3\2\2\2\u0603\u0604\3\2\2\2")
        buf.write("\u0604\u0606\3\2\2\2\u0605\u0607\5\u0080A\2\u0606\u0605")
        buf.write("\3\2\2\2\u0606\u0607\3\2\2\2\u0607\u0608\3\2\2\2\u0608")
        buf.write("\u0609\5\u010e\u0088\2\u0609\u0622\3\2\2\2\u060a\u060c")
        buf.write("\5\u0176\u00bc\2\u060b\u060a\3\2\2\2\u060b\u060c\3\2\2")
        buf.write("\2\u060c\u060e\3\2\2\2\u060d\u060f\5\u0158\u00ad\2\u060e")
        buf.write("\u060d\3\2\2\2\u060e\u060f\3\2\2\2\u060f\u0610\3\2\2\2")
        buf.write("\u0610\u0612\7\61\2\2\u0611\u0613\5\u0158\u00ad\2\u0612")
        buf.write("\u0611\3\2\2\2\u0612\u0613\3\2\2\2\u0613\u0614\3\2\2\2")
        buf.write("\u0614\u0615\7&\2\2\u0615\u0617\5\u010c\u0087\2\u0616")
        buf.write("\u0618\5z>\2\u0617\u0616\3\2\2\2\u0617\u0618\3\2\2\2\u0618")
        buf.write("\u061a\3\2\2\2\u0619\u061b\5\u0202\u0102\2\u061a\u0619")
        buf.write("\3\2\2\2\u061a\u061b\3\2\2\2\u061b\u061d\3\2\2\2\u061c")
        buf.write("\u061e\5\u0080A\2\u061d\u061c\3\2\2\2\u061d\u061e\3\2")
        buf.write("\2\2\u061e\u061f\3\2\2\2\u061f\u0620\5\u010e\u0088\2\u0620")
        buf.write("\u0622\3\2\2\2\u0621\u05f5\3\2\2\2\u0621\u060b\3\2\2\2")
        buf.write("\u0622\u010b\3\2\2\2\u0623\u0624\5\u0208\u0105\2\u0624")
        buf.write("\u010d\3\2\2\2\u0625\u0629\7\u0087\2\2\u0626\u0628\5\u0110")
        buf.write("\u0089\2\u0627\u0626\3\2\2\2\u0628\u062b\3\2\2\2\u0629")
        buf.write("\u0627\3\2\2\2\u0629\u062a\3\2\2\2\u062a\u062c\3\2\2\2")
        buf.write("\u062b\u0629\3\2\2\2\u062c\u062d\7\u008a\2\2\u062d\u010f")
        buf.write("\3\2\2\2\u062e\u0631\5\u0090I\2\u062f\u0631\5P)\2\u0630")
        buf.write("\u062e\3\2\2\2\u0630\u062f\3\2\2\2\u0631\u0111\3\2\2\2")
        buf.write("\u0632\u0634\5\u0176\u00bc\2\u0633\u0632\3\2\2\2\u0633")
        buf.write("\u0634\3\2\2\2\u0634\u0636\3\2\2\2\u0635\u0637\5\u0158")
        buf.write("\u00ad\2\u0636\u0635\3\2\2\2\u0636\u0637\3\2\2\2\u0637")
        buf.write("\u0638\3\2\2\2\u0638\u0639\7(\2\2\u0639\u063b\5\u0114")
        buf.write("\u008b\2\u063a\u063c\5\u0202\u0102\2\u063b\u063a\3\2\2")
        buf.write("\2\u063b\u063c\3\2\2\2\u063c\u063d\3\2\2\2\u063d\u063e")
        buf.write("\5\u0116\u008c\2\u063e\u0113\3\2\2\2\u063f\u0640\5\u0208")
        buf.write("\u0105\2\u0640\u0115\3\2\2\2\u0641\u0645\7\u0087\2\2\u0642")
        buf.write("\u0644\5\u0118\u008d\2\u0643\u0642\3\2\2\2\u0644\u0647")
        buf.write("\3\2\2\2\u0645\u0643\3\2\2\2\u0645\u0646\3\2\2\2\u0646")
        buf.write("\u0648\3\2\2\2\u0647\u0645\3\2\2\2\u0648\u0649\7\u008a")
        buf.write("\2\2\u0649\u0117\3\2\2\2\u064a\u064d\5\u011a\u008e\2\u064b")
        buf.write("\u064d\5P)\2\u064c\u064a\3\2\2\2\u064c\u064b\3\2\2\2\u064d")
        buf.write("\u0119\3\2\2\2\u064e\u0655\5\u011c\u008f\2\u064f\u0655")
        buf.write("\5\u011e\u0090\2\u0650\u0655\5\u0120\u0091\2\u0651\u0655")
        buf.write("\5\u0122\u0092\2\u0652\u0655\5\u0124\u0093\2\u0653\u0655")
        buf.write("\5\u00c2b\2\u0654\u064e\3\2\2\2\u0654\u064f\3\2\2\2\u0654")
        buf.write("\u0650\3\2\2\2\u0654\u0651\3\2\2\2\u0654\u0652\3\2\2\2")
        buf.write("\u0654\u0653\3\2\2\2\u0655\u011b\3\2\2\2\u0656\u0657\5")
        buf.write("\u00aaV\2\u0657\u0658\5\u00acW\2\u0658\u0659\5\u01e2\u00f2")
        buf.write("\2\u0659\u065a\5\u00b6\\\2\u065a\u011d\3\2\2\2\u065b\u065c")
        buf.write("\5\u00caf\2\u065c\u065e\5\u00ccg\2\u065d\u065f\5z>\2\u065e")
        buf.write("\u065d\3\2\2\2\u065e\u065f\3\2\2\2\u065f\u0660\3\2\2\2")
        buf.write("\u0660\u0662\5\u00ceh\2\u0661\u0663\5\u0080A\2\u0662\u0661")
        buf.write("\3\2\2\2\u0662\u0663\3\2\2\2\u0663\u011f\3\2\2\2\u0664")
        buf.write("\u0666\5\u0128\u0095\2\u0665\u0667\5z>\2\u0666\u0665\3")
        buf.write("\2\2\2\u0666\u0667\3\2\2\2\u0667\u0668\3\2\2\2\u0668\u066a")
        buf.write("\5\u00d4k\2\u0669\u066b\7.\2\2\u066a\u0669\3\2\2\2\u066a")
        buf.write("\u066b\3\2\2\2\u066b\u066d\3\2\2\2\u066c\u066e\5\u0080")
        buf.write("A\2\u066d\u066c\3\2\2\2\u066d\u066e\3\2\2\2\u066e\u0679")
        buf.write("\3\2\2\2\u066f\u0671\5\u0128\u0095\2\u0670\u0672\5z>\2")
        buf.write("\u0671\u0670\3\2\2\2\u0671\u0672\3\2\2\2\u0672\u0673\3")
        buf.write("\2\2\2\u0673\u0674\5\u00d4k\2\u0674\u0676\7/\2\2\u0675")
        buf.write("\u0677\5\u0080A\2\u0676\u0675\3\2\2\2\u0676\u0677\3\2")
        buf.write("\2\2\u0677\u0679\3\2\2\2\u0678\u0664\3\2\2\2\u0678\u066f")
        buf.write("\3\2\2\2\u0679\u0121\3\2\2\2\u067a\u067b\5\u0136\u009c")
        buf.write("\2\u067b\u067c\5\u0138\u009d\2\u067c\u067d\5\u00b6\\\2")
        buf.write("\u067d\u0123\3\2\2\2\u067e\u0680\5\u0176\u00bc\2\u067f")
        buf.write("\u067e\3\2\2\2\u067f\u0680\3\2\2\2\u0680\u0682\3\2\2\2")
        buf.write("\u0681\u0683\5\u0158\u00ad\2\u0682\u0681\3\2\2\2\u0682")
        buf.write("\u0683\3\2\2\2\u0683\u0684\3\2\2\2\u0684\u0685\7\62\2")
        buf.write("\2\u0685\u0687\5\u00c4c\2\u0686\u0688\5\u0202\u0102\2")
        buf.write("\u0687\u0686\3\2\2\2\u0687\u0688\3\2\2\2\u0688\u068a\3")
        buf.write("\2\2\2\u0689\u068b\5\u00c6d\2\u068a\u0689\3\2\2\2\u068a")
        buf.write("\u068b\3\2\2\2\u068b\u0125\3\2\2\2\u068c\u068e\5\u0128")
        buf.write("\u0095\2\u068d\u068f\5z>\2\u068e\u068d\3\2\2\2\u068e\u068f")
        buf.write("\3\2\2\2\u068f\u0690\3\2\2\2\u0690\u0692\5\u00d4k\2\u0691")
        buf.write("\u0693\7.\2\2\u0692\u0691\3\2\2\2\u0692\u0693\3\2\2\2")
        buf.write("\u0693\u0695\3\2\2\2\u0694\u0696\5\u0080A\2\u0695\u0694")
        buf.write("\3\2\2\2\u0695\u0696\3\2\2\2\u0696\u0697\3\2\2\2\u0697")
        buf.write("\u0698\5\u012a\u0096\2\u0698\u06a5\3\2\2\2\u0699\u069b")
        buf.write("\5\u0128\u0095\2\u069a\u069c\5z>\2\u069b\u069a\3\2\2\2")
        buf.write("\u069b\u069c\3\2\2\2\u069c\u069d\3\2\2\2\u069d\u069e\5")
        buf.write("\u00d4k\2\u069e\u06a0\7/\2\2\u069f\u06a1\5\u0080A\2\u06a0")
        buf.write("\u069f\3\2\2\2\u06a0\u06a1\3\2\2\2\u06a1\u06a2\3\2\2\2")
        buf.write("\u06a2\u06a3\5\u012a\u0096\2\u06a3\u06a5\3\2\2\2\u06a4")
        buf.write("\u068c\3\2\2\2\u06a4\u0699\3\2\2\2\u06a5\u0127\3\2\2\2")
        buf.write("\u06a6\u06a8\5\u0176\u00bc\2\u06a7\u06a6\3\2\2\2\u06a7")
        buf.write("\u06a8\3\2\2\2\u06a8\u06aa\3\2\2\2\u06a9\u06ab\5\u0156")
        buf.write("\u00ac\2\u06aa\u06a9\3\2\2\2\u06aa\u06ab\3\2\2\2\u06ab")
        buf.write("\u06ac\3\2\2\2\u06ac\u06be\7\63\2\2\u06ad\u06af\5\u0176")
        buf.write("\u00bc\2\u06ae\u06ad\3\2\2\2\u06ae\u06af\3\2\2\2\u06af")
        buf.write("\u06b1\3\2\2\2\u06b0\u06b2\5\u0156\u00ac\2\u06b1\u06b0")
        buf.write("\3\2\2\2\u06b1\u06b2\3\2\2\2\u06b2\u06b3\3\2\2\2\u06b3")
        buf.write("\u06b4\7\63\2\2\u06b4\u06be\7\u0094\2\2\u06b5\u06b7\5")
        buf.write("\u0176\u00bc\2\u06b6\u06b5\3\2\2\2\u06b6\u06b7\3\2\2\2")
        buf.write("\u06b7\u06b9\3\2\2\2\u06b8\u06ba\5\u0156\u00ac\2\u06b9")
        buf.write("\u06b8\3\2\2\2\u06b9\u06ba\3\2\2\2\u06ba\u06bb\3\2\2\2")
        buf.write("\u06bb\u06bc\7\63\2\2\u06bc\u06be\7\u0093\2\2\u06bd\u06a7")
        buf.write("\3\2\2\2\u06bd\u06ae\3\2\2\2\u06bd\u06b6\3\2\2\2\u06be")
        buf.write("\u0129\3\2\2\2\u06bf\u06c0\5\u0096L\2\u06c0\u012b\3\2")
        buf.write("\2\2\u06c1\u06c3\5\u0176\u00bc\2\u06c2\u06c1\3\2\2\2\u06c2")
        buf.write("\u06c3\3\2\2\2\u06c3\u06c4\3\2\2\2\u06c4\u06c5\7\64\2")
        buf.write("\2\u06c5\u06c6\5\u0096L\2\u06c6\u012d\3\2\2\2\u06c7\u06c9")
        buf.write("\5\u0176\u00bc\2\u06c8\u06c7\3\2\2\2\u06c8\u06c9\3\2\2")
        buf.write("\2\u06c9\u06cb\3\2\2\2\u06ca\u06cc\5\u0158\u00ad\2\u06cb")
        buf.write("\u06ca\3\2\2\2\u06cb\u06cc\3\2\2\2\u06cc\u06cd\3\2\2\2")
        buf.write("\u06cd\u06ce\7\65\2\2\u06ce\u06d0\5\u01e4\u00f3\2\u06cf")
        buf.write("\u06d1\5\u0202\u0102\2\u06d0\u06cf\3\2\2\2\u06d0\u06d1")
        buf.write("\3\2\2\2\u06d1\u06d2\3\2\2\2\u06d2\u06d3\5\u0130\u0099")
        buf.write("\2\u06d3\u06e0\3\2\2\2\u06d4\u06d6\5\u0176\u00bc\2\u06d5")
        buf.write("\u06d4\3\2\2\2\u06d5\u06d6\3\2\2\2\u06d6\u06d8\3\2\2\2")
        buf.write("\u06d7\u06d9\5\u0158\u00ad\2\u06d8\u06d7\3\2\2\2\u06d8")
        buf.write("\u06d9\3\2\2\2\u06d9\u06da\3\2\2\2\u06da\u06db\7\65\2")
        buf.write("\2\u06db\u06dc\5\u01e4\u00f3\2\u06dc\u06dd\5\u0080A\2")
        buf.write("\u06dd\u06de\5\u0130\u0099\2\u06de\u06e0\3\2\2\2\u06df")
        buf.write("\u06c8\3\2\2\2\u06df\u06d5\3\2\2\2\u06e0\u012f\3\2\2\2")
        buf.write("\u06e1\u06e5\7\u0087\2\2\u06e2\u06e4\5\u0132\u009a\2\u06e3")
        buf.write("\u06e2\3\2\2\2\u06e4\u06e7\3\2\2\2\u06e5\u06e3\3\2\2\2")
        buf.write("\u06e5\u06e6\3\2\2\2\u06e6\u06e8\3\2\2\2\u06e7\u06e5\3")
        buf.write("\2\2\2\u06e8\u06e9\7\u008a\2\2\u06e9\u0131\3\2\2\2\u06ea")
        buf.write("\u06ed\5\u0090I\2\u06eb\u06ed\5P)\2\u06ec\u06ea\3\2\2")
        buf.write("\2\u06ec\u06eb\3\2\2\2\u06ed\u0133\3\2\2\2\u06ee\u06ef")
        buf.write("\5\u0136\u009c\2\u06ef\u06f0\5\u0138\u009d\2\u06f0\u06f1")
        buf.write("\5\u0096L\2\u06f1\u06fb\3\2\2\2\u06f2\u06f3\5\u0136\u009c")
        buf.write("\2\u06f3\u06f4\5\u0138\u009d\2\u06f4\u06f5\5\u00aeX\2")
        buf.write("\u06f5\u06fb\3\2\2\2\u06f6\u06f7\5\u0136\u009c\2\u06f7")
        buf.write("\u06f8\5\u0138\u009d\2\u06f8\u06f9\5\u00b6\\\2\u06f9\u06fb")
        buf.write("\3\2\2\2\u06fa\u06ee\3\2\2\2\u06fa\u06f2\3\2\2\2\u06fa")
        buf.write("\u06f6\3\2\2\2\u06fb\u0135\3\2\2\2\u06fc\u06fe\5\u0176")
        buf.write("\u00bc\2\u06fd\u06fc\3\2\2\2\u06fd\u06fe\3\2\2\2\u06fe")
        buf.write("\u0700\3\2\2\2\u06ff\u0701\5\u0156\u00ac\2\u0700\u06ff")
        buf.write("\3\2\2\2\u0700\u0701\3\2\2\2\u0701\u0702\3\2\2\2\u0702")
        buf.write("\u0703\7\66\2\2\u0703\u0704\5\u00d4k\2\u0704\u0137\3\2")
        buf.write("\2\2\u0705\u0707\5\u021a\u010e\2\u0706\u0708\5\u0176\u00bc")
        buf.write("\2\u0707\u0706\3\2\2\2\u0707\u0708\3\2\2\2\u0708\u0709")
        buf.write("\3\2\2\2\u0709\u070a\5\u01e0\u00f1\2\u070a\u0139\3\2\2")
        buf.write("\2\u070b\u070f\5\u013c\u009f\2\u070c\u070f\5\u013e\u00a0")
        buf.write("\2\u070d\u070f\5\u0140\u00a1\2\u070e\u070b\3\2\2\2\u070e")
        buf.write("\u070c\3\2\2\2\u070e\u070d\3\2\2\2\u070f\u013b\3\2\2\2")
        buf.write("\u0710\u0711\7\67\2\2\u0711\u0712\78\2\2\u0712\u0713\5")
        buf.write("\u0226\u0114\2\u0713\u013d\3\2\2\2\u0714\u0715\79\2\2")
        buf.write("\u0715\u0716\78\2\2\u0716\u0717\5\u0226\u0114\2\u0717")
        buf.write("\u013f\3\2\2\2\u0718\u0719\7:\2\2\u0719\u071a\78\2\2\u071a")
        buf.write("\u071c\5\u0226\u0114\2\u071b\u071d\5\u0142\u00a2\2\u071c")
        buf.write("\u071b\3\2\2\2\u071c\u071d\3\2\2\2\u071d\u0141\3\2\2\2")
        buf.write("\u071e\u071f\7\u008e\2\2\u071f\u0720\5\u0152\u00aa\2\u0720")
        buf.write("\u0143\3\2\2\2\u0721\u0722\7;\2\2\u0722\u0723\5\u0152")
        buf.write("\u00aa\2\u0723\u0727\7\u0087\2\2\u0724\u0726\5\u0146\u00a4")
        buf.write("\2\u0725\u0724\3\2\2\2\u0726\u0729\3\2\2\2\u0727\u0725")
        buf.write("\3\2\2\2\u0727\u0728\3\2\2\2\u0728\u072a\3\2\2\2\u0729")
        buf.write("\u0727\3\2\2\2\u072a\u072b\7\u008a\2\2\u072b\u0145\3\2")
        buf.write("\2\2\u072c\u0730\5\u0148\u00a5\2\u072d\u0730\5\u014a\u00a6")
        buf.write("\2\u072e\u0730\5\u014c\u00a7\2\u072f\u072c\3\2\2\2\u072f")
        buf.write("\u072d\3\2\2\2\u072f\u072e\3\2\2\2\u0730\u0147\3\2\2\2")
        buf.write("\u0731\u0732\7<\2\2\u0732\u0733\7\u008e\2\2\u0733\u0738")
        buf.write("\5\u0150\u00a9\2\u0734\u0735\7=\2\2\u0735\u0736\7\u008e")
        buf.write("\2\2\u0736\u0738\5\u0150\u00a9\2\u0737\u0731\3\2\2\2\u0737")
        buf.write("\u0734\3\2\2\2\u0738\u0149\3\2\2\2\u0739\u073a\7>\2\2")
        buf.write("\u073a\u073b\7\u008e\2\2\u073b\u073c\5\u0234\u011b\2\u073c")
        buf.write("\u014b\3\2\2\2\u073d\u073e\7?\2\2\u073e\u073f\7\u008e")
        buf.write("\2\2\u073f\u0740\5\u014e\u00a8\2\u0740\u014d\3\2\2\2\u0741")
        buf.write("\u0742\t\4\2\2\u0742\u014f\3\2\2\2\u0743\u0748\5\u0152")
        buf.write("\u00aa\2\u0744\u0745\7\u008d\2\2\u0745\u0747\5\u0152\u00aa")
        buf.write("\2\u0746\u0744\3\2\2\2\u0747\u074a\3\2\2\2\u0748\u0746")
        buf.write("\3\2\2\2\u0748\u0749\3\2\2\2\u0749\u0151\3\2\2\2\u074a")
        buf.write("\u0748\3\2\2\2\u074b\u074c\5\u0208\u0105\2\u074c\u0153")
        buf.write("\3\2\2\2\u074d\u0766\7&\2\2\u074e\u0766\7C\2\2\u074f\u0766")
        buf.write("\7D\2\2\u0750\u0766\7\61\2\2\u0751\u0766\7:\2\2\u0752")
        buf.write("\u0766\7E\2\2\u0753\u0766\7F\2\2\u0754\u0766\7G\2\2\u0755")
        buf.write("\u0766\79\2\2\u0756\u0766\7\67\2\2\u0757\u0766\7H\2\2")
        buf.write("\u0758\u0766\7I\2\2\u0759\u0766\7J\2\2\u075a\u075b\7J")
        buf.write("\2\2\u075b\u075c\7\u0088\2\2\u075c\u075d\7K\2\2\u075d")
        buf.write("\u0766\7\u008b\2\2\u075e\u075f\7J\2\2\u075f\u0760\7\u0088")
        buf.write("\2\2\u0760\u0761\7L\2\2\u0761\u0766\7\u008b\2\2\u0762")
        buf.write("\u0766\7M\2\2\u0763\u0766\5\u0158\u00ad\2\u0764\u0766")
        buf.write("\5\u015a\u00ae\2\u0765\u074d\3\2\2\2\u0765\u074e\3\2\2")
        buf.write("\2\u0765\u074f\3\2\2\2\u0765\u0750\3\2\2\2\u0765\u0751")
        buf.write("\3\2\2\2\u0765\u0752\3\2\2\2\u0765\u0753\3\2\2\2\u0765")
        buf.write("\u0754\3\2\2\2\u0765\u0755\3\2\2\2\u0765\u0756\3\2\2\2")
        buf.write("\u0765\u0757\3\2\2\2\u0765\u0758\3\2\2\2\u0765\u0759\3")
        buf.write("\2\2\2\u0765\u075a\3\2\2\2\u0765\u075e\3\2\2\2\u0765\u0762")
        buf.write("\3\2\2\2\u0765\u0763\3\2\2\2\u0765\u0764\3\2\2\2\u0766")
        buf.write("\u0155\3\2\2\2\u0767\u0769\5\u0154\u00ab\2\u0768\u0767")
        buf.write("\3\2\2\2\u0769\u076a\3\2\2\2\u076a\u0768\3\2\2\2\u076a")
        buf.write("\u076b\3\2\2\2\u076b\u0157\3\2\2\2\u076c\u0786\7N\2\2")
        buf.write("\u076d\u076e\7N\2\2\u076e\u076f\7\u0088\2\2\u076f\u0770")
        buf.write("\7+\2\2\u0770\u0786\7\u008b\2\2\u0771\u0786\7O\2\2\u0772")
        buf.write("\u0773\7O\2\2\u0773\u0774\7\u0088\2\2\u0774\u0775\7+\2")
        buf.write("\2\u0775\u0786\7\u008b\2\2\u0776\u0786\7P\2\2\u0777\u0778")
        buf.write("\7P\2\2\u0778\u0779\7\u0088\2\2\u0779\u077a\7+\2\2\u077a")
        buf.write("\u0786\7\u008b\2\2\u077b\u0786\7Q\2\2\u077c\u077d\7Q\2")
        buf.write("\2\u077d\u077e\7\u0088\2\2\u077e\u077f\7+\2\2\u077f\u0786")
        buf.write("\7\u008b\2\2\u0780\u0786\7R\2\2\u0781\u0782\7R\2\2\u0782")
        buf.write("\u0783\7\u0088\2\2\u0783\u0784\7+\2\2\u0784\u0786\7\u008b")
        buf.write("\2\2\u0785\u076c\3\2\2\2\u0785\u076d\3\2\2\2\u0785\u0771")
        buf.write("\3\2\2\2\u0785\u0772\3\2\2\2\u0785\u0776\3\2\2\2\u0785")
        buf.write("\u0777\3\2\2\2\u0785\u077b\3\2\2\2\u0785\u077c\3\2\2\2")
        buf.write("\u0785\u0780\3\2\2\2\u0785\u0781\3\2\2\2\u0786\u0159\3")
        buf.write("\2\2\2\u0787\u0788\t\5\2\2\u0788\u015b\3\2\2\2\u0789\u078a")
        buf.write("\b\u00af\1\2\u078a\u078c\5\u015e\u00b0\2\u078b\u078d\5")
        buf.write("\u01e2\u00f2\2\u078c\u078b\3\2\2\2\u078c\u078d\3\2\2\2")
        buf.write("\u078d\u079d\3\2\2\2\u078e\u0790\5\u0160\u00b1\2\u078f")
        buf.write("\u0791\5\u01e2\u00f2\2\u0790\u078f\3\2\2\2\u0790\u0791")
        buf.write("\3\2\2\2\u0791\u079d\3\2\2\2\u0792\u079d\5\u0162\u00b2")
        buf.write("\2\u0793\u0795\5\u0164\u00b3\2\u0794\u0796\5\u01e2\u00f2")
        buf.write("\2\u0795\u0794\3\2\2\2\u0795\u0796\3\2\2\2\u0796\u079d")
        buf.write("\3\2\2\2\u0797\u079d\5\u016a\u00b6\2\u0798\u079d\5\u016c")
        buf.write("\u00b7\2\u0799\u079a\7U\2\2\u079a\u079d\5\u01e0\u00f1")
        buf.write("\2\u079b\u079d\5\u016e\u00b8\2\u079c\u0789\3\2\2\2\u079c")
        buf.write("\u078e\3\2\2\2\u079c\u0792\3\2\2\2\u079c\u0793\3\2\2\2")
        buf.write("\u079c\u0797\3\2\2\2\u079c\u0798\3\2\2\2\u079c\u0799\3")
        buf.write("\2\2\2\u079c\u079b\3\2\2\2\u079d\u07a3\3\2\2\2\u079e\u079f")
        buf.write("\f\4\2\2\u079f\u07a0\7V\2\2\u07a0\u07a2\5\u01e0\u00f1")
        buf.write("\2\u07a1\u079e\3\2\2\2\u07a2\u07a5\3\2\2\2\u07a3\u07a1")
        buf.write("\3\2\2\2\u07a3\u07a4\3\2\2\2\u07a4\u015d\3\2\2\2\u07a5")
        buf.write("\u07a3\3\2\2\2\u07a6\u07a7\7\u0092\2\2\u07a7\u015f\3\2")
        buf.write("\2\2\u07a8\u07a9\5\u0208\u0105\2\u07a9\u0161\3\2\2\2\u07aa")
        buf.write("\u07ab\7\b\2\2\u07ab\u07af\5\u015c\u00af\2\u07ac\u07ad")
        buf.write("\7\7\2\2\u07ad\u07af\5\u015c\u00af\2\u07ae\u07aa\3\2\2")
        buf.write("\2\u07ae\u07ac\3\2\2\2\u07af\u0163\3\2\2\2\u07b0\u07b2")
        buf.write("\7\u0088\2\2\u07b1\u07b3\5\u0166\u00b4\2\u07b2\u07b1\3")
        buf.write("\2\2\2\u07b2\u07b3\3\2\2\2\u07b3\u07b4\3\2\2\2\u07b4\u07b5")
        buf.write("\7\u008b\2\2\u07b5\u0165\3\2\2\2\u07b6\u07bb\5\u0168\u00b5")
        buf.write("\2\u07b7\u07b8\7\u008d\2\2\u07b8\u07ba\5\u0168\u00b5\2")
        buf.write("\u07b9\u07b7\3\2\2\2\u07ba\u07bd\3\2\2\2\u07bb\u07b9\3")
        buf.write("\2\2\2\u07bb\u07bc\3\2\2\2\u07bc\u0167\3\2\2\2\u07bd\u07bb")
        buf.write("\3\2\2\2\u07be\u07bf\5\u015c\u00af\2\u07bf\u0169\3\2\2")
        buf.write("\2\u07c0\u07c2\5\u01e4\u00f3\2\u07c1\u07c0\3\2\2\2\u07c1")
        buf.write("\u07c2\3\2\2\2\u07c2\u07c3\3\2\2\2\u07c3\u07c4\7\u0086")
        buf.write("\2\2\u07c4\u07c6\5\u00f0y\2\u07c5\u07c7\5\u0164\u00b3")
        buf.write("\2\u07c6\u07c5\3\2\2\2\u07c6\u07c7\3\2\2\2\u07c7\u016b")
        buf.write("\3\2\2\2\u07c8\u07c9\5\u0160\u00b1\2\u07c9\u07ca\7\u0094")
        buf.write("\2\2\u07ca\u016d\3\2\2\2\u07cb\u07cc\5\u017e\u00c0\2\u07cc")
        buf.write("\u016f\3\2\2\2\u07cd\u07ce\7\u0095\2\2\u07ce\u07d0\5\u0172")
        buf.write("\u00ba\2\u07cf\u07d1\5\u0174\u00bb\2\u07d0\u07cf\3\2\2")
        buf.write("\2\u07d0\u07d1\3\2\2\2\u07d1\u0171\3\2\2\2\u07d2\u07d3")
        buf.write("\5\u0208\u0105\2\u07d3\u0173\3\2\2\2\u07d4\u07d5\7\u0088")
        buf.write("\2\2\u07d5\u07d6\5\u0178\u00bd\2\u07d6\u07d7\7\u008b\2")
        buf.write("\2\u07d7\u0175\3\2\2\2\u07d8\u07da\5\u0170\u00b9\2\u07d9")
        buf.write("\u07d8\3\2\2\2\u07da\u07db\3\2\2\2\u07db\u07d9\3\2\2\2")
        buf.write("\u07db\u07dc\3\2\2\2\u07dc\u0177\3\2\2\2\u07dd\u07df\5")
        buf.write("\u017a\u00be\2\u07de\u07dd\3\2\2\2\u07df\u07e2\3\2\2\2")
        buf.write("\u07e0\u07de\3\2\2\2\u07e0\u07e1\3\2\2\2\u07e1\u0179\3")
        buf.write("\2\2\2\u07e2\u07e0\3\2\2\2\u07e3\u07e4\7\u0088\2\2\u07e4")
        buf.write("\u07e5\5\u0178\u00bd\2\u07e5\u07e6\7\u008b\2\2\u07e6\u07f5")
        buf.write("\3\2\2\2\u07e7\u07e8\7\u0089\2\2\u07e8\u07e9\5\u0178\u00bd")
        buf.write("\2\u07e9\u07ea\7\u008c\2\2\u07ea\u07f5\3\2\2\2\u07eb\u07ec")
        buf.write("\7\u0087\2\2\u07ec\u07ed\5\u0178\u00bd\2\u07ed\u07ee\7")
        buf.write("\u008a\2\2\u07ee\u07f5\3\2\2\2\u07ef\u07f5\5\u020a\u0106")
        buf.write("\2\u07f0\u07f5\5\u0230\u0119\2\u07f1\u07f5\5\u0226\u0114")
        buf.write("\2\u07f2\u07f5\7\u0084\2\2\u07f3\u07f5\5\u017c\u00bf\2")
        buf.write("\u07f4\u07e3\3\2\2\2\u07f4\u07e7\3\2\2\2\u07f4\u07eb\3")
        buf.write("\2\2\2\u07f4\u07ef\3\2\2\2\u07f4\u07f0\3\2\2\2\u07f4\u07f1")
        buf.write("\3\2\2\2\u07f4\u07f2\3\2\2\2\u07f4\u07f3\3\2\2\2\u07f5")
        buf.write("\u017b\3\2\2\2\u07f6\u07fd\t\6\2\2\u07f7\u07fd\5\u021a")
        buf.write("\u010e\2\u07f8\u07f9\6\u00bf\6\2\u07f9\u07fd\7\u0096\2")
        buf.write("\2\u07fa\u07fb\6\u00bf\7\2\u07fb\u07fd\7\u0093\2\2\u07fc")
        buf.write("\u07f6\3\2\2\2\u07fc\u07f7\3\2\2\2\u07fc\u07f8\3\2\2\2")
        buf.write("\u07fc\u07fa\3\2\2\2\u07fd\u017d\3\2\2\2\u07fe\u0800\5")
        buf.write("\u0186\u00c4\2\u07ff\u07fe\3\2\2\2\u07ff\u0800\3\2\2\2")
        buf.write("\u0800\u0801\3\2\2\2\u0801\u0803\5\u0182\u00c2\2\u0802")
        buf.write("\u0804\5\u018a\u00c6\2\u0803\u0802\3\2\2\2\u0803\u0804")
        buf.write("\3\2\2\2\u0804\u017f\3\2\2\2\u0805\u080a\5\u017e\u00c0")
        buf.write("\2\u0806\u0807\7\u008d\2\2\u0807\u0809\5\u017e\u00c0\2")
        buf.write("\u0808\u0806\3\2\2\2\u0809\u080c\3\2\2\2\u080a\u0808\3")
        buf.write("\2\2\2\u080a\u080b\3\2\2\2\u080b\u0181\3\2\2\2\u080c\u080a")
        buf.write("\3\2\2\2\u080d\u080e\5\u0222\u0112\2\u080e\u080f\5\u01d0")
        buf.write("\u00e9\2\u080f\u0813\3\2\2\2\u0810\u0813\5\u01d0\u00e9")
        buf.write("\2\u0811\u0813\5\u0184\u00c3\2\u0812\u080d\3\2\2\2\u0812")
        buf.write("\u0810\3\2\2\2\u0812\u0811\3\2\2\2\u0813\u0183\3\2\2\2")
        buf.write("\u0814\u0815\7\u0096\2\2\u0815\u0816\5\u0208\u0105\2\u0816")
        buf.write("\u0185\3\2\2\2\u0817\u0818\7Y\2\2\u0818\u081d\7\u0094")
        buf.write("\2\2\u0819\u081a\7Y\2\2\u081a\u081d\7\u0093\2\2\u081b")
        buf.write("\u081d\7Y\2\2\u081c\u0817\3\2\2\2\u081c\u0819\3\2\2\2")
        buf.write("\u081c\u081b\3\2\2\2\u081d\u0187\3\2\2\2\u081e\u081f\5")
        buf.write("\u0220\u0111\2\u081f\u0820\5\u0182\u00c2\2\u0820\u082f")
        buf.write("\3\2\2\2\u0821\u0823\5\u0210\u0109\2\u0822\u0824\5\u0186")
        buf.write("\u00c4\2\u0823\u0822\3\2\2\2\u0823\u0824\3\2\2\2\u0824")
        buf.write("\u0825\3\2\2\2\u0825\u0826\5\u0182\u00c2\2\u0826\u082f")
        buf.write("\3\2\2\2\u0827\u0829\5\u018c\u00c7\2\u0828\u082a\5\u0186")
        buf.write("\u00c4\2\u0829\u0828\3\2\2\2\u0829\u082a\3\2\2\2\u082a")
        buf.write("\u082b\3\2\2\2\u082b\u082c\5\u0182\u00c2\2\u082c\u082f")
        buf.write("\3\2\2\2\u082d\u082f\5\u018e\u00c8\2\u082e\u081e\3\2\2")
        buf.write("\2\u082e\u0821\3\2\2\2\u082e\u0827\3\2\2\2\u082e\u082d")
        buf.write("\3\2\2\2\u082f\u0189\3\2\2\2\u0830\u0832\5\u0188\u00c5")
        buf.write("\2\u0831\u0830\3\2\2\2\u0832\u0833\3\2\2\2\u0833\u0831")
        buf.write("\3\2\2\2\u0833\u0834\3\2\2\2\u0834\u018b\3\2\2\2\u0835")
        buf.write("\u0837\7\u0094\2\2\u0836\u0838\5\u0186\u00c4\2\u0837\u0836")
        buf.write("\3\2\2\2\u0837\u0838\3\2\2\2\u0838\u0839\3\2\2\2\u0839")
        buf.write("\u083a\5\u017e\u00c0\2\u083a\u083b\7\u008e\2\2\u083b\u018d")
        buf.write("\3\2\2\2\u083c\u083d\7U\2\2\u083d\u0847\5\u01e0\u00f1")
        buf.write("\2\u083e\u083f\7V\2\2\u083f\u0847\5\u01e0\u00f1\2\u0840")
        buf.write("\u0841\7V\2\2\u0841\u0842\7\u0094\2\2\u0842\u0847\5\u01e0")
        buf.write("\u00f1\2\u0843\u0844\7V\2\2\u0844\u0845\7\u0093\2\2\u0845")
        buf.write("\u0847\5\u01e0\u00f1\2\u0846\u083c\3\2\2\2\u0846\u083e")
        buf.write("\3\2\2\2\u0846\u0840\3\2\2\2\u0846\u0843\3\2\2\2\u0847")
        buf.write("\u018f\3\2\2\2\u0848\u084a\5\u0208\u0105\2\u0849\u084b")
        buf.write("\5\u008aF\2\u084a\u0849\3\2\2\2\u084a\u084b\3\2\2\2\u084b")
        buf.write("\u0857\3\2\2\2\u084c\u0857\5\u0192\u00ca\2\u084d\u0857")
        buf.write("\5\u01a2\u00d2\2\u084e\u0857\5\u01a4\u00d3\2\u084f\u0857")
        buf.write("\5\u01ac\u00d7\2\u0850\u0857\5\u01c4\u00e3\2\u0851\u0857")
        buf.write("\5\u01c6\u00e4\2\u0852\u0857\5\u01c2\u00e2\2\u0853\u0857")
        buf.write("\5\u01ca\u00e6\2\u0854\u0857\5\u01cc\u00e7\2\u0855\u0857")
        buf.write("\5\u01ce\u00e8\2\u0856\u0848\3\2\2\2\u0856\u084c\3\2\2")
        buf.write("\2\u0856\u084d\3\2\2\2\u0856\u084e\3\2\2\2\u0856\u084f")
        buf.write("\3\2\2\2\u0856\u0850\3\2\2\2\u0856\u0851\3\2\2\2\u0856")
        buf.write("\u0852\3\2\2\2\u0856\u0853\3\2\2\2\u0856\u0854\3\2\2\2")
        buf.write("\u0856\u0855\3\2\2\2\u0857\u0191\3\2\2\2\u0858\u0861\5")
        buf.write("\u0230\u0119\2\u0859\u0861\5\u0194\u00cb\2\u085a\u0861")
        buf.write("\5\u019a\u00ce\2\u085b\u0861\7Z\2\2\u085c\u0861\7[\2\2")
        buf.write("\u085d\u0861\7\\\2\2\u085e\u0861\7]\2\2\u085f\u0861\7")
        buf.write("^\2\2\u0860\u0858\3\2\2\2\u0860\u0859\3\2\2\2\u0860\u085a")
        buf.write("\3\2\2\2\u0860\u085b\3\2\2\2\u0860\u085c\3\2\2\2\u0860")
        buf.write("\u085d\3\2\2\2\u0860\u085e\3\2\2\2\u0860\u085f\3\2\2\2")
        buf.write("\u0861\u0193\3\2\2\2\u0862\u0864\7\u0089\2\2\u0863\u0865")
        buf.write("\5\u0196\u00cc\2\u0864\u0863\3\2\2\2\u0864\u0865\3\2\2")
        buf.write("\2\u0865\u0866\3\2\2\2\u0866\u0867\7\u008c\2\2\u0867\u0195")
        buf.write("\3\2\2\2\u0868\u086a\5\u0198\u00cd\2\u0869\u086b\7\u008d")
        buf.write("\2\2\u086a\u0869\3\2\2\2\u086a\u086b\3\2\2\2\u086b\u0871")
        buf.write("\3\2\2\2\u086c\u086d\5\u0198\u00cd\2\u086d\u086e\7\u008d")
        buf.write("\2\2\u086e\u086f\5\u0196\u00cc\2\u086f\u0871\3\2\2\2\u0870")
        buf.write("\u0868\3\2\2\2\u0870\u086c\3\2\2\2\u0871\u0197\3\2\2\2")
        buf.write("\u0872\u0873\5\u017e\u00c0\2\u0873\u0199\3\2\2\2\u0874")
        buf.write("\u0875\7\u0089\2\2\u0875\u0876\5\u019c\u00cf\2\u0876\u0877")
        buf.write("\7\u008c\2\2\u0877\u087c\3\2\2\2\u0878\u0879\7\u0089\2")
        buf.write("\2\u0879\u087a\7\u008e\2\2\u087a\u087c\7\u008c\2\2\u087b")
        buf.write("\u0874\3\2\2\2\u087b\u0878\3\2\2\2\u087c\u019b\3\2\2\2")
        buf.write("\u087d\u087f\5\u019e\u00d0\2\u087e\u0880\7\u008d\2\2\u087f")
        buf.write("\u087e\3\2\2\2\u087f\u0880\3\2\2\2\u0880\u0886\3\2\2\2")
        buf.write("\u0881\u0882\5\u019e\u00d0\2\u0882\u0883\7\u008d\2\2\u0883")
        buf.write("\u0884\5\u019c\u00cf\2\u0884\u0886\3\2\2\2\u0885\u087d")
        buf.write("\3\2\2\2\u0885\u0881\3\2\2\2\u0886\u019d\3\2\2\2\u0887")
        buf.write("\u0888\5\u017e\u00c0\2\u0888\u0889\7\u008e\2\2\u0889\u088a")
        buf.write("\5\u017e\u00c0\2\u088a\u019f\3\2\2\2\u088b\u088c\7_\2")
        buf.write("\2\u088c\u088d\7\u0088\2\2\u088d\u088e\7`\2\2\u088e\u088f")
        buf.write("\7\u008e\2\2\u088f\u0890\5\u017e\u00c0\2\u0890\u0891\7")
        buf.write("\u008d\2\2\u0891\u0892\7a\2\2\u0892\u0893\7\u008e\2\2")
        buf.write("\u0893\u0894\5\u017e\u00c0\2\u0894\u0895\7\u008d\2\2\u0895")
        buf.write("\u0896\7b\2\2\u0896\u0897\7\u008e\2\2\u0897\u0898\5\u017e")
        buf.write("\u00c0\2\u0898\u0899\7\u008d\2\2\u0899\u089a\7c\2\2\u089a")
        buf.write("\u089b\7\u008e\2\2\u089b\u089c\5\u017e\u00c0\2\u089c\u089d")
        buf.write("\7\u008b\2\2\u089d\u08ad\3\2\2\2\u089e\u089f\7d\2\2\u089f")
        buf.write("\u08a0\7\u0088\2\2\u08a0\u08a1\7e\2\2\u08a1\u08a2\7\u008e")
        buf.write("\2\2\u08a2\u08a3\5\u017e\u00c0\2\u08a3\u08a4\7\u008b\2")
        buf.write("\2\u08a4\u08ad\3\2\2\2\u08a5\u08a6\7f\2\2\u08a6\u08a7")
        buf.write("\7\u0088\2\2\u08a7\u08a8\7e\2\2\u08a8\u08a9\7\u008e\2")
        buf.write("\2\u08a9\u08aa\5\u017e\u00c0\2\u08aa\u08ab\7\u008b\2\2")
        buf.write("\u08ab\u08ad\3\2\2\2\u08ac\u088b\3\2\2\2\u08ac\u089e\3")
        buf.write("\2\2\2\u08ac\u08a5\3\2\2\2\u08ad\u01a1\3\2\2\2\u08ae\u08c2")
        buf.write("\7g\2\2\u08af\u08b0\7g\2\2\u08b0\u08b1\7\u0086\2\2\u08b1")
        buf.write("\u08c2\5\u0208\u0105\2\u08b2\u08b3\7g\2\2\u08b3\u08b4")
        buf.write("\7\u0089\2\2\u08b4\u08b5\5\u0180\u00c1\2\u08b5\u08b6\7")
        buf.write("\u008c\2\2\u08b6\u08c2\3\2\2\2\u08b7\u08b8\7g\2\2\u08b8")
        buf.write("\u08b9\7\u0086\2\2\u08b9\u08c2\7\63\2\2\u08ba\u08c2\7")
        buf.write("h\2\2\u08bb\u08bc\7h\2\2\u08bc\u08bd\7\u0086\2\2\u08bd")
        buf.write("\u08c2\5\u0208\u0105\2\u08be\u08bf\7h\2\2\u08bf\u08c0")
        buf.write("\7\u0086\2\2\u08c0\u08c2\7\63\2\2\u08c1\u08ae\3\2\2\2")
        buf.write("\u08c1\u08af\3\2\2\2\u08c1\u08b2\3\2\2\2\u08c1\u08b7\3")
        buf.write("\2\2\2\u08c1\u08ba\3\2\2\2\u08c1\u08bb\3\2\2\2\u08c1\u08be")
        buf.write("\3\2\2\2\u08c2\u01a3\3\2\2\2\u08c3\u08c7\5\u01a6\u00d4")
        buf.write("\2\u08c4\u08c7\5\u01a8\u00d5\2\u08c5\u08c7\5\u01aa\u00d6")
        buf.write("\2\u08c6\u08c3\3\2\2\2\u08c6\u08c4\3\2\2\2\u08c6\u08c5")
        buf.write("\3\2\2\2\u08c7\u01a5\3\2\2\2\u08c8\u08c9\7i\2\2\u08c9")
        buf.write("\u08ca\7\u0086\2\2\u08ca\u08cb\5\u0208\u0105\2\u08cb\u01a7")
        buf.write("\3\2\2\2\u08cc\u08cd\7i\2\2\u08cd\u08ce\7\u0089\2\2\u08ce")
        buf.write("\u08cf\5\u017e\u00c0\2\u08cf\u08d0\7\u008c\2\2\u08d0\u01a9")
        buf.write("\3\2\2\2\u08d1\u08d2\7i\2\2\u08d2\u08d3\7\u0086\2\2\u08d3")
        buf.write("\u08d4\7\63\2\2\u08d4\u01ab\3\2\2\2\u08d5\u08d7\7\u0087")
        buf.write("\2\2\u08d6\u08d8\5\u01ae\u00d8\2\u08d7\u08d6\3\2\2\2\u08d7")
        buf.write("\u08d8\3\2\2\2\u08d8\u08da\3\2\2\2\u08d9\u08db\5\6\4\2")
        buf.write("\u08da\u08d9\3\2\2\2\u08da\u08db\3\2\2\2\u08db\u08dc\3")
        buf.write("\2\2\2\u08dc\u08dd\7\u008a\2\2\u08dd\u01ad\3\2\2\2\u08de")
        buf.write("\u08e0\5\u01ba\u00de\2\u08df\u08de\3\2\2\2\u08df\u08e0")
        buf.write("\3\2\2\2\u08e0\u08e1\3\2\2\2\u08e1\u08e3\5\u01b0\u00d9")
        buf.write("\2\u08e2\u08e4\7.\2\2\u08e3\u08e2\3\2\2\2\u08e3\u08e4")
        buf.write("\3\2\2\2\u08e4\u08e6\3\2\2\2\u08e5\u08e7\5\u00d0i\2\u08e6")
        buf.write("\u08e5\3\2\2\2\u08e6\u08e7\3\2\2\2\u08e7\u08e8\3\2\2\2")
        buf.write("\u08e8\u08e9\7\5\2\2\u08e9\u08ee\3\2\2\2\u08ea\u08eb\5")
        buf.write("\u01ba\u00de\2\u08eb\u08ec\7\5\2\2\u08ec\u08ee\3\2\2\2")
        buf.write("\u08ed\u08df\3\2\2\2\u08ed\u08ea\3\2\2\2\u08ee\u01af\3")
        buf.write("\2\2\2\u08ef\u08f0\7\u0088\2\2\u08f0\u08f7\7\u008b\2\2")
        buf.write("\u08f1\u08f2\7\u0088\2\2\u08f2\u08f3\5\u01b4\u00db\2\u08f3")
        buf.write("\u08f4\7\u008b\2\2\u08f4\u08f7\3\2\2\2\u08f5\u08f7\5\u01b2")
        buf.write("\u00da\2\u08f6\u08ef\3\2\2\2\u08f6\u08f1\3\2\2\2\u08f6")
        buf.write("\u08f5\3\2\2\2\u08f7\u01b1\3\2\2\2\u08f8\u08fd\5\u0208")
        buf.write("\u0105\2\u08f9\u08fa\7\u008d\2\2\u08fa\u08fc\5\u0208\u0105")
        buf.write("\2\u08fb\u08f9\3\2\2\2\u08fc\u08ff\3\2\2\2\u08fd\u08fb")
        buf.write("\3\2\2\2\u08fd\u08fe\3\2\2\2\u08fe\u01b3\3\2\2\2\u08ff")
        buf.write("\u08fd\3\2\2\2\u0900\u0905\5\u01b6\u00dc\2\u0901\u0902")
        buf.write("\7\u008d\2\2\u0902\u0904\5\u01b6\u00dc\2\u0903\u0901\3")
        buf.write("\2\2\2\u0904\u0907\3\2\2\2\u0905\u0903\3\2\2\2\u0905\u0906")
        buf.write("\3\2\2\2\u0906\u01b5\3\2\2\2\u0907\u0905\3\2\2\2\u0908")
        buf.write("\u090a\5\u01b8\u00dd\2\u0909\u090b\5\u01e2\u00f2\2\u090a")
        buf.write("\u0909\3\2\2\2\u090a\u090b\3\2\2\2\u090b\u0911\3\2\2\2")
        buf.write("\u090c\u090d\5\u01b8\u00dd\2\u090d\u090e\5\u01e2\u00f2")
        buf.write("\2\u090e\u090f\5\u021c\u010f\2\u090f\u0911\3\2\2\2\u0910")
        buf.write("\u0908\3\2\2\2\u0910\u090c\3\2\2\2\u0911\u01b7\3\2\2\2")
        buf.write("\u0912\u0913\5\u020a\u0106\2\u0913\u01b9\3\2\2\2\u0914")
        buf.write("\u0915\7\u0089\2\2\u0915\u0916\5\u01bc\u00df\2\u0916\u0917")
        buf.write("\7\u008c\2\2\u0917\u01bb\3\2\2\2\u0918\u091d\5\u01be\u00e0")
        buf.write("\2\u0919\u091a\7\u008d\2\2\u091a\u091c\5\u01be\u00e0\2")
        buf.write("\u091b\u0919\3\2\2\2\u091c\u091f\3\2\2\2\u091d\u091b\3")
        buf.write("\2\2\2\u091d\u091e\3\2\2\2\u091e\u01bd\3\2\2\2\u091f\u091d")
        buf.write("\3\2\2\2\u0920\u0922\5\u01c0\u00e1\2\u0921\u0920\3\2\2")
        buf.write("\2\u0921\u0922\3\2\2\2\u0922\u0923\3\2\2\2\u0923\u0924")
        buf.write("\5\u017e\u00c0\2\u0924\u01bf\3\2\2\2\u0925\u0926\t\7\2")
        buf.write("\2\u0926\u01c1\3\2\2\2\u0927\u0928\7\u0086\2\2\u0928\u0929")
        buf.write("\5\u020a\u0106\2\u0929\u01c3\3\2\2\2\u092a\u092b\7\u0088")
        buf.write("\2\2\u092b\u092c\5\u017e\u00c0\2\u092c\u092d\7\u008b\2")
        buf.write("\2\u092d\u01c5\3\2\2\2\u092e\u092f\7\u0088\2\2\u092f\u093b")
        buf.write("\7\u008b\2\2\u0930\u0931\7\u0088\2\2\u0931\u0934\5\u01c8")
        buf.write("\u00e5\2\u0932\u0933\7\u008d\2\2\u0933\u0935\5\u01c8\u00e5")
        buf.write("\2\u0934\u0932\3\2\2\2\u0935\u0936\3\2\2\2\u0936\u0934")
        buf.write("\3\2\2\2\u0936\u0937\3\2\2\2\u0937\u0938\3\2\2\2\u0938")
        buf.write("\u0939\7\u008b\2\2\u0939\u093b\3\2\2\2\u093a\u092e\3\2")
        buf.write("\2\2\u093a\u0930\3\2\2\2\u093b\u01c7\3\2\2\2\u093c\u0942")
        buf.write("\5\u017e\u00c0\2\u093d\u093e\5\u020a\u0106\2\u093e\u093f")
        buf.write("\7\u008e\2\2\u093f\u0940\5\u017e\u00c0\2\u0940\u0942\3")
        buf.write("\2\2\2\u0941\u093c\3\2\2\2\u0941\u093d\3\2\2\2\u0942\u01c9")
        buf.write("\3\2\2\2\u0943\u0944\7\u0092\2\2\u0944\u01cb\3\2\2\2\u0945")
        buf.write("\u0946\7l\2\2\u0946\u0947\7\u0088\2\2\u0947\u0948\5\u017e")
        buf.write("\u00c0\2\u0948\u0949\7\u008b\2\2\u0949\u0957\3\2\2\2\u094a")
        buf.write("\u094b\7l\2\2\u094b\u094c\7\u0088\2\2\u094c\u094d\7m\2")
        buf.write("\2\u094d\u094e\5\u017e\u00c0\2\u094e\u094f\7\u008b\2\2")
        buf.write("\u094f\u0957\3\2\2\2\u0950\u0951\7l\2\2\u0951\u0952\7")
        buf.write("\u0088\2\2\u0952\u0953\7n\2\2\u0953\u0954\5\u017e\u00c0")
        buf.write("\2\u0954\u0955\7\u008b\2\2\u0955\u0957\3\2\2\2\u0956\u0945")
        buf.write("\3\2\2\2\u0956\u094a\3\2\2\2\u0956\u0950\3\2\2\2\u0957")
        buf.write("\u01cd\3\2\2\2\u0958\u0959\7o\2\2\u0959\u095a\7\u0088")
        buf.write("\2\2\u095a\u095b\5\u017e\u00c0\2\u095b\u095c\7\u008b\2")
        buf.write("\2\u095c\u01cf\3\2\2\2\u095d\u095e\b\u00e9\1\2\u095e\u0961")
        buf.write("\5\u0190\u00c9\2\u095f\u0961\5\u01de\u00f0\2\u0960\u095d")
        buf.write("\3\2\2\2\u0960\u095f\3\2\2\2\u0961\u0994\3\2\2\2\u0962")
        buf.write("\u0963\f\16\2\2\u0963\u0993\5\u0224\u0113\2\u0964\u0965")
        buf.write("\f\r\2\2\u0965\u0993\5\u01d2\u00ea\2\u0966\u0968\f\f\2")
        buf.write("\2\u0967\u0969\5\u01d2\u00ea\2\u0968\u0967\3\2\2\2\u0968")
        buf.write("\u0969\3\2\2\2\u0969\u096a\3\2\2\2\u096a\u0993\5\u01d8")
        buf.write("\u00ed\2\u096b\u096c\f\13\2\2\u096c\u096d\7\u0086\2\2")
        buf.write("\u096d\u0993\7\63\2\2\u096e\u096f\f\n\2\2\u096f\u0970")
        buf.write("\7\u0086\2\2\u0970\u0971\7\63\2\2\u0971\u0972\7\u0088")
        buf.write("\2\2\u0972\u0973\5\u01da\u00ee\2\u0973\u0974\7\u008b\2")
        buf.write("\2\u0974\u0993\3\2\2\2\u0975\u0976\f\t\2\2\u0976\u0977")
        buf.write("\7\u0086\2\2\u0977\u0993\7\u00a6\2\2\u0978\u0979\f\b\2")
        buf.write("\2\u0979\u097a\7\u0086\2\2\u097a\u097c\5\u0208\u0105\2")
        buf.write("\u097b\u097d\5\u008aF\2\u097c\u097b\3\2\2\2\u097c\u097d")
        buf.write("\3\2\2\2\u097d\u0993\3\2\2\2\u097e\u097f\f\7\2\2\u097f")
        buf.write("\u0980\7\u0086\2\2\u0980\u0981\5\u0208\u0105\2\u0981\u0982")
        buf.write("\7\u0088\2\2\u0982\u0983\5\u01da\u00ee\2\u0983\u0984\7")
        buf.write("\u008b\2\2\u0984\u0993\3\2\2\2\u0985\u0986\f\6\2\2\u0986")
        buf.write("\u0987\7\u0088\2\2\u0987\u0988\5\u01da\u00ee\2\u0988\u0989")
        buf.write("\7\u008b\2\2\u0989\u0993\3\2\2\2\u098a\u098b\f\5\2\2\u098b")
        buf.write("\u098c\7\u0086\2\2\u098c\u0993\7g\2\2\u098d\u098e\f\3")
        buf.write("\2\2\u098e\u098f\7\u0089\2\2\u098f\u0990\5\u0180\u00c1")
        buf.write("\2\u0990\u0991\7\u008c\2\2\u0991\u0993\3\2\2\2\u0992\u0962")
        buf.write("\3\2\2\2\u0992\u0964\3\2\2\2\u0992\u0966\3\2\2\2\u0992")
        buf.write("\u096b\3\2\2\2\u0992\u096e\3\2\2\2\u0992\u0975\3\2\2\2")
        buf.write("\u0992\u0978\3\2\2\2\u0992\u097e\3\2\2\2\u0992\u0985\3")
        buf.write("\2\2\2\u0992\u098a\3\2\2\2\u0992\u098d\3\2\2\2\u0993\u0996")
        buf.write("\3\2\2\2\u0994\u0992\3\2\2\2\u0994\u0995\3\2\2\2\u0995")
        buf.write("\u01d1\3\2\2\2\u0996\u0994\3\2\2\2\u0997\u0998\7\u0088")
        buf.write("\2\2\u0998\u099e\7\u008b\2\2\u0999\u099a\7\u0088\2\2\u099a")
        buf.write("\u099b\5\u01d4\u00eb\2\u099b\u099c\7\u008b\2\2\u099c\u099e")
        buf.write("\3\2\2\2\u099d\u0997\3\2\2\2\u099d\u0999\3\2\2\2\u099e")
        buf.write("\u01d3\3\2\2\2\u099f\u09a4\5\u01d6\u00ec\2\u09a0\u09a1")
        buf.write("\7\u008d\2\2\u09a1\u09a3\5\u01d6\u00ec\2\u09a2\u09a0\3")
        buf.write("\2\2\2\u09a3\u09a6\3\2\2\2\u09a4\u09a2\3\2\2\2\u09a4\u09a5")
        buf.write("\3\2\2\2\u09a5\u01d5\3\2\2\2\u09a6\u09a4\3\2\2\2\u09a7")
        buf.write("\u09b2\5\u017e\u00c0\2\u09a8\u09a9\5\u020a\u0106\2\u09a9")
        buf.write("\u09aa\7\u008e\2\2\u09aa\u09ab\5\u017e\u00c0\2\u09ab\u09b2")
        buf.write("\3\2\2\2\u09ac\u09b2\5\u0226\u0114\2\u09ad\u09ae\5\u020a")
        buf.write("\u0106\2\u09ae\u09af\7\u008e\2\2\u09af\u09b0\5\u0226\u0114")
        buf.write("\2\u09b0\u09b2\3\2\2\2\u09b1\u09a7\3\2\2\2\u09b1\u09a8")
        buf.write("\3\2\2\2\u09b1\u09ac\3\2\2\2\u09b1\u09ad\3\2\2\2\u09b2")
        buf.write("\u01d7\3\2\2\2\u09b3\u09b4\5\u01ac\u00d7\2\u09b4\u01d9")
        buf.write("\3\2\2\2\u09b5\u09b9\5\u01dc\u00ef\2\u09b6\u09b8\5\u01dc")
        buf.write("\u00ef\2\u09b7\u09b6\3\2\2\2\u09b8\u09bb\3\2\2\2\u09b9")
        buf.write("\u09b7\3\2\2\2\u09b9\u09ba\3\2\2\2\u09ba\u01db\3\2\2\2")
        buf.write("\u09bb\u09b9\3\2\2\2\u09bc\u09bd\5\u020a\u0106\2\u09bd")
        buf.write("\u09be\7\u008e\2\2\u09be\u01dd\3\2\2\2\u09bf\u09c0\7p")
        buf.write("\2\2\u09c0\u09c1\7\u0088\2\2\u09c1\u09c2\7q\2\2\u09c2")
        buf.write("\u09c3\7\u008e\2\2\u09c3\u09c4\5\u017e\u00c0\2\u09c4\u09c5")
        buf.write("\7\u008b\2\2\u09c5\u01df\3\2\2\2\u09c6\u09c7\b\u00f1\1")
        buf.write("\2\u09c7\u09d0\5\u01fa\u00fe\2\u09c8\u09d0\5\u01fc\u00ff")
        buf.write("\2\u09c9\u09d0\5\u01f0\u00f9\2\u09ca\u09d0\5\u01e4\u00f3")
        buf.write("\2\u09cb\u09d0\5\u01e8\u00f5\2\u09cc\u09d0\5\u01fe\u0100")
        buf.write("\2\u09cd\u09d0\7t\2\2\u09ce\u09d0\7h\2\2\u09cf\u09c6\3")
        buf.write("\2\2\2\u09cf\u09c8\3\2\2\2\u09cf\u09c9\3\2\2\2\u09cf\u09ca")
        buf.write("\3\2\2\2\u09cf\u09cb\3\2\2\2\u09cf\u09cc\3\2\2\2\u09cf")
        buf.write("\u09cd\3\2\2\2\u09cf\u09ce\3\2\2\2\u09d0\u09dd\3\2\2\2")
        buf.write("\u09d1\u09d2\f\t\2\2\u09d2\u09dc\7\u0094\2\2\u09d3\u09d4")
        buf.write("\f\b\2\2\u09d4\u09dc\7\u0093\2\2\u09d5\u09d6\f\6\2\2\u09d6")
        buf.write("\u09d7\7\u0086\2\2\u09d7\u09dc\7r\2\2\u09d8\u09d9\f\5")
        buf.write("\2\2\u09d9\u09da\7\u0086\2\2\u09da\u09dc\7s\2\2\u09db")
        buf.write("\u09d1\3\2\2\2\u09db\u09d3\3\2\2\2\u09db\u09d5\3\2\2\2")
        buf.write("\u09db\u09d8\3\2\2\2\u09dc\u09df\3\2\2\2\u09dd\u09db\3")
        buf.write("\2\2\2\u09dd\u09de\3\2\2\2\u09de\u01e1\3\2\2\2\u09df\u09dd")
        buf.write("\3\2\2\2\u09e0\u09e2\7\u008e\2\2\u09e1\u09e3\5\u0176\u00bc")
        buf.write("\2\u09e2\u09e1\3\2\2\2\u09e2\u09e3\3\2\2\2\u09e3\u09e5")
        buf.write("\3\2\2\2\u09e4\u09e6\7u\2\2\u09e5\u09e4\3\2\2\2\u09e5")
        buf.write("\u09e6\3\2\2\2\u09e6\u09e7\3\2\2\2\u09e7\u09e8\5\u01e0")
        buf.write("\u00f1\2\u09e8\u01e3\3\2\2\2\u09e9\u09eb\5\u01e6\u00f4")
        buf.write("\2\u09ea\u09ec\5\u008aF\2\u09eb\u09ea\3\2\2\2\u09eb\u09ec")
        buf.write("\3\2\2\2\u09ec\u09ef\3\2\2\2\u09ed\u09ee\7\u0086\2\2\u09ee")
        buf.write("\u09f0\5\u01e4\u00f3\2\u09ef\u09ed\3\2\2\2\u09ef\u09f0")
        buf.write("\3\2\2\2\u09f0\u01e5\3\2\2\2\u09f1\u09f2\5\u0208\u0105")
        buf.write("\2\u09f2\u01e7\3\2\2\2\u09f3\u09f5\7\u0088\2\2\u09f4\u09f6")
        buf.write("\5\u01ea\u00f6\2\u09f5\u09f4\3\2\2\2\u09f5\u09f6\3\2\2")
        buf.write("\2\u09f6\u09f7\3\2\2\2\u09f7\u09f8\7\u008b\2\2\u09f8\u01e9")
        buf.write("\3\2\2\2\u09f9\u09ff\5\u01ec\u00f7\2\u09fa\u09fb\5\u01ec")
        buf.write("\u00f7\2\u09fb\u09fc\7\u008d\2\2\u09fc\u09fd\5\u01ea\u00f6")
        buf.write("\2\u09fd\u09ff\3\2\2\2\u09fe\u09f9\3\2\2\2\u09fe\u09fa")
        buf.write("\3\2\2\2\u09ff\u01eb\3\2\2\2\u0a00\u0a01\5\u01ee\u00f8")
        buf.write("\2\u0a01\u0a02\5\u01e2\u00f2\2\u0a02\u0a05\3\2\2\2\u0a03")
        buf.write("\u0a05\5\u01e0\u00f1\2\u0a04\u0a00\3\2\2\2\u0a04\u0a03")
        buf.write("\3\2\2\2\u0a05\u01ed\3\2\2\2\u0a06\u0a07\5\u020a\u0106")
        buf.write("\2\u0a07\u01ef\3\2\2\2\u0a08\u0a0a\5\u0176\u00bc\2\u0a09")
        buf.write("\u0a08\3\2\2\2\u0a09\u0a0a\3\2\2\2\u0a0a\u0a0b\3\2\2\2")
        buf.write("\u0a0b\u0a0d\5\u01f2\u00fa\2\u0a0c\u0a0e\7.\2\2\u0a0d")
        buf.write("\u0a0c\3\2\2\2\u0a0d\u0a0e\3\2\2\2\u0a0e\u0a0f\3\2\2\2")
        buf.write("\u0a0f\u0a10\5\u021a\u010e\2\u0a10\u0a11\5\u01e0\u00f1")
        buf.write("\2\u0a11\u0a1b\3\2\2\2\u0a12\u0a14\5\u0176\u00bc\2\u0a13")
        buf.write("\u0a12\3\2\2\2\u0a13\u0a14\3\2\2\2\u0a14\u0a15\3\2\2\2")
        buf.write("\u0a15\u0a16\5\u01f2\u00fa\2\u0a16\u0a17\7/\2\2\u0a17")
        buf.write("\u0a18\5\u021a\u010e\2\u0a18\u0a19\5\u01e0\u00f1\2\u0a19")
        buf.write("\u0a1b\3\2\2\2\u0a1a\u0a09\3\2\2\2\u0a1a\u0a13\3\2\2\2")
        buf.write("\u0a1b\u01f1\3\2\2\2\u0a1c\u0a1d\7\u0088\2\2\u0a1d\u0a26")
        buf.write("\7\u008b\2\2\u0a1e\u0a1f\7\u0088\2\2\u0a1f\u0a21\5\u01f4")
        buf.write("\u00fb\2\u0a20\u0a22\5\u021c\u010f\2\u0a21\u0a20\3\2\2")
        buf.write("\2\u0a21\u0a22\3\2\2\2\u0a22\u0a23\3\2\2\2\u0a23\u0a24")
        buf.write("\7\u008b\2\2\u0a24\u0a26\3\2\2\2\u0a25\u0a1c\3\2\2\2\u0a25")
        buf.write("\u0a1e\3\2\2\2\u0a26\u01f3\3\2\2\2\u0a27\u0a2d\5\u01f6")
        buf.write("\u00fc\2\u0a28\u0a29\5\u01f6\u00fc\2\u0a29\u0a2a\7\u008d")
        buf.write("\2\2\u0a2a\u0a2b\5\u01f4\u00fb\2\u0a2b\u0a2d\3\2\2\2\u0a2c")
        buf.write("\u0a27\3\2\2\2\u0a2c\u0a28\3\2\2\2\u0a2d\u01f5\3\2\2\2")
        buf.write("\u0a2e\u0a30\5\u0176\u00bc\2\u0a2f\u0a2e\3\2\2\2\u0a2f")
        buf.write("\u0a30\3\2\2\2\u0a30\u0a32\3\2\2\2\u0a31\u0a33\7u\2\2")
        buf.write("\u0a32\u0a31\3\2\2\2\u0a32\u0a33\3\2\2\2\u0a33\u0a34\3")
        buf.write("\2\2\2\u0a34\u0a39\5\u01e0\u00f1\2\u0a35\u0a36\5\u01f8")
        buf.write("\u00fd\2\u0a36\u0a37\5\u01e2\u00f2\2\u0a37\u0a39\3\2\2")
        buf.write("\2\u0a38\u0a2f\3\2\2\2\u0a38\u0a35\3\2\2\2\u0a39\u01f7")
        buf.write("\3\2\2\2\u0a3a\u0a3b\5\u020a\u0106\2\u0a3b\u01f9\3\2\2")
        buf.write("\2\u0a3c\u0a3d\7\u0089\2\2\u0a3d\u0a3e\5\u01e0\u00f1\2")
        buf.write("\u0a3e\u0a3f\7\u008c\2\2\u0a3f\u01fb\3\2\2\2\u0a40\u0a41")
        buf.write("\7\u0089\2\2\u0a41\u0a42\5\u01e0\u00f1\2\u0a42\u0a43\7")
        buf.write("\u008e\2\2\u0a43\u0a44\5\u01e0\u00f1\2\u0a44\u0a45\7\u008c")
        buf.write("\2\2\u0a45\u01fd\3\2\2\2\u0a46\u0a49\5\u0200\u0101\2\u0a47")
        buf.write("\u0a48\7\u0096\2\2\u0a48\u0a4a\5\u0200\u0101\2\u0a49\u0a47")
        buf.write("\3\2\2\2\u0a4a\u0a4b\3\2\2\2\u0a4b\u0a49\3\2\2\2\u0a4b")
        buf.write("\u0a4c\3\2\2\2\u0a4c\u01ff\3\2\2\2\u0a4d\u0a4e\5\u01e4")
        buf.write("\u00f3\2\u0a4e\u0201\3\2\2\2\u0a4f\u0a50\7\u008e\2\2\u0a50")
        buf.write("\u0a51\5\u0206\u0104\2\u0a51\u0a52\7\u008d\2\2\u0a52\u0a53")
        buf.write("\5\u0204\u0103\2\u0a53\u0a59\3\2\2\2\u0a54\u0a55\7\u008e")
        buf.write("\2\2\u0a55\u0a59\5\u0206\u0104\2\u0a56\u0a57\7\u008e\2")
        buf.write("\2\u0a57\u0a59\5\u0204\u0103\2\u0a58\u0a4f\3\2\2\2\u0a58")
        buf.write("\u0a54\3\2\2\2\u0a58\u0a56\3\2\2\2\u0a59\u0203\3\2\2\2")
        buf.write("\u0a5a\u0a60\5\u01e4\u00f3\2\u0a5b\u0a5c\5\u01e4\u00f3")
        buf.write("\2\u0a5c\u0a5d\7\u008d\2\2\u0a5d\u0a5e\5\u0204\u0103\2")
        buf.write("\u0a5e\u0a60\3\2\2\2\u0a5f\u0a5a\3\2\2\2\u0a5f\u0a5b\3")
        buf.write("\2\2\2\u0a60\u0205\3\2\2\2\u0a61\u0a62\7&\2\2\u0a62\u0207")
        buf.write("\3\2\2\2\u0a63\u0a66\7\u0085\2\2\u0a64\u0a66\5\u020c\u0107")
        buf.write("\2\u0a65\u0a63\3\2\2\2\u0a65\u0a64\3\2\2\2\u0a66\u0209")
        buf.write("\3\2\2\2\u0a67\u0a6a\7\u0085\2\2\u0a68\u0a6a\5\u020e\u0108")
        buf.write("\2\u0a69\u0a67\3\2\2\2\u0a69\u0a68\3\2\2\2\u0a6a\u020b")
        buf.write("\3\2\2\2\u0a6b\u0a6c\t\b\2\2\u0a6c\u020d\3\2\2\2\u0a6d")
        buf.write("\u0a6e\t\t\2\2\u0a6e\u020f\3\2\2\2\u0a6f\u0a70\6\u0109")
        buf.write("\27\2\u0a70\u0a71\7\u0098\2\2\u0a71\u0211\3\2\2\2\u0a72")
        buf.write("\u0a73\6\u010a\30\2\u0a73\u0a74\7\u0097\2\2\u0a74\u0213")
        buf.write("\3\2\2\2\u0a75\u0a76\6\u010b\31\2\u0a76\u0a77\7\u0096")
        buf.write("\2\2\u0a77\u0a78\7\u0096\2\2\u0a78\u0215\3\2\2\2\u0a79")
        buf.write("\u0a7a\6\u010c\32\2\u0a7a\u0a7b\7\u0099\2\2\u0a7b\u0a7c")
        buf.write("\7\u0099\2\2\u0a7c\u0217\3\2\2\2\u0a7d\u0a7e\6\u010d\33")
        buf.write("\2\u0a7e\u0a7f\7\u0091\2\2\u0a7f\u0a80\7\u0098\2\2\u0a80")
        buf.write("\u0219\3\2\2\2\u0a81\u0a82\6\u010e\34\2\u0a82\u0a83\7")
        buf.write("\u0097\2\2\u0a83\u0a84\7\u0091\2\2\u0a84\u021b\3\2\2\2")
        buf.write("\u0a85\u0a86\6\u010f\35\2\u0a86\u0a87\7\u0086\2\2\u0a87")
        buf.write("\u0a88\7\u0086\2\2\u0a88\u0a89\7\u0086\2\2\u0a89\u021d")
        buf.write("\3\2\2\2\u0a8a\u0a8b\6\u0110\36\2\u0a8b\u0a8c\7\u0098")
        buf.write("\2\2\u0a8c\u0a8d\7\u0098\2\2\u0a8d\u021f\3\2\2\2\u0a8e")
        buf.write("\u0a8f\6\u0111\37\2\u0a8f\u0a90\5\u0226\u0114\2\u0a90")
        buf.write("\u0221\3\2\2\2\u0a91\u0a92\6\u0112 \2\u0a92\u0a93\5\u0226")
        buf.write("\u0114\2\u0a93\u0223\3\2\2\2\u0a94\u0a95\6\u0113!\2\u0a95")
        buf.write("\u0a96\5\u0226\u0114\2\u0a96\u0225\3\2\2\2\u0a97\u0a9c")
        buf.write("\5\u022a\u0116\2\u0a98\u0a99\6\u0114\"\2\u0a99\u0a9b\5")
        buf.write("\u0228\u0115\2\u0a9a\u0a98\3\2\2\2\u0a9b\u0a9e\3\2\2\2")
        buf.write("\u0a9c\u0a9a\3\2\2\2\u0a9c\u0a9d\3\2\2\2\u0a9d\u0aa8\3")
        buf.write("\2\2\2\u0a9e\u0a9c\3\2\2\2\u0a9f\u0aa4\5\u022c\u0117\2")
        buf.write("\u0aa0\u0aa1\6\u0114#\2\u0aa1\u0aa3\5\u022e\u0118\2\u0aa2")
        buf.write("\u0aa0\3\2\2\2\u0aa3\u0aa6\3\2\2\2\u0aa4\u0aa2\3\2\2\2")
        buf.write("\u0aa4\u0aa5\3\2\2\2\u0aa5\u0aa8\3\2\2\2\u0aa6\u0aa4\3")
        buf.write("\2\2\2\u0aa7\u0a97\3\2\2\2\u0aa7\u0a9f\3\2\2\2\u0aa8\u0227")
        buf.write("\3\2\2\2\u0aa9\u0aac\5\u022a\u0116\2\u0aaa\u0aac\7\u00a1")
        buf.write("\2\2\u0aab\u0aa9\3\2\2\2\u0aab\u0aaa\3\2\2\2\u0aac\u0229")
        buf.write("\3\2\2\2\u0aad\u0ab0\t\n\2\2\u0aae\u0ab0\7\u00a0\2\2\u0aaf")
        buf.write("\u0aad\3\2\2\2\u0aaf\u0aae\3\2\2\2\u0ab0\u022b\3\2\2\2")
        buf.write("\u0ab1\u0ab2\7\u0086\2\2\u0ab2\u022d\3\2\2\2\u0ab3\u0ab6")
        buf.write("\7\u0086\2\2\u0ab4\u0ab6\5\u0228\u0115\2\u0ab5\u0ab3\3")
        buf.write("\2\2\2\u0ab5\u0ab4\3\2\2\2\u0ab6\u022f\3\2\2\2\u0ab7\u0abc")
        buf.write("\5\u0232\u011a\2\u0ab8\u0abc\5\u023a\u011e\2\u0ab9\u0abc")
        buf.write("\5\u0234\u011b\2\u0aba\u0abc\5\u0236\u011c\2\u0abb\u0ab7")
        buf.write("\3\2\2\2\u0abb\u0ab8\3\2\2\2\u0abb\u0ab9\3\2\2\2\u0abb")
        buf.write("\u0aba\3\2\2\2\u0abc\u0231\3\2\2\2\u0abd\u0abf\5\u0212")
        buf.write("\u010a\2\u0abe\u0abd\3\2\2\2\u0abe\u0abf\3\2\2\2\u0abf")
        buf.write("\u0ac0\3\2\2\2\u0ac0\u0ac6\5\u0238\u011d\2\u0ac1\u0ac3")
        buf.write("\5\u0212\u010a\2\u0ac2\u0ac1\3\2\2\2\u0ac2\u0ac3\3\2\2")
        buf.write("\2\u0ac3\u0ac4\3\2\2\2\u0ac4\u0ac6\7\u00a8\2\2\u0ac5\u0abe")
        buf.write("\3\2\2\2\u0ac5\u0ac2\3\2\2\2\u0ac6\u0233\3\2\2\2\u0ac7")
        buf.write("\u0ac8\t\13\2\2\u0ac8\u0235\3\2\2\2\u0ac9\u0aca\7\u0082")
        buf.write("\2\2\u0aca\u0237\3\2\2\2\u0acb\u0acc\t\f\2\2\u0acc\u0239")
        buf.write("\3\2\2\2\u0acd\u0ace\t\r\2\2\u0ace\u023b\3\2\2\2\u0141")
        buf.write("\u023d\u0243\u0247\u024b\u024f\u0253\u0257\u025b\u025f")
        buf.write("\u0263\u0265\u026d\u0273\u0277\u027b\u027f\u0285\u0289")
        buf.write("\u028d\u0291\u0295\u0299\u029f\u02ac\u02b3\u02b9\u02c3")
        buf.write("\u02cd\u02d3\u02d9\u02e4\u02ea\u02f2\u02fa\u02fe\u0303")
        buf.write("\u0319\u0325\u0329\u032d\u0333\u033e\u0342\u0346\u0349")
        buf.write("\u034f\u0353\u0356\u035d\u0362\u0367\u036b\u037f\u0389")
        buf.write("\u038b\u039e\u03b6\u03c6\u03d4\u03e0\u03ea\u03ef\u03f9")
        buf.write("\u0408\u041d\u0422\u0425\u0429\u042e\u0432\u043d\u0442")
        buf.write("\u0445\u0448\u0452\u0457\u046f\u0478\u047f\u0482\u0485")
        buf.write("\u048e\u0497\u049a\u049d\u04a3\u04a6\u04aa\u04b5\u04be")
        buf.write("\u04c1\u04c4\u04c9\u04cc\u04d3\u04dc\u04df\u04e3\u04e8")
        buf.write("\u04ec\u04f1\u04f4\u04f9\u0505\u0509\u050c\u050f\u0512")
        buf.write("\u0518\u051c\u051f\u0524\u0526\u052a\u0536\u053d\u0541")
        buf.write("\u0546\u0549\u054f\u0555\u055f\u0562\u0566\u0569\u056c")
        buf.write("\u056f\u0574\u0577\u057a\u057e\u0584\u0589\u058c\u058f")
        buf.write("\u0599\u059d\u05a6\u05aa\u05b2\u05b7\u05ba\u05c4\u05c8")
        buf.write("\u05d0\u05d3\u05d6\u05db\u05de\u05e1\u05eb\u05f2\u05f5")
        buf.write("\u05f8\u05fb\u0600\u0603\u0606\u060b\u060e\u0612\u0617")
        buf.write("\u061a\u061d\u0621\u0629\u0630\u0633\u0636\u063b\u0645")
        buf.write("\u064c\u0654\u065e\u0662\u0666\u066a\u066d\u0671\u0676")
        buf.write("\u0678\u067f\u0682\u0687\u068a\u068e\u0692\u0695\u069b")
        buf.write("\u06a0\u06a4\u06a7\u06aa\u06ae\u06b1\u06b6\u06b9\u06bd")
        buf.write("\u06c2\u06c8\u06cb\u06d0\u06d5\u06d8\u06df\u06e5\u06ec")
        buf.write("\u06fa\u06fd\u0700\u0707\u070e\u071c\u0727\u072f\u0737")
        buf.write("\u0748\u0765\u076a\u0785\u078c\u0790\u0795\u079c\u07a3")
        buf.write("\u07ae\u07b2\u07bb\u07c1\u07c6\u07d0\u07db\u07e0\u07f4")
        buf.write("\u07fc\u07ff\u0803\u080a\u0812\u081c\u0823\u0829\u082e")
        buf.write("\u0833\u0837\u0846\u084a\u0856\u0860\u0864\u086a\u0870")
        buf.write("\u087b\u087f\u0885\u08ac\u08c1\u08c6\u08d7\u08da\u08df")
        buf.write("\u08e3\u08e6\u08ed\u08f6\u08fd\u0905\u090a\u0910\u091d")
        buf.write("\u0921\u0936\u093a\u0941\u0956\u0960\u0968\u097c\u0992")
        buf.write("\u0994\u099d\u09a4\u09b1\u09b9\u09cf\u09db\u09dd\u09e2")
        buf.write("\u09e5\u09eb\u09ef\u09f5\u09fe\u0a04\u0a09\u0a0d\u0a13")
        buf.write("\u0a1a\u0a21\u0a25\u0a2c\u0a2f\u0a32\u0a38\u0a4b\u0a58")
        buf.write("\u0a5f\u0a65\u0a69\u0a9c\u0aa4\u0aa7\u0aab\u0aaf\u0ab5")
        buf.write("\u0abb\u0abe\u0ac2\u0ac5")
        return buf.getvalue()


@PARSERS.register('swift')
class Swift3Parser ( Parser ):

    grammarFileName = "Swift3.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'for'", "'case'", "'in'", "'while'",
                     "'let'", "'var'", "'repeat'", "'if'", "'else'", "'guard'",
                     "'switch'", "'default'", "'where'", "'break'", "'continue'",
                     "'fallthrough'", "'return'", "'throw'", "'defer'",
                     "'do'", "'catch'", "'#if'", "'#elseif'", "'#else'",
                     "'#endif'", "'os'", "'arch'", "'swift'", "'#sourceLocation'",
                     "'file'", "'line'", "'#available'", "'import'", "'typealias'",
                     "'struct'", "'class'", "'enum'", "'protocol'", "'func'",
                     "'get'", "'set'", "'willSet'", "'didSet'", "'throws'",
                     "'rethrows'", "'indirect'", "'final'", "'associatedtype'",
                     "'init'", "'deinit'", "'extension'", "'subscript'",
                     "'prefix'", "'operator'", "'postfix'", "'infix'", "'precedencegroup'",
                     "'higherThan'", "'lowerThan'", "'assignment'", "'associativity'",
                     "'left'", "'right'", "'none'", "'convenience'", "'dynamic'",
                     "'lazy'", "'optional'", "'override'", "'required'",
                     "'static'", "'unowned'", "'safe'", "'unsafe'", "'weak'",
                     "'private'", "'fileprivate'", "'internal'", "'public'",
                     "'open'", "'mutating'", "'nonmutating'", "'is'", "'as'",
                     "'#'", "'`'", "'try'", "'#file'", "'#line'", "'#column'",
                     "'#function'", "'#dsohandle'", "'#colorLiteral'", "'red'",
                     "'green'", "'blue'", "'alpha'", "'#fileLiteral'", "'resourceName'",
                     "'#imageLiteral'", "'self'", "'Self'", "'super'", "'unowned(safe)'",
                     "'unowned(unsafe)'", "'#selector'", "'getter:'", "'setter:'",
                     "'#keyPath'", "'type'", "'of'", "'Type'", "'Protocol'",
                     "'Any'", "'inout'", "'arm'", "'arm64'", "'i386'", "'iOS'",
                     "'iOSApplicationExtension'", "'macOS'", "'macOSApplicationExtension'",
                     "'precedence'", "'tvOS'", "'watchOS'", "'x86_64'",
                     "'false'", "'nil'", "'true'", "<INVALID>", "<INVALID>",
                     "'.'", "'{'", "'('", "'['", "'}'", "')'", "']'", "','",
                     "':'", "';'", "'<'", "'>'", "'_'", "'!'", "'?'", "'@'",
                     "'&'", "'-'", "'='", "'|'", "'/'", "'+'", "'*'", "'%'",
                     "'^'", "'~'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>",
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>",
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>",
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>",
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>",
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>",
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>",
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>",
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>",
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>",
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>",
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>",
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>",
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>",
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>",
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>",
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>",
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>",
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>",
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>",
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>",
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>",
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>",
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>",
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>",
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>",
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>",
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>",
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>",
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>",
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>",
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>",
                      "<INVALID>", "<INVALID>", "Platform_name_platform_version",
                      "Identifier", "DOT", "LCURLY", "LPAREN", "LBRACK",
                      "RCURLY", "RPAREN", "RBRACK", "COMMA", "COLON", "SEMI",
                      "LT", "GT", "UNDERSCORE", "BANG", "QUESTION", "AT",
                      "AND", "SUB", "EQUAL", "OR", "DIV", "ADD", "MUL",
                      "MOD", "CARET", "TILDE", "Operator_head_other", "Operator_following_character",
                      "Implicit_parameter_name", "Binary_literal", "Octal_literal",
                      "Decimal_literal", "Pure_decimal_digits", "Hexadecimal_literal",
                      "Floating_point_literal", "Static_string_literal",
                      "Interpolated_string_literal", "WS", "Block_comment",
                      "Line_comment" ]

    RULE_top_level = 0
    RULE_statement = 1
    RULE_statements = 2
    RULE_statements_impl = 3
    RULE_loop_statement = 4
    RULE_for_statement = 5
    RULE_for_init = 6
    RULE_for_in_statement = 7
    RULE_while_statement = 8
    RULE_condition_list = 9
    RULE_condition = 10
    RULE_case_condition = 11
    RULE_optional_binding_condition = 12
    RULE_repeat_while_statement = 13
    RULE_branch_statement = 14
    RULE_if_statement = 15
    RULE_else_clause = 16
    RULE_guard_statement = 17
    RULE_switch_statement = 18
    RULE_switch_cases = 19
    RULE_switch_case = 20
    RULE_case_label = 21
    RULE_case_item_list = 22
    RULE_default_label = 23
    RULE_where_clause = 24
    RULE_where_expression = 25
    RULE_labeled_statement = 26
    RULE_statement_label = 27
    RULE_label_name = 28
    RULE_control_transfer_statement = 29
    RULE_break_statement = 30
    RULE_continue_statement = 31
    RULE_fallthrough_statement = 32
    RULE_return_statement = 33
    RULE_throw_statement = 34
    RULE_defer_statement = 35
    RULE_do_statement = 36
    RULE_catch_clauses = 37
    RULE_catch_clause = 38
    RULE_compiler_control_statement = 39
    RULE_conditional_compilation_block = 40
    RULE_if_directive_clause = 41
    RULE_elseif_directive_clauses = 42
    RULE_elseif_directive_clause = 43
    RULE_else_directive_clause = 44
    RULE_if_directive = 45
    RULE_elseif_directive = 46
    RULE_else_directive = 47
    RULE_endif_directive = 48
    RULE_compilation_condition = 49
    RULE_platform_condition = 50
    RULE_swift_version = 51
    RULE_operating_system = 52
    RULE_architecture = 53
    RULE_line_control_statement = 54
    RULE_line_number = 55
    RULE_file_name = 56
    RULE_availability_condition = 57
    RULE_availability_arguments = 58
    RULE_availability_argument = 59
    RULE_generic_parameter_clause = 60
    RULE_generic_parameter_list = 61
    RULE_generic_parameter = 62
    RULE_generic_where_clause = 63
    RULE_requirement_list = 64
    RULE_requirement = 65
    RULE_conformance_requirement = 66
    RULE_same_type_requirement = 67
    RULE_generic_argument_clause = 68
    RULE_generic_argument_list = 69
    RULE_generic_argument = 70
    RULE_declaration = 71
    RULE_declarations = 72
    RULE_top_level_declaration = 73
    RULE_code_block = 74
    RULE_import_declaration = 75
    RULE_import_kind = 76
    RULE_import_path = 77
    RULE_import_path_identifier = 78
    RULE_constant_declaration = 79
    RULE_pattern_initializer_list = 80
    RULE_pattern_initializer = 81
    RULE_initializer = 82
    RULE_variable_declaration = 83
    RULE_variable_declaration_head = 84
    RULE_variable_name = 85
    RULE_getter_setter_block = 86
    RULE_getter_clause = 87
    RULE_setter_clause = 88
    RULE_setter_name = 89
    RULE_getter_setter_keyword_block = 90
    RULE_getter_keyword_clause = 91
    RULE_setter_keyword_clause = 92
    RULE_willSet_didSet_block = 93
    RULE_willSet_clause = 94
    RULE_didSet_clause = 95
    RULE_typealias_declaration = 96
    RULE_typealias_name = 97
    RULE_typealias_assignment = 98
    RULE_function_declaration = 99
    RULE_function_head = 100
    RULE_function_name = 101
    RULE_function_signature = 102
    RULE_function_result = 103
    RULE_function_body = 104
    RULE_parameter_clause = 105
    RULE_parameter_list = 106
    RULE_parameter = 107
    RULE_external_parameter_name = 108
    RULE_local_parameter_name = 109
    RULE_default_argument_clause = 110
    RULE_enum_declaration = 111
    RULE_union_style_enum = 112
    RULE_union_style_enum_members = 113
    RULE_union_style_enum_member = 114
    RULE_union_style_enum_case_clause = 115
    RULE_union_style_enum_case_list = 116
    RULE_union_style_enum_case = 117
    RULE_enum_name = 118
    RULE_enum_case_name = 119
    RULE_raw_value_style_enum = 120
    RULE_raw_value_style_enum_members = 121
    RULE_raw_value_style_enum_member = 122
    RULE_raw_value_style_enum_case_clause = 123
    RULE_raw_value_style_enum_case_list = 124
    RULE_raw_value_style_enum_case = 125
    RULE_raw_value_assignment = 126
    RULE_raw_value_literal = 127
    RULE_struct_declaration = 128
    RULE_struct_name = 129
    RULE_struct_body = 130
    RULE_struct_member = 131
    RULE_class_declaration = 132
    RULE_class_name = 133
    RULE_class_body = 134
    RULE_class_member = 135
    RULE_protocol_declaration = 136
    RULE_protocol_name = 137
    RULE_protocol_body = 138
    RULE_protocol_member = 139
    RULE_protocol_member_declaration = 140
    RULE_protocol_property_declaration = 141
    RULE_protocol_method_declaration = 142
    RULE_protocol_initializer_declaration = 143
    RULE_protocol_subscript_declaration = 144
    RULE_protocol_associated_type_declaration = 145
    RULE_initializer_declaration = 146
    RULE_initializer_head = 147
    RULE_initializer_body = 148
    RULE_deinitializer_declaration = 149
    RULE_extension_declaration = 150
    RULE_extension_body = 151
    RULE_extension_member = 152
    RULE_subscript_declaration = 153
    RULE_subscript_head = 154
    RULE_subscript_result = 155
    RULE_operator_declaration = 156
    RULE_prefix_operator_declaration = 157
    RULE_postfix_operator_declaration = 158
    RULE_infix_operator_declaration = 159
    RULE_infix_operator_group = 160
    RULE_precedence_group_declaration = 161
    RULE_precedence_group_attribute = 162
    RULE_precedence_group_relation = 163
    RULE_precedence_group_assignment = 164
    RULE_precedence_group_associativity = 165
    RULE_associativity = 166
    RULE_precedence_group_names = 167
    RULE_precedence_group_name = 168
    RULE_declaration_modifier = 169
    RULE_declaration_modifiers = 170
    RULE_access_level_modifier = 171
    RULE_mutation_modifier = 172
    RULE_pattern = 173
    RULE_wildcard_pattern = 174
    RULE_identifier_pattern = 175
    RULE_value_binding_pattern = 176
    RULE_tuple_pattern = 177
    RULE_tuple_pattern_element_list = 178
    RULE_tuple_pattern_element = 179
    RULE_enum_case_pattern = 180
    RULE_optional_pattern = 181
    RULE_expression_pattern = 182
    RULE_attribute = 183
    RULE_attribute_name = 184
    RULE_attribute_argument_clause = 185
    RULE_attributes = 186
    RULE_balanced_tokens = 187
    RULE_balanced_token = 188
    RULE_any_punctuation_for_balanced_token = 189
    RULE_expression = 190
    RULE_expression_list = 191
    RULE_prefix_expression = 192
    RULE_in_out_expression = 193
    RULE_try_operator = 194
    RULE_binary_expression = 195
    RULE_binary_expressions = 196
    RULE_conditional_operator = 197
    RULE_type_casting_operator = 198
    RULE_primary_expression = 199
    RULE_literal_expression = 200
    RULE_array_literal = 201
    RULE_array_literal_items = 202
    RULE_array_literal_item = 203
    RULE_dictionary_literal = 204
    RULE_dictionary_literal_items = 205
    RULE_dictionary_literal_item = 206
    RULE_playground_literal = 207
    RULE_self_expression = 208
    RULE_superclass_expression = 209
    RULE_superclass_method_expression = 210
    RULE_superclass_subscript_expression = 211
    RULE_superclass_initializer_expression = 212
    RULE_closure_expression = 213
    RULE_closure_signature = 214
    RULE_closure_parameter_clause = 215
    RULE_closure_parameter_clause_identifier_list = 216
    RULE_closure_parameter_list = 217
    RULE_closure_parameter = 218
    RULE_closure_parameter_name = 219
    RULE_capture_list = 220
    RULE_capture_list_items = 221
    RULE_capture_list_item = 222
    RULE_capture_specifier = 223
    RULE_implicit_member_expression = 224
    RULE_parenthesized_expression = 225
    RULE_tuple_expression = 226
    RULE_tuple_element = 227
    RULE_wildcard_expression = 228
    RULE_selector_expression = 229
    RULE_key_path_expression = 230
    RULE_postfix_expression = 231
    RULE_function_call_argument_clause = 232
    RULE_function_call_argument_list = 233
    RULE_function_call_argument = 234
    RULE_trailing_closure = 235
    RULE_argument_names = 236
    RULE_argument_name = 237
    RULE_dynamic_type_expression = 238
    RULE_type = 239
    RULE_type_annotation = 240
    RULE_type_identifier = 241
    RULE_type_name = 242
    RULE_tuple_type = 243
    RULE_tuple_type_element_list = 244
    RULE_tuple_type_element = 245
    RULE_element_name = 246
    RULE_function_type = 247
    RULE_function_type_argument_clause = 248
    RULE_function_type_argument_list = 249
    RULE_function_type_argument = 250
    RULE_argument_label = 251
    RULE_array_type = 252
    RULE_dictionary_type = 253
    RULE_protocol_composition_type = 254
    RULE_protocol_identifier = 255
    RULE_type_inheritance_clause = 256
    RULE_type_inheritance_list = 257
    RULE_class_requirement = 258
    RULE_declaration_identifier = 259
    RULE_label_identifier = 260
    RULE_keyword_as_identifier_in_declarations = 261
    RULE_keyword_as_identifier_in_labels = 262
    RULE_assignment_operator = 263
    RULE_negate_prefix_operator = 264
    RULE_compilation_condition_AND = 265
    RULE_compilation_condition_OR = 266
    RULE_compilation_condition_GE = 267
    RULE_arrow_operator = 268
    RULE_range_operator = 269
    RULE_same_type_equals = 270
    RULE_binary_operator = 271
    RULE_prefix_operator = 272
    RULE_postfix_operator = 273
    RULE_operator = 274
    RULE_operator_character = 275
    RULE_operator_head = 276
    RULE_dot_operator_head = 277
    RULE_dot_operator_character = 278
    RULE_literal = 279
    RULE_numeric_literal = 280
    RULE_boolean_literal = 281
    RULE_nil_literal = 282
    RULE_integer_literal = 283
    RULE_string_literal = 284

    ruleNames =  [ "top_level", "statement", "statements", "statements_impl",
                   "loop_statement", "for_statement", "for_init", "for_in_statement",
                   "while_statement", "condition_list", "condition", "case_condition",
                   "optional_binding_condition", "repeat_while_statement",
                   "branch_statement", "if_statement", "else_clause", "guard_statement",
                   "switch_statement", "switch_cases", "switch_case", "case_label",
                   "case_item_list", "default_label", "where_clause", "where_expression",
                   "labeled_statement", "statement_label", "label_name",
                   "control_transfer_statement", "break_statement", "continue_statement",
                   "fallthrough_statement", "return_statement", "throw_statement",
                   "defer_statement", "do_statement", "catch_clauses", "catch_clause",
                   "compiler_control_statement", "conditional_compilation_block",
                   "if_directive_clause", "elseif_directive_clauses", "elseif_directive_clause",
                   "else_directive_clause", "if_directive", "elseif_directive",
                   "else_directive", "endif_directive", "compilation_condition",
                   "platform_condition", "swift_version", "operating_system",
                   "architecture", "line_control_statement", "line_number",
                   "file_name", "availability_condition", "availability_arguments",
                   "availability_argument", "generic_parameter_clause",
                   "generic_parameter_list", "generic_parameter", "generic_where_clause",
                   "requirement_list", "requirement", "conformance_requirement",
                   "same_type_requirement", "generic_argument_clause", "generic_argument_list",
                   "generic_argument", "declaration", "declarations", "top_level_declaration",
                   "code_block", "import_declaration", "import_kind", "import_path",
                   "import_path_identifier", "constant_declaration", "pattern_initializer_list",
                   "pattern_initializer", "initializer", "variable_declaration",
                   "variable_declaration_head", "variable_name", "getter_setter_block",
                   "getter_clause", "setter_clause", "setter_name", "getter_setter_keyword_block",
                   "getter_keyword_clause", "setter_keyword_clause", "willSet_didSet_block",
                   "willSet_clause", "didSet_clause", "typealias_declaration",
                   "typealias_name", "typealias_assignment", "function_declaration",
                   "function_head", "function_name", "function_signature",
                   "function_result", "function_body", "parameter_clause",
                   "parameter_list", "parameter", "external_parameter_name",
                   "local_parameter_name", "default_argument_clause", "enum_declaration",
                   "union_style_enum", "union_style_enum_members", "union_style_enum_member",
                   "union_style_enum_case_clause", "union_style_enum_case_list",
                   "union_style_enum_case", "enum_name", "enum_case_name",
                   "raw_value_style_enum", "raw_value_style_enum_members",
                   "raw_value_style_enum_member", "raw_value_style_enum_case_clause",
                   "raw_value_style_enum_case_list", "raw_value_style_enum_case",
                   "raw_value_assignment", "raw_value_literal", "struct_declaration",
                   "struct_name", "struct_body", "struct_member", "class_declaration",
                   "class_name", "class_body", "class_member", "protocol_declaration",
                   "protocol_name", "protocol_body", "protocol_member",
                   "protocol_member_declaration", "protocol_property_declaration",
                   "protocol_method_declaration", "protocol_initializer_declaration",
                   "protocol_subscript_declaration", "protocol_associated_type_declaration",
                   "initializer_declaration", "initializer_head", "initializer_body",
                   "deinitializer_declaration", "extension_declaration",
                   "extension_body", "extension_member", "subscript_declaration",
                   "subscript_head", "subscript_result", "operator_declaration",
                   "prefix_operator_declaration", "postfix_operator_declaration",
                   "infix_operator_declaration", "infix_operator_group",
                   "precedence_group_declaration", "precedence_group_attribute",
                   "precedence_group_relation", "precedence_group_assignment",
                   "precedence_group_associativity", "associativity", "precedence_group_names",
                   "precedence_group_name", "declaration_modifier", "declaration_modifiers",
                   "access_level_modifier", "mutation_modifier", "pattern",
                   "wildcard_pattern", "identifier_pattern", "value_binding_pattern",
                   "tuple_pattern", "tuple_pattern_element_list", "tuple_pattern_element",
                   "enum_case_pattern", "optional_pattern", "expression_pattern",
                   "attribute", "attribute_name", "attribute_argument_clause",
                   "attributes", "balanced_tokens", "balanced_token", "any_punctuation_for_balanced_token",
                   "expression", "expression_list", "prefix_expression",
                   "in_out_expression", "try_operator", "binary_expression",
                   "binary_expressions", "conditional_operator", "type_casting_operator",
                   "primary_expression", "literal_expression", "array_literal",
                   "array_literal_items", "array_literal_item", "dictionary_literal",
                   "dictionary_literal_items", "dictionary_literal_item",
                   "playground_literal", "self_expression", "superclass_expression",
                   "superclass_method_expression", "superclass_subscript_expression",
                   "superclass_initializer_expression", "closure_expression",
                   "closure_signature", "closure_parameter_clause", "closure_parameter_clause_identifier_list",
                   "closure_parameter_list", "closure_parameter", "closure_parameter_name",
                   "capture_list", "capture_list_items", "capture_list_item",
                   "capture_specifier", "implicit_member_expression", "parenthesized_expression",
                   "tuple_expression", "tuple_element", "wildcard_expression",
                   "selector_expression", "key_path_expression", "postfix_expression",
                   "function_call_argument_clause", "function_call_argument_list",
                   "function_call_argument", "trailing_closure", "argument_names",
                   "argument_name", "dynamic_type_expression", "type", "type_annotation",
                   "type_identifier", "type_name", "tuple_type", "tuple_type_element_list",
                   "tuple_type_element", "element_name", "function_type",
                   "function_type_argument_clause", "function_type_argument_list",
                   "function_type_argument", "argument_label", "array_type",
                   "dictionary_type", "protocol_composition_type", "protocol_identifier",
                   "type_inheritance_clause", "type_inheritance_list", "class_requirement",
                   "declaration_identifier", "label_identifier", "keyword_as_identifier_in_declarations",
                   "keyword_as_identifier_in_labels", "assignment_operator",
                   "negate_prefix_operator", "compilation_condition_AND",
                   "compilation_condition_OR", "compilation_condition_GE",
                   "arrow_operator", "range_operator", "same_type_equals",
                   "binary_operator", "prefix_operator", "postfix_operator",
                   "operator", "operator_character", "operator_head", "dot_operator_head",
                   "dot_operator_character", "literal", "numeric_literal",
                   "boolean_literal", "nil_literal", "integer_literal",
                   "string_literal" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    T__17=18
    T__18=19
    T__19=20
    T__20=21
    T__21=22
    T__22=23
    T__23=24
    T__24=25
    T__25=26
    T__26=27
    T__27=28
    T__28=29
    T__29=30
    T__30=31
    T__31=32
    T__32=33
    T__33=34
    T__34=35
    T__35=36
    T__36=37
    T__37=38
    T__38=39
    T__39=40
    T__40=41
    T__41=42
    T__42=43
    T__43=44
    T__44=45
    T__45=46
    T__46=47
    T__47=48
    T__48=49
    T__49=50
    T__50=51
    T__51=52
    T__52=53
    T__53=54
    T__54=55
    T__55=56
    T__56=57
    T__57=58
    T__58=59
    T__59=60
    T__60=61
    T__61=62
    T__62=63
    T__63=64
    T__64=65
    T__65=66
    T__66=67
    T__67=68
    T__68=69
    T__69=70
    T__70=71
    T__71=72
    T__72=73
    T__73=74
    T__74=75
    T__75=76
    T__76=77
    T__77=78
    T__78=79
    T__79=80
    T__80=81
    T__81=82
    T__82=83
    T__83=84
    T__84=85
    T__85=86
    T__86=87
    T__87=88
    T__88=89
    T__89=90
    T__90=91
    T__91=92
    T__92=93
    T__93=94
    T__94=95
    T__95=96
    T__96=97
    T__97=98
    T__98=99
    T__99=100
    T__100=101
    T__101=102
    T__102=103
    T__103=104
    T__104=105
    T__105=106
    T__106=107
    T__107=108
    T__108=109
    T__109=110
    T__110=111
    T__111=112
    T__112=113
    T__113=114
    T__114=115
    T__115=116
    T__116=117
    T__117=118
    T__118=119
    T__119=120
    T__120=121
    T__121=122
    T__122=123
    T__123=124
    T__124=125
    T__125=126
    T__126=127
    T__127=128
    T__128=129
    Platform_name_platform_version=130
    Identifier=131
    DOT=132
    LCURLY=133
    LPAREN=134
    LBRACK=135
    RCURLY=136
    RPAREN=137
    RBRACK=138
    COMMA=139
    COLON=140
    SEMI=141
    LT=142
    GT=143
    UNDERSCORE=144
    BANG=145
    QUESTION=146
    AT=147
    AND=148
    SUB=149
    EQUAL=150
    OR=151
    DIV=152
    ADD=153
    MUL=154
    MOD=155
    CARET=156
    TILDE=157
    Operator_head_other=158
    Operator_following_character=159
    Implicit_parameter_name=160
    Binary_literal=161
    Octal_literal=162
    Decimal_literal=163
    Pure_decimal_digits=164
    Hexadecimal_literal=165
    Floating_point_literal=166
    Static_string_literal=167
    Interpolated_string_literal=168
    WS=169
    Block_comment=170
    Line_comment=171

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class Top_levelContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(Swift3Parser.EOF, 0)

        def statements(self):
            return self.getTypedRuleContext(Swift3Parser.StatementsContext,0)


        def getRuleIndex(self):
            return Swift3Parser.RULE_top_level

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTop_level" ):
                listener.enterTop_level(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTop_level" ):
                listener.exitTop_level(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTop_level" ):
                return visitor.visitTop_level(self)
            else:
                return visitor.visitChildren(self)




    def top_level(self):

        localctx = Swift3Parser.Top_levelContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_top_level)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 571
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.state = 570
                self.statements()


            self.state = 573
            self.match(Swift3Parser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class StatementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(Swift3Parser.ExpressionContext,0)


        def declaration(self):
            return self.getTypedRuleContext(Swift3Parser.DeclarationContext,0)


        def loop_statement(self):
            return self.getTypedRuleContext(Swift3Parser.Loop_statementContext,0)


        def branch_statement(self):
            return self.getTypedRuleContext(Swift3Parser.Branch_statementContext,0)


        def labeled_statement(self):
            return self.getTypedRuleContext(Swift3Parser.Labeled_statementContext,0)


        def control_transfer_statement(self):
            return self.getTypedRuleContext(Swift3Parser.Control_transfer_statementContext,0)


        def defer_statement(self):
            return self.getTypedRuleContext(Swift3Parser.Defer_statementContext,0)


        def do_statement(self):
            return self.getTypedRuleContext(Swift3Parser.Do_statementContext,0)


        def compiler_control_statement(self):
            return self.getTypedRuleContext(Swift3Parser.Compiler_control_statementContext,0)


        def getRuleIndex(self):
            return Swift3Parser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = Swift3Parser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        try:
            self.state = 611
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 575
                self.expression()
                self.state = 577
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
                if la_ == 1:
                    self.state = 576
                    self.match(Swift3Parser.SEMI)


                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 579
                self.declaration()
                self.state = 581
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
                if la_ == 1:
                    self.state = 580
                    self.match(Swift3Parser.SEMI)


                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 583
                self.loop_statement()
                self.state = 585
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
                if la_ == 1:
                    self.state = 584
                    self.match(Swift3Parser.SEMI)


                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 587
                self.branch_statement()
                self.state = 589
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
                if la_ == 1:
                    self.state = 588
                    self.match(Swift3Parser.SEMI)


                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 591
                self.labeled_statement()
                self.state = 593
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
                if la_ == 1:
                    self.state = 592
                    self.match(Swift3Parser.SEMI)


                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 595
                self.control_transfer_statement()
                self.state = 597
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
                if la_ == 1:
                    self.state = 596
                    self.match(Swift3Parser.SEMI)


                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 599
                self.defer_statement()
                self.state = 601
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
                if la_ == 1:
                    self.state = 600
                    self.match(Swift3Parser.SEMI)


                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 603
                self.do_statement()
                self.state = 605
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
                if la_ == 1:
                    self.state = 604
                    self.match(Swift3Parser.SEMI)


                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 607
                self.compiler_control_statement()
                self.state = 609
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
                if la_ == 1:
                    self.state = 608
                    self.match(Swift3Parser.SEMI)


                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class StatementsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statements_impl(self):
            return self.getTypedRuleContext(Swift3Parser.Statements_implContext,0)


        def getRuleIndex(self):
            return Swift3Parser.RULE_statements

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatements" ):
                listener.enterStatements(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatements" ):
                listener.exitStatements(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatements" ):
                return visitor.visitStatements(self)
            else:
                return visitor.visitChildren(self)




    def statements(self):

        localctx = Swift3Parser.StatementsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_statements)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 613
            self.statements_impl(-1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Statements_implContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1, indexBefore:int=None):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.indexBefore = None
            self.indexAfter = -1
            self.indexBefore = indexBefore

        def statement(self):
            return self.getTypedRuleContext(Swift3Parser.StatementContext,0)


        def statements_impl(self):
            return self.getTypedRuleContext(Swift3Parser.Statements_implContext,0)


        def getRuleIndex(self):
            return Swift3Parser.RULE_statements_impl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatements_impl" ):
                listener.enterStatements_impl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatements_impl" ):
                listener.exitStatements_impl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatements_impl" ):
                return visitor.visitStatements_impl(self)
            else:
                return visitor.visitChildren(self)




    def statements_impl(self, indexBefore:int):

        localctx = Swift3Parser.Statements_implContext(self, self._ctx, self.state, indexBefore)
        self.enterRule(localctx, 6, self.RULE_statements_impl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 615
            if not SwiftSupport.isSeparatedStatement(_input, localctx.indexBefore):
                from antlr4.error.Errors import FailedPredicateException
                raise FailedPredicateException(self, "SwiftSupport.isSeparatedStatement(_input, $indexBefore)")
            self.state = 616
            self.statement()
            localctx.indexAfter =  _input.index()
            self.state = 619
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.state = 618
                self.statements_impl(localctx.indexAfter)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Loop_statementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def for_statement(self):
            return self.getTypedRuleContext(Swift3Parser.For_statementContext,0)


        def for_in_statement(self):
            return self.getTypedRuleContext(Swift3Parser.For_in_statementContext,0)


        def while_statement(self):
            return self.getTypedRuleContext(Swift3Parser.While_statementContext,0)


        def repeat_while_statement(self):
            return self.getTypedRuleContext(Swift3Parser.Repeat_while_statementContext,0)


        def getRuleIndex(self):
            return Swift3Parser.RULE_loop_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLoop_statement" ):
                listener.enterLoop_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLoop_statement" ):
                listener.exitLoop_statement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLoop_statement" ):
                return visitor.visitLoop_statement(self)
            else:
                return visitor.visitChildren(self)




    def loop_statement(self):

        localctx = Swift3Parser.Loop_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_loop_statement)
        try:
            self.state = 625
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 621
                self.for_statement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 622
                self.for_in_statement()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 623
                self.while_statement()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 624
                self.repeat_while_statement()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class For_statementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def code_block(self):
            return self.getTypedRuleContext(Swift3Parser.Code_blockContext,0)


        def for_init(self):
            return self.getTypedRuleContext(Swift3Parser.For_initContext,0)


        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Swift3Parser.ExpressionContext)
            else:
                return self.getTypedRuleContext(Swift3Parser.ExpressionContext,i)


        def getRuleIndex(self):
            return Swift3Parser.RULE_for_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFor_statement" ):
                listener.enterFor_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFor_statement" ):
                listener.exitFor_statement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_statement" ):
                return visitor.visitFor_statement(self)
            else:
                return visitor.visitChildren(self)




    def for_statement(self):

        localctx = Swift3Parser.For_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_for_statement)
        try:
            self.state = 655
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 627
                self.match(Swift3Parser.T__0)
                self.state = 629
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
                if la_ == 1:
                    self.state = 628
                    self.for_init()


                self.state = 631
                self.match(Swift3Parser.SEMI)
                self.state = 633
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
                if la_ == 1:
                    self.state = 632
                    self.expression()


                self.state = 635
                self.match(Swift3Parser.SEMI)
                self.state = 637
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
                if la_ == 1:
                    self.state = 636
                    self.expression()


                self.state = 639
                self.code_block()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 640
                self.match(Swift3Parser.T__0)
                self.state = 641
                self.match(Swift3Parser.LPAREN)
                self.state = 643
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
                if la_ == 1:
                    self.state = 642
                    self.for_init()


                self.state = 645
                self.match(Swift3Parser.SEMI)
                self.state = 647
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
                if la_ == 1:
                    self.state = 646
                    self.expression()


                self.state = 649
                self.match(Swift3Parser.SEMI)
                self.state = 651
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
                if la_ == 1:
                    self.state = 650
                    self.expression()


                self.state = 653
                self.match(Swift3Parser.RPAREN)
                self.state = 654
                self.code_block()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class For_initContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variable_declaration(self):
            return self.getTypedRuleContext(Swift3Parser.Variable_declarationContext,0)


        def expression_list(self):
            return self.getTypedRuleContext(Swift3Parser.Expression_listContext,0)


        def getRuleIndex(self):
            return Swift3Parser.RULE_for_init

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFor_init" ):
                listener.enterFor_init(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFor_init" ):
                listener.exitFor_init(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_init" ):
                return visitor.visitFor_init(self)
            else:
                return visitor.visitChildren(self)




    def for_init(self):

        localctx = Swift3Parser.For_initContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_for_init)
        try:
            self.state = 659
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 657
                self.variable_declaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 658
                self.expression_list()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class For_in_statementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def pattern(self):
            return self.getTypedRuleContext(Swift3Parser.PatternContext,0)


        def expression(self):
            return self.getTypedRuleContext(Swift3Parser.ExpressionContext,0)


        def code_block(self):
            return self.getTypedRuleContext(Swift3Parser.Code_blockContext,0)


        def where_clause(self):
            return self.getTypedRuleContext(Swift3Parser.Where_clauseContext,0)


        def getRuleIndex(self):
            return Swift3Parser.RULE_for_in_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFor_in_statement" ):
                listener.enterFor_in_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFor_in_statement" ):
                listener.exitFor_in_statement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_in_statement" ):
                return visitor.visitFor_in_statement(self)
            else:
                return visitor.visitChildren(self)




    def for_in_statement(self):

        localctx = Swift3Parser.For_in_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_for_in_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 661
            self.match(Swift3Parser.T__0)
            self.state = 663
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.state = 662
                self.match(Swift3Parser.T__1)


            self.state = 665
            self.pattern(0)
            self.state = 666
            self.match(Swift3Parser.T__2)
            self.state = 667
            self.expression()
            self.state = 669
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==Swift3Parser.T__12:
                self.state = 668
                self.where_clause()


            self.state = 671
            self.code_block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class While_statementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def condition_list(self):
            return self.getTypedRuleContext(Swift3Parser.Condition_listContext,0)


        def code_block(self):
            return self.getTypedRuleContext(Swift3Parser.Code_blockContext,0)


        def getRuleIndex(self):
            return Swift3Parser.RULE_while_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhile_statement" ):
                listener.enterWhile_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhile_statement" ):
                listener.exitWhile_statement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhile_statement" ):
                return visitor.visitWhile_statement(self)
            else:
                return visitor.visitChildren(self)




    def while_statement(self):

        localctx = Swift3Parser.While_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_while_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 673
            self.match(Swift3Parser.T__3)
            self.state = 674
            self.condition_list()
            self.state = 675
            self.code_block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Condition_listContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def condition(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Swift3Parser.ConditionContext)
            else:
                return self.getTypedRuleContext(Swift3Parser.ConditionContext,i)


        def getRuleIndex(self):
            return Swift3Parser.RULE_condition_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCondition_list" ):
                listener.enterCondition_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCondition_list" ):
                listener.exitCondition_list(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCondition_list" ):
                return visitor.visitCondition_list(self)
            else:
                return visitor.visitChildren(self)




    def condition_list(self):

        localctx = Swift3Parser.Condition_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_condition_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 677
            self.condition()
            self.state = 682
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==Swift3Parser.COMMA:
                self.state = 678
                self.match(Swift3Parser.COMMA)
                self.state = 679
                self.condition()
                self.state = 684
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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

        def expression(self):
            return self.getTypedRuleContext(Swift3Parser.ExpressionContext,0)


        def availability_condition(self):
            return self.getTypedRuleContext(Swift3Parser.Availability_conditionContext,0)


        def case_condition(self):
            return self.getTypedRuleContext(Swift3Parser.Case_conditionContext,0)


        def optional_binding_condition(self):
            return self.getTypedRuleContext(Swift3Parser.Optional_binding_conditionContext,0)


        def getRuleIndex(self):
            return Swift3Parser.RULE_condition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCondition" ):
                listener.enterCondition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCondition" ):
                listener.exitCondition(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCondition" ):
                return visitor.visitCondition(self)
            else:
                return visitor.visitChildren(self)




    def condition(self):

        localctx = Swift3Parser.ConditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_condition)
        try:
            self.state = 689
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 685
                self.expression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 686
                self.availability_condition()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 687
                self.case_condition()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 688
                self.optional_binding_condition()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Case_conditionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def pattern(self):
            return self.getTypedRuleContext(Swift3Parser.PatternContext,0)


        def initializer(self):
            return self.getTypedRuleContext(Swift3Parser.InitializerContext,0)


        def where_clause(self):
            return self.getTypedRuleContext(Swift3Parser.Where_clauseContext,0)


        def getRuleIndex(self):
            return Swift3Parser.RULE_case_condition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCase_condition" ):
                listener.enterCase_condition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCase_condition" ):
                listener.exitCase_condition(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCase_condition" ):
                return visitor.visitCase_condition(self)
            else:
                return visitor.visitChildren(self)




    def case_condition(self):

        localctx = Swift3Parser.Case_conditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_case_condition)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 691
            self.match(Swift3Parser.T__1)
            self.state = 692
            self.pattern(0)
            self.state = 693
            self.initializer()
            self.state = 695
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==Swift3Parser.T__12:
                self.state = 694
                self.where_clause()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Optional_binding_conditionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def pattern(self):
            return self.getTypedRuleContext(Swift3Parser.PatternContext,0)


        def initializer(self):
            return self.getTypedRuleContext(Swift3Parser.InitializerContext,0)


        def getRuleIndex(self):
            return Swift3Parser.RULE_optional_binding_condition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOptional_binding_condition" ):
                listener.enterOptional_binding_condition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOptional_binding_condition" ):
                listener.exitOptional_binding_condition(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOptional_binding_condition" ):
                return visitor.visitOptional_binding_condition(self)
            else:
                return visitor.visitChildren(self)




    def optional_binding_condition(self):

        localctx = Swift3Parser.Optional_binding_conditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_optional_binding_condition)
        try:
            self.state = 705
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [Swift3Parser.T__4]:
                self.enterOuterAlt(localctx, 1)
                self.state = 697
                self.match(Swift3Parser.T__4)
                self.state = 698
                self.pattern(0)
                self.state = 699
                self.initializer()
                pass
            elif token in [Swift3Parser.T__5]:
                self.enterOuterAlt(localctx, 2)
                self.state = 701
                self.match(Swift3Parser.T__5)
                self.state = 702
                self.pattern(0)
                self.state = 703
                self.initializer()
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

    class Repeat_while_statementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def code_block(self):
            return self.getTypedRuleContext(Swift3Parser.Code_blockContext,0)


        def expression(self):
            return self.getTypedRuleContext(Swift3Parser.ExpressionContext,0)


        def getRuleIndex(self):
            return Swift3Parser.RULE_repeat_while_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRepeat_while_statement" ):
                listener.enterRepeat_while_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRepeat_while_statement" ):
                listener.exitRepeat_while_statement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRepeat_while_statement" ):
                return visitor.visitRepeat_while_statement(self)
            else:
                return visitor.visitChildren(self)




    def repeat_while_statement(self):

        localctx = Swift3Parser.Repeat_while_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_repeat_while_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 707
            self.match(Swift3Parser.T__6)
            self.state = 708
            self.code_block()
            self.state = 709
            self.match(Swift3Parser.T__3)
            self.state = 710
            self.expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Branch_statementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def if_statement(self):
            return self.getTypedRuleContext(Swift3Parser.If_statementContext,0)


        def guard_statement(self):
            return self.getTypedRuleContext(Swift3Parser.Guard_statementContext,0)


        def switch_statement(self):
            return self.getTypedRuleContext(Swift3Parser.Switch_statementContext,0)


        def getRuleIndex(self):
            return Swift3Parser.RULE_branch_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBranch_statement" ):
                listener.enterBranch_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBranch_statement" ):
                listener.exitBranch_statement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBranch_statement" ):
                return visitor.visitBranch_statement(self)
            else:
                return visitor.visitChildren(self)




    def branch_statement(self):

        localctx = Swift3Parser.Branch_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_branch_statement)
        try:
            self.state = 715
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [Swift3Parser.T__7]:
                self.enterOuterAlt(localctx, 1)
                self.state = 712
                self.if_statement()
                pass
            elif token in [Swift3Parser.T__9]:
                self.enterOuterAlt(localctx, 2)
                self.state = 713
                self.guard_statement()
                pass
            elif token in [Swift3Parser.T__10]:
                self.enterOuterAlt(localctx, 3)
                self.state = 714
                self.switch_statement()
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

    class If_statementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def condition_list(self):
            return self.getTypedRuleContext(Swift3Parser.Condition_listContext,0)


        def code_block(self):
            return self.getTypedRuleContext(Swift3Parser.Code_blockContext,0)


        def else_clause(self):
            return self.getTypedRuleContext(Swift3Parser.Else_clauseContext,0)


        def getRuleIndex(self):
            return Swift3Parser.RULE_if_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIf_statement" ):
                listener.enterIf_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIf_statement" ):
                listener.exitIf_statement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf_statement" ):
                return visitor.visitIf_statement(self)
            else:
                return visitor.visitChildren(self)




    def if_statement(self):

        localctx = Swift3Parser.If_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_if_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 717
            self.match(Swift3Parser.T__7)
            self.state = 718
            self.condition_list()
            self.state = 719
            self.code_block()
            self.state = 721
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
            if la_ == 1:
                self.state = 720
                self.else_clause()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Else_clauseContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def code_block(self):
            return self.getTypedRuleContext(Swift3Parser.Code_blockContext,0)


        def if_statement(self):
            return self.getTypedRuleContext(Swift3Parser.If_statementContext,0)


        def getRuleIndex(self):
            return Swift3Parser.RULE_else_clause

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterElse_clause" ):
                listener.enterElse_clause(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitElse_clause" ):
                listener.exitElse_clause(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElse_clause" ):
                return visitor.visitElse_clause(self)
            else:
                return visitor.visitChildren(self)




    def else_clause(self):

        localctx = Swift3Parser.Else_clauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_else_clause)
        try:
            self.state = 727
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 723
                self.match(Swift3Parser.T__8)
                self.state = 724
                self.code_block()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 725
                self.match(Swift3Parser.T__8)
                self.state = 726
                self.if_statement()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Guard_statementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def condition_list(self):
            return self.getTypedRuleContext(Swift3Parser.Condition_listContext,0)


        def code_block(self):
            return self.getTypedRuleContext(Swift3Parser.Code_blockContext,0)


        def getRuleIndex(self):
            return Swift3Parser.RULE_guard_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGuard_statement" ):
                listener.enterGuard_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGuard_statement" ):
                listener.exitGuard_statement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGuard_statement" ):
                return visitor.visitGuard_statement(self)
            else:
                return visitor.visitChildren(self)




    def guard_statement(self):

        localctx = Swift3Parser.Guard_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_guard_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 729
            self.match(Swift3Parser.T__9)
            self.state = 730
            self.condition_list()
            self.state = 731
            self.match(Swift3Parser.T__8)
            self.state = 732
            self.code_block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Switch_statementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(Swift3Parser.ExpressionContext,0)


        def switch_cases(self):
            return self.getTypedRuleContext(Swift3Parser.Switch_casesContext,0)


        def getRuleIndex(self):
            return Swift3Parser.RULE_switch_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSwitch_statement" ):
                listener.enterSwitch_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSwitch_statement" ):
                listener.exitSwitch_statement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSwitch_statement" ):
                return visitor.visitSwitch_statement(self)
            else:
                return visitor.visitChildren(self)




    def switch_statement(self):

        localctx = Swift3Parser.Switch_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_switch_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 734
            self.match(Swift3Parser.T__10)
            self.state = 735
            self.expression()
            self.state = 736
            self.match(Swift3Parser.LCURLY)
            self.state = 738
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==Swift3Parser.T__1 or _la==Swift3Parser.T__11:
                self.state = 737
                self.switch_cases()


            self.state = 740
            self.match(Swift3Parser.RCURLY)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Switch_casesContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def switch_case(self):
            return self.getTypedRuleContext(Swift3Parser.Switch_caseContext,0)


        def switch_cases(self):
            return self.getTypedRuleContext(Swift3Parser.Switch_casesContext,0)


        def getRuleIndex(self):
            return Swift3Parser.RULE_switch_cases

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSwitch_cases" ):
                listener.enterSwitch_cases(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSwitch_cases" ):
                listener.exitSwitch_cases(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSwitch_cases" ):
                return visitor.visitSwitch_cases(self)
            else:
                return visitor.visitChildren(self)




    def switch_cases(self):

        localctx = Swift3Parser.Switch_casesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_switch_cases)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 742
            self.switch_case()
            self.state = 744
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==Swift3Parser.T__1 or _la==Swift3Parser.T__11:
                self.state = 743
                self.switch_cases()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Switch_caseContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def case_label(self):
            return self.getTypedRuleContext(Swift3Parser.Case_labelContext,0)


        def statements(self):
            return self.getTypedRuleContext(Swift3Parser.StatementsContext,0)


        def default_label(self):
            return self.getTypedRuleContext(Swift3Parser.Default_labelContext,0)


        def getRuleIndex(self):
            return Swift3Parser.RULE_switch_case

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSwitch_case" ):
                listener.enterSwitch_case(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSwitch_case" ):
                listener.exitSwitch_case(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSwitch_case" ):
                return visitor.visitSwitch_case(self)
            else:
                return visitor.visitChildren(self)




    def switch_case(self):

        localctx = Swift3Parser.Switch_caseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_switch_case)
        try:
            self.state = 752
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [Swift3Parser.T__1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 746
                self.case_label()
                self.state = 747
                self.statements()
                pass
            elif token in [Swift3Parser.T__11]:
                self.enterOuterAlt(localctx, 2)
                self.state = 749
                self.default_label()
                self.state = 750
                self.statements()
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

    class Case_labelContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def case_item_list(self):
            return self.getTypedRuleContext(Swift3Parser.Case_item_listContext,0)


        def getRuleIndex(self):
            return Swift3Parser.RULE_case_label

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCase_label" ):
                listener.enterCase_label(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCase_label" ):
                listener.exitCase_label(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCase_label" ):
                return visitor.visitCase_label(self)
            else:
                return visitor.visitChildren(self)




    def case_label(self):

        localctx = Swift3Parser.Case_labelContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_case_label)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 754
            self.match(Swift3Parser.T__1)
            self.state = 755
            self.case_item_list()
            self.state = 756
            self.match(Swift3Parser.COLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Case_item_listContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def pattern(self):
            return self.getTypedRuleContext(Swift3Parser.PatternContext,0)


        def where_clause(self):
            return self.getTypedRuleContext(Swift3Parser.Where_clauseContext,0)


        def case_item_list(self):
            return self.getTypedRuleContext(Swift3Parser.Case_item_listContext,0)


        def getRuleIndex(self):
            return Swift3Parser.RULE_case_item_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCase_item_list" ):
                listener.enterCase_item_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCase_item_list" ):
                listener.exitCase_item_list(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCase_item_list" ):
                return visitor.visitCase_item_list(self)
            else:
                return visitor.visitChildren(self)




    def case_item_list(self):

        localctx = Swift3Parser.Case_item_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_case_item_list)
        self._la = 0 # Token type
        try:
            self.state = 769
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,35,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 758
                self.pattern(0)
                self.state = 760
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==Swift3Parser.T__12:
                    self.state = 759
                    self.where_clause()


                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 762
                self.pattern(0)
                self.state = 764
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==Swift3Parser.T__12:
                    self.state = 763
                    self.where_clause()


                self.state = 766
                self.match(Swift3Parser.COMMA)
                self.state = 767
                self.case_item_list()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Default_labelContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return Swift3Parser.RULE_default_label

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDefault_label" ):
                listener.enterDefault_label(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDefault_label" ):
                listener.exitDefault_label(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDefault_label" ):
                return visitor.visitDefault_label(self)
            else:
                return visitor.visitChildren(self)




    def default_label(self):

        localctx = Swift3Parser.Default_labelContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_default_label)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 771
            self.match(Swift3Parser.T__11)
            self.state = 772
            self.match(Swift3Parser.COLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Where_clauseContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def where_expression(self):
            return self.getTypedRuleContext(Swift3Parser.Where_expressionContext,0)


        def getRuleIndex(self):
            return Swift3Parser.RULE_where_clause

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhere_clause" ):
                listener.enterWhere_clause(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhere_clause" ):
                listener.exitWhere_clause(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhere_clause" ):
                return visitor.visitWhere_clause(self)
            else:
                return visitor.visitChildren(self)




    def where_clause(self):

        localctx = Swift3Parser.Where_clauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_where_clause)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 774
            self.match(Swift3Parser.T__12)
            self.state = 775
            self.where_expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Where_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(Swift3Parser.ExpressionContext,0)


        def getRuleIndex(self):
            return Swift3Parser.RULE_where_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhere_expression" ):
                listener.enterWhere_expression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhere_expression" ):
                listener.exitWhere_expression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhere_expression" ):
                return visitor.visitWhere_expression(self)
            else:
                return visitor.visitChildren(self)




    def where_expression(self):

        localctx = Swift3Parser.Where_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_where_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 777
            self.expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Labeled_statementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement_label(self):
            return self.getTypedRuleContext(Swift3Parser.Statement_labelContext,0)


        def loop_statement(self):
            return self.getTypedRuleContext(Swift3Parser.Loop_statementContext,0)


        def if_statement(self):
            return self.getTypedRuleContext(Swift3Parser.If_statementContext,0)


        def switch_statement(self):
            return self.getTypedRuleContext(Swift3Parser.Switch_statementContext,0)


        def do_statement(self):
            return self.getTypedRuleContext(Swift3Parser.Do_statementContext,0)


        def getRuleIndex(self):
            return Swift3Parser.RULE_labeled_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLabeled_statement" ):
                listener.enterLabeled_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLabeled_statement" ):
                listener.exitLabeled_statement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLabeled_statement" ):
                return visitor.visitLabeled_statement(self)
            else:
                return visitor.visitChildren(self)




    def labeled_statement(self):

        localctx = Swift3Parser.Labeled_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_labeled_statement)
        try:
            self.state = 791
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,36,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 779
                self.statement_label()
                self.state = 780
                self.loop_statement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 782
                self.statement_label()
                self.state = 783
                self.if_statement()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 785
                self.statement_label()
                self.state = 786
                self.switch_statement()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 788
                self.statement_label()
                self.state = 789
                self.do_statement()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Statement_labelContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def label_name(self):
            return self.getTypedRuleContext(Swift3Parser.Label_nameContext,0)


        def getRuleIndex(self):
            return Swift3Parser.RULE_statement_label

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement_label" ):
                listener.enterStatement_label(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement_label" ):
                listener.exitStatement_label(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement_label" ):
                return visitor.visitStatement_label(self)
            else:
                return visitor.visitChildren(self)




    def statement_label(self):

        localctx = Swift3Parser.Statement_labelContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_statement_label)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 793
            self.label_name()
            self.state = 794
            self.match(Swift3Parser.COLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Label_nameContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declaration_identifier(self):
            return self.getTypedRuleContext(Swift3Parser.Declaration_identifierContext,0)


        def getRuleIndex(self):
            return Swift3Parser.RULE_label_name

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLabel_name" ):
                listener.enterLabel_name(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLabel_name" ):
                listener.exitLabel_name(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLabel_name" ):
                return visitor.visitLabel_name(self)
            else:
                return visitor.visitChildren(self)




    def label_name(self):

        localctx = Swift3Parser.Label_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_label_name)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 796
            self.declaration_identifier()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Control_transfer_statementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def break_statement(self):
            return self.getTypedRuleContext(Swift3Parser.Break_statementContext,0)


        def continue_statement(self):
            return self.getTypedRuleContext(Swift3Parser.Continue_statementContext,0)


        def fallthrough_statement(self):
            return self.getTypedRuleContext(Swift3Parser.Fallthrough_statementContext,0)


        def return_statement(self):
            return self.getTypedRuleContext(Swift3Parser.Return_statementContext,0)


        def throw_statement(self):
            return self.getTypedRuleContext(Swift3Parser.Throw_statementContext,0)


        def getRuleIndex(self):
            return Swift3Parser.RULE_control_transfer_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterControl_transfer_statement" ):
                listener.enterControl_transfer_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitControl_transfer_statement" ):
                listener.exitControl_transfer_statement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitControl_transfer_statement" ):
                return visitor.visitControl_transfer_statement(self)
            else:
                return visitor.visitChildren(self)




    def control_transfer_statement(self):

        localctx = Swift3Parser.Control_transfer_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_control_transfer_statement)
        try:
            self.state = 803
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [Swift3Parser.T__13]:
                self.enterOuterAlt(localctx, 1)
                self.state = 798
                self.break_statement()
                pass
            elif token in [Swift3Parser.T__14]:
                self.enterOuterAlt(localctx, 2)
                self.state = 799
                self.continue_statement()
                pass
            elif token in [Swift3Parser.T__15]:
                self.enterOuterAlt(localctx, 3)
                self.state = 800
                self.fallthrough_statement()
                pass
            elif token in [Swift3Parser.T__16]:
                self.enterOuterAlt(localctx, 4)
                self.state = 801
                self.return_statement()
                pass
            elif token in [Swift3Parser.T__17]:
                self.enterOuterAlt(localctx, 5)
                self.state = 802
                self.throw_statement()
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

    class Break_statementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def label_name(self):
            return self.getTypedRuleContext(Swift3Parser.Label_nameContext,0)


        def getRuleIndex(self):
            return Swift3Parser.RULE_break_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBreak_statement" ):
                listener.enterBreak_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBreak_statement" ):
                listener.exitBreak_statement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBreak_statement" ):
                return visitor.visitBreak_statement(self)
            else:
                return visitor.visitChildren(self)




    def break_statement(self):

        localctx = Swift3Parser.Break_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_break_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 805
            self.match(Swift3Parser.T__13)
            self.state = 807
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,38,self._ctx)
            if la_ == 1:
                self.state = 806
                self.label_name()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Continue_statementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def label_name(self):
            return self.getTypedRuleContext(Swift3Parser.Label_nameContext,0)


        def getRuleIndex(self):
            return Swift3Parser.RULE_continue_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterContinue_statement" ):
                listener.enterContinue_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitContinue_statement" ):
                listener.exitContinue_statement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitContinue_statement" ):
                return visitor.visitContinue_statement(self)
            else:
                return visitor.visitChildren(self)




    def continue_statement(self):

        localctx = Swift3Parser.Continue_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_continue_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 809
            self.match(Swift3Parser.T__14)
            self.state = 811
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,39,self._ctx)
            if la_ == 1:
                self.state = 810
                self.label_name()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Fallthrough_statementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return Swift3Parser.RULE_fallthrough_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFallthrough_statement" ):
                listener.enterFallthrough_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFallthrough_statement" ):
                listener.exitFallthrough_statement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFallthrough_statement" ):
                return visitor.visitFallthrough_statement(self)
            else:
                return visitor.visitChildren(self)




    def fallthrough_statement(self):

        localctx = Swift3Parser.Fallthrough_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_fallthrough_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 813
            self.match(Swift3Parser.T__15)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Return_statementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(Swift3Parser.ExpressionContext,0)


        def getRuleIndex(self):
            return Swift3Parser.RULE_return_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReturn_statement" ):
                listener.enterReturn_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReturn_statement" ):
                listener.exitReturn_statement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturn_statement" ):
                return visitor.visitReturn_statement(self)
            else:
                return visitor.visitChildren(self)




    def return_statement(self):

        localctx = Swift3Parser.Return_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_return_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 815
            self.match(Swift3Parser.T__16)
            self.state = 817
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,40,self._ctx)
            if la_ == 1:
                self.state = 816
                self.expression()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Throw_statementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(Swift3Parser.ExpressionContext,0)


        def getRuleIndex(self):
            return Swift3Parser.RULE_throw_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterThrow_statement" ):
                listener.enterThrow_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitThrow_statement" ):
                listener.exitThrow_statement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitThrow_statement" ):
                return visitor.visitThrow_statement(self)
            else:
                return visitor.visitChildren(self)




    def throw_statement(self):

        localctx = Swift3Parser.Throw_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_throw_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 819
            self.match(Swift3Parser.T__17)
            self.state = 820
            self.expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Defer_statementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def code_block(self):
            return self.getTypedRuleContext(Swift3Parser.Code_blockContext,0)


        def getRuleIndex(self):
            return Swift3Parser.RULE_defer_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDefer_statement" ):
                listener.enterDefer_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDefer_statement" ):
                listener.exitDefer_statement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDefer_statement" ):
                return visitor.visitDefer_statement(self)
            else:
                return visitor.visitChildren(self)




    def defer_statement(self):

        localctx = Swift3Parser.Defer_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_defer_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 822
            self.match(Swift3Parser.T__18)
            self.state = 823
            self.code_block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Do_statementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def code_block(self):
            return self.getTypedRuleContext(Swift3Parser.Code_blockContext,0)


        def catch_clauses(self):
            return self.getTypedRuleContext(Swift3Parser.Catch_clausesContext,0)


        def getRuleIndex(self):
            return Swift3Parser.RULE_do_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDo_statement" ):
                listener.enterDo_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDo_statement" ):
                listener.exitDo_statement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDo_statement" ):
                return visitor.visitDo_statement(self)
            else:
                return visitor.visitChildren(self)




    def do_statement(self):

        localctx = Swift3Parser.Do_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_do_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 825
            self.match(Swift3Parser.T__19)
            self.state = 826
            self.code_block()
            self.state = 828
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,41,self._ctx)
            if la_ == 1:
                self.state = 827
                self.catch_clauses()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Catch_clausesContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def catch_clause(self):
            return self.getTypedRuleContext(Swift3Parser.Catch_clauseContext,0)


        def catch_clauses(self):
            return self.getTypedRuleContext(Swift3Parser.Catch_clausesContext,0)


        def getRuleIndex(self):
            return Swift3Parser.RULE_catch_clauses

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCatch_clauses" ):
                listener.enterCatch_clauses(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCatch_clauses" ):
                listener.exitCatch_clauses(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCatch_clauses" ):
                return visitor.visitCatch_clauses(self)
            else:
                return visitor.visitChildren(self)




    def catch_clauses(self):

        localctx = Swift3Parser.Catch_clausesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_catch_clauses)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 830
            self.catch_clause()
            self.state = 832
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,42,self._ctx)
            if la_ == 1:
                self.state = 831
                self.catch_clauses()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Catch_clauseContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def code_block(self):
            return self.getTypedRuleContext(Swift3Parser.Code_blockContext,0)


        def pattern(self):
            return self.getTypedRuleContext(Swift3Parser.PatternContext,0)


        def where_clause(self):
            return self.getTypedRuleContext(Swift3Parser.Where_clauseContext,0)


        def getRuleIndex(self):
            return Swift3Parser.RULE_catch_clause

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCatch_clause" ):
                listener.enterCatch_clause(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCatch_clause" ):
                listener.exitCatch_clause(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCatch_clause" ):
                return visitor.visitCatch_clause(self)
            else:
                return visitor.visitChildren(self)




    def catch_clause(self):

        localctx = Swift3Parser.Catch_clauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_catch_clause)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 834
            self.match(Swift3Parser.T__20)
            self.state = 836
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,43,self._ctx)
            if la_ == 1:
                self.state = 835
                self.pattern(0)


            self.state = 839
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==Swift3Parser.T__12:
                self.state = 838
                self.where_clause()


            self.state = 841
            self.code_block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Compiler_control_statementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def conditional_compilation_block(self):
            return self.getTypedRuleContext(Swift3Parser.Conditional_compilation_blockContext,0)


        def line_control_statement(self):
            return self.getTypedRuleContext(Swift3Parser.Line_control_statementContext,0)


        def getRuleIndex(self):
            return Swift3Parser.RULE_compiler_control_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCompiler_control_statement" ):
                listener.enterCompiler_control_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCompiler_control_statement" ):
                listener.exitCompiler_control_statement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCompiler_control_statement" ):
                return visitor.visitCompiler_control_statement(self)
            else:
                return visitor.visitChildren(self)




    def compiler_control_statement(self):

        localctx = Swift3Parser.Compiler_control_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_compiler_control_statement)
        try:
            self.state = 845
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [Swift3Parser.T__21]:
                self.enterOuterAlt(localctx, 1)
                self.state = 843
                self.conditional_compilation_block()
                pass
            elif token in [Swift3Parser.T__28]:
                self.enterOuterAlt(localctx, 2)
                self.state = 844
                self.line_control_statement()
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

    class Conditional_compilation_blockContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def if_directive_clause(self):
            return self.getTypedRuleContext(Swift3Parser.If_directive_clauseContext,0)


        def endif_directive(self):
            return self.getTypedRuleContext(Swift3Parser.Endif_directiveContext,0)


        def elseif_directive_clauses(self):
            return self.getTypedRuleContext(Swift3Parser.Elseif_directive_clausesContext,0)


        def else_directive_clause(self):
            return self.getTypedRuleContext(Swift3Parser.Else_directive_clauseContext,0)


        def getRuleIndex(self):
            return Swift3Parser.RULE_conditional_compilation_block

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConditional_compilation_block" ):
                listener.enterConditional_compilation_block(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConditional_compilation_block" ):
                listener.exitConditional_compilation_block(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConditional_compilation_block" ):
                return visitor.visitConditional_compilation_block(self)
            else:
                return visitor.visitChildren(self)




    def conditional_compilation_block(self):

        localctx = Swift3Parser.Conditional_compilation_blockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_conditional_compilation_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 847
            self.if_directive_clause()
            self.state = 849
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==Swift3Parser.T__22:
                self.state = 848
                self.elseif_directive_clauses()


            self.state = 852
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==Swift3Parser.T__23:
                self.state = 851
                self.else_directive_clause()


            self.state = 854
            self.endif_directive()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class If_directive_clauseContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def if_directive(self):
            return self.getTypedRuleContext(Swift3Parser.If_directiveContext,0)


        def compilation_condition(self):
            return self.getTypedRuleContext(Swift3Parser.Compilation_conditionContext,0)


        def statements(self):
            return self.getTypedRuleContext(Swift3Parser.StatementsContext,0)


        def getRuleIndex(self):
            return Swift3Parser.RULE_if_directive_clause

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIf_directive_clause" ):
                listener.enterIf_directive_clause(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIf_directive_clause" ):
                listener.exitIf_directive_clause(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf_directive_clause" ):
                return visitor.visitIf_directive_clause(self)
            else:
                return visitor.visitChildren(self)




    def if_directive_clause(self):

        localctx = Swift3Parser.If_directive_clauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_if_directive_clause)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 856
            self.if_directive()
            self.state = 857
            self.compilation_condition(0)
            self.state = 859
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,48,self._ctx)
            if la_ == 1:
                self.state = 858
                self.statements()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Elseif_directive_clausesContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def elseif_directive_clause(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Swift3Parser.Elseif_directive_clauseContext)
            else:
                return self.getTypedRuleContext(Swift3Parser.Elseif_directive_clauseContext,i)


        def getRuleIndex(self):
            return Swift3Parser.RULE_elseif_directive_clauses

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterElseif_directive_clauses" ):
                listener.enterElseif_directive_clauses(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitElseif_directive_clauses" ):
                listener.exitElseif_directive_clauses(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElseif_directive_clauses" ):
                return visitor.visitElseif_directive_clauses(self)
            else:
                return visitor.visitChildren(self)




    def elseif_directive_clauses(self):

        localctx = Swift3Parser.Elseif_directive_clausesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_elseif_directive_clauses)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 862
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 861
                self.elseif_directive_clause()
                self.state = 864
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==Swift3Parser.T__22):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Elseif_directive_clauseContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def elseif_directive(self):
            return self.getTypedRuleContext(Swift3Parser.Elseif_directiveContext,0)


        def compilation_condition(self):
            return self.getTypedRuleContext(Swift3Parser.Compilation_conditionContext,0)


        def statements(self):
            return self.getTypedRuleContext(Swift3Parser.StatementsContext,0)


        def getRuleIndex(self):
            return Swift3Parser.RULE_elseif_directive_clause

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterElseif_directive_clause" ):
                listener.enterElseif_directive_clause(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitElseif_directive_clause" ):
                listener.exitElseif_directive_clause(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElseif_directive_clause" ):
                return visitor.visitElseif_directive_clause(self)
            else:
                return visitor.visitChildren(self)




    def elseif_directive_clause(self):

        localctx = Swift3Parser.Elseif_directive_clauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_elseif_directive_clause)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 866
            self.elseif_directive()
            self.state = 867
            self.compilation_condition(0)
            self.state = 869
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,50,self._ctx)
            if la_ == 1:
                self.state = 868
                self.statements()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Else_directive_clauseContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def else_directive(self):
            return self.getTypedRuleContext(Swift3Parser.Else_directiveContext,0)


        def statements(self):
            return self.getTypedRuleContext(Swift3Parser.StatementsContext,0)


        def getRuleIndex(self):
            return Swift3Parser.RULE_else_directive_clause

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterElse_directive_clause" ):
                listener.enterElse_directive_clause(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitElse_directive_clause" ):
                listener.exitElse_directive_clause(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElse_directive_clause" ):
                return visitor.visitElse_directive_clause(self)
            else:
                return visitor.visitChildren(self)




    def else_directive_clause(self):

        localctx = Swift3Parser.Else_directive_clauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_else_directive_clause)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 871
            self.else_directive()
            self.state = 873
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,51,self._ctx)
            if la_ == 1:
                self.state = 872
                self.statements()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class If_directiveContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return Swift3Parser.RULE_if_directive

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIf_directive" ):
                listener.enterIf_directive(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIf_directive" ):
                listener.exitIf_directive(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf_directive" ):
                return visitor.visitIf_directive(self)
            else:
                return visitor.visitChildren(self)




    def if_directive(self):

        localctx = Swift3Parser.If_directiveContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_if_directive)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 875
            self.match(Swift3Parser.T__21)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Elseif_directiveContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return Swift3Parser.RULE_elseif_directive

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterElseif_directive" ):
                listener.enterElseif_directive(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitElseif_directive" ):
                listener.exitElseif_directive(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElseif_directive" ):
                return visitor.visitElseif_directive(self)
            else:
                return visitor.visitChildren(self)




    def elseif_directive(self):

        localctx = Swift3Parser.Elseif_directiveContext(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_elseif_directive)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 877
            self.match(Swift3Parser.T__22)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Else_directiveContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return Swift3Parser.RULE_else_directive

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterElse_directive" ):
                listener.enterElse_directive(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitElse_directive" ):
                listener.exitElse_directive(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElse_directive" ):
                return visitor.visitElse_directive(self)
            else:
                return visitor.visitChildren(self)




    def else_directive(self):

        localctx = Swift3Parser.Else_directiveContext(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_else_directive)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 879
            self.match(Swift3Parser.T__23)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Endif_directiveContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return Swift3Parser.RULE_endif_directive

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEndif_directive" ):
                listener.enterEndif_directive(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEndif_directive" ):
                listener.exitEndif_directive(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEndif_directive" ):
                return visitor.visitEndif_directive(self)
            else:
                return visitor.visitChildren(self)




    def endif_directive(self):

        localctx = Swift3Parser.Endif_directiveContext(self, self._ctx, self.state)
        self.enterRule(localctx, 96, self.RULE_endif_directive)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 881
            self.match(Swift3Parser.T__24)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Compilation_conditionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def platform_condition(self):
            return self.getTypedRuleContext(Swift3Parser.Platform_conditionContext,0)


        def label_identifier(self):
            return self.getTypedRuleContext(Swift3Parser.Label_identifierContext,0)


        def boolean_literal(self):
            return self.getTypedRuleContext(Swift3Parser.Boolean_literalContext,0)


        def compilation_condition(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Swift3Parser.Compilation_conditionContext)
            else:
                return self.getTypedRuleContext(Swift3Parser.Compilation_conditionContext,i)


        def compilation_condition_AND(self):
            return self.getTypedRuleContext(Swift3Parser.Compilation_condition_ANDContext,0)


        def compilation_condition_OR(self):
            return self.getTypedRuleContext(Swift3Parser.Compilation_condition_ORContext,0)


        def getRuleIndex(self):
            return Swift3Parser.RULE_compilation_condition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCompilation_condition" ):
                listener.enterCompilation_condition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCompilation_condition" ):
                listener.exitCompilation_condition(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCompilation_condition" ):
                return visitor.visitCompilation_condition(self)
            else:
                return visitor.visitChildren(self)



    def compilation_condition(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = Swift3Parser.Compilation_conditionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 98
        self.enterRecursionRule(localctx, 98, self.RULE_compilation_condition, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 893
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,52,self._ctx)
            if la_ == 1:
                self.state = 884
                self.platform_condition()
                pass

            elif la_ == 2:
                self.state = 885
                self.label_identifier()
                pass

            elif la_ == 3:
                self.state = 886
                self.boolean_literal()
                pass

            elif la_ == 4:
                self.state = 887
                self.match(Swift3Parser.LPAREN)
                self.state = 888
                self.compilation_condition(0)
                self.state = 889
                self.match(Swift3Parser.RPAREN)
                pass

            elif la_ == 5:
                self.state = 891
                self.match(Swift3Parser.BANG)
                self.state = 892
                self.compilation_condition(3)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 905
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,54,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 903
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,53,self._ctx)
                    if la_ == 1:
                        localctx = Swift3Parser.Compilation_conditionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_compilation_condition)
                        self.state = 895
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 896
                        self.compilation_condition_AND()
                        self.state = 897
                        self.compilation_condition(3)
                        pass

                    elif la_ == 2:
                        localctx = Swift3Parser.Compilation_conditionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_compilation_condition)
                        self.state = 899
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 900
                        self.compilation_condition_OR()
                        self.state = 901
                        self.compilation_condition(2)
                        pass


                self.state = 907
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,54,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Platform_conditionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def operating_system(self):
            return self.getTypedRuleContext(Swift3Parser.Operating_systemContext,0)


        def architecture(self):
            return self.getTypedRuleContext(Swift3Parser.ArchitectureContext,0)


        def compilation_condition_GE(self):
            return self.getTypedRuleContext(Swift3Parser.Compilation_condition_GEContext,0)


        def swift_version(self):
            return self.getTypedRuleContext(Swift3Parser.Swift_versionContext,0)


        def getRuleIndex(self):
            return Swift3Parser.RULE_platform_condition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPlatform_condition" ):
                listener.enterPlatform_condition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPlatform_condition" ):
                listener.exitPlatform_condition(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPlatform_condition" ):
                return visitor.visitPlatform_condition(self)
            else:
                return visitor.visitChildren(self)




    def platform_condition(self):

        localctx = Swift3Parser.Platform_conditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 100, self.RULE_platform_condition)
        try:
            self.state = 924
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [Swift3Parser.T__25]:
                self.enterOuterAlt(localctx, 1)
                self.state = 908
                self.match(Swift3Parser.T__25)
                self.state = 909
                self.match(Swift3Parser.LPAREN)
                self.state = 910
                self.operating_system()
                self.state = 911
                self.match(Swift3Parser.RPAREN)
                pass
            elif token in [Swift3Parser.T__26]:
                self.enterOuterAlt(localctx, 2)
                self.state = 913
                self.match(Swift3Parser.T__26)
                self.state = 914
                self.match(Swift3Parser.LPAREN)
                self.state = 915
                self.architecture()
                self.state = 916
                self.match(Swift3Parser.RPAREN)
                pass
            elif token in [Swift3Parser.T__27]:
                self.enterOuterAlt(localctx, 3)
                self.state = 918
                self.match(Swift3Parser.T__27)
                self.state = 919
                self.match(Swift3Parser.LPAREN)
                self.state = 920
                self.compilation_condition_GE()
                self.state = 921
                self.swift_version()
                self.state = 922
                self.match(Swift3Parser.RPAREN)
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

    class Swift_versionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Pure_decimal_digits(self, i:int=None):
            if i is None:
                return self.getTokens(Swift3Parser.Pure_decimal_digits)
            else:
                return self.getToken(Swift3Parser.Pure_decimal_digits, i)

        def getRuleIndex(self):
            return Swift3Parser.RULE_swift_version

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSwift_version" ):
                listener.enterSwift_version(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSwift_version" ):
                listener.exitSwift_version(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSwift_version" ):
                return visitor.visitSwift_version(self)
            else:
                return visitor.visitChildren(self)




    def swift_version(self):

        localctx = Swift3Parser.Swift_versionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 102, self.RULE_swift_version)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 926
            self.match(Swift3Parser.Pure_decimal_digits)
            self.state = 927
            self.match(Swift3Parser.DOT)
            self.state = 928
            self.match(Swift3Parser.Pure_decimal_digits)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Operating_systemContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declaration_identifier(self):
            return self.getTypedRuleContext(Swift3Parser.Declaration_identifierContext,0)


        def getRuleIndex(self):
            return Swift3Parser.RULE_operating_system

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOperating_system" ):
                listener.enterOperating_system(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOperating_system" ):
                listener.exitOperating_system(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOperating_system" ):
                return visitor.visitOperating_system(self)
            else:
                return visitor.visitChildren(self)




    def operating_system(self):

        localctx = Swift3Parser.Operating_systemContext(self, self._ctx, self.state)
        self.enterRule(localctx, 104, self.RULE_operating_system)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 930
            self.declaration_identifier()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ArchitectureContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declaration_identifier(self):
            return self.getTypedRuleContext(Swift3Parser.Declaration_identifierContext,0)


        def getRuleIndex(self):
            return Swift3Parser.RULE_architecture

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArchitecture" ):
                listener.enterArchitecture(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArchitecture" ):
                listener.exitArchitecture(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArchitecture" ):
                return visitor.visitArchitecture(self)
            else:
                return visitor.visitChildren(self)




    def architecture(self):

        localctx = Swift3Parser.ArchitectureContext(self, self._ctx, self.state)
        self.enterRule(localctx, 106, self.RULE_architecture)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 932
            self.declaration_identifier()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Line_control_statementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def file_name(self):
            return self.getTypedRuleContext(Swift3Parser.File_nameContext,0)


        def line_number(self):
            return self.getTypedRuleContext(Swift3Parser.Line_numberContext,0)


        def getRuleIndex(self):
            return Swift3Parser.RULE_line_control_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLine_control_statement" ):
                listener.enterLine_control_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLine_control_statement" ):
                listener.exitLine_control_statement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLine_control_statement" ):
                return visitor.visitLine_control_statement(self)
            else:
                return visitor.visitChildren(self)




    def line_control_statement(self):

        localctx = Swift3Parser.Line_control_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 108, self.RULE_line_control_statement)
        try:
            self.state = 948
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,56,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 934
                self.match(Swift3Parser.T__28)
                self.state = 935
                self.match(Swift3Parser.LPAREN)
                self.state = 936
                self.match(Swift3Parser.T__29)
                self.state = 937
                self.match(Swift3Parser.COLON)
                self.state = 938
                self.file_name()
                self.state = 939
                self.match(Swift3Parser.COMMA)
                self.state = 940
                self.match(Swift3Parser.T__30)
                self.state = 941
                self.match(Swift3Parser.COLON)
                self.state = 942
                self.line_number()
                self.state = 943
                self.match(Swift3Parser.RPAREN)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 945
                self.match(Swift3Parser.T__28)
                self.state = 946
                self.match(Swift3Parser.LPAREN)
                self.state = 947
                self.match(Swift3Parser.RPAREN)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Line_numberContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def integer_literal(self):
            return self.getTypedRuleContext(Swift3Parser.Integer_literalContext,0)


        def getRuleIndex(self):
            return Swift3Parser.RULE_line_number

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLine_number" ):
                listener.enterLine_number(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLine_number" ):
                listener.exitLine_number(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLine_number" ):
                return visitor.visitLine_number(self)
            else:
                return visitor.visitChildren(self)




    def line_number(self):

        localctx = Swift3Parser.Line_numberContext(self, self._ctx, self.state)
        self.enterRule(localctx, 110, self.RULE_line_number)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 950
            self.integer_literal()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class File_nameContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Static_string_literal(self):
            return self.getToken(Swift3Parser.Static_string_literal, 0)

        def getRuleIndex(self):
            return Swift3Parser.RULE_file_name

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFile_name" ):
                listener.enterFile_name(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFile_name" ):
                listener.exitFile_name(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFile_name" ):
                return visitor.visitFile_name(self)
            else:
                return visitor.visitChildren(self)




    def file_name(self):

        localctx = Swift3Parser.File_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 112, self.RULE_file_name)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 952
            self.match(Swift3Parser.Static_string_literal)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Availability_conditionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def availability_arguments(self):
            return self.getTypedRuleContext(Swift3Parser.Availability_argumentsContext,0)


        def getRuleIndex(self):
            return Swift3Parser.RULE_availability_condition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAvailability_condition" ):
                listener.enterAvailability_condition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAvailability_condition" ):
                listener.exitAvailability_condition(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAvailability_condition" ):
                return visitor.visitAvailability_condition(self)
            else:
                return visitor.visitChildren(self)




    def availability_condition(self):

        localctx = Swift3Parser.Availability_conditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 114, self.RULE_availability_condition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 954
            self.match(Swift3Parser.T__31)
            self.state = 955
            self.match(Swift3Parser.LPAREN)
            self.state = 956
            self.availability_arguments()
            self.state = 957
            self.match(Swift3Parser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Availability_argumentsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def availability_argument(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Swift3Parser.Availability_argumentContext)
            else:
                return self.getTypedRuleContext(Swift3Parser.Availability_argumentContext,i)


        def getRuleIndex(self):
            return Swift3Parser.RULE_availability_arguments

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAvailability_arguments" ):
                listener.enterAvailability_arguments(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAvailability_arguments" ):
                listener.exitAvailability_arguments(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAvailability_arguments" ):
                return visitor.visitAvailability_arguments(self)
            else:
                return visitor.visitChildren(self)




    def availability_arguments(self):

        localctx = Swift3Parser.Availability_argumentsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 116, self.RULE_availability_arguments)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 959
            self.availability_argument()
            self.state = 964
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==Swift3Parser.COMMA:
                self.state = 960
                self.match(Swift3Parser.COMMA)
                self.state = 961
                self.availability_argument()
                self.state = 966
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Availability_argumentContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Platform_name_platform_version(self):
            return self.getToken(Swift3Parser.Platform_name_platform_version, 0)

        def getRuleIndex(self):
            return Swift3Parser.RULE_availability_argument

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAvailability_argument" ):
                listener.enterAvailability_argument(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAvailability_argument" ):
                listener.exitAvailability_argument(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAvailability_argument" ):
                return visitor.visitAvailability_argument(self)
            else:
                return visitor.visitChildren(self)




    def availability_argument(self):

        localctx = Swift3Parser.Availability_argumentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 118, self.RULE_availability_argument)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 967
            _la = self._input.LA(1)
            if not(_la==Swift3Parser.Platform_name_platform_version or _la==Swift3Parser.MUL):
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

    class Generic_parameter_clauseContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def generic_parameter_list(self):
            return self.getTypedRuleContext(Swift3Parser.Generic_parameter_listContext,0)


        def getRuleIndex(self):
            return Swift3Parser.RULE_generic_parameter_clause

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGeneric_parameter_clause" ):
                listener.enterGeneric_parameter_clause(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGeneric_parameter_clause" ):
                listener.exitGeneric_parameter_clause(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGeneric_parameter_clause" ):
                return visitor.visitGeneric_parameter_clause(self)
            else:
                return visitor.visitChildren(self)




    def generic_parameter_clause(self):

        localctx = Swift3Parser.Generic_parameter_clauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 120, self.RULE_generic_parameter_clause)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 969
            self.match(Swift3Parser.LT)
            self.state = 970
            self.generic_parameter_list()
            self.state = 971
            self.match(Swift3Parser.GT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Generic_parameter_listContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def generic_parameter(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Swift3Parser.Generic_parameterContext)
            else:
                return self.getTypedRuleContext(Swift3Parser.Generic_parameterContext,i)


        def getRuleIndex(self):
            return Swift3Parser.RULE_generic_parameter_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGeneric_parameter_list" ):
                listener.enterGeneric_parameter_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGeneric_parameter_list" ):
                listener.exitGeneric_parameter_list(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGeneric_parameter_list" ):
                return visitor.visitGeneric_parameter_list(self)
            else:
                return visitor.visitChildren(self)




    def generic_parameter_list(self):

        localctx = Swift3Parser.Generic_parameter_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 122, self.RULE_generic_parameter_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 973
            self.generic_parameter()
            self.state = 978
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==Swift3Parser.COMMA:
                self.state = 974
                self.match(Swift3Parser.COMMA)
                self.state = 975
                self.generic_parameter()
                self.state = 980
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Generic_parameterContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_name(self):
            return self.getTypedRuleContext(Swift3Parser.Type_nameContext,0)


        def type_identifier(self):
            return self.getTypedRuleContext(Swift3Parser.Type_identifierContext,0)


        def protocol_composition_type(self):
            return self.getTypedRuleContext(Swift3Parser.Protocol_composition_typeContext,0)


        def getRuleIndex(self):
            return Swift3Parser.RULE_generic_parameter

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGeneric_parameter" ):
                listener.enterGeneric_parameter(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGeneric_parameter" ):
                listener.exitGeneric_parameter(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGeneric_parameter" ):
                return visitor.visitGeneric_parameter(self)
            else:
                return visitor.visitChildren(self)




    def generic_parameter(self):

        localctx = Swift3Parser.Generic_parameterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 124, self.RULE_generic_parameter)
        try:
            self.state = 990
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,59,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 981
                self.type_name()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 982
                self.type_name()
                self.state = 983
                self.match(Swift3Parser.COLON)
                self.state = 984
                self.type_identifier()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 986
                self.type_name()
                self.state = 987
                self.match(Swift3Parser.COLON)
                self.state = 988
                self.protocol_composition_type()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Generic_where_clauseContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def requirement_list(self):
            return self.getTypedRuleContext(Swift3Parser.Requirement_listContext,0)


        def getRuleIndex(self):
            return Swift3Parser.RULE_generic_where_clause

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGeneric_where_clause" ):
                listener.enterGeneric_where_clause(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGeneric_where_clause" ):
                listener.exitGeneric_where_clause(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGeneric_where_clause" ):
                return visitor.visitGeneric_where_clause(self)
            else:
                return visitor.visitChildren(self)




    def generic_where_clause(self):

        localctx = Swift3Parser.Generic_where_clauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 126, self.RULE_generic_where_clause)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 992
            self.match(Swift3Parser.T__12)
            self.state = 993
            self.requirement_list()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Requirement_listContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def requirement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Swift3Parser.RequirementContext)
            else:
                return self.getTypedRuleContext(Swift3Parser.RequirementContext,i)


        def getRuleIndex(self):
            return Swift3Parser.RULE_requirement_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRequirement_list" ):
                listener.enterRequirement_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRequirement_list" ):
                listener.exitRequirement_list(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRequirement_list" ):
                return visitor.visitRequirement_list(self)
            else:
                return visitor.visitChildren(self)




    def requirement_list(self):

        localctx = Swift3Parser.Requirement_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 128, self.RULE_requirement_list)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 995
            self.requirement()
            self.state = 1000
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,60,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 996
                    self.match(Swift3Parser.COMMA)
                    self.state = 997
                    self.requirement()
                self.state = 1002
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,60,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class RequirementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def conformance_requirement(self):
            return self.getTypedRuleContext(Swift3Parser.Conformance_requirementContext,0)


        def same_type_requirement(self):
            return self.getTypedRuleContext(Swift3Parser.Same_type_requirementContext,0)


        def getRuleIndex(self):
            return Swift3Parser.RULE_requirement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRequirement" ):
                listener.enterRequirement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRequirement" ):
                listener.exitRequirement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRequirement" ):
                return visitor.visitRequirement(self)
            else:
                return visitor.visitChildren(self)




    def requirement(self):

        localctx = Swift3Parser.RequirementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 130, self.RULE_requirement)
        try:
            self.state = 1005
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,61,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 1003
                self.conformance_requirement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 1004
                self.same_type_requirement()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Conformance_requirementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_identifier(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Swift3Parser.Type_identifierContext)
            else:
                return self.getTypedRuleContext(Swift3Parser.Type_identifierContext,i)


        def protocol_composition_type(self):
            return self.getTypedRuleContext(Swift3Parser.Protocol_composition_typeContext,0)


        def getRuleIndex(self):
            return Swift3Parser.RULE_conformance_requirement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConformance_requirement" ):
                listener.enterConformance_requirement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConformance_requirement" ):
                listener.exitConformance_requirement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConformance_requirement" ):
                return visitor.visitConformance_requirement(self)
            else:
                return visitor.visitChildren(self)




    def conformance_requirement(self):

        localctx = Swift3Parser.Conformance_requirementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 132, self.RULE_conformance_requirement)
        try:
            self.state = 1015
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,62,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 1007
                self.type_identifier()
                self.state = 1008
                self.match(Swift3Parser.COLON)
                self.state = 1009
                self.type_identifier()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 1011
                self.type_identifier()
                self.state = 1012
                self.match(Swift3Parser.COLON)
                self.state = 1013
                self.protocol_composition_type()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Same_type_requirementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_identifier(self):
            return self.getTypedRuleContext(Swift3Parser.Type_identifierContext,0)


        def same_type_equals(self):
            return self.getTypedRuleContext(Swift3Parser.Same_type_equalsContext,0)


        def type(self):
            return self.getTypedRuleContext(Swift3Parser.TypeContext,0)


        def getRuleIndex(self):
            return Swift3Parser.RULE_same_type_requirement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSame_type_requirement" ):
                listener.enterSame_type_requirement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSame_type_requirement" ):
                listener.exitSame_type_requirement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSame_type_requirement" ):
                return visitor.visitSame_type_requirement(self)
            else:
                return visitor.visitChildren(self)




    def same_type_requirement(self):

        localctx = Swift3Parser.Same_type_requirementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 134, self.RULE_same_type_requirement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1017
            self.type_identifier()
            self.state = 1018
            self.same_type_equals()
            self.state = 1019
            self.type(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Generic_argument_clauseContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def generic_argument_list(self):
            return self.getTypedRuleContext(Swift3Parser.Generic_argument_listContext,0)


        def getRuleIndex(self):
            return Swift3Parser.RULE_generic_argument_clause

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGeneric_argument_clause" ):
                listener.enterGeneric_argument_clause(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGeneric_argument_clause" ):
                listener.exitGeneric_argument_clause(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGeneric_argument_clause" ):
                return visitor.visitGeneric_argument_clause(self)
            else:
                return visitor.visitChildren(self)




    def generic_argument_clause(self):

        localctx = Swift3Parser.Generic_argument_clauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 136, self.RULE_generic_argument_clause)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1021
            self.match(Swift3Parser.LT)
            self.state = 1022
            self.generic_argument_list()
            self.state = 1023
            self.match(Swift3Parser.GT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Generic_argument_listContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def generic_argument(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Swift3Parser.Generic_argumentContext)
            else:
                return self.getTypedRuleContext(Swift3Parser.Generic_argumentContext,i)


        def getRuleIndex(self):
            return Swift3Parser.RULE_generic_argument_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGeneric_argument_list" ):
                listener.enterGeneric_argument_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGeneric_argument_list" ):
                listener.exitGeneric_argument_list(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGeneric_argument_list" ):
                return visitor.visitGeneric_argument_list(self)
            else:
                return visitor.visitChildren(self)




    def generic_argument_list(self):

        localctx = Swift3Parser.Generic_argument_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 138, self.RULE_generic_argument_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1025
            self.generic_argument()
            self.state = 1030
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==Swift3Parser.COMMA:
                self.state = 1026
                self.match(Swift3Parser.COMMA)
                self.state = 1027
                self.generic_argument()
                self.state = 1032
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Generic_argumentContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type(self):
            return self.getTypedRuleContext(Swift3Parser.TypeContext,0)


        def getRuleIndex(self):
            return Swift3Parser.RULE_generic_argument

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGeneric_argument" ):
                listener.enterGeneric_argument(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGeneric_argument" ):
                listener.exitGeneric_argument(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGeneric_argument" ):
                return visitor.visitGeneric_argument(self)
            else:
                return visitor.visitChildren(self)




    def generic_argument(self):

        localctx = Swift3Parser.Generic_argumentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 140, self.RULE_generic_argument)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1033
            self.type(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class DeclarationContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def import_declaration(self):
            return self.getTypedRuleContext(Swift3Parser.Import_declarationContext,0)


        def constant_declaration(self):
            return self.getTypedRuleContext(Swift3Parser.Constant_declarationContext,0)


        def variable_declaration(self):
            return self.getTypedRuleContext(Swift3Parser.Variable_declarationContext,0)


        def typealias_declaration(self):
            return self.getTypedRuleContext(Swift3Parser.Typealias_declarationContext,0)


        def function_declaration(self):
            return self.getTypedRuleContext(Swift3Parser.Function_declarationContext,0)


        def enum_declaration(self):
            return self.getTypedRuleContext(Swift3Parser.Enum_declarationContext,0)


        def struct_declaration(self):
            return self.getTypedRuleContext(Swift3Parser.Struct_declarationContext,0)


        def class_declaration(self):
            return self.getTypedRuleContext(Swift3Parser.Class_declarationContext,0)


        def protocol_declaration(self):
            return self.getTypedRuleContext(Swift3Parser.Protocol_declarationContext,0)


        def initializer_declaration(self):
            return self.getTypedRuleContext(Swift3Parser.Initializer_declarationContext,0)


        def deinitializer_declaration(self):
            return self.getTypedRuleContext(Swift3Parser.Deinitializer_declarationContext,0)


        def extension_declaration(self):
            return self.getTypedRuleContext(Swift3Parser.Extension_declarationContext,0)


        def subscript_declaration(self):
            return self.getTypedRuleContext(Swift3Parser.Subscript_declarationContext,0)


        def operator_declaration(self):
            return self.getTypedRuleContext(Swift3Parser.Operator_declarationContext,0)


        def precedence_group_declaration(self):
            return self.getTypedRuleContext(Swift3Parser.Precedence_group_declarationContext,0)


        def getRuleIndex(self):
            return Swift3Parser.RULE_declaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclaration" ):
                listener.enterDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclaration" ):
                listener.exitDeclaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclaration" ):
                return visitor.visitDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def declaration(self):

        localctx = Swift3Parser.DeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 142, self.RULE_declaration)
        try:
            self.state = 1051
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,64,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 1035
                self.import_declaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 1036
                self.constant_declaration()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 1037
                self.variable_declaration()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 1038
                self.typealias_declaration()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 1039
                self.function_declaration()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 1040
                self.enum_declaration()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 1041
                self.struct_declaration()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 1042
                self.class_declaration()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 1043
                self.protocol_declaration()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 1044
                self.initializer_declaration()
                pass

            elif la_ == 11:
                self.enterOuterAlt(localctx, 11)
                self.state = 1045
                self.deinitializer_declaration()
                pass

            elif la_ == 12:
                self.enterOuterAlt(localctx, 12)
                self.state = 1046
                self.extension_declaration()
                pass

            elif la_ == 13:
                self.enterOuterAlt(localctx, 13)
                self.state = 1047
                self.subscript_declaration()
                pass

            elif la_ == 14:
                self.enterOuterAlt(localctx, 14)
                self.state = 1048
                self.operator_declaration()
                pass

            elif la_ == 15:
                self.enterOuterAlt(localctx, 15)
                self.state = 1049
                self.operator_declaration()
                pass

            elif la_ == 16:
                self.enterOuterAlt(localctx, 16)
                self.state = 1050
                self.precedence_group_declaration()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class DeclarationsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Swift3Parser.DeclarationContext)
            else:
                return self.getTypedRuleContext(Swift3Parser.DeclarationContext,i)


        def getRuleIndex(self):
            return Swift3Parser.RULE_declarations

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclarations" ):
                listener.enterDeclarations(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclarations" ):
                listener.exitDeclarations(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclarations" ):
                return visitor.visitDeclarations(self)
            else:
                return visitor.visitChildren(self)




    def declarations(self):

        localctx = Swift3Parser.DeclarationsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 144, self.RULE_declarations)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1054
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 1053
                self.declaration()
                self.state = 1056
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << Swift3Parser.T__4) | (1 << Swift3Parser.T__5) | (1 << Swift3Parser.T__32) | (1 << Swift3Parser.T__33) | (1 << Swift3Parser.T__34) | (1 << Swift3Parser.T__35) | (1 << Swift3Parser.T__36) | (1 << Swift3Parser.T__37) | (1 << Swift3Parser.T__38) | (1 << Swift3Parser.T__45) | (1 << Swift3Parser.T__46) | (1 << Swift3Parser.T__48) | (1 << Swift3Parser.T__49) | (1 << Swift3Parser.T__50) | (1 << Swift3Parser.T__51) | (1 << Swift3Parser.T__52) | (1 << Swift3Parser.T__54) | (1 << Swift3Parser.T__55) | (1 << Swift3Parser.T__56))) != 0) or ((((_la - 65)) & ~0x3f) == 0 and ((1 << (_la - 65)) & ((1 << (Swift3Parser.T__64 - 65)) | (1 << (Swift3Parser.T__65 - 65)) | (1 << (Swift3Parser.T__66 - 65)) | (1 << (Swift3Parser.T__67 - 65)) | (1 << (Swift3Parser.T__68 - 65)) | (1 << (Swift3Parser.T__69 - 65)) | (1 << (Swift3Parser.T__70 - 65)) | (1 << (Swift3Parser.T__71 - 65)) | (1 << (Swift3Parser.T__74 - 65)) | (1 << (Swift3Parser.T__75 - 65)) | (1 << (Swift3Parser.T__76 - 65)) | (1 << (Swift3Parser.T__77 - 65)) | (1 << (Swift3Parser.T__78 - 65)) | (1 << (Swift3Parser.T__79 - 65)) | (1 << (Swift3Parser.T__80 - 65)) | (1 << (Swift3Parser.T__81 - 65)))) != 0) or _la==Swift3Parser.AT):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Top_level_declarationContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statements(self):
            return self.getTypedRuleContext(Swift3Parser.StatementsContext,0)


        def getRuleIndex(self):
            return Swift3Parser.RULE_top_level_declaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTop_level_declaration" ):
                listener.enterTop_level_declaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTop_level_declaration" ):
                listener.exitTop_level_declaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTop_level_declaration" ):
                return visitor.visitTop_level_declaration(self)
            else:
                return visitor.visitChildren(self)




    def top_level_declaration(self):

        localctx = Swift3Parser.Top_level_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 146, self.RULE_top_level_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1059
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,66,self._ctx)
            if la_ == 1:
                self.state = 1058
                self.statements()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Code_blockContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statements(self):
            return self.getTypedRuleContext(Swift3Parser.StatementsContext,0)


        def getRuleIndex(self):
            return Swift3Parser.RULE_code_block

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCode_block" ):
                listener.enterCode_block(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCode_block" ):
                listener.exitCode_block(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCode_block" ):
                return visitor.visitCode_block(self)
            else:
                return visitor.visitChildren(self)




    def code_block(self):

        localctx = Swift3Parser.Code_blockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 148, self.RULE_code_block)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1061
            self.match(Swift3Parser.LCURLY)
            self.state = 1063
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,67,self._ctx)
            if la_ == 1:
                self.state = 1062
                self.statements()


            self.state = 1065
            self.match(Swift3Parser.RCURLY)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Import_declarationContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def import_path(self):
            return self.getTypedRuleContext(Swift3Parser.Import_pathContext,0)


        def attributes(self):
            return self.getTypedRuleContext(Swift3Parser.AttributesContext,0)


        def import_kind(self):
            return self.getTypedRuleContext(Swift3Parser.Import_kindContext,0)


        def getRuleIndex(self):
            return Swift3Parser.RULE_import_declaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterImport_declaration" ):
                listener.enterImport_declaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitImport_declaration" ):
                listener.exitImport_declaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitImport_declaration" ):
                return visitor.visitImport_declaration(self)
            else:
                return visitor.visitChildren(self)




    def import_declaration(self):

        localctx = Swift3Parser.Import_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 150, self.RULE_import_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1068
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==Swift3Parser.AT:
                self.state = 1067
                self.attributes()


            self.state = 1070
            self.match(Swift3Parser.T__32)
            self.state = 1072
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << Swift3Parser.T__5) | (1 << Swift3Parser.T__33) | (1 << Swift3Parser.T__34) | (1 << Swift3Parser.T__35) | (1 << Swift3Parser.T__36) | (1 << Swift3Parser.T__37) | (1 << Swift3Parser.T__38))) != 0):
                self.state = 1071
                self.import_kind()


            self.state = 1074
            self.import_path()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Import_kindContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return Swift3Parser.RULE_import_kind

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterImport_kind" ):
                listener.enterImport_kind(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitImport_kind" ):
                listener.exitImport_kind(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitImport_kind" ):
                return visitor.visitImport_kind(self)
            else:
                return visitor.visitChildren(self)




    def import_kind(self):

        localctx = Swift3Parser.Import_kindContext(self, self._ctx, self.state)
        self.enterRule(localctx, 152, self.RULE_import_kind)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1076
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << Swift3Parser.T__5) | (1 << Swift3Parser.T__33) | (1 << Swift3Parser.T__34) | (1 << Swift3Parser.T__35) | (1 << Swift3Parser.T__36) | (1 << Swift3Parser.T__37) | (1 << Swift3Parser.T__38))) != 0)):
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

    class Import_pathContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def import_path_identifier(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Swift3Parser.Import_path_identifierContext)
            else:
                return self.getTypedRuleContext(Swift3Parser.Import_path_identifierContext,i)


        def getRuleIndex(self):
            return Swift3Parser.RULE_import_path

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterImport_path" ):
                listener.enterImport_path(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitImport_path" ):
                listener.exitImport_path(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitImport_path" ):
                return visitor.visitImport_path(self)
            else:
                return visitor.visitChildren(self)




    def import_path(self):

        localctx = Swift3Parser.Import_pathContext(self, self._ctx, self.state)
        self.enterRule(localctx, 154, self.RULE_import_path)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1078
            self.import_path_identifier()
            self.state = 1083
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,70,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1079
                    self.match(Swift3Parser.DOT)
                    self.state = 1080
                    self.import_path_identifier()
                self.state = 1085
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,70,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Import_path_identifierContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declaration_identifier(self):
            return self.getTypedRuleContext(Swift3Parser.Declaration_identifierContext,0)


        def operator(self):
            return self.getTypedRuleContext(Swift3Parser.OperatorContext,0)


        def getRuleIndex(self):
            return Swift3Parser.RULE_import_path_identifier

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterImport_path_identifier" ):
                listener.enterImport_path_identifier(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitImport_path_identifier" ):
                listener.exitImport_path_identifier(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitImport_path_identifier" ):
                return visitor.visitImport_path_identifier(self)
            else:
                return visitor.visitChildren(self)




    def import_path_identifier(self):

        localctx = Swift3Parser.Import_path_identifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 156, self.RULE_import_path_identifier)
        try:
            self.state = 1088
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [Swift3Parser.T__25, Swift3Parser.T__26, Swift3Parser.T__27, Swift3Parser.T__29, Swift3Parser.T__30, Swift3Parser.T__39, Swift3Parser.T__40, Swift3Parser.T__41, Swift3Parser.T__42, Swift3Parser.T__45, Swift3Parser.T__46, Swift3Parser.T__52, Swift3Parser.T__54, Swift3Parser.T__55, Swift3Parser.T__57, Swift3Parser.T__58, Swift3Parser.T__59, Swift3Parser.T__60, Swift3Parser.T__61, Swift3Parser.T__62, Swift3Parser.T__63, Swift3Parser.T__64, Swift3Parser.T__65, Swift3Parser.T__66, Swift3Parser.T__67, Swift3Parser.T__68, Swift3Parser.T__69, Swift3Parser.T__71, Swift3Parser.T__72, Swift3Parser.T__73, Swift3Parser.T__74, Swift3Parser.T__79, Swift3Parser.T__80, Swift3Parser.T__81, Swift3Parser.T__93, Swift3Parser.T__94, Swift3Parser.T__95, Swift3Parser.T__96, Swift3Parser.T__98, Swift3Parser.T__109, Swift3Parser.T__110, Swift3Parser.T__111, Swift3Parser.T__112, Swift3Parser.T__115, Swift3Parser.T__116, Swift3Parser.T__117, Swift3Parser.T__118, Swift3Parser.T__119, Swift3Parser.T__120, Swift3Parser.T__121, Swift3Parser.T__122, Swift3Parser.T__123, Swift3Parser.T__124, Swift3Parser.T__125, Swift3Parser.Identifier]:
                self.enterOuterAlt(localctx, 1)
                self.state = 1086
                self.declaration_identifier()
                pass
            elif token in [Swift3Parser.DOT, Swift3Parser.LT, Swift3Parser.GT, Swift3Parser.BANG, Swift3Parser.QUESTION, Swift3Parser.AND, Swift3Parser.SUB, Swift3Parser.EQUAL, Swift3Parser.OR, Swift3Parser.DIV, Swift3Parser.ADD, Swift3Parser.MUL, Swift3Parser.MOD, Swift3Parser.CARET, Swift3Parser.TILDE, Swift3Parser.Operator_head_other]:
                self.enterOuterAlt(localctx, 2)
                self.state = 1087
                self.operator()
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

    class Constant_declarationContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def pattern_initializer_list(self):
            return self.getTypedRuleContext(Swift3Parser.Pattern_initializer_listContext,0)


        def attributes(self):
            return self.getTypedRuleContext(Swift3Parser.AttributesContext,0)


        def declaration_modifiers(self):
            return self.getTypedRuleContext(Swift3Parser.Declaration_modifiersContext,0)


        def getRuleIndex(self):
            return Swift3Parser.RULE_constant_declaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConstant_declaration" ):
                listener.enterConstant_declaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConstant_declaration" ):
                listener.exitConstant_declaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConstant_declaration" ):
                return visitor.visitConstant_declaration(self)
            else:
                return visitor.visitChildren(self)




    def constant_declaration(self):

        localctx = Swift3Parser.Constant_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 158, self.RULE_constant_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1091
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==Swift3Parser.AT:
                self.state = 1090
                self.attributes()


            self.state = 1094
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((((_la - 36)) & ~0x3f) == 0 and ((1 << (_la - 36)) & ((1 << (Swift3Parser.T__35 - 36)) | (1 << (Swift3Parser.T__46 - 36)) | (1 << (Swift3Parser.T__52 - 36)) | (1 << (Swift3Parser.T__54 - 36)) | (1 << (Swift3Parser.T__55 - 36)) | (1 << (Swift3Parser.T__64 - 36)) | (1 << (Swift3Parser.T__65 - 36)) | (1 << (Swift3Parser.T__66 - 36)) | (1 << (Swift3Parser.T__67 - 36)) | (1 << (Swift3Parser.T__68 - 36)) | (1 << (Swift3Parser.T__69 - 36)) | (1 << (Swift3Parser.T__70 - 36)) | (1 << (Swift3Parser.T__71 - 36)) | (1 << (Swift3Parser.T__74 - 36)) | (1 << (Swift3Parser.T__75 - 36)) | (1 << (Swift3Parser.T__76 - 36)) | (1 << (Swift3Parser.T__77 - 36)) | (1 << (Swift3Parser.T__78 - 36)) | (1 << (Swift3Parser.T__79 - 36)) | (1 << (Swift3Parser.T__80 - 36)) | (1 << (Swift3Parser.T__81 - 36)))) != 0):
                self.state = 1093
                self.declaration_modifiers()


            self.state = 1096
            self.match(Swift3Parser.T__4)
            self.state = 1097
            self.pattern_initializer_list()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Pattern_initializer_listContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def pattern_initializer(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Swift3Parser.Pattern_initializerContext)
            else:
                return self.getTypedRuleContext(Swift3Parser.Pattern_initializerContext,i)


        def getRuleIndex(self):
            return Swift3Parser.RULE_pattern_initializer_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPattern_initializer_list" ):
                listener.enterPattern_initializer_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPattern_initializer_list" ):
                listener.exitPattern_initializer_list(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPattern_initializer_list" ):
                return visitor.visitPattern_initializer_list(self)
            else:
                return visitor.visitChildren(self)




    def pattern_initializer_list(self):

        localctx = Swift3Parser.Pattern_initializer_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 160, self.RULE_pattern_initializer_list)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1099
            self.pattern_initializer()
            self.state = 1104
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,74,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1100
                    self.match(Swift3Parser.COMMA)
                    self.state = 1101
                    self.pattern_initializer()
                self.state = 1106
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,74,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Pattern_initializerContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def pattern(self):
            return self.getTypedRuleContext(Swift3Parser.PatternContext,0)


        def initializer(self):
            return self.getTypedRuleContext(Swift3Parser.InitializerContext,0)


        def getRuleIndex(self):
            return Swift3Parser.RULE_pattern_initializer

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPattern_initializer" ):
                listener.enterPattern_initializer(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPattern_initializer" ):
                listener.exitPattern_initializer(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPattern_initializer" ):
                return visitor.visitPattern_initializer(self)
            else:
                return visitor.visitChildren(self)




    def pattern_initializer(self):

        localctx = Swift3Parser.Pattern_initializerContext(self, self._ctx, self.state)
        self.enterRule(localctx, 162, self.RULE_pattern_initializer)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1107
            self.pattern(0)
            self.state = 1109
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,75,self._ctx)
            if la_ == 1:
                self.state = 1108
                self.initializer()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class InitializerContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assignment_operator(self):
            return self.getTypedRuleContext(Swift3Parser.Assignment_operatorContext,0)


        def expression(self):
            return self.getTypedRuleContext(Swift3Parser.ExpressionContext,0)


        def getRuleIndex(self):
            return Swift3Parser.RULE_initializer

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInitializer" ):
                listener.enterInitializer(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInitializer" ):
                listener.exitInitializer(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInitializer" ):
                return visitor.visitInitializer(self)
            else:
                return visitor.visitChildren(self)




    def initializer(self):

        localctx = Swift3Parser.InitializerContext(self, self._ctx, self.state)
        self.enterRule(localctx, 164, self.RULE_initializer)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1111
            self.assignment_operator()
            self.state = 1112
            self.expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Variable_declarationContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variable_declaration_head(self):
            return self.getTypedRuleContext(Swift3Parser.Variable_declaration_headContext,0)


        def variable_name(self):
            return self.getTypedRuleContext(Swift3Parser.Variable_nameContext,0)


        def type_annotation(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Swift3Parser.Type_annotationContext)
            else:
                return self.getTypedRuleContext(Swift3Parser.Type_annotationContext,i)


        def code_block(self):
            return self.getTypedRuleContext(Swift3Parser.Code_blockContext,0)


        def getter_setter_block(self):
            return self.getTypedRuleContext(Swift3Parser.Getter_setter_blockContext,0)


        def getter_setter_keyword_block(self):
            return self.getTypedRuleContext(Swift3Parser.Getter_setter_keyword_blockContext,0)


        def willSet_didSet_block(self):
            return self.getTypedRuleContext(Swift3Parser.WillSet_didSet_blockContext,0)


        def initializer(self):
            return self.getTypedRuleContext(Swift3Parser.InitializerContext,0)


        def pattern_initializer_list(self):
            return self.getTypedRuleContext(Swift3Parser.Pattern_initializer_listContext,0)


        def getRuleIndex(self):
            return Swift3Parser.RULE_variable_declaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariable_declaration" ):
                listener.enterVariable_declaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariable_declaration" ):
                listener.exitVariable_declaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariable_declaration" ):
                return visitor.visitVariable_declaration(self)
            else:
                return visitor.visitChildren(self)




    def variable_declaration(self):

        localctx = Swift3Parser.Variable_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 166, self.RULE_variable_declaration)
        try:
            self.state = 1149
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,78,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 1114
                self.variable_declaration_head()
                self.state = 1115
                self.variable_name()
                self.state = 1116
                self.type_annotation()
                self.state = 1117
                self.code_block()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 1119
                self.variable_declaration_head()
                self.state = 1120
                self.variable_name()
                self.state = 1121
                self.type_annotation()
                self.state = 1122
                self.getter_setter_block()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 1124
                self.variable_declaration_head()
                self.state = 1125
                self.variable_name()
                self.state = 1126
                self.type_annotation()
                self.state = 1127
                self.getter_setter_keyword_block()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 1129
                self.variable_declaration_head()
                self.state = 1130
                self.variable_name()
                self.state = 1131
                self.type_annotation()
                self.state = 1133
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,76,self._ctx)
                if la_ == 1:
                    self.state = 1132
                    self.initializer()


                self.state = 1135
                self.willSet_didSet_block()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 1137
                self.variable_declaration_head()
                self.state = 1138
                self.variable_name()
                self.state = 1139
                self.type_annotation()
                self.state = 1140
                self.type_annotation()
                self.state = 1142
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,77,self._ctx)
                if la_ == 1:
                    self.state = 1141
                    self.initializer()


                self.state = 1144
                self.willSet_didSet_block()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 1146
                self.variable_declaration_head()
                self.state = 1147
                self.pattern_initializer_list()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Variable_declaration_headContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def attributes(self):
            return self.getTypedRuleContext(Swift3Parser.AttributesContext,0)


        def declaration_modifiers(self):
            return self.getTypedRuleContext(Swift3Parser.Declaration_modifiersContext,0)


        def getRuleIndex(self):
            return Swift3Parser.RULE_variable_declaration_head

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariable_declaration_head" ):
                listener.enterVariable_declaration_head(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariable_declaration_head" ):
                listener.exitVariable_declaration_head(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariable_declaration_head" ):
                return visitor.visitVariable_declaration_head(self)
            else:
                return visitor.visitChildren(self)




    def variable_declaration_head(self):

        localctx = Swift3Parser.Variable_declaration_headContext(self, self._ctx, self.state)
        self.enterRule(localctx, 168, self.RULE_variable_declaration_head)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1152
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==Swift3Parser.AT:
                self.state = 1151
                self.attributes()


            self.state = 1155
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((((_la - 36)) & ~0x3f) == 0 and ((1 << (_la - 36)) & ((1 << (Swift3Parser.T__35 - 36)) | (1 << (Swift3Parser.T__46 - 36)) | (1 << (Swift3Parser.T__52 - 36)) | (1 << (Swift3Parser.T__54 - 36)) | (1 << (Swift3Parser.T__55 - 36)) | (1 << (Swift3Parser.T__64 - 36)) | (1 << (Swift3Parser.T__65 - 36)) | (1 << (Swift3Parser.T__66 - 36)) | (1 << (Swift3Parser.T__67 - 36)) | (1 << (Swift3Parser.T__68 - 36)) | (1 << (Swift3Parser.T__69 - 36)) | (1 << (Swift3Parser.T__70 - 36)) | (1 << (Swift3Parser.T__71 - 36)) | (1 << (Swift3Parser.T__74 - 36)) | (1 << (Swift3Parser.T__75 - 36)) | (1 << (Swift3Parser.T__76 - 36)) | (1 << (Swift3Parser.T__77 - 36)) | (1 << (Swift3Parser.T__78 - 36)) | (1 << (Swift3Parser.T__79 - 36)) | (1 << (Swift3Parser.T__80 - 36)) | (1 << (Swift3Parser.T__81 - 36)))) != 0):
                self.state = 1154
                self.declaration_modifiers()


            self.state = 1157
            self.match(Swift3Parser.T__5)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Variable_nameContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declaration_identifier(self):
            return self.getTypedRuleContext(Swift3Parser.Declaration_identifierContext,0)


        def getRuleIndex(self):
            return Swift3Parser.RULE_variable_name

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariable_name" ):
                listener.enterVariable_name(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariable_name" ):
                listener.exitVariable_name(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariable_name" ):
                return visitor.visitVariable_name(self)
            else:
                return visitor.visitChildren(self)




    def variable_name(self):

        localctx = Swift3Parser.Variable_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 170, self.RULE_variable_name)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1159
            self.declaration_identifier()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Getter_setter_blockContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def getter_clause(self):
            return self.getTypedRuleContext(Swift3Parser.Getter_clauseContext,0)


        def setter_clause(self):
            return self.getTypedRuleContext(Swift3Parser.Setter_clauseContext,0)


        def getRuleIndex(self):
            return Swift3Parser.RULE_getter_setter_block

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGetter_setter_block" ):
                listener.enterGetter_setter_block(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGetter_setter_block" ):
                listener.exitGetter_setter_block(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGetter_setter_block" ):
                return visitor.visitGetter_setter_block(self)
            else:
                return visitor.visitChildren(self)




    def getter_setter_block(self):

        localctx = Swift3Parser.Getter_setter_blockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 172, self.RULE_getter_setter_block)
        self._la = 0 # Token type
        try:
            self.state = 1173
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,82,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 1161
                self.match(Swift3Parser.LCURLY)
                self.state = 1162
                self.getter_clause()
                self.state = 1164
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if ((((_la - 41)) & ~0x3f) == 0 and ((1 << (_la - 41)) & ((1 << (Swift3Parser.T__40 - 41)) | (1 << (Swift3Parser.T__80 - 41)) | (1 << (Swift3Parser.T__81 - 41)))) != 0) or _la==Swift3Parser.AT:
                    self.state = 1163
                    self.setter_clause()


                self.state = 1166
                self.match(Swift3Parser.RCURLY)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 1168
                self.match(Swift3Parser.LCURLY)
                self.state = 1169
                self.setter_clause()
                self.state = 1170
                self.getter_clause()
                self.state = 1171
                self.match(Swift3Parser.RCURLY)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Getter_clauseContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def code_block(self):
            return self.getTypedRuleContext(Swift3Parser.Code_blockContext,0)


        def attributes(self):
            return self.getTypedRuleContext(Swift3Parser.AttributesContext,0)


        def mutation_modifier(self):
            return self.getTypedRuleContext(Swift3Parser.Mutation_modifierContext,0)


        def getRuleIndex(self):
            return Swift3Parser.RULE_getter_clause

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGetter_clause" ):
                listener.enterGetter_clause(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGetter_clause" ):
                listener.exitGetter_clause(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGetter_clause" ):
                return visitor.visitGetter_clause(self)
            else:
                return visitor.visitChildren(self)




    def getter_clause(self):

        localctx = Swift3Parser.Getter_clauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 174, self.RULE_getter_clause)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1176
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==Swift3Parser.AT:
                self.state = 1175
                self.attributes()


            self.state = 1179
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==Swift3Parser.T__80 or _la==Swift3Parser.T__81:
                self.state = 1178
                self.mutation_modifier()


            self.state = 1181
            self.match(Swift3Parser.T__39)
            self.state = 1182
            self.code_block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Setter_clauseContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def code_block(self):
            return self.getTypedRuleContext(Swift3Parser.Code_blockContext,0)


        def attributes(self):
            return self.getTypedRuleContext(Swift3Parser.AttributesContext,0)


        def mutation_modifier(self):
            return self.getTypedRuleContext(Swift3Parser.Mutation_modifierContext,0)


        def setter_name(self):
            return self.getTypedRuleContext(Swift3Parser.Setter_nameContext,0)


        def getRuleIndex(self):
            return Swift3Parser.RULE_setter_clause

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSetter_clause" ):
                listener.enterSetter_clause(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSetter_clause" ):
                listener.exitSetter_clause(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSetter_clause" ):
                return visitor.visitSetter_clause(self)
            else:
                return visitor.visitChildren(self)




    def setter_clause(self):

        localctx = Swift3Parser.Setter_clauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 176, self.RULE_setter_clause)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1185
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==Swift3Parser.AT:
                self.state = 1184
                self.attributes()


            self.state = 1188
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==Swift3Parser.T__80 or _la==Swift3Parser.T__81:
                self.state = 1187
                self.mutation_modifier()


            self.state = 1190
            self.match(Swift3Parser.T__40)
            self.state = 1192
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==Swift3Parser.LPAREN:
                self.state = 1191
                self.setter_name()


            self.state = 1194
            self.code_block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Setter_nameContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declaration_identifier(self):
            return self.getTypedRuleContext(Swift3Parser.Declaration_identifierContext,0)


        def getRuleIndex(self):
            return Swift3Parser.RULE_setter_name

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSetter_name" ):
                listener.enterSetter_name(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSetter_name" ):
                listener.exitSetter_name(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSetter_name" ):
                return visitor.visitSetter_name(self)
            else:
                return visitor.visitChildren(self)




    def setter_name(self):

        localctx = Swift3Parser.Setter_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 178, self.RULE_setter_name)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1196
            self.match(Swift3Parser.LPAREN)
            self.state = 1197
            self.declaration_identifier()
            self.state = 1198
            self.match(Swift3Parser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Getter_setter_keyword_blockContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def getter_keyword_clause(self):
            return self.getTypedRuleContext(Swift3Parser.Getter_keyword_clauseContext,0)


        def setter_keyword_clause(self):
            return self.getTypedRuleContext(Swift3Parser.Setter_keyword_clauseContext,0)


        def getRuleIndex(self):
            return Swift3Parser.RULE_getter_setter_keyword_block

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGetter_setter_keyword_block" ):
                listener.enterGetter_setter_keyword_block(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGetter_setter_keyword_block" ):
                listener.exitGetter_setter_keyword_block(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGetter_setter_keyword_block" ):
                return visitor.visitGetter_setter_keyword_block(self)
            else:
                return visitor.visitChildren(self)




    def getter_setter_keyword_block(self):

        localctx = Swift3Parser.Getter_setter_keyword_blockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 180, self.RULE_getter_setter_keyword_block)
        self._la = 0 # Token type
        try:
            self.state = 1212
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,89,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 1200
                self.match(Swift3Parser.LCURLY)
                self.state = 1201
                self.getter_keyword_clause()
                self.state = 1203
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if ((((_la - 41)) & ~0x3f) == 0 and ((1 << (_la - 41)) & ((1 << (Swift3Parser.T__40 - 41)) | (1 << (Swift3Parser.T__80 - 41)) | (1 << (Swift3Parser.T__81 - 41)))) != 0) or _la==Swift3Parser.AT:
                    self.state = 1202
                    self.setter_keyword_clause()


                self.state = 1205
                self.match(Swift3Parser.RCURLY)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 1207
                self.match(Swift3Parser.LCURLY)
                self.state = 1208
                self.setter_keyword_clause()
                self.state = 1209
                self.getter_keyword_clause()
                self.state = 1210
                self.match(Swift3Parser.RCURLY)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Getter_keyword_clauseContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def attributes(self):
            return self.getTypedRuleContext(Swift3Parser.AttributesContext,0)


        def mutation_modifier(self):
            return self.getTypedRuleContext(Swift3Parser.Mutation_modifierContext,0)


        def getRuleIndex(self):
            return Swift3Parser.RULE_getter_keyword_clause

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGetter_keyword_clause" ):
                listener.enterGetter_keyword_clause(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGetter_keyword_clause" ):
                listener.exitGetter_keyword_clause(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGetter_keyword_clause" ):
                return visitor.visitGetter_keyword_clause(self)
            else:
                return visitor.visitChildren(self)




    def getter_keyword_clause(self):

        localctx = Swift3Parser.Getter_keyword_clauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 182, self.RULE_getter_keyword_clause)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1215
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==Swift3Parser.AT:
                self.state = 1214
                self.attributes()


            self.state = 1218
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==Swift3Parser.T__80 or _la==Swift3Parser.T__81:
                self.state = 1217
                self.mutation_modifier()


            self.state = 1220
            self.match(Swift3Parser.T__39)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Setter_keyword_clauseContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def attributes(self):
            return self.getTypedRuleContext(Swift3Parser.AttributesContext,0)


        def mutation_modifier(self):
            return self.getTypedRuleContext(Swift3Parser.Mutation_modifierContext,0)


        def getRuleIndex(self):
            return Swift3Parser.RULE_setter_keyword_clause

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSetter_keyword_clause" ):
                listener.enterSetter_keyword_clause(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSetter_keyword_clause" ):
                listener.exitSetter_keyword_clause(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSetter_keyword_clause" ):
                return visitor.visitSetter_keyword_clause(self)
            else:
                return visitor.visitChildren(self)




    def setter_keyword_clause(self):

        localctx = Swift3Parser.Setter_keyword_clauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 184, self.RULE_setter_keyword_clause)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1223
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==Swift3Parser.AT:
                self.state = 1222
                self.attributes()


            self.state = 1226
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==Swift3Parser.T__80 or _la==Swift3Parser.T__81:
                self.state = 1225
                self.mutation_modifier()


            self.state = 1228
            self.match(Swift3Parser.T__40)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class WillSet_didSet_blockContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def willSet_clause(self):
            return self.getTypedRuleContext(Swift3Parser.WillSet_clauseContext,0)


        def didSet_clause(self):
            return self.getTypedRuleContext(Swift3Parser.DidSet_clauseContext,0)


        def getRuleIndex(self):
            return Swift3Parser.RULE_willSet_didSet_block

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWillSet_didSet_block" ):
                listener.enterWillSet_didSet_block(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWillSet_didSet_block" ):
                listener.exitWillSet_didSet_block(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWillSet_didSet_block" ):
                return visitor.visitWillSet_didSet_block(self)
            else:
                return visitor.visitChildren(self)




    def willSet_didSet_block(self):

        localctx = Swift3Parser.WillSet_didSet_blockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 186, self.RULE_willSet_didSet_block)
        self._la = 0 # Token type
        try:
            self.state = 1242
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,95,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 1230
                self.match(Swift3Parser.LCURLY)
                self.state = 1231
                self.willSet_clause()
                self.state = 1233
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==Swift3Parser.T__42 or _la==Swift3Parser.AT:
                    self.state = 1232
                    self.didSet_clause()


                self.state = 1235
                self.match(Swift3Parser.RCURLY)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 1237
                self.match(Swift3Parser.LCURLY)
                self.state = 1238
                self.didSet_clause()
                self.state = 1239
                self.willSet_clause()
                self.state = 1240
                self.match(Swift3Parser.RCURLY)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class WillSet_clauseContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def code_block(self):
            return self.getTypedRuleContext(Swift3Parser.Code_blockContext,0)


        def attributes(self):
            return self.getTypedRuleContext(Swift3Parser.AttributesContext,0)


        def setter_name(self):
            return self.getTypedRuleContext(Swift3Parser.Setter_nameContext,0)


        def getRuleIndex(self):
            return Swift3Parser.RULE_willSet_clause

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWillSet_clause" ):
                listener.enterWillSet_clause(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWillSet_clause" ):
                listener.exitWillSet_clause(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWillSet_clause" ):
                return visitor.visitWillSet_clause(self)
            else:
                return visitor.visitChildren(self)




    def willSet_clause(self):

        localctx = Swift3Parser.WillSet_clauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 188, self.RULE_willSet_clause)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1245
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==Swift3Parser.AT:
                self.state = 1244
                self.attributes()


            self.state = 1247
            self.match(Swift3Parser.T__41)
            self.state = 1249
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==Swift3Parser.LPAREN:
                self.state = 1248
                self.setter_name()


            self.state = 1251
            self.code_block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class DidSet_clauseContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def code_block(self):
            return self.getTypedRuleContext(Swift3Parser.Code_blockContext,0)


        def attributes(self):
            return self.getTypedRuleContext(Swift3Parser.AttributesContext,0)


        def setter_name(self):
            return self.getTypedRuleContext(Swift3Parser.Setter_nameContext,0)


        def getRuleIndex(self):
            return Swift3Parser.RULE_didSet_clause

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDidSet_clause" ):
                listener.enterDidSet_clause(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDidSet_clause" ):
                listener.exitDidSet_clause(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDidSet_clause" ):
                return visitor.visitDidSet_clause(self)
            else:
                return visitor.visitChildren(self)




    def didSet_clause(self):

        localctx = Swift3Parser.DidSet_clauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 190, self.RULE_didSet_clause)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1254
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==Swift3Parser.AT:
                self.state = 1253
                self.attributes()


            self.state = 1256
            self.match(Swift3Parser.T__42)
            self.state = 1258
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==Swift3Parser.LPAREN:
                self.state = 1257
                self.setter_name()


            self.state = 1260
            self.code_block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Typealias_declarationContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def typealias_name(self):
            return self.getTypedRuleContext(Swift3Parser.Typealias_nameContext,0)


        def typealias_assignment(self):
            return self.getTypedRuleContext(Swift3Parser.Typealias_assignmentContext,0)


        def attributes(self):
            return self.getTypedRuleContext(Swift3Parser.AttributesContext,0)


        def access_level_modifier(self):
            return self.getTypedRuleContext(Swift3Parser.Access_level_modifierContext,0)


        def generic_parameter_clause(self):
            return self.getTypedRuleContext(Swift3Parser.Generic_parameter_clauseContext,0)


        def getRuleIndex(self):
            return Swift3Parser.RULE_typealias_declaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTypealias_declaration" ):
                listener.enterTypealias_declaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTypealias_declaration" ):
                listener.exitTypealias_declaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTypealias_declaration" ):
                return visitor.visitTypealias_declaration(self)
            else:
                return visitor.visitChildren(self)




    def typealias_declaration(self):

        localctx = Swift3Parser.Typealias_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 192, self.RULE_typealias_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1263
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==Swift3Parser.AT:
                self.state = 1262
                self.attributes()


            self.state = 1266
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((((_la - 76)) & ~0x3f) == 0 and ((1 << (_la - 76)) & ((1 << (Swift3Parser.T__75 - 76)) | (1 << (Swift3Parser.T__76 - 76)) | (1 << (Swift3Parser.T__77 - 76)) | (1 << (Swift3Parser.T__78 - 76)) | (1 << (Swift3Parser.T__79 - 76)))) != 0):
                self.state = 1265
                self.access_level_modifier()


            self.state = 1268
            self.match(Swift3Parser.T__33)
            self.state = 1269
            self.typealias_name()
            self.state = 1271
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,102,self._ctx)
            if la_ == 1:
                self.state = 1270
                self.generic_parameter_clause()


            self.state = 1273
            self.typealias_assignment()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Typealias_nameContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declaration_identifier(self):
            return self.getTypedRuleContext(Swift3Parser.Declaration_identifierContext,0)


        def getRuleIndex(self):
            return Swift3Parser.RULE_typealias_name

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTypealias_name" ):
                listener.enterTypealias_name(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTypealias_name" ):
                listener.exitTypealias_name(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTypealias_name" ):
                return visitor.visitTypealias_name(self)
            else:
                return visitor.visitChildren(self)




    def typealias_name(self):

        localctx = Swift3Parser.Typealias_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 194, self.RULE_typealias_name)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1275
            self.declaration_identifier()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Typealias_assignmentContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assignment_operator(self):
            return self.getTypedRuleContext(Swift3Parser.Assignment_operatorContext,0)


        def type(self):
            return self.getTypedRuleContext(Swift3Parser.TypeContext,0)


        def getRuleIndex(self):
            return Swift3Parser.RULE_typealias_assignment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTypealias_assignment" ):
                listener.enterTypealias_assignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTypealias_assignment" ):
                listener.exitTypealias_assignment(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTypealias_assignment" ):
                return visitor.visitTypealias_assignment(self)
            else:
                return visitor.visitChildren(self)




    def typealias_assignment(self):

        localctx = Swift3Parser.Typealias_assignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 196, self.RULE_typealias_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1277
            self.assignment_operator()
            self.state = 1278
            self.type(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Function_declarationContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def function_head(self):
            return self.getTypedRuleContext(Swift3Parser.Function_headContext,0)


        def function_name(self):
            return self.getTypedRuleContext(Swift3Parser.Function_nameContext,0)


        def function_signature(self):
            return self.getTypedRuleContext(Swift3Parser.Function_signatureContext,0)


        def generic_parameter_clause(self):
            return self.getTypedRuleContext(Swift3Parser.Generic_parameter_clauseContext,0)


        def generic_where_clause(self):
            return self.getTypedRuleContext(Swift3Parser.Generic_where_clauseContext,0)


        def function_body(self):
            return self.getTypedRuleContext(Swift3Parser.Function_bodyContext,0)


        def getRuleIndex(self):
            return Swift3Parser.RULE_function_declaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunction_declaration" ):
                listener.enterFunction_declaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunction_declaration" ):
                listener.exitFunction_declaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunction_declaration" ):
                return visitor.visitFunction_declaration(self)
            else:
                return visitor.visitChildren(self)




    def function_declaration(self):

        localctx = Swift3Parser.Function_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 198, self.RULE_function_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1280
            self.function_head()
            self.state = 1281
            self.function_name()
            self.state = 1283
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==Swift3Parser.LT:
                self.state = 1282
                self.generic_parameter_clause()


            self.state = 1285
            self.function_signature()
            self.state = 1287
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,104,self._ctx)
            if la_ == 1:
                self.state = 1286
                self.generic_where_clause()


            self.state = 1290
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,105,self._ctx)
            if la_ == 1:
                self.state = 1289
                self.function_body()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Function_headContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def attributes(self):
            return self.getTypedRuleContext(Swift3Parser.AttributesContext,0)


        def declaration_modifiers(self):
            return self.getTypedRuleContext(Swift3Parser.Declaration_modifiersContext,0)


        def getRuleIndex(self):
            return Swift3Parser.RULE_function_head

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunction_head" ):
                listener.enterFunction_head(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunction_head" ):
                listener.exitFunction_head(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunction_head" ):
                return visitor.visitFunction_head(self)
            else:
                return visitor.visitChildren(self)




    def function_head(self):

        localctx = Swift3Parser.Function_headContext(self, self._ctx, self.state)
        self.enterRule(localctx, 200, self.RULE_function_head)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1293
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==Swift3Parser.AT:
                self.state = 1292
                self.attributes()


            self.state = 1296
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((((_la - 36)) & ~0x3f) == 0 and ((1 << (_la - 36)) & ((1 << (Swift3Parser.T__35 - 36)) | (1 << (Swift3Parser.T__46 - 36)) | (1 << (Swift3Parser.T__52 - 36)) | (1 << (Swift3Parser.T__54 - 36)) | (1 << (Swift3Parser.T__55 - 36)) | (1 << (Swift3Parser.T__64 - 36)) | (1 << (Swift3Parser.T__65 - 36)) | (1 << (Swift3Parser.T__66 - 36)) | (1 << (Swift3Parser.T__67 - 36)) | (1 << (Swift3Parser.T__68 - 36)) | (1 << (Swift3Parser.T__69 - 36)) | (1 << (Swift3Parser.T__70 - 36)) | (1 << (Swift3Parser.T__71 - 36)) | (1 << (Swift3Parser.T__74 - 36)) | (1 << (Swift3Parser.T__75 - 36)) | (1 << (Swift3Parser.T__76 - 36)) | (1 << (Swift3Parser.T__77 - 36)) | (1 << (Swift3Parser.T__78 - 36)) | (1 << (Swift3Parser.T__79 - 36)) | (1 << (Swift3Parser.T__80 - 36)) | (1 << (Swift3Parser.T__81 - 36)))) != 0):
                self.state = 1295
                self.declaration_modifiers()


            self.state = 1298
            self.match(Swift3Parser.T__38)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Function_nameContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declaration_identifier(self):
            return self.getTypedRuleContext(Swift3Parser.Declaration_identifierContext,0)


        def operator(self):
            return self.getTypedRuleContext(Swift3Parser.OperatorContext,0)


        def getRuleIndex(self):
            return Swift3Parser.RULE_function_name

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunction_name" ):
                listener.enterFunction_name(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunction_name" ):
                listener.exitFunction_name(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunction_name" ):
                return visitor.visitFunction_name(self)
            else:
                return visitor.visitChildren(self)




    def function_name(self):

        localctx = Swift3Parser.Function_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 202, self.RULE_function_name)
        try:
            self.state = 1302
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [Swift3Parser.T__25, Swift3Parser.T__26, Swift3Parser.T__27, Swift3Parser.T__29, Swift3Parser.T__30, Swift3Parser.T__39, Swift3Parser.T__40, Swift3Parser.T__41, Swift3Parser.T__42, Swift3Parser.T__45, Swift3Parser.T__46, Swift3Parser.T__52, Swift3Parser.T__54, Swift3Parser.T__55, Swift3Parser.T__57, Swift3Parser.T__58, Swift3Parser.T__59, Swift3Parser.T__60, Swift3Parser.T__61, Swift3Parser.T__62, Swift3Parser.T__63, Swift3Parser.T__64, Swift3Parser.T__65, Swift3Parser.T__66, Swift3Parser.T__67, Swift3Parser.T__68, Swift3Parser.T__69, Swift3Parser.T__71, Swift3Parser.T__72, Swift3Parser.T__73, Swift3Parser.T__74, Swift3Parser.T__79, Swift3Parser.T__80, Swift3Parser.T__81, Swift3Parser.T__93, Swift3Parser.T__94, Swift3Parser.T__95, Swift3Parser.T__96, Swift3Parser.T__98, Swift3Parser.T__109, Swift3Parser.T__110, Swift3Parser.T__111, Swift3Parser.T__112, Swift3Parser.T__115, Swift3Parser.T__116, Swift3Parser.T__117, Swift3Parser.T__118, Swift3Parser.T__119, Swift3Parser.T__120, Swift3Parser.T__121, Swift3Parser.T__122, Swift3Parser.T__123, Swift3Parser.T__124, Swift3Parser.T__125, Swift3Parser.Identifier]:
                self.enterOuterAlt(localctx, 1)
                self.state = 1300
                self.declaration_identifier()
                pass
            elif token in [Swift3Parser.DOT, Swift3Parser.LT, Swift3Parser.GT, Swift3Parser.BANG, Swift3Parser.QUESTION, Swift3Parser.AND, Swift3Parser.SUB, Swift3Parser.EQUAL, Swift3Parser.OR, Swift3Parser.DIV, Swift3Parser.ADD, Swift3Parser.MUL, Swift3Parser.MOD, Swift3Parser.CARET, Swift3Parser.TILDE, Swift3Parser.Operator_head_other]:
                self.enterOuterAlt(localctx, 2)
                self.state = 1301
                self.operator()
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

    class Function_signatureContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def parameter_clause(self):
            return self.getTypedRuleContext(Swift3Parser.Parameter_clauseContext,0)


        def function_result(self):
            return self.getTypedRuleContext(Swift3Parser.Function_resultContext,0)


        def getRuleIndex(self):
            return Swift3Parser.RULE_function_signature

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunction_signature" ):
                listener.enterFunction_signature(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunction_signature" ):
                listener.exitFunction_signature(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunction_signature" ):
                return visitor.visitFunction_signature(self)
            else:
                return visitor.visitChildren(self)




    def function_signature(self):

        localctx = Swift3Parser.Function_signatureContext(self, self._ctx, self.state)
        self.enterRule(localctx, 204, self.RULE_function_signature)
        try:
            self.state = 1316
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,112,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 1304
                self.parameter_clause()
                self.state = 1306
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,109,self._ctx)
                if la_ == 1:
                    self.state = 1305
                    self.match(Swift3Parser.T__43)


                self.state = 1309
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,110,self._ctx)
                if la_ == 1:
                    self.state = 1308
                    self.function_result()


                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 1311
                self.parameter_clause()
                self.state = 1312
                self.match(Swift3Parser.T__44)
                self.state = 1314
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,111,self._ctx)
                if la_ == 1:
                    self.state = 1313
                    self.function_result()


                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Function_resultContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def arrow_operator(self):
            return self.getTypedRuleContext(Swift3Parser.Arrow_operatorContext,0)


        def type(self):
            return self.getTypedRuleContext(Swift3Parser.TypeContext,0)


        def attributes(self):
            return self.getTypedRuleContext(Swift3Parser.AttributesContext,0)


        def getRuleIndex(self):
            return Swift3Parser.RULE_function_result

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunction_result" ):
                listener.enterFunction_result(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunction_result" ):
                listener.exitFunction_result(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunction_result" ):
                return visitor.visitFunction_result(self)
            else:
                return visitor.visitChildren(self)




    def function_result(self):

        localctx = Swift3Parser.Function_resultContext(self, self._ctx, self.state)
        self.enterRule(localctx, 206, self.RULE_function_result)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1318
            self.arrow_operator()
            self.state = 1320
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,113,self._ctx)
            if la_ == 1:
                self.state = 1319
                self.attributes()


            self.state = 1322
            self.type(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Function_bodyContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def code_block(self):
            return self.getTypedRuleContext(Swift3Parser.Code_blockContext,0)


        def getRuleIndex(self):
            return Swift3Parser.RULE_function_body

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunction_body" ):
                listener.enterFunction_body(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunction_body" ):
                listener.exitFunction_body(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunction_body" ):
                return visitor.visitFunction_body(self)
            else:
                return visitor.visitChildren(self)




    def function_body(self):

        localctx = Swift3Parser.Function_bodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 208, self.RULE_function_body)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1324
            self.code_block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Parameter_clauseContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def parameter_list(self):
            return self.getTypedRuleContext(Swift3Parser.Parameter_listContext,0)


        def getRuleIndex(self):
            return Swift3Parser.RULE_parameter_clause

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParameter_clause" ):
                listener.enterParameter_clause(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParameter_clause" ):
                listener.exitParameter_clause(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParameter_clause" ):
                return visitor.visitParameter_clause(self)
            else:
                return visitor.visitChildren(self)




    def parameter_clause(self):

        localctx = Swift3Parser.Parameter_clauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 210, self.RULE_parameter_clause)
        try:
            self.state = 1332
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,114,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 1326
                self.match(Swift3Parser.LPAREN)
                self.state = 1327
                self.match(Swift3Parser.RPAREN)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 1328
                self.match(Swift3Parser.LPAREN)
                self.state = 1329
                self.parameter_list()
                self.state = 1330
                self.match(Swift3Parser.RPAREN)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Parameter_listContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def parameter(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Swift3Parser.ParameterContext)
            else:
                return self.getTypedRuleContext(Swift3Parser.ParameterContext,i)


        def getRuleIndex(self):
            return Swift3Parser.RULE_parameter_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParameter_list" ):
                listener.enterParameter_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParameter_list" ):
                listener.exitParameter_list(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParameter_list" ):
                return visitor.visitParameter_list(self)
            else:
                return visitor.visitChildren(self)




    def parameter_list(self):

        localctx = Swift3Parser.Parameter_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 212, self.RULE_parameter_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1334
            self.parameter()
            self.state = 1339
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==Swift3Parser.COMMA:
                self.state = 1335
                self.match(Swift3Parser.COMMA)
                self.state = 1336
                self.parameter()
                self.state = 1341
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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

        def local_parameter_name(self):
            return self.getTypedRuleContext(Swift3Parser.Local_parameter_nameContext,0)


        def type_annotation(self):
            return self.getTypedRuleContext(Swift3Parser.Type_annotationContext,0)


        def external_parameter_name(self):
            return self.getTypedRuleContext(Swift3Parser.External_parameter_nameContext,0)


        def default_argument_clause(self):
            return self.getTypedRuleContext(Swift3Parser.Default_argument_clauseContext,0)


        def range_operator(self):
            return self.getTypedRuleContext(Swift3Parser.Range_operatorContext,0)


        def getRuleIndex(self):
            return Swift3Parser.RULE_parameter

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParameter" ):
                listener.enterParameter(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParameter" ):
                listener.exitParameter(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParameter" ):
                return visitor.visitParameter(self)
            else:
                return visitor.visitChildren(self)




    def parameter(self):

        localctx = Swift3Parser.ParameterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 214, self.RULE_parameter)
        try:
            self.state = 1363
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,120,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 1343
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,116,self._ctx)
                if la_ == 1:
                    self.state = 1342
                    self.external_parameter_name()


                self.state = 1345
                self.local_parameter_name()
                self.state = 1346
                self.type_annotation()
                self.state = 1348
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,117,self._ctx)
                if la_ == 1:
                    self.state = 1347
                    self.default_argument_clause()


                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 1351
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,118,self._ctx)
                if la_ == 1:
                    self.state = 1350
                    self.external_parameter_name()


                self.state = 1353
                self.local_parameter_name()
                self.state = 1354
                self.type_annotation()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 1357
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,119,self._ctx)
                if la_ == 1:
                    self.state = 1356
                    self.external_parameter_name()


                self.state = 1359
                self.local_parameter_name()
                self.state = 1360
                self.type_annotation()
                self.state = 1361
                self.range_operator()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class External_parameter_nameContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def label_identifier(self):
            return self.getTypedRuleContext(Swift3Parser.Label_identifierContext,0)


        def getRuleIndex(self):
            return Swift3Parser.RULE_external_parameter_name

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExternal_parameter_name" ):
                listener.enterExternal_parameter_name(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExternal_parameter_name" ):
                listener.exitExternal_parameter_name(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExternal_parameter_name" ):
                return visitor.visitExternal_parameter_name(self)
            else:
                return visitor.visitChildren(self)




    def external_parameter_name(self):

        localctx = Swift3Parser.External_parameter_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 216, self.RULE_external_parameter_name)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1365
            self.label_identifier()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Local_parameter_nameContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def label_identifier(self):
            return self.getTypedRuleContext(Swift3Parser.Label_identifierContext,0)


        def getRuleIndex(self):
            return Swift3Parser.RULE_local_parameter_name

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLocal_parameter_name" ):
                listener.enterLocal_parameter_name(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLocal_parameter_name" ):
                listener.exitLocal_parameter_name(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLocal_parameter_name" ):
                return visitor.visitLocal_parameter_name(self)
            else:
                return visitor.visitChildren(self)




    def local_parameter_name(self):

        localctx = Swift3Parser.Local_parameter_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 218, self.RULE_local_parameter_name)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1367
            self.label_identifier()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Default_argument_clauseContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assignment_operator(self):
            return self.getTypedRuleContext(Swift3Parser.Assignment_operatorContext,0)


        def expression(self):
            return self.getTypedRuleContext(Swift3Parser.ExpressionContext,0)


        def getRuleIndex(self):
            return Swift3Parser.RULE_default_argument_clause

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDefault_argument_clause" ):
                listener.enterDefault_argument_clause(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDefault_argument_clause" ):
                listener.exitDefault_argument_clause(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDefault_argument_clause" ):
                return visitor.visitDefault_argument_clause(self)
            else:
                return visitor.visitChildren(self)




    def default_argument_clause(self):

        localctx = Swift3Parser.Default_argument_clauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 220, self.RULE_default_argument_clause)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1369
            self.assignment_operator()
            self.state = 1370
            self.expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Enum_declarationContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def union_style_enum(self):
            return self.getTypedRuleContext(Swift3Parser.Union_style_enumContext,0)


        def attributes(self):
            return self.getTypedRuleContext(Swift3Parser.AttributesContext,0)


        def access_level_modifier(self):
            return self.getTypedRuleContext(Swift3Parser.Access_level_modifierContext,0)


        def raw_value_style_enum(self):
            return self.getTypedRuleContext(Swift3Parser.Raw_value_style_enumContext,0)


        def getRuleIndex(self):
            return Swift3Parser.RULE_enum_declaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEnum_declaration" ):
                listener.enterEnum_declaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEnum_declaration" ):
                listener.exitEnum_declaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEnum_declaration" ):
                return visitor.visitEnum_declaration(self)
            else:
                return visitor.visitChildren(self)




    def enum_declaration(self):

        localctx = Swift3Parser.Enum_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 222, self.RULE_enum_declaration)
        self._la = 0 # Token type
        try:
            self.state = 1386
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,125,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 1373
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==Swift3Parser.AT:
                    self.state = 1372
                    self.attributes()


                self.state = 1376
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if ((((_la - 76)) & ~0x3f) == 0 and ((1 << (_la - 76)) & ((1 << (Swift3Parser.T__75 - 76)) | (1 << (Swift3Parser.T__76 - 76)) | (1 << (Swift3Parser.T__77 - 76)) | (1 << (Swift3Parser.T__78 - 76)) | (1 << (Swift3Parser.T__79 - 76)))) != 0):
                    self.state = 1375
                    self.access_level_modifier()


                self.state = 1378
                self.union_style_enum()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 1380
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==Swift3Parser.AT:
                    self.state = 1379
                    self.attributes()


                self.state = 1383
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if ((((_la - 76)) & ~0x3f) == 0 and ((1 << (_la - 76)) & ((1 << (Swift3Parser.T__75 - 76)) | (1 << (Swift3Parser.T__76 - 76)) | (1 << (Swift3Parser.T__77 - 76)) | (1 << (Swift3Parser.T__78 - 76)) | (1 << (Swift3Parser.T__79 - 76)))) != 0):
                    self.state = 1382
                    self.access_level_modifier()


                self.state = 1385
                self.raw_value_style_enum()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Union_style_enumContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def enum_name(self):
            return self.getTypedRuleContext(Swift3Parser.Enum_nameContext,0)


        def generic_parameter_clause(self):
            return self.getTypedRuleContext(Swift3Parser.Generic_parameter_clauseContext,0)


        def type_inheritance_clause(self):
            return self.getTypedRuleContext(Swift3Parser.Type_inheritance_clauseContext,0)


        def generic_where_clause(self):
            return self.getTypedRuleContext(Swift3Parser.Generic_where_clauseContext,0)


        def union_style_enum_members(self):
            return self.getTypedRuleContext(Swift3Parser.Union_style_enum_membersContext,0)


        def getRuleIndex(self):
            return Swift3Parser.RULE_union_style_enum

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnion_style_enum" ):
                listener.enterUnion_style_enum(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnion_style_enum" ):
                listener.exitUnion_style_enum(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnion_style_enum" ):
                return visitor.visitUnion_style_enum(self)
            else:
                return visitor.visitChildren(self)




    def union_style_enum(self):

        localctx = Swift3Parser.Union_style_enumContext(self, self._ctx, self.state)
        self.enterRule(localctx, 224, self.RULE_union_style_enum)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1389
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==Swift3Parser.T__45:
                self.state = 1388
                self.match(Swift3Parser.T__45)


            self.state = 1391
            self.match(Swift3Parser.T__36)
            self.state = 1392
            self.enum_name()
            self.state = 1394
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==Swift3Parser.LT:
                self.state = 1393
                self.generic_parameter_clause()


            self.state = 1397
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==Swift3Parser.COLON:
                self.state = 1396
                self.type_inheritance_clause()


            self.state = 1400
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==Swift3Parser.T__12:
                self.state = 1399
                self.generic_where_clause()


            self.state = 1402
            self.match(Swift3Parser.LCURLY)
            self.state = 1404
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << Swift3Parser.T__1) | (1 << Swift3Parser.T__4) | (1 << Swift3Parser.T__5) | (1 << Swift3Parser.T__21) | (1 << Swift3Parser.T__28) | (1 << Swift3Parser.T__32) | (1 << Swift3Parser.T__33) | (1 << Swift3Parser.T__34) | (1 << Swift3Parser.T__35) | (1 << Swift3Parser.T__36) | (1 << Swift3Parser.T__37) | (1 << Swift3Parser.T__38) | (1 << Swift3Parser.T__45) | (1 << Swift3Parser.T__46) | (1 << Swift3Parser.T__48) | (1 << Swift3Parser.T__49) | (1 << Swift3Parser.T__50) | (1 << Swift3Parser.T__51) | (1 << Swift3Parser.T__52) | (1 << Swift3Parser.T__54) | (1 << Swift3Parser.T__55) | (1 << Swift3Parser.T__56))) != 0) or ((((_la - 65)) & ~0x3f) == 0 and ((1 << (_la - 65)) & ((1 << (Swift3Parser.T__64 - 65)) | (1 << (Swift3Parser.T__65 - 65)) | (1 << (Swift3Parser.T__66 - 65)) | (1 << (Swift3Parser.T__67 - 65)) | (1 << (Swift3Parser.T__68 - 65)) | (1 << (Swift3Parser.T__69 - 65)) | (1 << (Swift3Parser.T__70 - 65)) | (1 << (Swift3Parser.T__71 - 65)) | (1 << (Swift3Parser.T__74 - 65)) | (1 << (Swift3Parser.T__75 - 65)) | (1 << (Swift3Parser.T__76 - 65)) | (1 << (Swift3Parser.T__77 - 65)) | (1 << (Swift3Parser.T__78 - 65)) | (1 << (Swift3Parser.T__79 - 65)) | (1 << (Swift3Parser.T__80 - 65)) | (1 << (Swift3Parser.T__81 - 65)))) != 0) or _la==Swift3Parser.AT:
                self.state = 1403
                self.union_style_enum_members()


            self.state = 1406
            self.match(Swift3Parser.RCURLY)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Union_style_enum_membersContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def union_style_enum_member(self):
            return self.getTypedRuleContext(Swift3Parser.Union_style_enum_memberContext,0)


        def union_style_enum_members(self):
            return self.getTypedRuleContext(Swift3Parser.Union_style_enum_membersContext,0)


        def getRuleIndex(self):
            return Swift3Parser.RULE_union_style_enum_members

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnion_style_enum_members" ):
                listener.enterUnion_style_enum_members(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnion_style_enum_members" ):
                listener.exitUnion_style_enum_members(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnion_style_enum_members" ):
                return visitor.visitUnion_style_enum_members(self)
            else:
                return visitor.visitChildren(self)




    def union_style_enum_members(self):

        localctx = Swift3Parser.Union_style_enum_membersContext(self, self._ctx, self.state)
        self.enterRule(localctx, 226, self.RULE_union_style_enum_members)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1408
            self.union_style_enum_member()
            self.state = 1410
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << Swift3Parser.T__1) | (1 << Swift3Parser.T__4) | (1 << Swift3Parser.T__5) | (1 << Swift3Parser.T__21) | (1 << Swift3Parser.T__28) | (1 << Swift3Parser.T__32) | (1 << Swift3Parser.T__33) | (1 << Swift3Parser.T__34) | (1 << Swift3Parser.T__35) | (1 << Swift3Parser.T__36) | (1 << Swift3Parser.T__37) | (1 << Swift3Parser.T__38) | (1 << Swift3Parser.T__45) | (1 << Swift3Parser.T__46) | (1 << Swift3Parser.T__48) | (1 << Swift3Parser.T__49) | (1 << Swift3Parser.T__50) | (1 << Swift3Parser.T__51) | (1 << Swift3Parser.T__52) | (1 << Swift3Parser.T__54) | (1 << Swift3Parser.T__55) | (1 << Swift3Parser.T__56))) != 0) or ((((_la - 65)) & ~0x3f) == 0 and ((1 << (_la - 65)) & ((1 << (Swift3Parser.T__64 - 65)) | (1 << (Swift3Parser.T__65 - 65)) | (1 << (Swift3Parser.T__66 - 65)) | (1 << (Swift3Parser.T__67 - 65)) | (1 << (Swift3Parser.T__68 - 65)) | (1 << (Swift3Parser.T__69 - 65)) | (1 << (Swift3Parser.T__70 - 65)) | (1 << (Swift3Parser.T__71 - 65)) | (1 << (Swift3Parser.T__74 - 65)) | (1 << (Swift3Parser.T__75 - 65)) | (1 << (Swift3Parser.T__76 - 65)) | (1 << (Swift3Parser.T__77 - 65)) | (1 << (Swift3Parser.T__78 - 65)) | (1 << (Swift3Parser.T__79 - 65)) | (1 << (Swift3Parser.T__80 - 65)) | (1 << (Swift3Parser.T__81 - 65)))) != 0) or _la==Swift3Parser.AT:
                self.state = 1409
                self.union_style_enum_members()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Union_style_enum_memberContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declaration(self):
            return self.getTypedRuleContext(Swift3Parser.DeclarationContext,0)


        def union_style_enum_case_clause(self):
            return self.getTypedRuleContext(Swift3Parser.Union_style_enum_case_clauseContext,0)


        def compiler_control_statement(self):
            return self.getTypedRuleContext(Swift3Parser.Compiler_control_statementContext,0)


        def getRuleIndex(self):
            return Swift3Parser.RULE_union_style_enum_member

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnion_style_enum_member" ):
                listener.enterUnion_style_enum_member(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnion_style_enum_member" ):
                listener.exitUnion_style_enum_member(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnion_style_enum_member" ):
                return visitor.visitUnion_style_enum_member(self)
            else:
                return visitor.visitChildren(self)




    def union_style_enum_member(self):

        localctx = Swift3Parser.Union_style_enum_memberContext(self, self._ctx, self.state)
        self.enterRule(localctx, 228, self.RULE_union_style_enum_member)
        try:
            self.state = 1415
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,132,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 1412
                self.declaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 1413
                self.union_style_enum_case_clause()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 1414
                self.compiler_control_statement()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Union_style_enum_case_clauseContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def union_style_enum_case_list(self):
            return self.getTypedRuleContext(Swift3Parser.Union_style_enum_case_listContext,0)


        def attributes(self):
            return self.getTypedRuleContext(Swift3Parser.AttributesContext,0)


        def getRuleIndex(self):
            return Swift3Parser.RULE_union_style_enum_case_clause

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnion_style_enum_case_clause" ):
                listener.enterUnion_style_enum_case_clause(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnion_style_enum_case_clause" ):
                listener.exitUnion_style_enum_case_clause(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnion_style_enum_case_clause" ):
                return visitor.visitUnion_style_enum_case_clause(self)
            else:
                return visitor.visitChildren(self)




    def union_style_enum_case_clause(self):

        localctx = Swift3Parser.Union_style_enum_case_clauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 230, self.RULE_union_style_enum_case_clause)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1418
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==Swift3Parser.AT:
                self.state = 1417
                self.attributes()


            self.state = 1421
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==Swift3Parser.T__45:
                self.state = 1420
                self.match(Swift3Parser.T__45)


            self.state = 1423
            self.match(Swift3Parser.T__1)
            self.state = 1424
            self.union_style_enum_case_list()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Union_style_enum_case_listContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def union_style_enum_case(self):
            return self.getTypedRuleContext(Swift3Parser.Union_style_enum_caseContext,0)


        def union_style_enum_case_list(self):
            return self.getTypedRuleContext(Swift3Parser.Union_style_enum_case_listContext,0)


        def getRuleIndex(self):
            return Swift3Parser.RULE_union_style_enum_case_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnion_style_enum_case_list" ):
                listener.enterUnion_style_enum_case_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnion_style_enum_case_list" ):
                listener.exitUnion_style_enum_case_list(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnion_style_enum_case_list" ):
                return visitor.visitUnion_style_enum_case_list(self)
            else:
                return visitor.visitChildren(self)




    def union_style_enum_case_list(self):

        localctx = Swift3Parser.Union_style_enum_case_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 232, self.RULE_union_style_enum_case_list)
        try:
            self.state = 1431
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,135,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 1426
                self.union_style_enum_case()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 1427
                self.union_style_enum_case()
                self.state = 1428
                self.match(Swift3Parser.COMMA)
                self.state = 1429
                self.union_style_enum_case_list()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Union_style_enum_caseContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def enum_case_name(self):
            return self.getTypedRuleContext(Swift3Parser.Enum_case_nameContext,0)


        def tuple_type(self):
            return self.getTypedRuleContext(Swift3Parser.Tuple_typeContext,0)


        def getRuleIndex(self):
            return Swift3Parser.RULE_union_style_enum_case

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnion_style_enum_case" ):
                listener.enterUnion_style_enum_case(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnion_style_enum_case" ):
                listener.exitUnion_style_enum_case(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnion_style_enum_case" ):
                return visitor.visitUnion_style_enum_case(self)
            else:
                return visitor.visitChildren(self)




    def union_style_enum_case(self):

        localctx = Swift3Parser.Union_style_enum_caseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 234, self.RULE_union_style_enum_case)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1433
            self.enum_case_name()
            self.state = 1435
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==Swift3Parser.LPAREN:
                self.state = 1434
                self.tuple_type()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Enum_nameContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declaration_identifier(self):
            return self.getTypedRuleContext(Swift3Parser.Declaration_identifierContext,0)


        def getRuleIndex(self):
            return Swift3Parser.RULE_enum_name

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEnum_name" ):
                listener.enterEnum_name(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEnum_name" ):
                listener.exitEnum_name(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEnum_name" ):
                return visitor.visitEnum_name(self)
            else:
                return visitor.visitChildren(self)




    def enum_name(self):

        localctx = Swift3Parser.Enum_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 236, self.RULE_enum_name)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1437
            self.declaration_identifier()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Enum_case_nameContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declaration_identifier(self):
            return self.getTypedRuleContext(Swift3Parser.Declaration_identifierContext,0)


        def getRuleIndex(self):
            return Swift3Parser.RULE_enum_case_name

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEnum_case_name" ):
                listener.enterEnum_case_name(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEnum_case_name" ):
                listener.exitEnum_case_name(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEnum_case_name" ):
                return visitor.visitEnum_case_name(self)
            else:
                return visitor.visitChildren(self)




    def enum_case_name(self):

        localctx = Swift3Parser.Enum_case_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 238, self.RULE_enum_case_name)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1439
            self.declaration_identifier()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Raw_value_style_enumContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def enum_name(self):
            return self.getTypedRuleContext(Swift3Parser.Enum_nameContext,0)


        def type_inheritance_clause(self):
            return self.getTypedRuleContext(Swift3Parser.Type_inheritance_clauseContext,0)


        def raw_value_style_enum_members(self):
            return self.getTypedRuleContext(Swift3Parser.Raw_value_style_enum_membersContext,0)


        def generic_parameter_clause(self):
            return self.getTypedRuleContext(Swift3Parser.Generic_parameter_clauseContext,0)


        def generic_where_clause(self):
            return self.getTypedRuleContext(Swift3Parser.Generic_where_clauseContext,0)


        def getRuleIndex(self):
            return Swift3Parser.RULE_raw_value_style_enum

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRaw_value_style_enum" ):
                listener.enterRaw_value_style_enum(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRaw_value_style_enum" ):
                listener.exitRaw_value_style_enum(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRaw_value_style_enum" ):
                return visitor.visitRaw_value_style_enum(self)
            else:
                return visitor.visitChildren(self)




    def raw_value_style_enum(self):

        localctx = Swift3Parser.Raw_value_style_enumContext(self, self._ctx, self.state)
        self.enterRule(localctx, 240, self.RULE_raw_value_style_enum)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1441
            self.match(Swift3Parser.T__36)
            self.state = 1442
            self.enum_name()
            self.state = 1444
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==Swift3Parser.LT:
                self.state = 1443
                self.generic_parameter_clause()


            self.state = 1446
            self.type_inheritance_clause()
            self.state = 1448
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==Swift3Parser.T__12:
                self.state = 1447
                self.generic_where_clause()


            self.state = 1450
            self.match(Swift3Parser.LCURLY)
            self.state = 1451
            self.raw_value_style_enum_members()
            self.state = 1452
            self.match(Swift3Parser.RCURLY)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Raw_value_style_enum_membersContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def raw_value_style_enum_member(self):
            return self.getTypedRuleContext(Swift3Parser.Raw_value_style_enum_memberContext,0)


        def raw_value_style_enum_members(self):
            return self.getTypedRuleContext(Swift3Parser.Raw_value_style_enum_membersContext,0)


        def getRuleIndex(self):
            return Swift3Parser.RULE_raw_value_style_enum_members

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRaw_value_style_enum_members" ):
                listener.enterRaw_value_style_enum_members(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRaw_value_style_enum_members" ):
                listener.exitRaw_value_style_enum_members(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRaw_value_style_enum_members" ):
                return visitor.visitRaw_value_style_enum_members(self)
            else:
                return visitor.visitChildren(self)




    def raw_value_style_enum_members(self):

        localctx = Swift3Parser.Raw_value_style_enum_membersContext(self, self._ctx, self.state)
        self.enterRule(localctx, 242, self.RULE_raw_value_style_enum_members)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1454
            self.raw_value_style_enum_member()
            self.state = 1456
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << Swift3Parser.T__1) | (1 << Swift3Parser.T__4) | (1 << Swift3Parser.T__5) | (1 << Swift3Parser.T__21) | (1 << Swift3Parser.T__28) | (1 << Swift3Parser.T__32) | (1 << Swift3Parser.T__33) | (1 << Swift3Parser.T__34) | (1 << Swift3Parser.T__35) | (1 << Swift3Parser.T__36) | (1 << Swift3Parser.T__37) | (1 << Swift3Parser.T__38) | (1 << Swift3Parser.T__45) | (1 << Swift3Parser.T__46) | (1 << Swift3Parser.T__48) | (1 << Swift3Parser.T__49) | (1 << Swift3Parser.T__50) | (1 << Swift3Parser.T__51) | (1 << Swift3Parser.T__52) | (1 << Swift3Parser.T__54) | (1 << Swift3Parser.T__55) | (1 << Swift3Parser.T__56))) != 0) or ((((_la - 65)) & ~0x3f) == 0 and ((1 << (_la - 65)) & ((1 << (Swift3Parser.T__64 - 65)) | (1 << (Swift3Parser.T__65 - 65)) | (1 << (Swift3Parser.T__66 - 65)) | (1 << (Swift3Parser.T__67 - 65)) | (1 << (Swift3Parser.T__68 - 65)) | (1 << (Swift3Parser.T__69 - 65)) | (1 << (Swift3Parser.T__70 - 65)) | (1 << (Swift3Parser.T__71 - 65)) | (1 << (Swift3Parser.T__74 - 65)) | (1 << (Swift3Parser.T__75 - 65)) | (1 << (Swift3Parser.T__76 - 65)) | (1 << (Swift3Parser.T__77 - 65)) | (1 << (Swift3Parser.T__78 - 65)) | (1 << (Swift3Parser.T__79 - 65)) | (1 << (Swift3Parser.T__80 - 65)) | (1 << (Swift3Parser.T__81 - 65)))) != 0) or _la==Swift3Parser.AT:
                self.state = 1455
                self.raw_value_style_enum_members()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Raw_value_style_enum_memberContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declaration(self):
            return self.getTypedRuleContext(Swift3Parser.DeclarationContext,0)


        def raw_value_style_enum_case_clause(self):
            return self.getTypedRuleContext(Swift3Parser.Raw_value_style_enum_case_clauseContext,0)


        def compiler_control_statement(self):
            return self.getTypedRuleContext(Swift3Parser.Compiler_control_statementContext,0)


        def getRuleIndex(self):
            return Swift3Parser.RULE_raw_value_style_enum_member

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRaw_value_style_enum_member" ):
                listener.enterRaw_value_style_enum_member(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRaw_value_style_enum_member" ):
                listener.exitRaw_value_style_enum_member(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRaw_value_style_enum_member" ):
                return visitor.visitRaw_value_style_enum_member(self)
            else:
                return visitor.visitChildren(self)




    def raw_value_style_enum_member(self):

        localctx = Swift3Parser.Raw_value_style_enum_memberContext(self, self._ctx, self.state)
        self.enterRule(localctx, 244, self.RULE_raw_value_style_enum_member)
        try:
            self.state = 1461
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,140,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 1458
                self.declaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 1459
                self.raw_value_style_enum_case_clause()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 1460
                self.compiler_control_statement()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Raw_value_style_enum_case_clauseContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def raw_value_style_enum_case_list(self):
            return self.getTypedRuleContext(Swift3Parser.Raw_value_style_enum_case_listContext,0)


        def attributes(self):
            return self.getTypedRuleContext(Swift3Parser.AttributesContext,0)


        def getRuleIndex(self):
            return Swift3Parser.RULE_raw_value_style_enum_case_clause

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRaw_value_style_enum_case_clause" ):
                listener.enterRaw_value_style_enum_case_clause(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRaw_value_style_enum_case_clause" ):
                listener.exitRaw_value_style_enum_case_clause(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRaw_value_style_enum_case_clause" ):
                return visitor.visitRaw_value_style_enum_case_clause(self)
            else:
                return visitor.visitChildren(self)




    def raw_value_style_enum_case_clause(self):

        localctx = Swift3Parser.Raw_value_style_enum_case_clauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 246, self.RULE_raw_value_style_enum_case_clause)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1464
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==Swift3Parser.AT:
                self.state = 1463
                self.attributes()


            self.state = 1466
            self.match(Swift3Parser.T__1)
            self.state = 1467
            self.raw_value_style_enum_case_list()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Raw_value_style_enum_case_listContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def raw_value_style_enum_case(self):
            return self.getTypedRuleContext(Swift3Parser.Raw_value_style_enum_caseContext,0)


        def raw_value_style_enum_case_list(self):
            return self.getTypedRuleContext(Swift3Parser.Raw_value_style_enum_case_listContext,0)


        def getRuleIndex(self):
            return Swift3Parser.RULE_raw_value_style_enum_case_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRaw_value_style_enum_case_list" ):
                listener.enterRaw_value_style_enum_case_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRaw_value_style_enum_case_list" ):
                listener.exitRaw_value_style_enum_case_list(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRaw_value_style_enum_case_list" ):
                return visitor.visitRaw_value_style_enum_case_list(self)
            else:
                return visitor.visitChildren(self)




    def raw_value_style_enum_case_list(self):

        localctx = Swift3Parser.Raw_value_style_enum_case_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 248, self.RULE_raw_value_style_enum_case_list)
        try:
            self.state = 1474
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,142,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 1469
                self.raw_value_style_enum_case()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 1470
                self.raw_value_style_enum_case()
                self.state = 1471
                self.match(Swift3Parser.COMMA)
                self.state = 1472
                self.raw_value_style_enum_case_list()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Raw_value_style_enum_caseContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def enum_case_name(self):
            return self.getTypedRuleContext(Swift3Parser.Enum_case_nameContext,0)


        def raw_value_assignment(self):
            return self.getTypedRuleContext(Swift3Parser.Raw_value_assignmentContext,0)


        def getRuleIndex(self):
            return Swift3Parser.RULE_raw_value_style_enum_case

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRaw_value_style_enum_case" ):
                listener.enterRaw_value_style_enum_case(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRaw_value_style_enum_case" ):
                listener.exitRaw_value_style_enum_case(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRaw_value_style_enum_case" ):
                return visitor.visitRaw_value_style_enum_case(self)
            else:
                return visitor.visitChildren(self)




    def raw_value_style_enum_case(self):

        localctx = Swift3Parser.Raw_value_style_enum_caseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 250, self.RULE_raw_value_style_enum_case)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1476
            self.enum_case_name()
            self.state = 1478
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,143,self._ctx)
            if la_ == 1:
                self.state = 1477
                self.raw_value_assignment()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Raw_value_assignmentContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assignment_operator(self):
            return self.getTypedRuleContext(Swift3Parser.Assignment_operatorContext,0)


        def raw_value_literal(self):
            return self.getTypedRuleContext(Swift3Parser.Raw_value_literalContext,0)


        def getRuleIndex(self):
            return Swift3Parser.RULE_raw_value_assignment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRaw_value_assignment" ):
                listener.enterRaw_value_assignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRaw_value_assignment" ):
                listener.exitRaw_value_assignment(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRaw_value_assignment" ):
                return visitor.visitRaw_value_assignment(self)
            else:
                return visitor.visitChildren(self)




    def raw_value_assignment(self):

        localctx = Swift3Parser.Raw_value_assignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 252, self.RULE_raw_value_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1480
            self.assignment_operator()
            self.state = 1481
            self.raw_value_literal()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Raw_value_literalContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def numeric_literal(self):
            return self.getTypedRuleContext(Swift3Parser.Numeric_literalContext,0)


        def Static_string_literal(self):
            return self.getToken(Swift3Parser.Static_string_literal, 0)

        def boolean_literal(self):
            return self.getTypedRuleContext(Swift3Parser.Boolean_literalContext,0)


        def getRuleIndex(self):
            return Swift3Parser.RULE_raw_value_literal

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRaw_value_literal" ):
                listener.enterRaw_value_literal(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRaw_value_literal" ):
                listener.exitRaw_value_literal(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRaw_value_literal" ):
                return visitor.visitRaw_value_literal(self)
            else:
                return visitor.visitChildren(self)




    def raw_value_literal(self):

        localctx = Swift3Parser.Raw_value_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 254, self.RULE_raw_value_literal)
        try:
            self.state = 1486
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,144,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 1483
                self.numeric_literal()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 1484
                self.match(Swift3Parser.Static_string_literal)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 1485
                self.boolean_literal()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Struct_declarationContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def struct_name(self):
            return self.getTypedRuleContext(Swift3Parser.Struct_nameContext,0)


        def struct_body(self):
            return self.getTypedRuleContext(Swift3Parser.Struct_bodyContext,0)


        def attributes(self):
            return self.getTypedRuleContext(Swift3Parser.AttributesContext,0)


        def access_level_modifier(self):
            return self.getTypedRuleContext(Swift3Parser.Access_level_modifierContext,0)


        def generic_parameter_clause(self):
            return self.getTypedRuleContext(Swift3Parser.Generic_parameter_clauseContext,0)


        def type_inheritance_clause(self):
            return self.getTypedRuleContext(Swift3Parser.Type_inheritance_clauseContext,0)


        def generic_where_clause(self):
            return self.getTypedRuleContext(Swift3Parser.Generic_where_clauseContext,0)


        def getRuleIndex(self):
            return Swift3Parser.RULE_struct_declaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStruct_declaration" ):
                listener.enterStruct_declaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStruct_declaration" ):
                listener.exitStruct_declaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStruct_declaration" ):
                return visitor.visitStruct_declaration(self)
            else:
                return visitor.visitChildren(self)




    def struct_declaration(self):

        localctx = Swift3Parser.Struct_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 256, self.RULE_struct_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1489
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==Swift3Parser.AT:
                self.state = 1488
                self.attributes()


            self.state = 1492
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((((_la - 76)) & ~0x3f) == 0 and ((1 << (_la - 76)) & ((1 << (Swift3Parser.T__75 - 76)) | (1 << (Swift3Parser.T__76 - 76)) | (1 << (Swift3Parser.T__77 - 76)) | (1 << (Swift3Parser.T__78 - 76)) | (1 << (Swift3Parser.T__79 - 76)))) != 0):
                self.state = 1491
                self.access_level_modifier()


            self.state = 1494
            self.match(Swift3Parser.T__34)
            self.state = 1495
            self.struct_name()
            self.state = 1497
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==Swift3Parser.LT:
                self.state = 1496
                self.generic_parameter_clause()


            self.state = 1500
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==Swift3Parser.COLON:
                self.state = 1499
                self.type_inheritance_clause()


            self.state = 1503
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==Swift3Parser.T__12:
                self.state = 1502
                self.generic_where_clause()


            self.state = 1505
            self.struct_body()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Struct_nameContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declaration_identifier(self):
            return self.getTypedRuleContext(Swift3Parser.Declaration_identifierContext,0)


        def getRuleIndex(self):
            return Swift3Parser.RULE_struct_name

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStruct_name" ):
                listener.enterStruct_name(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStruct_name" ):
                listener.exitStruct_name(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStruct_name" ):
                return visitor.visitStruct_name(self)
            else:
                return visitor.visitChildren(self)




    def struct_name(self):

        localctx = Swift3Parser.Struct_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 258, self.RULE_struct_name)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1507
            self.declaration_identifier()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Struct_bodyContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def struct_member(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Swift3Parser.Struct_memberContext)
            else:
                return self.getTypedRuleContext(Swift3Parser.Struct_memberContext,i)


        def getRuleIndex(self):
            return Swift3Parser.RULE_struct_body

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStruct_body" ):
                listener.enterStruct_body(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStruct_body" ):
                listener.exitStruct_body(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStruct_body" ):
                return visitor.visitStruct_body(self)
            else:
                return visitor.visitChildren(self)




    def struct_body(self):

        localctx = Swift3Parser.Struct_bodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 260, self.RULE_struct_body)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1509
            self.match(Swift3Parser.LCURLY)
            self.state = 1513
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << Swift3Parser.T__4) | (1 << Swift3Parser.T__5) | (1 << Swift3Parser.T__21) | (1 << Swift3Parser.T__28) | (1 << Swift3Parser.T__32) | (1 << Swift3Parser.T__33) | (1 << Swift3Parser.T__34) | (1 << Swift3Parser.T__35) | (1 << Swift3Parser.T__36) | (1 << Swift3Parser.T__37) | (1 << Swift3Parser.T__38) | (1 << Swift3Parser.T__45) | (1 << Swift3Parser.T__46) | (1 << Swift3Parser.T__48) | (1 << Swift3Parser.T__49) | (1 << Swift3Parser.T__50) | (1 << Swift3Parser.T__51) | (1 << Swift3Parser.T__52) | (1 << Swift3Parser.T__54) | (1 << Swift3Parser.T__55) | (1 << Swift3Parser.T__56))) != 0) or ((((_la - 65)) & ~0x3f) == 0 and ((1 << (_la - 65)) & ((1 << (Swift3Parser.T__64 - 65)) | (1 << (Swift3Parser.T__65 - 65)) | (1 << (Swift3Parser.T__66 - 65)) | (1 << (Swift3Parser.T__67 - 65)) | (1 << (Swift3Parser.T__68 - 65)) | (1 << (Swift3Parser.T__69 - 65)) | (1 << (Swift3Parser.T__70 - 65)) | (1 << (Swift3Parser.T__71 - 65)) | (1 << (Swift3Parser.T__74 - 65)) | (1 << (Swift3Parser.T__75 - 65)) | (1 << (Swift3Parser.T__76 - 65)) | (1 << (Swift3Parser.T__77 - 65)) | (1 << (Swift3Parser.T__78 - 65)) | (1 << (Swift3Parser.T__79 - 65)) | (1 << (Swift3Parser.T__80 - 65)) | (1 << (Swift3Parser.T__81 - 65)))) != 0) or _la==Swift3Parser.AT:
                self.state = 1510
                self.struct_member()
                self.state = 1515
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 1516
            self.match(Swift3Parser.RCURLY)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Struct_memberContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declaration(self):
            return self.getTypedRuleContext(Swift3Parser.DeclarationContext,0)


        def compiler_control_statement(self):
            return self.getTypedRuleContext(Swift3Parser.Compiler_control_statementContext,0)


        def getRuleIndex(self):
            return Swift3Parser.RULE_struct_member

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStruct_member" ):
                listener.enterStruct_member(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStruct_member" ):
                listener.exitStruct_member(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStruct_member" ):
                return visitor.visitStruct_member(self)
            else:
                return visitor.visitChildren(self)




    def struct_member(self):

        localctx = Swift3Parser.Struct_memberContext(self, self._ctx, self.state)
        self.enterRule(localctx, 262, self.RULE_struct_member)
        try:
            self.state = 1520
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [Swift3Parser.T__4, Swift3Parser.T__5, Swift3Parser.T__32, Swift3Parser.T__33, Swift3Parser.T__34, Swift3Parser.T__35, Swift3Parser.T__36, Swift3Parser.T__37, Swift3Parser.T__38, Swift3Parser.T__45, Swift3Parser.T__46, Swift3Parser.T__48, Swift3Parser.T__49, Swift3Parser.T__50, Swift3Parser.T__51, Swift3Parser.T__52, Swift3Parser.T__54, Swift3Parser.T__55, Swift3Parser.T__56, Swift3Parser.T__64, Swift3Parser.T__65, Swift3Parser.T__66, Swift3Parser.T__67, Swift3Parser.T__68, Swift3Parser.T__69, Swift3Parser.T__70, Swift3Parser.T__71, Swift3Parser.T__74, Swift3Parser.T__75, Swift3Parser.T__76, Swift3Parser.T__77, Swift3Parser.T__78, Swift3Parser.T__79, Swift3Parser.T__80, Swift3Parser.T__81, Swift3Parser.AT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 1518
                self.declaration()
                pass
            elif token in [Swift3Parser.T__21, Swift3Parser.T__28]:
                self.enterOuterAlt(localctx, 2)
                self.state = 1519
                self.compiler_control_statement()
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

    class Class_declarationContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def class_name(self):
            return self.getTypedRuleContext(Swift3Parser.Class_nameContext,0)


        def class_body(self):
            return self.getTypedRuleContext(Swift3Parser.Class_bodyContext,0)


        def attributes(self):
            return self.getTypedRuleContext(Swift3Parser.AttributesContext,0)


        def access_level_modifier(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Swift3Parser.Access_level_modifierContext)
            else:
                return self.getTypedRuleContext(Swift3Parser.Access_level_modifierContext,i)


        def generic_parameter_clause(self):
            return self.getTypedRuleContext(Swift3Parser.Generic_parameter_clauseContext,0)


        def type_inheritance_clause(self):
            return self.getTypedRuleContext(Swift3Parser.Type_inheritance_clauseContext,0)


        def generic_where_clause(self):
            return self.getTypedRuleContext(Swift3Parser.Generic_where_clauseContext,0)


        def getRuleIndex(self):
            return Swift3Parser.RULE_class_declaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterClass_declaration" ):
                listener.enterClass_declaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitClass_declaration" ):
                listener.exitClass_declaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClass_declaration" ):
                return visitor.visitClass_declaration(self)
            else:
                return visitor.visitChildren(self)




    def class_declaration(self):

        localctx = Swift3Parser.Class_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 264, self.RULE_class_declaration)
        self._la = 0 # Token type
        try:
            self.state = 1567
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,164,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 1523
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==Swift3Parser.AT:
                    self.state = 1522
                    self.attributes()


                self.state = 1526
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if ((((_la - 76)) & ~0x3f) == 0 and ((1 << (_la - 76)) & ((1 << (Swift3Parser.T__75 - 76)) | (1 << (Swift3Parser.T__76 - 76)) | (1 << (Swift3Parser.T__77 - 76)) | (1 << (Swift3Parser.T__78 - 76)) | (1 << (Swift3Parser.T__79 - 76)))) != 0):
                    self.state = 1525
                    self.access_level_modifier()


                self.state = 1529
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==Swift3Parser.T__46:
                    self.state = 1528
                    self.match(Swift3Parser.T__46)


                self.state = 1531
                self.match(Swift3Parser.T__35)
                self.state = 1532
                self.class_name()
                self.state = 1534
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==Swift3Parser.LT:
                    self.state = 1533
                    self.generic_parameter_clause()


                self.state = 1537
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==Swift3Parser.COLON:
                    self.state = 1536
                    self.type_inheritance_clause()


                self.state = 1540
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==Swift3Parser.T__12:
                    self.state = 1539
                    self.generic_where_clause()


                self.state = 1542
                self.class_body()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 1545
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==Swift3Parser.AT:
                    self.state = 1544
                    self.attributes()


                self.state = 1548
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if ((((_la - 76)) & ~0x3f) == 0 and ((1 << (_la - 76)) & ((1 << (Swift3Parser.T__75 - 76)) | (1 << (Swift3Parser.T__76 - 76)) | (1 << (Swift3Parser.T__77 - 76)) | (1 << (Swift3Parser.T__78 - 76)) | (1 << (Swift3Parser.T__79 - 76)))) != 0):
                    self.state = 1547
                    self.access_level_modifier()


                self.state = 1550
                self.match(Swift3Parser.T__46)
                self.state = 1552
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if ((((_la - 76)) & ~0x3f) == 0 and ((1 << (_la - 76)) & ((1 << (Swift3Parser.T__75 - 76)) | (1 << (Swift3Parser.T__76 - 76)) | (1 << (Swift3Parser.T__77 - 76)) | (1 << (Swift3Parser.T__78 - 76)) | (1 << (Swift3Parser.T__79 - 76)))) != 0):
                    self.state = 1551
                    self.access_level_modifier()


                self.state = 1554
                self.match(Swift3Parser.T__35)
                self.state = 1555
                self.class_name()
                self.state = 1557
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==Swift3Parser.LT:
                    self.state = 1556
                    self.generic_parameter_clause()


                self.state = 1560
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==Swift3Parser.COLON:
                    self.state = 1559
                    self.type_inheritance_clause()


                self.state = 1563
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==Swift3Parser.T__12:
                    self.state = 1562
                    self.generic_where_clause()


                self.state = 1565
                self.class_body()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Class_nameContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declaration_identifier(self):
            return self.getTypedRuleContext(Swift3Parser.Declaration_identifierContext,0)


        def getRuleIndex(self):
            return Swift3Parser.RULE_class_name

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterClass_name" ):
                listener.enterClass_name(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitClass_name" ):
                listener.exitClass_name(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClass_name" ):
                return visitor.visitClass_name(self)
            else:
                return visitor.visitChildren(self)




    def class_name(self):

        localctx = Swift3Parser.Class_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 266, self.RULE_class_name)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1569
            self.declaration_identifier()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Class_bodyContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def class_member(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Swift3Parser.Class_memberContext)
            else:
                return self.getTypedRuleContext(Swift3Parser.Class_memberContext,i)


        def getRuleIndex(self):
            return Swift3Parser.RULE_class_body

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterClass_body" ):
                listener.enterClass_body(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitClass_body" ):
                listener.exitClass_body(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClass_body" ):
                return visitor.visitClass_body(self)
            else:
                return visitor.visitChildren(self)




    def class_body(self):

        localctx = Swift3Parser.Class_bodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 268, self.RULE_class_body)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1571
            self.match(Swift3Parser.LCURLY)
            self.state = 1575
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << Swift3Parser.T__4) | (1 << Swift3Parser.T__5) | (1 << Swift3Parser.T__21) | (1 << Swift3Parser.T__28) | (1 << Swift3Parser.T__32) | (1 << Swift3Parser.T__33) | (1 << Swift3Parser.T__34) | (1 << Swift3Parser.T__35) | (1 << Swift3Parser.T__36) | (1 << Swift3Parser.T__37) | (1 << Swift3Parser.T__38) | (1 << Swift3Parser.T__45) | (1 << Swift3Parser.T__46) | (1 << Swift3Parser.T__48) | (1 << Swift3Parser.T__49) | (1 << Swift3Parser.T__50) | (1 << Swift3Parser.T__51) | (1 << Swift3Parser.T__52) | (1 << Swift3Parser.T__54) | (1 << Swift3Parser.T__55) | (1 << Swift3Parser.T__56))) != 0) or ((((_la - 65)) & ~0x3f) == 0 and ((1 << (_la - 65)) & ((1 << (Swift3Parser.T__64 - 65)) | (1 << (Swift3Parser.T__65 - 65)) | (1 << (Swift3Parser.T__66 - 65)) | (1 << (Swift3Parser.T__67 - 65)) | (1 << (Swift3Parser.T__68 - 65)) | (1 << (Swift3Parser.T__69 - 65)) | (1 << (Swift3Parser.T__70 - 65)) | (1 << (Swift3Parser.T__71 - 65)) | (1 << (Swift3Parser.T__74 - 65)) | (1 << (Swift3Parser.T__75 - 65)) | (1 << (Swift3Parser.T__76 - 65)) | (1 << (Swift3Parser.T__77 - 65)) | (1 << (Swift3Parser.T__78 - 65)) | (1 << (Swift3Parser.T__79 - 65)) | (1 << (Swift3Parser.T__80 - 65)) | (1 << (Swift3Parser.T__81 - 65)))) != 0) or _la==Swift3Parser.AT:
                self.state = 1572
                self.class_member()
                self.state = 1577
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 1578
            self.match(Swift3Parser.RCURLY)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Class_memberContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declaration(self):
            return self.getTypedRuleContext(Swift3Parser.DeclarationContext,0)


        def compiler_control_statement(self):
            return self.getTypedRuleContext(Swift3Parser.Compiler_control_statementContext,0)


        def getRuleIndex(self):
            return Swift3Parser.RULE_class_member

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterClass_member" ):
                listener.enterClass_member(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitClass_member" ):
                listener.exitClass_member(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClass_member" ):
                return visitor.visitClass_member(self)
            else:
                return visitor.visitChildren(self)




    def class_member(self):

        localctx = Swift3Parser.Class_memberContext(self, self._ctx, self.state)
        self.enterRule(localctx, 270, self.RULE_class_member)
        try:
            self.state = 1582
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [Swift3Parser.T__4, Swift3Parser.T__5, Swift3Parser.T__32, Swift3Parser.T__33, Swift3Parser.T__34, Swift3Parser.T__35, Swift3Parser.T__36, Swift3Parser.T__37, Swift3Parser.T__38, Swift3Parser.T__45, Swift3Parser.T__46, Swift3Parser.T__48, Swift3Parser.T__49, Swift3Parser.T__50, Swift3Parser.T__51, Swift3Parser.T__52, Swift3Parser.T__54, Swift3Parser.T__55, Swift3Parser.T__56, Swift3Parser.T__64, Swift3Parser.T__65, Swift3Parser.T__66, Swift3Parser.T__67, Swift3Parser.T__68, Swift3Parser.T__69, Swift3Parser.T__70, Swift3Parser.T__71, Swift3Parser.T__74, Swift3Parser.T__75, Swift3Parser.T__76, Swift3Parser.T__77, Swift3Parser.T__78, Swift3Parser.T__79, Swift3Parser.T__80, Swift3Parser.T__81, Swift3Parser.AT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 1580
                self.declaration()
                pass
            elif token in [Swift3Parser.T__21, Swift3Parser.T__28]:
                self.enterOuterAlt(localctx, 2)
                self.state = 1581
                self.compiler_control_statement()
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

    class Protocol_declarationContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def protocol_name(self):
            return self.getTypedRuleContext(Swift3Parser.Protocol_nameContext,0)


        def protocol_body(self):
            return self.getTypedRuleContext(Swift3Parser.Protocol_bodyContext,0)


        def attributes(self):
            return self.getTypedRuleContext(Swift3Parser.AttributesContext,0)


        def access_level_modifier(self):
            return self.getTypedRuleContext(Swift3Parser.Access_level_modifierContext,0)


        def type_inheritance_clause(self):
            return self.getTypedRuleContext(Swift3Parser.Type_inheritance_clauseContext,0)


        def getRuleIndex(self):
            return Swift3Parser.RULE_protocol_declaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProtocol_declaration" ):
                listener.enterProtocol_declaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProtocol_declaration" ):
                listener.exitProtocol_declaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProtocol_declaration" ):
                return visitor.visitProtocol_declaration(self)
            else:
                return visitor.visitChildren(self)




    def protocol_declaration(self):

        localctx = Swift3Parser.Protocol_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 272, self.RULE_protocol_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1585
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==Swift3Parser.AT:
                self.state = 1584
                self.attributes()


            self.state = 1588
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((((_la - 76)) & ~0x3f) == 0 and ((1 << (_la - 76)) & ((1 << (Swift3Parser.T__75 - 76)) | (1 << (Swift3Parser.T__76 - 76)) | (1 << (Swift3Parser.T__77 - 76)) | (1 << (Swift3Parser.T__78 - 76)) | (1 << (Swift3Parser.T__79 - 76)))) != 0):
                self.state = 1587
                self.access_level_modifier()


            self.state = 1590
            self.match(Swift3Parser.T__37)
            self.state = 1591
            self.protocol_name()
            self.state = 1593
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==Swift3Parser.COLON:
                self.state = 1592
                self.type_inheritance_clause()


            self.state = 1595
            self.protocol_body()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Protocol_nameContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declaration_identifier(self):
            return self.getTypedRuleContext(Swift3Parser.Declaration_identifierContext,0)


        def getRuleIndex(self):
            return Swift3Parser.RULE_protocol_name

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProtocol_name" ):
                listener.enterProtocol_name(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProtocol_name" ):
                listener.exitProtocol_name(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProtocol_name" ):
                return visitor.visitProtocol_name(self)
            else:
                return visitor.visitChildren(self)




    def protocol_name(self):

        localctx = Swift3Parser.Protocol_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 274, self.RULE_protocol_name)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1597
            self.declaration_identifier()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Protocol_bodyContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def protocol_member(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Swift3Parser.Protocol_memberContext)
            else:
                return self.getTypedRuleContext(Swift3Parser.Protocol_memberContext,i)


        def getRuleIndex(self):
            return Swift3Parser.RULE_protocol_body

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProtocol_body" ):
                listener.enterProtocol_body(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProtocol_body" ):
                listener.exitProtocol_body(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProtocol_body" ):
                return visitor.visitProtocol_body(self)
            else:
                return visitor.visitChildren(self)




    def protocol_body(self):

        localctx = Swift3Parser.Protocol_bodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 276, self.RULE_protocol_body)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1599
            self.match(Swift3Parser.LCURLY)
            self.state = 1603
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << Swift3Parser.T__5) | (1 << Swift3Parser.T__21) | (1 << Swift3Parser.T__28) | (1 << Swift3Parser.T__33) | (1 << Swift3Parser.T__35) | (1 << Swift3Parser.T__38) | (1 << Swift3Parser.T__46) | (1 << Swift3Parser.T__47) | (1 << Swift3Parser.T__48) | (1 << Swift3Parser.T__51) | (1 << Swift3Parser.T__52) | (1 << Swift3Parser.T__54) | (1 << Swift3Parser.T__55))) != 0) or ((((_la - 65)) & ~0x3f) == 0 and ((1 << (_la - 65)) & ((1 << (Swift3Parser.T__64 - 65)) | (1 << (Swift3Parser.T__65 - 65)) | (1 << (Swift3Parser.T__66 - 65)) | (1 << (Swift3Parser.T__67 - 65)) | (1 << (Swift3Parser.T__68 - 65)) | (1 << (Swift3Parser.T__69 - 65)) | (1 << (Swift3Parser.T__70 - 65)) | (1 << (Swift3Parser.T__71 - 65)) | (1 << (Swift3Parser.T__74 - 65)) | (1 << (Swift3Parser.T__75 - 65)) | (1 << (Swift3Parser.T__76 - 65)) | (1 << (Swift3Parser.T__77 - 65)) | (1 << (Swift3Parser.T__78 - 65)) | (1 << (Swift3Parser.T__79 - 65)) | (1 << (Swift3Parser.T__80 - 65)) | (1 << (Swift3Parser.T__81 - 65)))) != 0) or _la==Swift3Parser.AT:
                self.state = 1600
                self.protocol_member()
                self.state = 1605
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 1606
            self.match(Swift3Parser.RCURLY)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Protocol_memberContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def protocol_member_declaration(self):
            return self.getTypedRuleContext(Swift3Parser.Protocol_member_declarationContext,0)


        def compiler_control_statement(self):
            return self.getTypedRuleContext(Swift3Parser.Compiler_control_statementContext,0)


        def getRuleIndex(self):
            return Swift3Parser.RULE_protocol_member

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProtocol_member" ):
                listener.enterProtocol_member(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProtocol_member" ):
                listener.exitProtocol_member(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProtocol_member" ):
                return visitor.visitProtocol_member(self)
            else:
                return visitor.visitChildren(self)




    def protocol_member(self):

        localctx = Swift3Parser.Protocol_memberContext(self, self._ctx, self.state)
        self.enterRule(localctx, 278, self.RULE_protocol_member)
        try:
            self.state = 1610
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [Swift3Parser.T__5, Swift3Parser.T__33, Swift3Parser.T__35, Swift3Parser.T__38, Swift3Parser.T__46, Swift3Parser.T__47, Swift3Parser.T__48, Swift3Parser.T__51, Swift3Parser.T__52, Swift3Parser.T__54, Swift3Parser.T__55, Swift3Parser.T__64, Swift3Parser.T__65, Swift3Parser.T__66, Swift3Parser.T__67, Swift3Parser.T__68, Swift3Parser.T__69, Swift3Parser.T__70, Swift3Parser.T__71, Swift3Parser.T__74, Swift3Parser.T__75, Swift3Parser.T__76, Swift3Parser.T__77, Swift3Parser.T__78, Swift3Parser.T__79, Swift3Parser.T__80, Swift3Parser.T__81, Swift3Parser.AT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 1608
                self.protocol_member_declaration()
                pass
            elif token in [Swift3Parser.T__21, Swift3Parser.T__28]:
                self.enterOuterAlt(localctx, 2)
                self.state = 1609
                self.compiler_control_statement()
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

    class Protocol_member_declarationContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def protocol_property_declaration(self):
            return self.getTypedRuleContext(Swift3Parser.Protocol_property_declarationContext,0)


        def protocol_method_declaration(self):
            return self.getTypedRuleContext(Swift3Parser.Protocol_method_declarationContext,0)


        def protocol_initializer_declaration(self):
            return self.getTypedRuleContext(Swift3Parser.Protocol_initializer_declarationContext,0)


        def protocol_subscript_declaration(self):
            return self.getTypedRuleContext(Swift3Parser.Protocol_subscript_declarationContext,0)


        def protocol_associated_type_declaration(self):
            return self.getTypedRuleContext(Swift3Parser.Protocol_associated_type_declarationContext,0)


        def typealias_declaration(self):
            return self.getTypedRuleContext(Swift3Parser.Typealias_declarationContext,0)


        def getRuleIndex(self):
            return Swift3Parser.RULE_protocol_member_declaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProtocol_member_declaration" ):
                listener.enterProtocol_member_declaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProtocol_member_declaration" ):
                listener.exitProtocol_member_declaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProtocol_member_declaration" ):
                return visitor.visitProtocol_member_declaration(self)
            else:
                return visitor.visitChildren(self)




    def protocol_member_declaration(self):

        localctx = Swift3Parser.Protocol_member_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 280, self.RULE_protocol_member_declaration)
        try:
            self.state = 1618
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,172,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 1612
                self.protocol_property_declaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 1613
                self.protocol_method_declaration()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 1614
                self.protocol_initializer_declaration()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 1615
                self.protocol_subscript_declaration()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 1616
                self.protocol_associated_type_declaration()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 1617
                self.typealias_declaration()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Protocol_property_declarationContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variable_declaration_head(self):
            return self.getTypedRuleContext(Swift3Parser.Variable_declaration_headContext,0)


        def variable_name(self):
            return self.getTypedRuleContext(Swift3Parser.Variable_nameContext,0)


        def type_annotation(self):
            return self.getTypedRuleContext(Swift3Parser.Type_annotationContext,0)


        def getter_setter_keyword_block(self):
            return self.getTypedRuleContext(Swift3Parser.Getter_setter_keyword_blockContext,0)


        def getRuleIndex(self):
            return Swift3Parser.RULE_protocol_property_declaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProtocol_property_declaration" ):
                listener.enterProtocol_property_declaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProtocol_property_declaration" ):
                listener.exitProtocol_property_declaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProtocol_property_declaration" ):
                return visitor.visitProtocol_property_declaration(self)
            else:
                return visitor.visitChildren(self)




    def protocol_property_declaration(self):

        localctx = Swift3Parser.Protocol_property_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 282, self.RULE_protocol_property_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1620
            self.variable_declaration_head()
            self.state = 1621
            self.variable_name()
            self.state = 1622
            self.type_annotation()
            self.state = 1623
            self.getter_setter_keyword_block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Protocol_method_declarationContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def function_head(self):
            return self.getTypedRuleContext(Swift3Parser.Function_headContext,0)


        def function_name(self):
            return self.getTypedRuleContext(Swift3Parser.Function_nameContext,0)


        def function_signature(self):
            return self.getTypedRuleContext(Swift3Parser.Function_signatureContext,0)


        def generic_parameter_clause(self):
            return self.getTypedRuleContext(Swift3Parser.Generic_parameter_clauseContext,0)


        def generic_where_clause(self):
            return self.getTypedRuleContext(Swift3Parser.Generic_where_clauseContext,0)


        def getRuleIndex(self):
            return Swift3Parser.RULE_protocol_method_declaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProtocol_method_declaration" ):
                listener.enterProtocol_method_declaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProtocol_method_declaration" ):
                listener.exitProtocol_method_declaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProtocol_method_declaration" ):
                return visitor.visitProtocol_method_declaration(self)
            else:
                return visitor.visitChildren(self)




    def protocol_method_declaration(self):

        localctx = Swift3Parser.Protocol_method_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 284, self.RULE_protocol_method_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1625
            self.function_head()
            self.state = 1626
            self.function_name()
            self.state = 1628
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==Swift3Parser.LT:
                self.state = 1627
                self.generic_parameter_clause()


            self.state = 1630
            self.function_signature()
            self.state = 1632
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==Swift3Parser.T__12:
                self.state = 1631
                self.generic_where_clause()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Protocol_initializer_declarationContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def initializer_head(self):
            return self.getTypedRuleContext(Swift3Parser.Initializer_headContext,0)


        def parameter_clause(self):
            return self.getTypedRuleContext(Swift3Parser.Parameter_clauseContext,0)


        def generic_parameter_clause(self):
            return self.getTypedRuleContext(Swift3Parser.Generic_parameter_clauseContext,0)


        def generic_where_clause(self):
            return self.getTypedRuleContext(Swift3Parser.Generic_where_clauseContext,0)


        def getRuleIndex(self):
            return Swift3Parser.RULE_protocol_initializer_declaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProtocol_initializer_declaration" ):
                listener.enterProtocol_initializer_declaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProtocol_initializer_declaration" ):
                listener.exitProtocol_initializer_declaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProtocol_initializer_declaration" ):
                return visitor.visitProtocol_initializer_declaration(self)
            else:
                return visitor.visitChildren(self)




    def protocol_initializer_declaration(self):

        localctx = Swift3Parser.Protocol_initializer_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 286, self.RULE_protocol_initializer_declaration)
        self._la = 0 # Token type
        try:
            self.state = 1654
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,180,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 1634
                self.initializer_head()
                self.state = 1636
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==Swift3Parser.LT:
                    self.state = 1635
                    self.generic_parameter_clause()


                self.state = 1638
                self.parameter_clause()
                self.state = 1640
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==Swift3Parser.T__43:
                    self.state = 1639
                    self.match(Swift3Parser.T__43)


                self.state = 1643
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==Swift3Parser.T__12:
                    self.state = 1642
                    self.generic_where_clause()


                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 1645
                self.initializer_head()
                self.state = 1647
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==Swift3Parser.LT:
                    self.state = 1646
                    self.generic_parameter_clause()


                self.state = 1649
                self.parameter_clause()
                self.state = 1650
                self.match(Swift3Parser.T__44)
                self.state = 1652
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==Swift3Parser.T__12:
                    self.state = 1651
                    self.generic_where_clause()


                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Protocol_subscript_declarationContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def subscript_head(self):
            return self.getTypedRuleContext(Swift3Parser.Subscript_headContext,0)


        def subscript_result(self):
            return self.getTypedRuleContext(Swift3Parser.Subscript_resultContext,0)


        def getter_setter_keyword_block(self):
            return self.getTypedRuleContext(Swift3Parser.Getter_setter_keyword_blockContext,0)


        def getRuleIndex(self):
            return Swift3Parser.RULE_protocol_subscript_declaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProtocol_subscript_declaration" ):
                listener.enterProtocol_subscript_declaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProtocol_subscript_declaration" ):
                listener.exitProtocol_subscript_declaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProtocol_subscript_declaration" ):
                return visitor.visitProtocol_subscript_declaration(self)
            else:
                return visitor.visitChildren(self)




    def protocol_subscript_declaration(self):

        localctx = Swift3Parser.Protocol_subscript_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 288, self.RULE_protocol_subscript_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1656
            self.subscript_head()
            self.state = 1657
            self.subscript_result()
            self.state = 1658
            self.getter_setter_keyword_block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Protocol_associated_type_declarationContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def typealias_name(self):
            return self.getTypedRuleContext(Swift3Parser.Typealias_nameContext,0)


        def attributes(self):
            return self.getTypedRuleContext(Swift3Parser.AttributesContext,0)


        def access_level_modifier(self):
            return self.getTypedRuleContext(Swift3Parser.Access_level_modifierContext,0)


        def type_inheritance_clause(self):
            return self.getTypedRuleContext(Swift3Parser.Type_inheritance_clauseContext,0)


        def typealias_assignment(self):
            return self.getTypedRuleContext(Swift3Parser.Typealias_assignmentContext,0)


        def getRuleIndex(self):
            return Swift3Parser.RULE_protocol_associated_type_declaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProtocol_associated_type_declaration" ):
                listener.enterProtocol_associated_type_declaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProtocol_associated_type_declaration" ):
                listener.exitProtocol_associated_type_declaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProtocol_associated_type_declaration" ):
                return visitor.visitProtocol_associated_type_declaration(self)
            else:
                return visitor.visitChildren(self)




    def protocol_associated_type_declaration(self):

        localctx = Swift3Parser.Protocol_associated_type_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 290, self.RULE_protocol_associated_type_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1661
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==Swift3Parser.AT:
                self.state = 1660
                self.attributes()


            self.state = 1664
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((((_la - 76)) & ~0x3f) == 0 and ((1 << (_la - 76)) & ((1 << (Swift3Parser.T__75 - 76)) | (1 << (Swift3Parser.T__76 - 76)) | (1 << (Swift3Parser.T__77 - 76)) | (1 << (Swift3Parser.T__78 - 76)) | (1 << (Swift3Parser.T__79 - 76)))) != 0):
                self.state = 1663
                self.access_level_modifier()


            self.state = 1666
            self.match(Swift3Parser.T__47)
            self.state = 1667
            self.typealias_name()
            self.state = 1669
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,183,self._ctx)
            if la_ == 1:
                self.state = 1668
                self.type_inheritance_clause()


            self.state = 1672
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,184,self._ctx)
            if la_ == 1:
                self.state = 1671
                self.typealias_assignment()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Initializer_declarationContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def initializer_head(self):
            return self.getTypedRuleContext(Swift3Parser.Initializer_headContext,0)


        def parameter_clause(self):
            return self.getTypedRuleContext(Swift3Parser.Parameter_clauseContext,0)


        def initializer_body(self):
            return self.getTypedRuleContext(Swift3Parser.Initializer_bodyContext,0)


        def generic_parameter_clause(self):
            return self.getTypedRuleContext(Swift3Parser.Generic_parameter_clauseContext,0)


        def generic_where_clause(self):
            return self.getTypedRuleContext(Swift3Parser.Generic_where_clauseContext,0)


        def getRuleIndex(self):
            return Swift3Parser.RULE_initializer_declaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInitializer_declaration" ):
                listener.enterInitializer_declaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInitializer_declaration" ):
                listener.exitInitializer_declaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInitializer_declaration" ):
                return visitor.visitInitializer_declaration(self)
            else:
                return visitor.visitChildren(self)




    def initializer_declaration(self):

        localctx = Swift3Parser.Initializer_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 292, self.RULE_initializer_declaration)
        self._la = 0 # Token type
        try:
            self.state = 1698
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,190,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 1674
                self.initializer_head()
                self.state = 1676
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==Swift3Parser.LT:
                    self.state = 1675
                    self.generic_parameter_clause()


                self.state = 1678
                self.parameter_clause()
                self.state = 1680
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==Swift3Parser.T__43:
                    self.state = 1679
                    self.match(Swift3Parser.T__43)


                self.state = 1683
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==Swift3Parser.T__12:
                    self.state = 1682
                    self.generic_where_clause()


                self.state = 1685
                self.initializer_body()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 1687
                self.initializer_head()
                self.state = 1689
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==Swift3Parser.LT:
                    self.state = 1688
                    self.generic_parameter_clause()


                self.state = 1691
                self.parameter_clause()
                self.state = 1692
                self.match(Swift3Parser.T__44)
                self.state = 1694
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==Swift3Parser.T__12:
                    self.state = 1693
                    self.generic_where_clause()


                self.state = 1696
                self.initializer_body()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Initializer_headContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def attributes(self):
            return self.getTypedRuleContext(Swift3Parser.AttributesContext,0)


        def declaration_modifiers(self):
            return self.getTypedRuleContext(Swift3Parser.Declaration_modifiersContext,0)


        def getRuleIndex(self):
            return Swift3Parser.RULE_initializer_head

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInitializer_head" ):
                listener.enterInitializer_head(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInitializer_head" ):
                listener.exitInitializer_head(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInitializer_head" ):
                return visitor.visitInitializer_head(self)
            else:
                return visitor.visitChildren(self)




    def initializer_head(self):

        localctx = Swift3Parser.Initializer_headContext(self, self._ctx, self.state)
        self.enterRule(localctx, 294, self.RULE_initializer_head)
        self._la = 0 # Token type
        try:
            self.state = 1723
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,197,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 1701
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==Swift3Parser.AT:
                    self.state = 1700
                    self.attributes()


                self.state = 1704
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if ((((_la - 36)) & ~0x3f) == 0 and ((1 << (_la - 36)) & ((1 << (Swift3Parser.T__35 - 36)) | (1 << (Swift3Parser.T__46 - 36)) | (1 << (Swift3Parser.T__52 - 36)) | (1 << (Swift3Parser.T__54 - 36)) | (1 << (Swift3Parser.T__55 - 36)) | (1 << (Swift3Parser.T__64 - 36)) | (1 << (Swift3Parser.T__65 - 36)) | (1 << (Swift3Parser.T__66 - 36)) | (1 << (Swift3Parser.T__67 - 36)) | (1 << (Swift3Parser.T__68 - 36)) | (1 << (Swift3Parser.T__69 - 36)) | (1 << (Swift3Parser.T__70 - 36)) | (1 << (Swift3Parser.T__71 - 36)) | (1 << (Swift3Parser.T__74 - 36)) | (1 << (Swift3Parser.T__75 - 36)) | (1 << (Swift3Parser.T__76 - 36)) | (1 << (Swift3Parser.T__77 - 36)) | (1 << (Swift3Parser.T__78 - 36)) | (1 << (Swift3Parser.T__79 - 36)) | (1 << (Swift3Parser.T__80 - 36)) | (1 << (Swift3Parser.T__81 - 36)))) != 0):
                    self.state = 1703
                    self.declaration_modifiers()


                self.state = 1706
                self.match(Swift3Parser.T__48)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 1708
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==Swift3Parser.AT:
                    self.state = 1707
                    self.attributes()


                self.state = 1711
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if ((((_la - 36)) & ~0x3f) == 0 and ((1 << (_la - 36)) & ((1 << (Swift3Parser.T__35 - 36)) | (1 << (Swift3Parser.T__46 - 36)) | (1 << (Swift3Parser.T__52 - 36)) | (1 << (Swift3Parser.T__54 - 36)) | (1 << (Swift3Parser.T__55 - 36)) | (1 << (Swift3Parser.T__64 - 36)) | (1 << (Swift3Parser.T__65 - 36)) | (1 << (Swift3Parser.T__66 - 36)) | (1 << (Swift3Parser.T__67 - 36)) | (1 << (Swift3Parser.T__68 - 36)) | (1 << (Swift3Parser.T__69 - 36)) | (1 << (Swift3Parser.T__70 - 36)) | (1 << (Swift3Parser.T__71 - 36)) | (1 << (Swift3Parser.T__74 - 36)) | (1 << (Swift3Parser.T__75 - 36)) | (1 << (Swift3Parser.T__76 - 36)) | (1 << (Swift3Parser.T__77 - 36)) | (1 << (Swift3Parser.T__78 - 36)) | (1 << (Swift3Parser.T__79 - 36)) | (1 << (Swift3Parser.T__80 - 36)) | (1 << (Swift3Parser.T__81 - 36)))) != 0):
                    self.state = 1710
                    self.declaration_modifiers()


                self.state = 1713
                self.match(Swift3Parser.T__48)
                self.state = 1714
                self.match(Swift3Parser.QUESTION)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 1716
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==Swift3Parser.AT:
                    self.state = 1715
                    self.attributes()


                self.state = 1719
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if ((((_la - 36)) & ~0x3f) == 0 and ((1 << (_la - 36)) & ((1 << (Swift3Parser.T__35 - 36)) | (1 << (Swift3Parser.T__46 - 36)) | (1 << (Swift3Parser.T__52 - 36)) | (1 << (Swift3Parser.T__54 - 36)) | (1 << (Swift3Parser.T__55 - 36)) | (1 << (Swift3Parser.T__64 - 36)) | (1 << (Swift3Parser.T__65 - 36)) | (1 << (Swift3Parser.T__66 - 36)) | (1 << (Swift3Parser.T__67 - 36)) | (1 << (Swift3Parser.T__68 - 36)) | (1 << (Swift3Parser.T__69 - 36)) | (1 << (Swift3Parser.T__70 - 36)) | (1 << (Swift3Parser.T__71 - 36)) | (1 << (Swift3Parser.T__74 - 36)) | (1 << (Swift3Parser.T__75 - 36)) | (1 << (Swift3Parser.T__76 - 36)) | (1 << (Swift3Parser.T__77 - 36)) | (1 << (Swift3Parser.T__78 - 36)) | (1 << (Swift3Parser.T__79 - 36)) | (1 << (Swift3Parser.T__80 - 36)) | (1 << (Swift3Parser.T__81 - 36)))) != 0):
                    self.state = 1718
                    self.declaration_modifiers()


                self.state = 1721
                self.match(Swift3Parser.T__48)
                self.state = 1722
                self.match(Swift3Parser.BANG)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Initializer_bodyContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def code_block(self):
            return self.getTypedRuleContext(Swift3Parser.Code_blockContext,0)


        def getRuleIndex(self):
            return Swift3Parser.RULE_initializer_body

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInitializer_body" ):
                listener.enterInitializer_body(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInitializer_body" ):
                listener.exitInitializer_body(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInitializer_body" ):
                return visitor.visitInitializer_body(self)
            else:
                return visitor.visitChildren(self)




    def initializer_body(self):

        localctx = Swift3Parser.Initializer_bodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 296, self.RULE_initializer_body)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1725
            self.code_block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Deinitializer_declarationContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def code_block(self):
            return self.getTypedRuleContext(Swift3Parser.Code_blockContext,0)


        def attributes(self):
            return self.getTypedRuleContext(Swift3Parser.AttributesContext,0)


        def getRuleIndex(self):
            return Swift3Parser.RULE_deinitializer_declaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeinitializer_declaration" ):
                listener.enterDeinitializer_declaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeinitializer_declaration" ):
                listener.exitDeinitializer_declaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeinitializer_declaration" ):
                return visitor.visitDeinitializer_declaration(self)
            else:
                return visitor.visitChildren(self)




    def deinitializer_declaration(self):

        localctx = Swift3Parser.Deinitializer_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 298, self.RULE_deinitializer_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1728
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==Swift3Parser.AT:
                self.state = 1727
                self.attributes()


            self.state = 1730
            self.match(Swift3Parser.T__49)
            self.state = 1731
            self.code_block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Extension_declarationContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_identifier(self):
            return self.getTypedRuleContext(Swift3Parser.Type_identifierContext,0)


        def extension_body(self):
            return self.getTypedRuleContext(Swift3Parser.Extension_bodyContext,0)


        def attributes(self):
            return self.getTypedRuleContext(Swift3Parser.AttributesContext,0)


        def access_level_modifier(self):
            return self.getTypedRuleContext(Swift3Parser.Access_level_modifierContext,0)


        def type_inheritance_clause(self):
            return self.getTypedRuleContext(Swift3Parser.Type_inheritance_clauseContext,0)


        def generic_where_clause(self):
            return self.getTypedRuleContext(Swift3Parser.Generic_where_clauseContext,0)


        def getRuleIndex(self):
            return Swift3Parser.RULE_extension_declaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExtension_declaration" ):
                listener.enterExtension_declaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExtension_declaration" ):
                listener.exitExtension_declaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExtension_declaration" ):
                return visitor.visitExtension_declaration(self)
            else:
                return visitor.visitChildren(self)




    def extension_declaration(self):

        localctx = Swift3Parser.Extension_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 300, self.RULE_extension_declaration)
        self._la = 0 # Token type
        try:
            self.state = 1757
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,204,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 1734
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==Swift3Parser.AT:
                    self.state = 1733
                    self.attributes()


                self.state = 1737
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if ((((_la - 76)) & ~0x3f) == 0 and ((1 << (_la - 76)) & ((1 << (Swift3Parser.T__75 - 76)) | (1 << (Swift3Parser.T__76 - 76)) | (1 << (Swift3Parser.T__77 - 76)) | (1 << (Swift3Parser.T__78 - 76)) | (1 << (Swift3Parser.T__79 - 76)))) != 0):
                    self.state = 1736
                    self.access_level_modifier()


                self.state = 1739
                self.match(Swift3Parser.T__50)
                self.state = 1740
                self.type_identifier()
                self.state = 1742
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==Swift3Parser.COLON:
                    self.state = 1741
                    self.type_inheritance_clause()


                self.state = 1744
                self.extension_body()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 1747
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==Swift3Parser.AT:
                    self.state = 1746
                    self.attributes()


                self.state = 1750
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if ((((_la - 76)) & ~0x3f) == 0 and ((1 << (_la - 76)) & ((1 << (Swift3Parser.T__75 - 76)) | (1 << (Swift3Parser.T__76 - 76)) | (1 << (Swift3Parser.T__77 - 76)) | (1 << (Swift3Parser.T__78 - 76)) | (1 << (Swift3Parser.T__79 - 76)))) != 0):
                    self.state = 1749
                    self.access_level_modifier()


                self.state = 1752
                self.match(Swift3Parser.T__50)
                self.state = 1753
                self.type_identifier()
                self.state = 1754
                self.generic_where_clause()
                self.state = 1755
                self.extension_body()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Extension_bodyContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def extension_member(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Swift3Parser.Extension_memberContext)
            else:
                return self.getTypedRuleContext(Swift3Parser.Extension_memberContext,i)


        def getRuleIndex(self):
            return Swift3Parser.RULE_extension_body

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExtension_body" ):
                listener.enterExtension_body(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExtension_body" ):
                listener.exitExtension_body(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExtension_body" ):
                return visitor.visitExtension_body(self)
            else:
                return visitor.visitChildren(self)




    def extension_body(self):

        localctx = Swift3Parser.Extension_bodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 302, self.RULE_extension_body)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1759
            self.match(Swift3Parser.LCURLY)
            self.state = 1763
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << Swift3Parser.T__4) | (1 << Swift3Parser.T__5) | (1 << Swift3Parser.T__21) | (1 << Swift3Parser.T__28) | (1 << Swift3Parser.T__32) | (1 << Swift3Parser.T__33) | (1 << Swift3Parser.T__34) | (1 << Swift3Parser.T__35) | (1 << Swift3Parser.T__36) | (1 << Swift3Parser.T__37) | (1 << Swift3Parser.T__38) | (1 << Swift3Parser.T__45) | (1 << Swift3Parser.T__46) | (1 << Swift3Parser.T__48) | (1 << Swift3Parser.T__49) | (1 << Swift3Parser.T__50) | (1 << Swift3Parser.T__51) | (1 << Swift3Parser.T__52) | (1 << Swift3Parser.T__54) | (1 << Swift3Parser.T__55) | (1 << Swift3Parser.T__56))) != 0) or ((((_la - 65)) & ~0x3f) == 0 and ((1 << (_la - 65)) & ((1 << (Swift3Parser.T__64 - 65)) | (1 << (Swift3Parser.T__65 - 65)) | (1 << (Swift3Parser.T__66 - 65)) | (1 << (Swift3Parser.T__67 - 65)) | (1 << (Swift3Parser.T__68 - 65)) | (1 << (Swift3Parser.T__69 - 65)) | (1 << (Swift3Parser.T__70 - 65)) | (1 << (Swift3Parser.T__71 - 65)) | (1 << (Swift3Parser.T__74 - 65)) | (1 << (Swift3Parser.T__75 - 65)) | (1 << (Swift3Parser.T__76 - 65)) | (1 << (Swift3Parser.T__77 - 65)) | (1 << (Swift3Parser.T__78 - 65)) | (1 << (Swift3Parser.T__79 - 65)) | (1 << (Swift3Parser.T__80 - 65)) | (1 << (Swift3Parser.T__81 - 65)))) != 0) or _la==Swift3Parser.AT:
                self.state = 1760
                self.extension_member()
                self.state = 1765
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 1766
            self.match(Swift3Parser.RCURLY)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Extension_memberContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declaration(self):
            return self.getTypedRuleContext(Swift3Parser.DeclarationContext,0)


        def compiler_control_statement(self):
            return self.getTypedRuleContext(Swift3Parser.Compiler_control_statementContext,0)


        def getRuleIndex(self):
            return Swift3Parser.RULE_extension_member

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExtension_member" ):
                listener.enterExtension_member(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExtension_member" ):
                listener.exitExtension_member(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExtension_member" ):
                return visitor.visitExtension_member(self)
            else:
                return visitor.visitChildren(self)




    def extension_member(self):

        localctx = Swift3Parser.Extension_memberContext(self, self._ctx, self.state)
        self.enterRule(localctx, 304, self.RULE_extension_member)
        try:
            self.state = 1770
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [Swift3Parser.T__4, Swift3Parser.T__5, Swift3Parser.T__32, Swift3Parser.T__33, Swift3Parser.T__34, Swift3Parser.T__35, Swift3Parser.T__36, Swift3Parser.T__37, Swift3Parser.T__38, Swift3Parser.T__45, Swift3Parser.T__46, Swift3Parser.T__48, Swift3Parser.T__49, Swift3Parser.T__50, Swift3Parser.T__51, Swift3Parser.T__52, Swift3Parser.T__54, Swift3Parser.T__55, Swift3Parser.T__56, Swift3Parser.T__64, Swift3Parser.T__65, Swift3Parser.T__66, Swift3Parser.T__67, Swift3Parser.T__68, Swift3Parser.T__69, Swift3Parser.T__70, Swift3Parser.T__71, Swift3Parser.T__74, Swift3Parser.T__75, Swift3Parser.T__76, Swift3Parser.T__77, Swift3Parser.T__78, Swift3Parser.T__79, Swift3Parser.T__80, Swift3Parser.T__81, Swift3Parser.AT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 1768
                self.declaration()
                pass
            elif token in [Swift3Parser.T__21, Swift3Parser.T__28]:
                self.enterOuterAlt(localctx, 2)
                self.state = 1769
                self.compiler_control_statement()
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

    class Subscript_declarationContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def subscript_head(self):
            return self.getTypedRuleContext(Swift3Parser.Subscript_headContext,0)


        def subscript_result(self):
            return self.getTypedRuleContext(Swift3Parser.Subscript_resultContext,0)


        def code_block(self):
            return self.getTypedRuleContext(Swift3Parser.Code_blockContext,0)


        def getter_setter_block(self):
            return self.getTypedRuleContext(Swift3Parser.Getter_setter_blockContext,0)


        def getter_setter_keyword_block(self):
            return self.getTypedRuleContext(Swift3Parser.Getter_setter_keyword_blockContext,0)


        def getRuleIndex(self):
            return Swift3Parser.RULE_subscript_declaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSubscript_declaration" ):
                listener.enterSubscript_declaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSubscript_declaration" ):
                listener.exitSubscript_declaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSubscript_declaration" ):
                return visitor.visitSubscript_declaration(self)
            else:
                return visitor.visitChildren(self)




    def subscript_declaration(self):

        localctx = Swift3Parser.Subscript_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 306, self.RULE_subscript_declaration)
        try:
            self.state = 1784
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,207,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 1772
                self.subscript_head()
                self.state = 1773
                self.subscript_result()
                self.state = 1774
                self.code_block()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 1776
                self.subscript_head()
                self.state = 1777
                self.subscript_result()
                self.state = 1778
                self.getter_setter_block()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 1780
                self.subscript_head()
                self.state = 1781
                self.subscript_result()
                self.state = 1782
                self.getter_setter_keyword_block()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Subscript_headContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def parameter_clause(self):
            return self.getTypedRuleContext(Swift3Parser.Parameter_clauseContext,0)


        def attributes(self):
            return self.getTypedRuleContext(Swift3Parser.AttributesContext,0)


        def declaration_modifiers(self):
            return self.getTypedRuleContext(Swift3Parser.Declaration_modifiersContext,0)


        def getRuleIndex(self):
            return Swift3Parser.RULE_subscript_head

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSubscript_head" ):
                listener.enterSubscript_head(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSubscript_head" ):
                listener.exitSubscript_head(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSubscript_head" ):
                return visitor.visitSubscript_head(self)
            else:
                return visitor.visitChildren(self)




    def subscript_head(self):

        localctx = Swift3Parser.Subscript_headContext(self, self._ctx, self.state)
        self.enterRule(localctx, 308, self.RULE_subscript_head)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1787
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==Swift3Parser.AT:
                self.state = 1786
                self.attributes()


            self.state = 1790
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((((_la - 36)) & ~0x3f) == 0 and ((1 << (_la - 36)) & ((1 << (Swift3Parser.T__35 - 36)) | (1 << (Swift3Parser.T__46 - 36)) | (1 << (Swift3Parser.T__52 - 36)) | (1 << (Swift3Parser.T__54 - 36)) | (1 << (Swift3Parser.T__55 - 36)) | (1 << (Swift3Parser.T__64 - 36)) | (1 << (Swift3Parser.T__65 - 36)) | (1 << (Swift3Parser.T__66 - 36)) | (1 << (Swift3Parser.T__67 - 36)) | (1 << (Swift3Parser.T__68 - 36)) | (1 << (Swift3Parser.T__69 - 36)) | (1 << (Swift3Parser.T__70 - 36)) | (1 << (Swift3Parser.T__71 - 36)) | (1 << (Swift3Parser.T__74 - 36)) | (1 << (Swift3Parser.T__75 - 36)) | (1 << (Swift3Parser.T__76 - 36)) | (1 << (Swift3Parser.T__77 - 36)) | (1 << (Swift3Parser.T__78 - 36)) | (1 << (Swift3Parser.T__79 - 36)) | (1 << (Swift3Parser.T__80 - 36)) | (1 << (Swift3Parser.T__81 - 36)))) != 0):
                self.state = 1789
                self.declaration_modifiers()


            self.state = 1792
            self.match(Swift3Parser.T__51)
            self.state = 1793
            self.parameter_clause()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Subscript_resultContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def arrow_operator(self):
            return self.getTypedRuleContext(Swift3Parser.Arrow_operatorContext,0)


        def type(self):
            return self.getTypedRuleContext(Swift3Parser.TypeContext,0)


        def attributes(self):
            return self.getTypedRuleContext(Swift3Parser.AttributesContext,0)


        def getRuleIndex(self):
            return Swift3Parser.RULE_subscript_result

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSubscript_result" ):
                listener.enterSubscript_result(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSubscript_result" ):
                listener.exitSubscript_result(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSubscript_result" ):
                return visitor.visitSubscript_result(self)
            else:
                return visitor.visitChildren(self)




    def subscript_result(self):

        localctx = Swift3Parser.Subscript_resultContext(self, self._ctx, self.state)
        self.enterRule(localctx, 310, self.RULE_subscript_result)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1795
            self.arrow_operator()
            self.state = 1797
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,210,self._ctx)
            if la_ == 1:
                self.state = 1796
                self.attributes()


            self.state = 1799
            self.type(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Operator_declarationContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def prefix_operator_declaration(self):
            return self.getTypedRuleContext(Swift3Parser.Prefix_operator_declarationContext,0)


        def postfix_operator_declaration(self):
            return self.getTypedRuleContext(Swift3Parser.Postfix_operator_declarationContext,0)


        def infix_operator_declaration(self):
            return self.getTypedRuleContext(Swift3Parser.Infix_operator_declarationContext,0)


        def getRuleIndex(self):
            return Swift3Parser.RULE_operator_declaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOperator_declaration" ):
                listener.enterOperator_declaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOperator_declaration" ):
                listener.exitOperator_declaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOperator_declaration" ):
                return visitor.visitOperator_declaration(self)
            else:
                return visitor.visitChildren(self)




    def operator_declaration(self):

        localctx = Swift3Parser.Operator_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 312, self.RULE_operator_declaration)
        try:
            self.state = 1804
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [Swift3Parser.T__52]:
                self.enterOuterAlt(localctx, 1)
                self.state = 1801
                self.prefix_operator_declaration()
                pass
            elif token in [Swift3Parser.T__54]:
                self.enterOuterAlt(localctx, 2)
                self.state = 1802
                self.postfix_operator_declaration()
                pass
            elif token in [Swift3Parser.T__55]:
                self.enterOuterAlt(localctx, 3)
                self.state = 1803
                self.infix_operator_declaration()
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

    class Prefix_operator_declarationContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def operator(self):
            return self.getTypedRuleContext(Swift3Parser.OperatorContext,0)


        def getRuleIndex(self):
            return Swift3Parser.RULE_prefix_operator_declaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrefix_operator_declaration" ):
                listener.enterPrefix_operator_declaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrefix_operator_declaration" ):
                listener.exitPrefix_operator_declaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrefix_operator_declaration" ):
                return visitor.visitPrefix_operator_declaration(self)
            else:
                return visitor.visitChildren(self)




    def prefix_operator_declaration(self):

        localctx = Swift3Parser.Prefix_operator_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 314, self.RULE_prefix_operator_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1806
            self.match(Swift3Parser.T__52)
            self.state = 1807
            self.match(Swift3Parser.T__53)
            self.state = 1808
            self.operator()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Postfix_operator_declarationContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def operator(self):
            return self.getTypedRuleContext(Swift3Parser.OperatorContext,0)


        def getRuleIndex(self):
            return Swift3Parser.RULE_postfix_operator_declaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPostfix_operator_declaration" ):
                listener.enterPostfix_operator_declaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPostfix_operator_declaration" ):
                listener.exitPostfix_operator_declaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPostfix_operator_declaration" ):
                return visitor.visitPostfix_operator_declaration(self)
            else:
                return visitor.visitChildren(self)




    def postfix_operator_declaration(self):

        localctx = Swift3Parser.Postfix_operator_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 316, self.RULE_postfix_operator_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1810
            self.match(Swift3Parser.T__54)
            self.state = 1811
            self.match(Swift3Parser.T__53)
            self.state = 1812
            self.operator()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Infix_operator_declarationContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def operator(self):
            return self.getTypedRuleContext(Swift3Parser.OperatorContext,0)


        def infix_operator_group(self):
            return self.getTypedRuleContext(Swift3Parser.Infix_operator_groupContext,0)


        def getRuleIndex(self):
            return Swift3Parser.RULE_infix_operator_declaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInfix_operator_declaration" ):
                listener.enterInfix_operator_declaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInfix_operator_declaration" ):
                listener.exitInfix_operator_declaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInfix_operator_declaration" ):
                return visitor.visitInfix_operator_declaration(self)
            else:
                return visitor.visitChildren(self)




    def infix_operator_declaration(self):

        localctx = Swift3Parser.Infix_operator_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 318, self.RULE_infix_operator_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1814
            self.match(Swift3Parser.T__55)
            self.state = 1815
            self.match(Swift3Parser.T__53)
            self.state = 1816
            self.operator()
            self.state = 1818
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,212,self._ctx)
            if la_ == 1:
                self.state = 1817
                self.infix_operator_group()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Infix_operator_groupContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def precedence_group_name(self):
            return self.getTypedRuleContext(Swift3Parser.Precedence_group_nameContext,0)


        def getRuleIndex(self):
            return Swift3Parser.RULE_infix_operator_group

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInfix_operator_group" ):
                listener.enterInfix_operator_group(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInfix_operator_group" ):
                listener.exitInfix_operator_group(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInfix_operator_group" ):
                return visitor.visitInfix_operator_group(self)
            else:
                return visitor.visitChildren(self)




    def infix_operator_group(self):

        localctx = Swift3Parser.Infix_operator_groupContext(self, self._ctx, self.state)
        self.enterRule(localctx, 320, self.RULE_infix_operator_group)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1820
            self.match(Swift3Parser.COLON)
            self.state = 1821
            self.precedence_group_name()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Precedence_group_declarationContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def precedence_group_name(self):
            return self.getTypedRuleContext(Swift3Parser.Precedence_group_nameContext,0)


        def precedence_group_attribute(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Swift3Parser.Precedence_group_attributeContext)
            else:
                return self.getTypedRuleContext(Swift3Parser.Precedence_group_attributeContext,i)


        def getRuleIndex(self):
            return Swift3Parser.RULE_precedence_group_declaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrecedence_group_declaration" ):
                listener.enterPrecedence_group_declaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrecedence_group_declaration" ):
                listener.exitPrecedence_group_declaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrecedence_group_declaration" ):
                return visitor.visitPrecedence_group_declaration(self)
            else:
                return visitor.visitChildren(self)




    def precedence_group_declaration(self):

        localctx = Swift3Parser.Precedence_group_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 322, self.RULE_precedence_group_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1823
            self.match(Swift3Parser.T__56)
            self.state = 1824
            self.precedence_group_name()
            self.state = 1825
            self.match(Swift3Parser.LCURLY)
            self.state = 1829
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << Swift3Parser.T__57) | (1 << Swift3Parser.T__58) | (1 << Swift3Parser.T__59) | (1 << Swift3Parser.T__60))) != 0):
                self.state = 1826
                self.precedence_group_attribute()
                self.state = 1831
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 1832
            self.match(Swift3Parser.RCURLY)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Precedence_group_attributeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def precedence_group_relation(self):
            return self.getTypedRuleContext(Swift3Parser.Precedence_group_relationContext,0)


        def precedence_group_assignment(self):
            return self.getTypedRuleContext(Swift3Parser.Precedence_group_assignmentContext,0)


        def precedence_group_associativity(self):
            return self.getTypedRuleContext(Swift3Parser.Precedence_group_associativityContext,0)


        def getRuleIndex(self):
            return Swift3Parser.RULE_precedence_group_attribute

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrecedence_group_attribute" ):
                listener.enterPrecedence_group_attribute(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrecedence_group_attribute" ):
                listener.exitPrecedence_group_attribute(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrecedence_group_attribute" ):
                return visitor.visitPrecedence_group_attribute(self)
            else:
                return visitor.visitChildren(self)




    def precedence_group_attribute(self):

        localctx = Swift3Parser.Precedence_group_attributeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 324, self.RULE_precedence_group_attribute)
        try:
            self.state = 1837
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [Swift3Parser.T__57, Swift3Parser.T__58]:
                self.enterOuterAlt(localctx, 1)
                self.state = 1834
                self.precedence_group_relation()
                pass
            elif token in [Swift3Parser.T__59]:
                self.enterOuterAlt(localctx, 2)
                self.state = 1835
                self.precedence_group_assignment()
                pass
            elif token in [Swift3Parser.T__60]:
                self.enterOuterAlt(localctx, 3)
                self.state = 1836
                self.precedence_group_associativity()
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

    class Precedence_group_relationContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def precedence_group_names(self):
            return self.getTypedRuleContext(Swift3Parser.Precedence_group_namesContext,0)


        def getRuleIndex(self):
            return Swift3Parser.RULE_precedence_group_relation

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrecedence_group_relation" ):
                listener.enterPrecedence_group_relation(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrecedence_group_relation" ):
                listener.exitPrecedence_group_relation(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrecedence_group_relation" ):
                return visitor.visitPrecedence_group_relation(self)
            else:
                return visitor.visitChildren(self)




    def precedence_group_relation(self):

        localctx = Swift3Parser.Precedence_group_relationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 326, self.RULE_precedence_group_relation)
        try:
            self.state = 1845
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [Swift3Parser.T__57]:
                self.enterOuterAlt(localctx, 1)
                self.state = 1839
                self.match(Swift3Parser.T__57)
                self.state = 1840
                self.match(Swift3Parser.COLON)
                self.state = 1841
                self.precedence_group_names()
                pass
            elif token in [Swift3Parser.T__58]:
                self.enterOuterAlt(localctx, 2)
                self.state = 1842
                self.match(Swift3Parser.T__58)
                self.state = 1843
                self.match(Swift3Parser.COLON)
                self.state = 1844
                self.precedence_group_names()
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

    class Precedence_group_assignmentContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def boolean_literal(self):
            return self.getTypedRuleContext(Swift3Parser.Boolean_literalContext,0)


        def getRuleIndex(self):
            return Swift3Parser.RULE_precedence_group_assignment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrecedence_group_assignment" ):
                listener.enterPrecedence_group_assignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrecedence_group_assignment" ):
                listener.exitPrecedence_group_assignment(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrecedence_group_assignment" ):
                return visitor.visitPrecedence_group_assignment(self)
            else:
                return visitor.visitChildren(self)




    def precedence_group_assignment(self):

        localctx = Swift3Parser.Precedence_group_assignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 328, self.RULE_precedence_group_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1847
            self.match(Swift3Parser.T__59)
            self.state = 1848
            self.match(Swift3Parser.COLON)
            self.state = 1849
            self.boolean_literal()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Precedence_group_associativityContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def associativity(self):
            return self.getTypedRuleContext(Swift3Parser.AssociativityContext,0)


        def getRuleIndex(self):
            return Swift3Parser.RULE_precedence_group_associativity

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrecedence_group_associativity" ):
                listener.enterPrecedence_group_associativity(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrecedence_group_associativity" ):
                listener.exitPrecedence_group_associativity(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrecedence_group_associativity" ):
                return visitor.visitPrecedence_group_associativity(self)
            else:
                return visitor.visitChildren(self)




    def precedence_group_associativity(self):

        localctx = Swift3Parser.Precedence_group_associativityContext(self, self._ctx, self.state)
        self.enterRule(localctx, 330, self.RULE_precedence_group_associativity)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1851
            self.match(Swift3Parser.T__60)
            self.state = 1852
            self.match(Swift3Parser.COLON)
            self.state = 1853
            self.associativity()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class AssociativityContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return Swift3Parser.RULE_associativity

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssociativity" ):
                listener.enterAssociativity(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssociativity" ):
                listener.exitAssociativity(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssociativity" ):
                return visitor.visitAssociativity(self)
            else:
                return visitor.visitChildren(self)




    def associativity(self):

        localctx = Swift3Parser.AssociativityContext(self, self._ctx, self.state)
        self.enterRule(localctx, 332, self.RULE_associativity)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1855
            _la = self._input.LA(1)
            if not(((((_la - 62)) & ~0x3f) == 0 and ((1 << (_la - 62)) & ((1 << (Swift3Parser.T__61 - 62)) | (1 << (Swift3Parser.T__62 - 62)) | (1 << (Swift3Parser.T__63 - 62)))) != 0)):
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

    class Precedence_group_namesContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def precedence_group_name(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Swift3Parser.Precedence_group_nameContext)
            else:
                return self.getTypedRuleContext(Swift3Parser.Precedence_group_nameContext,i)


        def getRuleIndex(self):
            return Swift3Parser.RULE_precedence_group_names

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrecedence_group_names" ):
                listener.enterPrecedence_group_names(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrecedence_group_names" ):
                listener.exitPrecedence_group_names(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrecedence_group_names" ):
                return visitor.visitPrecedence_group_names(self)
            else:
                return visitor.visitChildren(self)




    def precedence_group_names(self):

        localctx = Swift3Parser.Precedence_group_namesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 334, self.RULE_precedence_group_names)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1857
            self.precedence_group_name()
            self.state = 1862
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==Swift3Parser.COMMA:
                self.state = 1858
                self.match(Swift3Parser.COMMA)
                self.state = 1859
                self.precedence_group_name()
                self.state = 1864
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Precedence_group_nameContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declaration_identifier(self):
            return self.getTypedRuleContext(Swift3Parser.Declaration_identifierContext,0)


        def getRuleIndex(self):
            return Swift3Parser.RULE_precedence_group_name

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrecedence_group_name" ):
                listener.enterPrecedence_group_name(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrecedence_group_name" ):
                listener.exitPrecedence_group_name(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrecedence_group_name" ):
                return visitor.visitPrecedence_group_name(self)
            else:
                return visitor.visitChildren(self)




    def precedence_group_name(self):

        localctx = Swift3Parser.Precedence_group_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 336, self.RULE_precedence_group_name)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1865
            self.declaration_identifier()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Declaration_modifierContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def access_level_modifier(self):
            return self.getTypedRuleContext(Swift3Parser.Access_level_modifierContext,0)


        def mutation_modifier(self):
            return self.getTypedRuleContext(Swift3Parser.Mutation_modifierContext,0)


        def getRuleIndex(self):
            return Swift3Parser.RULE_declaration_modifier

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclaration_modifier" ):
                listener.enterDeclaration_modifier(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclaration_modifier" ):
                listener.exitDeclaration_modifier(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclaration_modifier" ):
                return visitor.visitDeclaration_modifier(self)
            else:
                return visitor.visitChildren(self)




    def declaration_modifier(self):

        localctx = Swift3Parser.Declaration_modifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 338, self.RULE_declaration_modifier)
        try:
            self.state = 1891
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,217,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 1867
                self.match(Swift3Parser.T__35)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 1868
                self.match(Swift3Parser.T__64)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 1869
                self.match(Swift3Parser.T__65)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 1870
                self.match(Swift3Parser.T__46)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 1871
                self.match(Swift3Parser.T__55)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 1872
                self.match(Swift3Parser.T__66)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 1873
                self.match(Swift3Parser.T__67)
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 1874
                self.match(Swift3Parser.T__68)
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 1875
                self.match(Swift3Parser.T__54)
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 1876
                self.match(Swift3Parser.T__52)
                pass

            elif la_ == 11:
                self.enterOuterAlt(localctx, 11)
                self.state = 1877
                self.match(Swift3Parser.T__69)
                pass

            elif la_ == 12:
                self.enterOuterAlt(localctx, 12)
                self.state = 1878
                self.match(Swift3Parser.T__70)
                pass

            elif la_ == 13:
                self.enterOuterAlt(localctx, 13)
                self.state = 1879
                self.match(Swift3Parser.T__71)
                pass

            elif la_ == 14:
                self.enterOuterAlt(localctx, 14)
                self.state = 1880
                self.match(Swift3Parser.T__71)
                self.state = 1881
                self.match(Swift3Parser.LPAREN)
                self.state = 1882
                self.match(Swift3Parser.T__72)
                self.state = 1883
                self.match(Swift3Parser.RPAREN)
                pass

            elif la_ == 15:
                self.enterOuterAlt(localctx, 15)
                self.state = 1884
                self.match(Swift3Parser.T__71)
                self.state = 1885
                self.match(Swift3Parser.LPAREN)
                self.state = 1886
                self.match(Swift3Parser.T__73)
                self.state = 1887
                self.match(Swift3Parser.RPAREN)
                pass

            elif la_ == 16:
                self.enterOuterAlt(localctx, 16)
                self.state = 1888
                self.match(Swift3Parser.T__74)
                pass

            elif la_ == 17:
                self.enterOuterAlt(localctx, 17)
                self.state = 1889
                self.access_level_modifier()
                pass

            elif la_ == 18:
                self.enterOuterAlt(localctx, 18)
                self.state = 1890
                self.mutation_modifier()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Declaration_modifiersContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declaration_modifier(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Swift3Parser.Declaration_modifierContext)
            else:
                return self.getTypedRuleContext(Swift3Parser.Declaration_modifierContext,i)


        def getRuleIndex(self):
            return Swift3Parser.RULE_declaration_modifiers

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclaration_modifiers" ):
                listener.enterDeclaration_modifiers(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclaration_modifiers" ):
                listener.exitDeclaration_modifiers(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclaration_modifiers" ):
                return visitor.visitDeclaration_modifiers(self)
            else:
                return visitor.visitChildren(self)




    def declaration_modifiers(self):

        localctx = Swift3Parser.Declaration_modifiersContext(self, self._ctx, self.state)
        self.enterRule(localctx, 340, self.RULE_declaration_modifiers)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1894
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 1893
                self.declaration_modifier()
                self.state = 1896
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (((((_la - 36)) & ~0x3f) == 0 and ((1 << (_la - 36)) & ((1 << (Swift3Parser.T__35 - 36)) | (1 << (Swift3Parser.T__46 - 36)) | (1 << (Swift3Parser.T__52 - 36)) | (1 << (Swift3Parser.T__54 - 36)) | (1 << (Swift3Parser.T__55 - 36)) | (1 << (Swift3Parser.T__64 - 36)) | (1 << (Swift3Parser.T__65 - 36)) | (1 << (Swift3Parser.T__66 - 36)) | (1 << (Swift3Parser.T__67 - 36)) | (1 << (Swift3Parser.T__68 - 36)) | (1 << (Swift3Parser.T__69 - 36)) | (1 << (Swift3Parser.T__70 - 36)) | (1 << (Swift3Parser.T__71 - 36)) | (1 << (Swift3Parser.T__74 - 36)) | (1 << (Swift3Parser.T__75 - 36)) | (1 << (Swift3Parser.T__76 - 36)) | (1 << (Swift3Parser.T__77 - 36)) | (1 << (Swift3Parser.T__78 - 36)) | (1 << (Swift3Parser.T__79 - 36)) | (1 << (Swift3Parser.T__80 - 36)) | (1 << (Swift3Parser.T__81 - 36)))) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Access_level_modifierContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return Swift3Parser.RULE_access_level_modifier

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAccess_level_modifier" ):
                listener.enterAccess_level_modifier(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAccess_level_modifier" ):
                listener.exitAccess_level_modifier(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAccess_level_modifier" ):
                return visitor.visitAccess_level_modifier(self)
            else:
                return visitor.visitChildren(self)




    def access_level_modifier(self):

        localctx = Swift3Parser.Access_level_modifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 342, self.RULE_access_level_modifier)
        try:
            self.state = 1923
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,219,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 1898
                self.match(Swift3Parser.T__75)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 1899
                self.match(Swift3Parser.T__75)
                self.state = 1900
                self.match(Swift3Parser.LPAREN)
                self.state = 1901
                self.match(Swift3Parser.T__40)
                self.state = 1902
                self.match(Swift3Parser.RPAREN)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 1903
                self.match(Swift3Parser.T__76)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 1904
                self.match(Swift3Parser.T__76)
                self.state = 1905
                self.match(Swift3Parser.LPAREN)
                self.state = 1906
                self.match(Swift3Parser.T__40)
                self.state = 1907
                self.match(Swift3Parser.RPAREN)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 1908
                self.match(Swift3Parser.T__77)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 1909
                self.match(Swift3Parser.T__77)
                self.state = 1910
                self.match(Swift3Parser.LPAREN)
                self.state = 1911
                self.match(Swift3Parser.T__40)
                self.state = 1912
                self.match(Swift3Parser.RPAREN)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 1913
                self.match(Swift3Parser.T__78)
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 1914
                self.match(Swift3Parser.T__78)
                self.state = 1915
                self.match(Swift3Parser.LPAREN)
                self.state = 1916
                self.match(Swift3Parser.T__40)
                self.state = 1917
                self.match(Swift3Parser.RPAREN)
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 1918
                self.match(Swift3Parser.T__79)
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 1919
                self.match(Swift3Parser.T__79)
                self.state = 1920
                self.match(Swift3Parser.LPAREN)
                self.state = 1921
                self.match(Swift3Parser.T__40)
                self.state = 1922
                self.match(Swift3Parser.RPAREN)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Mutation_modifierContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return Swift3Parser.RULE_mutation_modifier

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMutation_modifier" ):
                listener.enterMutation_modifier(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMutation_modifier" ):
                listener.exitMutation_modifier(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMutation_modifier" ):
                return visitor.visitMutation_modifier(self)
            else:
                return visitor.visitChildren(self)




    def mutation_modifier(self):

        localctx = Swift3Parser.Mutation_modifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 344, self.RULE_mutation_modifier)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1925
            _la = self._input.LA(1)
            if not(_la==Swift3Parser.T__80 or _la==Swift3Parser.T__81):
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

    class PatternContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def wildcard_pattern(self):
            return self.getTypedRuleContext(Swift3Parser.Wildcard_patternContext,0)


        def type_annotation(self):
            return self.getTypedRuleContext(Swift3Parser.Type_annotationContext,0)


        def identifier_pattern(self):
            return self.getTypedRuleContext(Swift3Parser.Identifier_patternContext,0)


        def value_binding_pattern(self):
            return self.getTypedRuleContext(Swift3Parser.Value_binding_patternContext,0)


        def tuple_pattern(self):
            return self.getTypedRuleContext(Swift3Parser.Tuple_patternContext,0)


        def enum_case_pattern(self):
            return self.getTypedRuleContext(Swift3Parser.Enum_case_patternContext,0)


        def optional_pattern(self):
            return self.getTypedRuleContext(Swift3Parser.Optional_patternContext,0)


        def type(self):
            return self.getTypedRuleContext(Swift3Parser.TypeContext,0)


        def expression_pattern(self):
            return self.getTypedRuleContext(Swift3Parser.Expression_patternContext,0)


        def pattern(self):
            return self.getTypedRuleContext(Swift3Parser.PatternContext,0)


        def getRuleIndex(self):
            return Swift3Parser.RULE_pattern

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPattern" ):
                listener.enterPattern(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPattern" ):
                listener.exitPattern(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPattern" ):
                return visitor.visitPattern(self)
            else:
                return visitor.visitChildren(self)



    def pattern(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = Swift3Parser.PatternContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 346
        self.enterRecursionRule(localctx, 346, self.RULE_pattern, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1946
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,223,self._ctx)
            if la_ == 1:
                self.state = 1928
                self.wildcard_pattern()
                self.state = 1930
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,220,self._ctx)
                if la_ == 1:
                    self.state = 1929
                    self.type_annotation()


                pass

            elif la_ == 2:
                self.state = 1932
                self.identifier_pattern()
                self.state = 1934
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,221,self._ctx)
                if la_ == 1:
                    self.state = 1933
                    self.type_annotation()


                pass

            elif la_ == 3:
                self.state = 1936
                self.value_binding_pattern()
                pass

            elif la_ == 4:
                self.state = 1937
                self.tuple_pattern()
                self.state = 1939
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,222,self._ctx)
                if la_ == 1:
                    self.state = 1938
                    self.type_annotation()


                pass

            elif la_ == 5:
                self.state = 1941
                self.enum_case_pattern()
                pass

            elif la_ == 6:
                self.state = 1942
                self.optional_pattern()
                pass

            elif la_ == 7:
                self.state = 1943
                self.match(Swift3Parser.T__82)
                self.state = 1944
                self.type(0)
                pass

            elif la_ == 8:
                self.state = 1945
                self.expression_pattern()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 1953
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,224,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = Swift3Parser.PatternContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_pattern)
                    self.state = 1948
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 1949
                    self.match(Swift3Parser.T__83)
                    self.state = 1950
                    self.type(0)
                self.state = 1955
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,224,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Wildcard_patternContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return Swift3Parser.RULE_wildcard_pattern

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWildcard_pattern" ):
                listener.enterWildcard_pattern(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWildcard_pattern" ):
                listener.exitWildcard_pattern(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWildcard_pattern" ):
                return visitor.visitWildcard_pattern(self)
            else:
                return visitor.visitChildren(self)




    def wildcard_pattern(self):

        localctx = Swift3Parser.Wildcard_patternContext(self, self._ctx, self.state)
        self.enterRule(localctx, 348, self.RULE_wildcard_pattern)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1956
            self.match(Swift3Parser.UNDERSCORE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Identifier_patternContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declaration_identifier(self):
            return self.getTypedRuleContext(Swift3Parser.Declaration_identifierContext,0)


        def getRuleIndex(self):
            return Swift3Parser.RULE_identifier_pattern

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIdentifier_pattern" ):
                listener.enterIdentifier_pattern(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIdentifier_pattern" ):
                listener.exitIdentifier_pattern(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdentifier_pattern" ):
                return visitor.visitIdentifier_pattern(self)
            else:
                return visitor.visitChildren(self)




    def identifier_pattern(self):

        localctx = Swift3Parser.Identifier_patternContext(self, self._ctx, self.state)
        self.enterRule(localctx, 350, self.RULE_identifier_pattern)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1958
            self.declaration_identifier()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Value_binding_patternContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def pattern(self):
            return self.getTypedRuleContext(Swift3Parser.PatternContext,0)


        def getRuleIndex(self):
            return Swift3Parser.RULE_value_binding_pattern

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterValue_binding_pattern" ):
                listener.enterValue_binding_pattern(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitValue_binding_pattern" ):
                listener.exitValue_binding_pattern(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitValue_binding_pattern" ):
                return visitor.visitValue_binding_pattern(self)
            else:
                return visitor.visitChildren(self)




    def value_binding_pattern(self):

        localctx = Swift3Parser.Value_binding_patternContext(self, self._ctx, self.state)
        self.enterRule(localctx, 352, self.RULE_value_binding_pattern)
        try:
            self.state = 1964
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [Swift3Parser.T__5]:
                self.enterOuterAlt(localctx, 1)
                self.state = 1960
                self.match(Swift3Parser.T__5)
                self.state = 1961
                self.pattern(0)
                pass
            elif token in [Swift3Parser.T__4]:
                self.enterOuterAlt(localctx, 2)
                self.state = 1962
                self.match(Swift3Parser.T__4)
                self.state = 1963
                self.pattern(0)
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

    class Tuple_patternContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def tuple_pattern_element_list(self):
            return self.getTypedRuleContext(Swift3Parser.Tuple_pattern_element_listContext,0)


        def getRuleIndex(self):
            return Swift3Parser.RULE_tuple_pattern

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTuple_pattern" ):
                listener.enterTuple_pattern(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTuple_pattern" ):
                listener.exitTuple_pattern(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTuple_pattern" ):
                return visitor.visitTuple_pattern(self)
            else:
                return visitor.visitChildren(self)




    def tuple_pattern(self):

        localctx = Swift3Parser.Tuple_patternContext(self, self._ctx, self.state)
        self.enterRule(localctx, 354, self.RULE_tuple_pattern)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1966
            self.match(Swift3Parser.LPAREN)
            self.state = 1968
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,226,self._ctx)
            if la_ == 1:
                self.state = 1967
                self.tuple_pattern_element_list()


            self.state = 1970
            self.match(Swift3Parser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Tuple_pattern_element_listContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def tuple_pattern_element(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Swift3Parser.Tuple_pattern_elementContext)
            else:
                return self.getTypedRuleContext(Swift3Parser.Tuple_pattern_elementContext,i)


        def getRuleIndex(self):
            return Swift3Parser.RULE_tuple_pattern_element_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTuple_pattern_element_list" ):
                listener.enterTuple_pattern_element_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTuple_pattern_element_list" ):
                listener.exitTuple_pattern_element_list(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTuple_pattern_element_list" ):
                return visitor.visitTuple_pattern_element_list(self)
            else:
                return visitor.visitChildren(self)




    def tuple_pattern_element_list(self):

        localctx = Swift3Parser.Tuple_pattern_element_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 356, self.RULE_tuple_pattern_element_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1972
            self.tuple_pattern_element()
            self.state = 1977
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==Swift3Parser.COMMA:
                self.state = 1973
                self.match(Swift3Parser.COMMA)
                self.state = 1974
                self.tuple_pattern_element()
                self.state = 1979
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Tuple_pattern_elementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def pattern(self):
            return self.getTypedRuleContext(Swift3Parser.PatternContext,0)


        def getRuleIndex(self):
            return Swift3Parser.RULE_tuple_pattern_element

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTuple_pattern_element" ):
                listener.enterTuple_pattern_element(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTuple_pattern_element" ):
                listener.exitTuple_pattern_element(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTuple_pattern_element" ):
                return visitor.visitTuple_pattern_element(self)
            else:
                return visitor.visitChildren(self)




    def tuple_pattern_element(self):

        localctx = Swift3Parser.Tuple_pattern_elementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 358, self.RULE_tuple_pattern_element)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1980
            self.pattern(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Enum_case_patternContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def enum_case_name(self):
            return self.getTypedRuleContext(Swift3Parser.Enum_case_nameContext,0)


        def type_identifier(self):
            return self.getTypedRuleContext(Swift3Parser.Type_identifierContext,0)


        def tuple_pattern(self):
            return self.getTypedRuleContext(Swift3Parser.Tuple_patternContext,0)


        def getRuleIndex(self):
            return Swift3Parser.RULE_enum_case_pattern

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEnum_case_pattern" ):
                listener.enterEnum_case_pattern(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEnum_case_pattern" ):
                listener.exitEnum_case_pattern(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEnum_case_pattern" ):
                return visitor.visitEnum_case_pattern(self)
            else:
                return visitor.visitChildren(self)




    def enum_case_pattern(self):

        localctx = Swift3Parser.Enum_case_patternContext(self, self._ctx, self.state)
        self.enterRule(localctx, 360, self.RULE_enum_case_pattern)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1983
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((((_la - 26)) & ~0x3f) == 0 and ((1 << (_la - 26)) & ((1 << (Swift3Parser.T__25 - 26)) | (1 << (Swift3Parser.T__26 - 26)) | (1 << (Swift3Parser.T__27 - 26)) | (1 << (Swift3Parser.T__29 - 26)) | (1 << (Swift3Parser.T__30 - 26)) | (1 << (Swift3Parser.T__39 - 26)) | (1 << (Swift3Parser.T__40 - 26)) | (1 << (Swift3Parser.T__41 - 26)) | (1 << (Swift3Parser.T__42 - 26)) | (1 << (Swift3Parser.T__45 - 26)) | (1 << (Swift3Parser.T__46 - 26)) | (1 << (Swift3Parser.T__52 - 26)) | (1 << (Swift3Parser.T__54 - 26)) | (1 << (Swift3Parser.T__55 - 26)) | (1 << (Swift3Parser.T__57 - 26)) | (1 << (Swift3Parser.T__58 - 26)) | (1 << (Swift3Parser.T__59 - 26)) | (1 << (Swift3Parser.T__60 - 26)) | (1 << (Swift3Parser.T__61 - 26)) | (1 << (Swift3Parser.T__62 - 26)) | (1 << (Swift3Parser.T__63 - 26)) | (1 << (Swift3Parser.T__64 - 26)) | (1 << (Swift3Parser.T__65 - 26)) | (1 << (Swift3Parser.T__66 - 26)) | (1 << (Swift3Parser.T__67 - 26)) | (1 << (Swift3Parser.T__68 - 26)) | (1 << (Swift3Parser.T__69 - 26)) | (1 << (Swift3Parser.T__71 - 26)) | (1 << (Swift3Parser.T__72 - 26)) | (1 << (Swift3Parser.T__73 - 26)) | (1 << (Swift3Parser.T__74 - 26)) | (1 << (Swift3Parser.T__79 - 26)) | (1 << (Swift3Parser.T__80 - 26)) | (1 << (Swift3Parser.T__81 - 26)))) != 0) or ((((_la - 94)) & ~0x3f) == 0 and ((1 << (_la - 94)) & ((1 << (Swift3Parser.T__93 - 94)) | (1 << (Swift3Parser.T__94 - 94)) | (1 << (Swift3Parser.T__95 - 94)) | (1 << (Swift3Parser.T__96 - 94)) | (1 << (Swift3Parser.T__98 - 94)) | (1 << (Swift3Parser.T__109 - 94)) | (1 << (Swift3Parser.T__110 - 94)) | (1 << (Swift3Parser.T__111 - 94)) | (1 << (Swift3Parser.T__112 - 94)) | (1 << (Swift3Parser.T__115 - 94)) | (1 << (Swift3Parser.T__116 - 94)) | (1 << (Swift3Parser.T__117 - 94)) | (1 << (Swift3Parser.T__118 - 94)) | (1 << (Swift3Parser.T__119 - 94)) | (1 << (Swift3Parser.T__120 - 94)) | (1 << (Swift3Parser.T__121 - 94)) | (1 << (Swift3Parser.T__122 - 94)) | (1 << (Swift3Parser.T__123 - 94)) | (1 << (Swift3Parser.T__124 - 94)) | (1 << (Swift3Parser.T__125 - 94)) | (1 << (Swift3Parser.Identifier - 94)))) != 0):
                self.state = 1982
                self.type_identifier()


            self.state = 1985
            self.match(Swift3Parser.DOT)
            self.state = 1986
            self.enum_case_name()
            self.state = 1988
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,229,self._ctx)
            if la_ == 1:
                self.state = 1987
                self.tuple_pattern()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Optional_patternContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def identifier_pattern(self):
            return self.getTypedRuleContext(Swift3Parser.Identifier_patternContext,0)


        def getRuleIndex(self):
            return Swift3Parser.RULE_optional_pattern

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOptional_pattern" ):
                listener.enterOptional_pattern(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOptional_pattern" ):
                listener.exitOptional_pattern(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOptional_pattern" ):
                return visitor.visitOptional_pattern(self)
            else:
                return visitor.visitChildren(self)




    def optional_pattern(self):

        localctx = Swift3Parser.Optional_patternContext(self, self._ctx, self.state)
        self.enterRule(localctx, 362, self.RULE_optional_pattern)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1990
            self.identifier_pattern()
            self.state = 1991
            self.match(Swift3Parser.QUESTION)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Expression_patternContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(Swift3Parser.ExpressionContext,0)


        def getRuleIndex(self):
            return Swift3Parser.RULE_expression_pattern

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression_pattern" ):
                listener.enterExpression_pattern(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression_pattern" ):
                listener.exitExpression_pattern(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression_pattern" ):
                return visitor.visitExpression_pattern(self)
            else:
                return visitor.visitChildren(self)




    def expression_pattern(self):

        localctx = Swift3Parser.Expression_patternContext(self, self._ctx, self.state)
        self.enterRule(localctx, 364, self.RULE_expression_pattern)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1993
            self.expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class AttributeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def attribute_name(self):
            return self.getTypedRuleContext(Swift3Parser.Attribute_nameContext,0)


        def attribute_argument_clause(self):
            return self.getTypedRuleContext(Swift3Parser.Attribute_argument_clauseContext,0)


        def getRuleIndex(self):
            return Swift3Parser.RULE_attribute

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAttribute" ):
                listener.enterAttribute(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAttribute" ):
                listener.exitAttribute(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAttribute" ):
                return visitor.visitAttribute(self)
            else:
                return visitor.visitChildren(self)




    def attribute(self):

        localctx = Swift3Parser.AttributeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 366, self.RULE_attribute)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1995
            self.match(Swift3Parser.AT)
            self.state = 1996
            self.attribute_name()
            self.state = 1998
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,230,self._ctx)
            if la_ == 1:
                self.state = 1997
                self.attribute_argument_clause()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Attribute_nameContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declaration_identifier(self):
            return self.getTypedRuleContext(Swift3Parser.Declaration_identifierContext,0)


        def getRuleIndex(self):
            return Swift3Parser.RULE_attribute_name

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAttribute_name" ):
                listener.enterAttribute_name(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAttribute_name" ):
                listener.exitAttribute_name(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAttribute_name" ):
                return visitor.visitAttribute_name(self)
            else:
                return visitor.visitChildren(self)




    def attribute_name(self):

        localctx = Swift3Parser.Attribute_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 368, self.RULE_attribute_name)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2000
            self.declaration_identifier()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Attribute_argument_clauseContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def balanced_tokens(self):
            return self.getTypedRuleContext(Swift3Parser.Balanced_tokensContext,0)


        def getRuleIndex(self):
            return Swift3Parser.RULE_attribute_argument_clause

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAttribute_argument_clause" ):
                listener.enterAttribute_argument_clause(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAttribute_argument_clause" ):
                listener.exitAttribute_argument_clause(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAttribute_argument_clause" ):
                return visitor.visitAttribute_argument_clause(self)
            else:
                return visitor.visitChildren(self)




    def attribute_argument_clause(self):

        localctx = Swift3Parser.Attribute_argument_clauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 370, self.RULE_attribute_argument_clause)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2002
            self.match(Swift3Parser.LPAREN)
            self.state = 2003
            self.balanced_tokens()
            self.state = 2004
            self.match(Swift3Parser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class AttributesContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def attribute(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Swift3Parser.AttributeContext)
            else:
                return self.getTypedRuleContext(Swift3Parser.AttributeContext,i)


        def getRuleIndex(self):
            return Swift3Parser.RULE_attributes

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAttributes" ):
                listener.enterAttributes(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAttributes" ):
                listener.exitAttributes(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAttributes" ):
                return visitor.visitAttributes(self)
            else:
                return visitor.visitChildren(self)




    def attributes(self):

        localctx = Swift3Parser.AttributesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 372, self.RULE_attributes)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2007
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 2006
                    self.attribute()

                else:
                    raise NoViableAltException(self)
                self.state = 2009
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,231,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Balanced_tokensContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def balanced_token(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Swift3Parser.Balanced_tokenContext)
            else:
                return self.getTypedRuleContext(Swift3Parser.Balanced_tokenContext,i)


        def getRuleIndex(self):
            return Swift3Parser.RULE_balanced_tokens

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBalanced_tokens" ):
                listener.enterBalanced_tokens(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBalanced_tokens" ):
                listener.exitBalanced_tokens(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBalanced_tokens" ):
                return visitor.visitBalanced_tokens(self)
            else:
                return visitor.visitChildren(self)




    def balanced_tokens(self):

        localctx = Swift3Parser.Balanced_tokensContext(self, self._ctx, self.state)
        self.enterRule(localctx, 374, self.RULE_balanced_tokens)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2014
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,232,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 2011
                    self.balanced_token()
                self.state = 2016
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,232,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Balanced_tokenContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def balanced_tokens(self):
            return self.getTypedRuleContext(Swift3Parser.Balanced_tokensContext,0)


        def label_identifier(self):
            return self.getTypedRuleContext(Swift3Parser.Label_identifierContext,0)


        def literal(self):
            return self.getTypedRuleContext(Swift3Parser.LiteralContext,0)


        def operator(self):
            return self.getTypedRuleContext(Swift3Parser.OperatorContext,0)


        def Platform_name_platform_version(self):
            return self.getToken(Swift3Parser.Platform_name_platform_version, 0)

        def any_punctuation_for_balanced_token(self):
            return self.getTypedRuleContext(Swift3Parser.Any_punctuation_for_balanced_tokenContext,0)


        def getRuleIndex(self):
            return Swift3Parser.RULE_balanced_token

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBalanced_token" ):
                listener.enterBalanced_token(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBalanced_token" ):
                listener.exitBalanced_token(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBalanced_token" ):
                return visitor.visitBalanced_token(self)
            else:
                return visitor.visitChildren(self)




    def balanced_token(self):

        localctx = Swift3Parser.Balanced_tokenContext(self, self._ctx, self.state)
        self.enterRule(localctx, 376, self.RULE_balanced_token)
        try:
            self.state = 2034
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,233,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 2017
                self.match(Swift3Parser.LPAREN)
                self.state = 2018
                self.balanced_tokens()
                self.state = 2019
                self.match(Swift3Parser.RPAREN)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 2021
                self.match(Swift3Parser.LBRACK)
                self.state = 2022
                self.balanced_tokens()
                self.state = 2023
                self.match(Swift3Parser.RBRACK)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 2025
                self.match(Swift3Parser.LCURLY)
                self.state = 2026
                self.balanced_tokens()
                self.state = 2027
                self.match(Swift3Parser.RCURLY)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 2029
                self.label_identifier()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 2030
                self.literal()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 2031
                self.operator()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 2032
                self.match(Swift3Parser.Platform_name_platform_version)
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 2033
                self.any_punctuation_for_balanced_token()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Any_punctuation_for_balanced_tokenContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def arrow_operator(self):
            return self.getTypedRuleContext(Swift3Parser.Arrow_operatorContext,0)


        def getRuleIndex(self):
            return Swift3Parser.RULE_any_punctuation_for_balanced_token

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAny_punctuation_for_balanced_token" ):
                listener.enterAny_punctuation_for_balanced_token(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAny_punctuation_for_balanced_token" ):
                listener.exitAny_punctuation_for_balanced_token(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAny_punctuation_for_balanced_token" ):
                return visitor.visitAny_punctuation_for_balanced_token(self)
            else:
                return visitor.visitChildren(self)




    def any_punctuation_for_balanced_token(self):

        localctx = Swift3Parser.Any_punctuation_for_balanced_tokenContext(self, self._ctx, self.state)
        self.enterRule(localctx, 378, self.RULE_any_punctuation_for_balanced_token)
        self._la = 0 # Token type
        try:
            self.state = 2042
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,234,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 2036
                _la = self._input.LA(1)
                if not(((((_la - 85)) & ~0x3f) == 0 and ((1 << (_la - 85)) & ((1 << (Swift3Parser.T__84 - 85)) | (1 << (Swift3Parser.T__85 - 85)) | (1 << (Swift3Parser.DOT - 85)) | (1 << (Swift3Parser.COMMA - 85)) | (1 << (Swift3Parser.COLON - 85)) | (1 << (Swift3Parser.SEMI - 85)) | (1 << (Swift3Parser.QUESTION - 85)) | (1 << (Swift3Parser.AT - 85)))) != 0) or _la==Swift3Parser.EQUAL):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 2037
                self.arrow_operator()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 2038
                if not SwiftSupport.isPrefixOp(_input):
                    from antlr4.error.Errors import FailedPredicateException
                    raise FailedPredicateException(self, "SwiftSupport.isPrefixOp(_input)")
                self.state = 2039
                self.match(Swift3Parser.AND)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 2040
                if not SwiftSupport.isPostfixOp(_input):
                    from antlr4.error.Errors import FailedPredicateException
                    raise FailedPredicateException(self, "SwiftSupport.isPostfixOp(_input)")
                self.state = 2041
                self.match(Swift3Parser.BANG)
                pass


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

        def prefix_expression(self):
            return self.getTypedRuleContext(Swift3Parser.Prefix_expressionContext,0)


        def try_operator(self):
            return self.getTypedRuleContext(Swift3Parser.Try_operatorContext,0)


        def binary_expressions(self):
            return self.getTypedRuleContext(Swift3Parser.Binary_expressionsContext,0)


        def getRuleIndex(self):
            return Swift3Parser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression" ):
                return visitor.visitExpression(self)
            else:
                return visitor.visitChildren(self)




    def expression(self):

        localctx = Swift3Parser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 380, self.RULE_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2045
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,235,self._ctx)
            if la_ == 1:
                self.state = 2044
                self.try_operator()


            self.state = 2047
            self.prefix_expression()
            self.state = 2049
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,236,self._ctx)
            if la_ == 1:
                self.state = 2048
                self.binary_expressions()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Expression_listContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Swift3Parser.ExpressionContext)
            else:
                return self.getTypedRuleContext(Swift3Parser.ExpressionContext,i)


        def getRuleIndex(self):
            return Swift3Parser.RULE_expression_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression_list" ):
                listener.enterExpression_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression_list" ):
                listener.exitExpression_list(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression_list" ):
                return visitor.visitExpression_list(self)
            else:
                return visitor.visitChildren(self)




    def expression_list(self):

        localctx = Swift3Parser.Expression_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 382, self.RULE_expression_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2051
            self.expression()
            self.state = 2056
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==Swift3Parser.COMMA:
                self.state = 2052
                self.match(Swift3Parser.COMMA)
                self.state = 2053
                self.expression()
                self.state = 2058
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Prefix_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def prefix_operator(self):
            return self.getTypedRuleContext(Swift3Parser.Prefix_operatorContext,0)


        def postfix_expression(self):
            return self.getTypedRuleContext(Swift3Parser.Postfix_expressionContext,0)


        def in_out_expression(self):
            return self.getTypedRuleContext(Swift3Parser.In_out_expressionContext,0)


        def getRuleIndex(self):
            return Swift3Parser.RULE_prefix_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrefix_expression" ):
                listener.enterPrefix_expression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrefix_expression" ):
                listener.exitPrefix_expression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrefix_expression" ):
                return visitor.visitPrefix_expression(self)
            else:
                return visitor.visitChildren(self)




    def prefix_expression(self):

        localctx = Swift3Parser.Prefix_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 384, self.RULE_prefix_expression)
        try:
            self.state = 2064
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,238,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 2059
                self.prefix_operator()
                self.state = 2060
                self.postfix_expression(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 2062
                self.postfix_expression(0)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 2063
                self.in_out_expression()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class In_out_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declaration_identifier(self):
            return self.getTypedRuleContext(Swift3Parser.Declaration_identifierContext,0)


        def getRuleIndex(self):
            return Swift3Parser.RULE_in_out_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIn_out_expression" ):
                listener.enterIn_out_expression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIn_out_expression" ):
                listener.exitIn_out_expression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIn_out_expression" ):
                return visitor.visitIn_out_expression(self)
            else:
                return visitor.visitChildren(self)




    def in_out_expression(self):

        localctx = Swift3Parser.In_out_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 386, self.RULE_in_out_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2066
            self.match(Swift3Parser.AND)
            self.state = 2067
            self.declaration_identifier()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Try_operatorContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return Swift3Parser.RULE_try_operator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTry_operator" ):
                listener.enterTry_operator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTry_operator" ):
                listener.exitTry_operator(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTry_operator" ):
                return visitor.visitTry_operator(self)
            else:
                return visitor.visitChildren(self)




    def try_operator(self):

        localctx = Swift3Parser.Try_operatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 388, self.RULE_try_operator)
        try:
            self.state = 2074
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,239,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 2069
                self.match(Swift3Parser.T__86)
                self.state = 2070
                self.match(Swift3Parser.QUESTION)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 2071
                self.match(Swift3Parser.T__86)
                self.state = 2072
                self.match(Swift3Parser.BANG)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 2073
                self.match(Swift3Parser.T__86)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Binary_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def binary_operator(self):
            return self.getTypedRuleContext(Swift3Parser.Binary_operatorContext,0)


        def prefix_expression(self):
            return self.getTypedRuleContext(Swift3Parser.Prefix_expressionContext,0)


        def assignment_operator(self):
            return self.getTypedRuleContext(Swift3Parser.Assignment_operatorContext,0)


        def try_operator(self):
            return self.getTypedRuleContext(Swift3Parser.Try_operatorContext,0)


        def conditional_operator(self):
            return self.getTypedRuleContext(Swift3Parser.Conditional_operatorContext,0)


        def type_casting_operator(self):
            return self.getTypedRuleContext(Swift3Parser.Type_casting_operatorContext,0)


        def getRuleIndex(self):
            return Swift3Parser.RULE_binary_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBinary_expression" ):
                listener.enterBinary_expression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBinary_expression" ):
                listener.exitBinary_expression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBinary_expression" ):
                return visitor.visitBinary_expression(self)
            else:
                return visitor.visitChildren(self)




    def binary_expression(self):

        localctx = Swift3Parser.Binary_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 390, self.RULE_binary_expression)
        try:
            self.state = 2092
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,242,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 2076
                self.binary_operator()
                self.state = 2077
                self.prefix_expression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 2079
                self.assignment_operator()
                self.state = 2081
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,240,self._ctx)
                if la_ == 1:
                    self.state = 2080
                    self.try_operator()


                self.state = 2083
                self.prefix_expression()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 2085
                self.conditional_operator()
                self.state = 2087
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,241,self._ctx)
                if la_ == 1:
                    self.state = 2086
                    self.try_operator()


                self.state = 2089
                self.prefix_expression()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 2091
                self.type_casting_operator()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Binary_expressionsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def binary_expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Swift3Parser.Binary_expressionContext)
            else:
                return self.getTypedRuleContext(Swift3Parser.Binary_expressionContext,i)


        def getRuleIndex(self):
            return Swift3Parser.RULE_binary_expressions

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBinary_expressions" ):
                listener.enterBinary_expressions(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBinary_expressions" ):
                listener.exitBinary_expressions(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBinary_expressions" ):
                return visitor.visitBinary_expressions(self)
            else:
                return visitor.visitChildren(self)




    def binary_expressions(self):

        localctx = Swift3Parser.Binary_expressionsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 392, self.RULE_binary_expressions)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2095
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 2094
                    self.binary_expression()

                else:
                    raise NoViableAltException(self)
                self.state = 2097
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,243,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Conditional_operatorContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(Swift3Parser.ExpressionContext,0)


        def try_operator(self):
            return self.getTypedRuleContext(Swift3Parser.Try_operatorContext,0)


        def getRuleIndex(self):
            return Swift3Parser.RULE_conditional_operator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConditional_operator" ):
                listener.enterConditional_operator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConditional_operator" ):
                listener.exitConditional_operator(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConditional_operator" ):
                return visitor.visitConditional_operator(self)
            else:
                return visitor.visitChildren(self)




    def conditional_operator(self):

        localctx = Swift3Parser.Conditional_operatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 394, self.RULE_conditional_operator)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2099
            self.match(Swift3Parser.QUESTION)
            self.state = 2101
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,244,self._ctx)
            if la_ == 1:
                self.state = 2100
                self.try_operator()


            self.state = 2103
            self.expression()
            self.state = 2104
            self.match(Swift3Parser.COLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Type_casting_operatorContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type(self):
            return self.getTypedRuleContext(Swift3Parser.TypeContext,0)


        def getRuleIndex(self):
            return Swift3Parser.RULE_type_casting_operator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterType_casting_operator" ):
                listener.enterType_casting_operator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitType_casting_operator" ):
                listener.exitType_casting_operator(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitType_casting_operator" ):
                return visitor.visitType_casting_operator(self)
            else:
                return visitor.visitChildren(self)




    def type_casting_operator(self):

        localctx = Swift3Parser.Type_casting_operatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 396, self.RULE_type_casting_operator)
        try:
            self.state = 2116
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,245,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 2106
                self.match(Swift3Parser.T__82)
                self.state = 2107
                self.type(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 2108
                self.match(Swift3Parser.T__83)
                self.state = 2109
                self.type(0)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 2110
                self.match(Swift3Parser.T__83)
                self.state = 2111
                self.match(Swift3Parser.QUESTION)
                self.state = 2112
                self.type(0)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 2113
                self.match(Swift3Parser.T__83)
                self.state = 2114
                self.match(Swift3Parser.BANG)
                self.state = 2115
                self.type(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Primary_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declaration_identifier(self):
            return self.getTypedRuleContext(Swift3Parser.Declaration_identifierContext,0)


        def generic_argument_clause(self):
            return self.getTypedRuleContext(Swift3Parser.Generic_argument_clauseContext,0)


        def literal_expression(self):
            return self.getTypedRuleContext(Swift3Parser.Literal_expressionContext,0)


        def self_expression(self):
            return self.getTypedRuleContext(Swift3Parser.Self_expressionContext,0)


        def superclass_expression(self):
            return self.getTypedRuleContext(Swift3Parser.Superclass_expressionContext,0)


        def closure_expression(self):
            return self.getTypedRuleContext(Swift3Parser.Closure_expressionContext,0)


        def parenthesized_expression(self):
            return self.getTypedRuleContext(Swift3Parser.Parenthesized_expressionContext,0)


        def tuple_expression(self):
            return self.getTypedRuleContext(Swift3Parser.Tuple_expressionContext,0)


        def implicit_member_expression(self):
            return self.getTypedRuleContext(Swift3Parser.Implicit_member_expressionContext,0)


        def wildcard_expression(self):
            return self.getTypedRuleContext(Swift3Parser.Wildcard_expressionContext,0)


        def selector_expression(self):
            return self.getTypedRuleContext(Swift3Parser.Selector_expressionContext,0)


        def key_path_expression(self):
            return self.getTypedRuleContext(Swift3Parser.Key_path_expressionContext,0)


        def getRuleIndex(self):
            return Swift3Parser.RULE_primary_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrimary_expression" ):
                listener.enterPrimary_expression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrimary_expression" ):
                listener.exitPrimary_expression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrimary_expression" ):
                return visitor.visitPrimary_expression(self)
            else:
                return visitor.visitChildren(self)




    def primary_expression(self):

        localctx = Swift3Parser.Primary_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 398, self.RULE_primary_expression)
        try:
            self.state = 2132
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,247,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 2118
                self.declaration_identifier()
                self.state = 2120
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,246,self._ctx)
                if la_ == 1:
                    self.state = 2119
                    self.generic_argument_clause()


                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 2122
                self.literal_expression()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 2123
                self.self_expression()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 2124
                self.superclass_expression()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 2125
                self.closure_expression()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 2126
                self.parenthesized_expression()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 2127
                self.tuple_expression()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 2128
                self.implicit_member_expression()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 2129
                self.wildcard_expression()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 2130
                self.selector_expression()
                pass

            elif la_ == 11:
                self.enterOuterAlt(localctx, 11)
                self.state = 2131
                self.key_path_expression()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Literal_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def literal(self):
            return self.getTypedRuleContext(Swift3Parser.LiteralContext,0)


        def array_literal(self):
            return self.getTypedRuleContext(Swift3Parser.Array_literalContext,0)


        def dictionary_literal(self):
            return self.getTypedRuleContext(Swift3Parser.Dictionary_literalContext,0)


        def getRuleIndex(self):
            return Swift3Parser.RULE_literal_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLiteral_expression" ):
                listener.enterLiteral_expression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLiteral_expression" ):
                listener.exitLiteral_expression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiteral_expression" ):
                return visitor.visitLiteral_expression(self)
            else:
                return visitor.visitChildren(self)




    def literal_expression(self):

        localctx = Swift3Parser.Literal_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 400, self.RULE_literal_expression)
        try:
            self.state = 2142
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,248,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 2134
                self.literal()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 2135
                self.array_literal()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 2136
                self.dictionary_literal()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 2137
                self.match(Swift3Parser.T__87)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 2138
                self.match(Swift3Parser.T__88)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 2139
                self.match(Swift3Parser.T__89)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 2140
                self.match(Swift3Parser.T__90)
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 2141
                self.match(Swift3Parser.T__91)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Array_literalContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def array_literal_items(self):
            return self.getTypedRuleContext(Swift3Parser.Array_literal_itemsContext,0)


        def getRuleIndex(self):
            return Swift3Parser.RULE_array_literal

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArray_literal" ):
                listener.enterArray_literal(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArray_literal" ):
                listener.exitArray_literal(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_literal" ):
                return visitor.visitArray_literal(self)
            else:
                return visitor.visitChildren(self)




    def array_literal(self):

        localctx = Swift3Parser.Array_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 402, self.RULE_array_literal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2144
            self.match(Swift3Parser.LBRACK)
            self.state = 2146
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,249,self._ctx)
            if la_ == 1:
                self.state = 2145
                self.array_literal_items()


            self.state = 2148
            self.match(Swift3Parser.RBRACK)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Array_literal_itemsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def array_literal_item(self):
            return self.getTypedRuleContext(Swift3Parser.Array_literal_itemContext,0)


        def array_literal_items(self):
            return self.getTypedRuleContext(Swift3Parser.Array_literal_itemsContext,0)


        def getRuleIndex(self):
            return Swift3Parser.RULE_array_literal_items

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArray_literal_items" ):
                listener.enterArray_literal_items(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArray_literal_items" ):
                listener.exitArray_literal_items(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_literal_items" ):
                return visitor.visitArray_literal_items(self)
            else:
                return visitor.visitChildren(self)




    def array_literal_items(self):

        localctx = Swift3Parser.Array_literal_itemsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 404, self.RULE_array_literal_items)
        self._la = 0 # Token type
        try:
            self.state = 2158
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,251,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 2150
                self.array_literal_item()
                self.state = 2152
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==Swift3Parser.COMMA:
                    self.state = 2151
                    self.match(Swift3Parser.COMMA)


                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 2154
                self.array_literal_item()
                self.state = 2155
                self.match(Swift3Parser.COMMA)
                self.state = 2156
                self.array_literal_items()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Array_literal_itemContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(Swift3Parser.ExpressionContext,0)


        def getRuleIndex(self):
            return Swift3Parser.RULE_array_literal_item

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArray_literal_item" ):
                listener.enterArray_literal_item(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArray_literal_item" ):
                listener.exitArray_literal_item(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_literal_item" ):
                return visitor.visitArray_literal_item(self)
            else:
                return visitor.visitChildren(self)




    def array_literal_item(self):

        localctx = Swift3Parser.Array_literal_itemContext(self, self._ctx, self.state)
        self.enterRule(localctx, 406, self.RULE_array_literal_item)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2160
            self.expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Dictionary_literalContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def dictionary_literal_items(self):
            return self.getTypedRuleContext(Swift3Parser.Dictionary_literal_itemsContext,0)


        def getRuleIndex(self):
            return Swift3Parser.RULE_dictionary_literal

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDictionary_literal" ):
                listener.enterDictionary_literal(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDictionary_literal" ):
                listener.exitDictionary_literal(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDictionary_literal" ):
                return visitor.visitDictionary_literal(self)
            else:
                return visitor.visitChildren(self)




    def dictionary_literal(self):

        localctx = Swift3Parser.Dictionary_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 408, self.RULE_dictionary_literal)
        try:
            self.state = 2169
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,252,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 2162
                self.match(Swift3Parser.LBRACK)
                self.state = 2163
                self.dictionary_literal_items()
                self.state = 2164
                self.match(Swift3Parser.RBRACK)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 2166
                self.match(Swift3Parser.LBRACK)
                self.state = 2167
                self.match(Swift3Parser.COLON)
                self.state = 2168
                self.match(Swift3Parser.RBRACK)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Dictionary_literal_itemsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def dictionary_literal_item(self):
            return self.getTypedRuleContext(Swift3Parser.Dictionary_literal_itemContext,0)


        def dictionary_literal_items(self):
            return self.getTypedRuleContext(Swift3Parser.Dictionary_literal_itemsContext,0)


        def getRuleIndex(self):
            return Swift3Parser.RULE_dictionary_literal_items

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDictionary_literal_items" ):
                listener.enterDictionary_literal_items(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDictionary_literal_items" ):
                listener.exitDictionary_literal_items(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDictionary_literal_items" ):
                return visitor.visitDictionary_literal_items(self)
            else:
                return visitor.visitChildren(self)




    def dictionary_literal_items(self):

        localctx = Swift3Parser.Dictionary_literal_itemsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 410, self.RULE_dictionary_literal_items)
        self._la = 0 # Token type
        try:
            self.state = 2179
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,254,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 2171
                self.dictionary_literal_item()
                self.state = 2173
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==Swift3Parser.COMMA:
                    self.state = 2172
                    self.match(Swift3Parser.COMMA)


                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 2175
                self.dictionary_literal_item()
                self.state = 2176
                self.match(Swift3Parser.COMMA)
                self.state = 2177
                self.dictionary_literal_items()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Dictionary_literal_itemContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Swift3Parser.ExpressionContext)
            else:
                return self.getTypedRuleContext(Swift3Parser.ExpressionContext,i)


        def getRuleIndex(self):
            return Swift3Parser.RULE_dictionary_literal_item

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDictionary_literal_item" ):
                listener.enterDictionary_literal_item(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDictionary_literal_item" ):
                listener.exitDictionary_literal_item(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDictionary_literal_item" ):
                return visitor.visitDictionary_literal_item(self)
            else:
                return visitor.visitChildren(self)




    def dictionary_literal_item(self):

        localctx = Swift3Parser.Dictionary_literal_itemContext(self, self._ctx, self.state)
        self.enterRule(localctx, 412, self.RULE_dictionary_literal_item)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2181
            self.expression()
            self.state = 2182
            self.match(Swift3Parser.COLON)
            self.state = 2183
            self.expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Playground_literalContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Swift3Parser.ExpressionContext)
            else:
                return self.getTypedRuleContext(Swift3Parser.ExpressionContext,i)


        def getRuleIndex(self):
            return Swift3Parser.RULE_playground_literal

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPlayground_literal" ):
                listener.enterPlayground_literal(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPlayground_literal" ):
                listener.exitPlayground_literal(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPlayground_literal" ):
                return visitor.visitPlayground_literal(self)
            else:
                return visitor.visitChildren(self)




    def playground_literal(self):

        localctx = Swift3Parser.Playground_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 414, self.RULE_playground_literal)
        try:
            self.state = 2218
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [Swift3Parser.T__92]:
                self.enterOuterAlt(localctx, 1)
                self.state = 2185
                self.match(Swift3Parser.T__92)
                self.state = 2186
                self.match(Swift3Parser.LPAREN)
                self.state = 2187
                self.match(Swift3Parser.T__93)
                self.state = 2188
                self.match(Swift3Parser.COLON)
                self.state = 2189
                self.expression()
                self.state = 2190
                self.match(Swift3Parser.COMMA)
                self.state = 2191
                self.match(Swift3Parser.T__94)
                self.state = 2192
                self.match(Swift3Parser.COLON)
                self.state = 2193
                self.expression()
                self.state = 2194
                self.match(Swift3Parser.COMMA)
                self.state = 2195
                self.match(Swift3Parser.T__95)
                self.state = 2196
                self.match(Swift3Parser.COLON)
                self.state = 2197
                self.expression()
                self.state = 2198
                self.match(Swift3Parser.COMMA)
                self.state = 2199
                self.match(Swift3Parser.T__96)
                self.state = 2200
                self.match(Swift3Parser.COLON)
                self.state = 2201
                self.expression()
                self.state = 2202
                self.match(Swift3Parser.RPAREN)
                pass
            elif token in [Swift3Parser.T__97]:
                self.enterOuterAlt(localctx, 2)
                self.state = 2204
                self.match(Swift3Parser.T__97)
                self.state = 2205
                self.match(Swift3Parser.LPAREN)
                self.state = 2206
                self.match(Swift3Parser.T__98)
                self.state = 2207
                self.match(Swift3Parser.COLON)
                self.state = 2208
                self.expression()
                self.state = 2209
                self.match(Swift3Parser.RPAREN)
                pass
            elif token in [Swift3Parser.T__99]:
                self.enterOuterAlt(localctx, 3)
                self.state = 2211
                self.match(Swift3Parser.T__99)
                self.state = 2212
                self.match(Swift3Parser.LPAREN)
                self.state = 2213
                self.match(Swift3Parser.T__98)
                self.state = 2214
                self.match(Swift3Parser.COLON)
                self.state = 2215
                self.expression()
                self.state = 2216
                self.match(Swift3Parser.RPAREN)
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

    class Self_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declaration_identifier(self):
            return self.getTypedRuleContext(Swift3Parser.Declaration_identifierContext,0)


        def expression_list(self):
            return self.getTypedRuleContext(Swift3Parser.Expression_listContext,0)


        def getRuleIndex(self):
            return Swift3Parser.RULE_self_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSelf_expression" ):
                listener.enterSelf_expression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSelf_expression" ):
                listener.exitSelf_expression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSelf_expression" ):
                return visitor.visitSelf_expression(self)
            else:
                return visitor.visitChildren(self)




    def self_expression(self):

        localctx = Swift3Parser.Self_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 416, self.RULE_self_expression)
        try:
            self.state = 2239
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,256,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 2220
                self.match(Swift3Parser.T__100)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 2221
                self.match(Swift3Parser.T__100)
                self.state = 2222
                self.match(Swift3Parser.DOT)
                self.state = 2223
                self.declaration_identifier()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 2224
                self.match(Swift3Parser.T__100)
                self.state = 2225
                self.match(Swift3Parser.LBRACK)
                self.state = 2226
                self.expression_list()
                self.state = 2227
                self.match(Swift3Parser.RBRACK)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 2229
                self.match(Swift3Parser.T__100)
                self.state = 2230
                self.match(Swift3Parser.DOT)
                self.state = 2231
                self.match(Swift3Parser.T__48)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 2232
                self.match(Swift3Parser.T__101)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 2233
                self.match(Swift3Parser.T__101)
                self.state = 2234
                self.match(Swift3Parser.DOT)
                self.state = 2235
                self.declaration_identifier()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 2236
                self.match(Swift3Parser.T__101)
                self.state = 2237
                self.match(Swift3Parser.DOT)
                self.state = 2238
                self.match(Swift3Parser.T__48)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Superclass_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def superclass_method_expression(self):
            return self.getTypedRuleContext(Swift3Parser.Superclass_method_expressionContext,0)


        def superclass_subscript_expression(self):
            return self.getTypedRuleContext(Swift3Parser.Superclass_subscript_expressionContext,0)


        def superclass_initializer_expression(self):
            return self.getTypedRuleContext(Swift3Parser.Superclass_initializer_expressionContext,0)


        def getRuleIndex(self):
            return Swift3Parser.RULE_superclass_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSuperclass_expression" ):
                listener.enterSuperclass_expression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSuperclass_expression" ):
                listener.exitSuperclass_expression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSuperclass_expression" ):
                return visitor.visitSuperclass_expression(self)
            else:
                return visitor.visitChildren(self)




    def superclass_expression(self):

        localctx = Swift3Parser.Superclass_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 418, self.RULE_superclass_expression)
        try:
            self.state = 2244
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,257,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 2241
                self.superclass_method_expression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 2242
                self.superclass_subscript_expression()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 2243
                self.superclass_initializer_expression()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Superclass_method_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declaration_identifier(self):
            return self.getTypedRuleContext(Swift3Parser.Declaration_identifierContext,0)


        def getRuleIndex(self):
            return Swift3Parser.RULE_superclass_method_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSuperclass_method_expression" ):
                listener.enterSuperclass_method_expression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSuperclass_method_expression" ):
                listener.exitSuperclass_method_expression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSuperclass_method_expression" ):
                return visitor.visitSuperclass_method_expression(self)
            else:
                return visitor.visitChildren(self)




    def superclass_method_expression(self):

        localctx = Swift3Parser.Superclass_method_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 420, self.RULE_superclass_method_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2246
            self.match(Swift3Parser.T__102)
            self.state = 2247
            self.match(Swift3Parser.DOT)
            self.state = 2248
            self.declaration_identifier()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Superclass_subscript_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(Swift3Parser.ExpressionContext,0)


        def getRuleIndex(self):
            return Swift3Parser.RULE_superclass_subscript_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSuperclass_subscript_expression" ):
                listener.enterSuperclass_subscript_expression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSuperclass_subscript_expression" ):
                listener.exitSuperclass_subscript_expression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSuperclass_subscript_expression" ):
                return visitor.visitSuperclass_subscript_expression(self)
            else:
                return visitor.visitChildren(self)




    def superclass_subscript_expression(self):

        localctx = Swift3Parser.Superclass_subscript_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 422, self.RULE_superclass_subscript_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2250
            self.match(Swift3Parser.T__102)
            self.state = 2251
            self.match(Swift3Parser.LBRACK)
            self.state = 2252
            self.expression()
            self.state = 2253
            self.match(Swift3Parser.RBRACK)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Superclass_initializer_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return Swift3Parser.RULE_superclass_initializer_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSuperclass_initializer_expression" ):
                listener.enterSuperclass_initializer_expression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSuperclass_initializer_expression" ):
                listener.exitSuperclass_initializer_expression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSuperclass_initializer_expression" ):
                return visitor.visitSuperclass_initializer_expression(self)
            else:
                return visitor.visitChildren(self)




    def superclass_initializer_expression(self):

        localctx = Swift3Parser.Superclass_initializer_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 424, self.RULE_superclass_initializer_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2255
            self.match(Swift3Parser.T__102)
            self.state = 2256
            self.match(Swift3Parser.DOT)
            self.state = 2257
            self.match(Swift3Parser.T__48)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Closure_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def closure_signature(self):
            return self.getTypedRuleContext(Swift3Parser.Closure_signatureContext,0)


        def statements(self):
            return self.getTypedRuleContext(Swift3Parser.StatementsContext,0)


        def getRuleIndex(self):
            return Swift3Parser.RULE_closure_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterClosure_expression" ):
                listener.enterClosure_expression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitClosure_expression" ):
                listener.exitClosure_expression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClosure_expression" ):
                return visitor.visitClosure_expression(self)
            else:
                return visitor.visitChildren(self)




    def closure_expression(self):

        localctx = Swift3Parser.Closure_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 426, self.RULE_closure_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2259
            self.match(Swift3Parser.LCURLY)
            self.state = 2261
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,258,self._ctx)
            if la_ == 1:
                self.state = 2260
                self.closure_signature()


            self.state = 2264
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,259,self._ctx)
            if la_ == 1:
                self.state = 2263
                self.statements()


            self.state = 2266
            self.match(Swift3Parser.RCURLY)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Closure_signatureContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def closure_parameter_clause(self):
            return self.getTypedRuleContext(Swift3Parser.Closure_parameter_clauseContext,0)


        def capture_list(self):
            return self.getTypedRuleContext(Swift3Parser.Capture_listContext,0)


        def function_result(self):
            return self.getTypedRuleContext(Swift3Parser.Function_resultContext,0)


        def getRuleIndex(self):
            return Swift3Parser.RULE_closure_signature

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterClosure_signature" ):
                listener.enterClosure_signature(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitClosure_signature" ):
                listener.exitClosure_signature(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClosure_signature" ):
                return visitor.visitClosure_signature(self)
            else:
                return visitor.visitChildren(self)




    def closure_signature(self):

        localctx = Swift3Parser.Closure_signatureContext(self, self._ctx, self.state)
        self.enterRule(localctx, 428, self.RULE_closure_signature)
        self._la = 0 # Token type
        try:
            self.state = 2283
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,263,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 2269
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==Swift3Parser.LBRACK:
                    self.state = 2268
                    self.capture_list()


                self.state = 2271
                self.closure_parameter_clause()
                self.state = 2273
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,261,self._ctx)
                if la_ == 1:
                    self.state = 2272
                    self.match(Swift3Parser.T__43)


                self.state = 2276
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,262,self._ctx)
                if la_ == 1:
                    self.state = 2275
                    self.function_result()


                self.state = 2278
                self.match(Swift3Parser.T__2)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 2280
                self.capture_list()
                self.state = 2281
                self.match(Swift3Parser.T__2)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Closure_parameter_clauseContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def closure_parameter_list(self):
            return self.getTypedRuleContext(Swift3Parser.Closure_parameter_listContext,0)


        def closure_parameter_clause_identifier_list(self):
            return self.getTypedRuleContext(Swift3Parser.Closure_parameter_clause_identifier_listContext,0)


        def getRuleIndex(self):
            return Swift3Parser.RULE_closure_parameter_clause

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterClosure_parameter_clause" ):
                listener.enterClosure_parameter_clause(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitClosure_parameter_clause" ):
                listener.exitClosure_parameter_clause(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClosure_parameter_clause" ):
                return visitor.visitClosure_parameter_clause(self)
            else:
                return visitor.visitChildren(self)




    def closure_parameter_clause(self):

        localctx = Swift3Parser.Closure_parameter_clauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 430, self.RULE_closure_parameter_clause)
        try:
            self.state = 2292
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,264,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 2285
                self.match(Swift3Parser.LPAREN)
                self.state = 2286
                self.match(Swift3Parser.RPAREN)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 2287
                self.match(Swift3Parser.LPAREN)
                self.state = 2288
                self.closure_parameter_list()
                self.state = 2289
                self.match(Swift3Parser.RPAREN)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 2291
                self.closure_parameter_clause_identifier_list()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Closure_parameter_clause_identifier_listContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declaration_identifier(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Swift3Parser.Declaration_identifierContext)
            else:
                return self.getTypedRuleContext(Swift3Parser.Declaration_identifierContext,i)


        def getRuleIndex(self):
            return Swift3Parser.RULE_closure_parameter_clause_identifier_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterClosure_parameter_clause_identifier_list" ):
                listener.enterClosure_parameter_clause_identifier_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitClosure_parameter_clause_identifier_list" ):
                listener.exitClosure_parameter_clause_identifier_list(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClosure_parameter_clause_identifier_list" ):
                return visitor.visitClosure_parameter_clause_identifier_list(self)
            else:
                return visitor.visitChildren(self)




    def closure_parameter_clause_identifier_list(self):

        localctx = Swift3Parser.Closure_parameter_clause_identifier_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 432, self.RULE_closure_parameter_clause_identifier_list)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2294
            self.declaration_identifier()
            self.state = 2299
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,265,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 2295
                    self.match(Swift3Parser.COMMA)
                    self.state = 2296
                    self.declaration_identifier()
                self.state = 2301
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,265,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Closure_parameter_listContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def closure_parameter(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Swift3Parser.Closure_parameterContext)
            else:
                return self.getTypedRuleContext(Swift3Parser.Closure_parameterContext,i)


        def getRuleIndex(self):
            return Swift3Parser.RULE_closure_parameter_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterClosure_parameter_list" ):
                listener.enterClosure_parameter_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitClosure_parameter_list" ):
                listener.exitClosure_parameter_list(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClosure_parameter_list" ):
                return visitor.visitClosure_parameter_list(self)
            else:
                return visitor.visitChildren(self)




    def closure_parameter_list(self):

        localctx = Swift3Parser.Closure_parameter_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 434, self.RULE_closure_parameter_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2302
            self.closure_parameter()
            self.state = 2307
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==Swift3Parser.COMMA:
                self.state = 2303
                self.match(Swift3Parser.COMMA)
                self.state = 2304
                self.closure_parameter()
                self.state = 2309
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Closure_parameterContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def closure_parameter_name(self):
            return self.getTypedRuleContext(Swift3Parser.Closure_parameter_nameContext,0)


        def type_annotation(self):
            return self.getTypedRuleContext(Swift3Parser.Type_annotationContext,0)


        def range_operator(self):
            return self.getTypedRuleContext(Swift3Parser.Range_operatorContext,0)


        def getRuleIndex(self):
            return Swift3Parser.RULE_closure_parameter

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterClosure_parameter" ):
                listener.enterClosure_parameter(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitClosure_parameter" ):
                listener.exitClosure_parameter(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClosure_parameter" ):
                return visitor.visitClosure_parameter(self)
            else:
                return visitor.visitChildren(self)




    def closure_parameter(self):

        localctx = Swift3Parser.Closure_parameterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 436, self.RULE_closure_parameter)
        self._la = 0 # Token type
        try:
            self.state = 2318
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,268,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 2310
                self.closure_parameter_name()
                self.state = 2312
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==Swift3Parser.COLON:
                    self.state = 2311
                    self.type_annotation()


                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 2314
                self.closure_parameter_name()
                self.state = 2315
                self.type_annotation()
                self.state = 2316
                self.range_operator()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Closure_parameter_nameContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def label_identifier(self):
            return self.getTypedRuleContext(Swift3Parser.Label_identifierContext,0)


        def getRuleIndex(self):
            return Swift3Parser.RULE_closure_parameter_name

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterClosure_parameter_name" ):
                listener.enterClosure_parameter_name(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitClosure_parameter_name" ):
                listener.exitClosure_parameter_name(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClosure_parameter_name" ):
                return visitor.visitClosure_parameter_name(self)
            else:
                return visitor.visitChildren(self)




    def closure_parameter_name(self):

        localctx = Swift3Parser.Closure_parameter_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 438, self.RULE_closure_parameter_name)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2320
            self.label_identifier()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Capture_listContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def capture_list_items(self):
            return self.getTypedRuleContext(Swift3Parser.Capture_list_itemsContext,0)


        def getRuleIndex(self):
            return Swift3Parser.RULE_capture_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCapture_list" ):
                listener.enterCapture_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCapture_list" ):
                listener.exitCapture_list(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCapture_list" ):
                return visitor.visitCapture_list(self)
            else:
                return visitor.visitChildren(self)




    def capture_list(self):

        localctx = Swift3Parser.Capture_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 440, self.RULE_capture_list)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2322
            self.match(Swift3Parser.LBRACK)
            self.state = 2323
            self.capture_list_items()
            self.state = 2324
            self.match(Swift3Parser.RBRACK)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Capture_list_itemsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def capture_list_item(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Swift3Parser.Capture_list_itemContext)
            else:
                return self.getTypedRuleContext(Swift3Parser.Capture_list_itemContext,i)


        def getRuleIndex(self):
            return Swift3Parser.RULE_capture_list_items

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCapture_list_items" ):
                listener.enterCapture_list_items(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCapture_list_items" ):
                listener.exitCapture_list_items(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCapture_list_items" ):
                return visitor.visitCapture_list_items(self)
            else:
                return visitor.visitChildren(self)




    def capture_list_items(self):

        localctx = Swift3Parser.Capture_list_itemsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 442, self.RULE_capture_list_items)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2326
            self.capture_list_item()
            self.state = 2331
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==Swift3Parser.COMMA:
                self.state = 2327
                self.match(Swift3Parser.COMMA)
                self.state = 2328
                self.capture_list_item()
                self.state = 2333
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Capture_list_itemContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(Swift3Parser.ExpressionContext,0)


        def capture_specifier(self):
            return self.getTypedRuleContext(Swift3Parser.Capture_specifierContext,0)


        def getRuleIndex(self):
            return Swift3Parser.RULE_capture_list_item

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCapture_list_item" ):
                listener.enterCapture_list_item(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCapture_list_item" ):
                listener.exitCapture_list_item(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCapture_list_item" ):
                return visitor.visitCapture_list_item(self)
            else:
                return visitor.visitChildren(self)




    def capture_list_item(self):

        localctx = Swift3Parser.Capture_list_itemContext(self, self._ctx, self.state)
        self.enterRule(localctx, 444, self.RULE_capture_list_item)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2335
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,270,self._ctx)
            if la_ == 1:
                self.state = 2334
                self.capture_specifier()


            self.state = 2337
            self.expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Capture_specifierContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return Swift3Parser.RULE_capture_specifier

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCapture_specifier" ):
                listener.enterCapture_specifier(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCapture_specifier" ):
                listener.exitCapture_specifier(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCapture_specifier" ):
                return visitor.visitCapture_specifier(self)
            else:
                return visitor.visitChildren(self)




    def capture_specifier(self):

        localctx = Swift3Parser.Capture_specifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 446, self.RULE_capture_specifier)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2339
            _la = self._input.LA(1)
            if not(((((_la - 72)) & ~0x3f) == 0 and ((1 << (_la - 72)) & ((1 << (Swift3Parser.T__71 - 72)) | (1 << (Swift3Parser.T__74 - 72)) | (1 << (Swift3Parser.T__103 - 72)) | (1 << (Swift3Parser.T__104 - 72)))) != 0)):
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

    class Implicit_member_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def label_identifier(self):
            return self.getTypedRuleContext(Swift3Parser.Label_identifierContext,0)


        def getRuleIndex(self):
            return Swift3Parser.RULE_implicit_member_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterImplicit_member_expression" ):
                listener.enterImplicit_member_expression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitImplicit_member_expression" ):
                listener.exitImplicit_member_expression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitImplicit_member_expression" ):
                return visitor.visitImplicit_member_expression(self)
            else:
                return visitor.visitChildren(self)




    def implicit_member_expression(self):

        localctx = Swift3Parser.Implicit_member_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 448, self.RULE_implicit_member_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2341
            self.match(Swift3Parser.DOT)
            self.state = 2342
            self.label_identifier()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Parenthesized_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(Swift3Parser.ExpressionContext,0)


        def getRuleIndex(self):
            return Swift3Parser.RULE_parenthesized_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParenthesized_expression" ):
                listener.enterParenthesized_expression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParenthesized_expression" ):
                listener.exitParenthesized_expression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParenthesized_expression" ):
                return visitor.visitParenthesized_expression(self)
            else:
                return visitor.visitChildren(self)




    def parenthesized_expression(self):

        localctx = Swift3Parser.Parenthesized_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 450, self.RULE_parenthesized_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2344
            self.match(Swift3Parser.LPAREN)
            self.state = 2345
            self.expression()
            self.state = 2346
            self.match(Swift3Parser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Tuple_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def tuple_element(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Swift3Parser.Tuple_elementContext)
            else:
                return self.getTypedRuleContext(Swift3Parser.Tuple_elementContext,i)


        def getRuleIndex(self):
            return Swift3Parser.RULE_tuple_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTuple_expression" ):
                listener.enterTuple_expression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTuple_expression" ):
                listener.exitTuple_expression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTuple_expression" ):
                return visitor.visitTuple_expression(self)
            else:
                return visitor.visitChildren(self)




    def tuple_expression(self):

        localctx = Swift3Parser.Tuple_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 452, self.RULE_tuple_expression)
        self._la = 0 # Token type
        try:
            self.state = 2360
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,272,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 2348
                self.match(Swift3Parser.LPAREN)
                self.state = 2349
                self.match(Swift3Parser.RPAREN)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 2350
                self.match(Swift3Parser.LPAREN)
                self.state = 2351
                self.tuple_element()
                self.state = 2354
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 2352
                    self.match(Swift3Parser.COMMA)
                    self.state = 2353
                    self.tuple_element()
                    self.state = 2356
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==Swift3Parser.COMMA):
                        break

                self.state = 2358
                self.match(Swift3Parser.RPAREN)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Tuple_elementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(Swift3Parser.ExpressionContext,0)


        def label_identifier(self):
            return self.getTypedRuleContext(Swift3Parser.Label_identifierContext,0)


        def getRuleIndex(self):
            return Swift3Parser.RULE_tuple_element

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTuple_element" ):
                listener.enterTuple_element(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTuple_element" ):
                listener.exitTuple_element(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTuple_element" ):
                return visitor.visitTuple_element(self)
            else:
                return visitor.visitChildren(self)




    def tuple_element(self):

        localctx = Swift3Parser.Tuple_elementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 454, self.RULE_tuple_element)
        try:
            self.state = 2367
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,273,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 2362
                self.expression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 2363
                self.label_identifier()
                self.state = 2364
                self.match(Swift3Parser.COLON)
                self.state = 2365
                self.expression()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Wildcard_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return Swift3Parser.RULE_wildcard_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWildcard_expression" ):
                listener.enterWildcard_expression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWildcard_expression" ):
                listener.exitWildcard_expression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWildcard_expression" ):
                return visitor.visitWildcard_expression(self)
            else:
                return visitor.visitChildren(self)




    def wildcard_expression(self):

        localctx = Swift3Parser.Wildcard_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 456, self.RULE_wildcard_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2369
            self.match(Swift3Parser.UNDERSCORE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Selector_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(Swift3Parser.ExpressionContext,0)


        def getRuleIndex(self):
            return Swift3Parser.RULE_selector_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSelector_expression" ):
                listener.enterSelector_expression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSelector_expression" ):
                listener.exitSelector_expression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSelector_expression" ):
                return visitor.visitSelector_expression(self)
            else:
                return visitor.visitChildren(self)




    def selector_expression(self):

        localctx = Swift3Parser.Selector_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 458, self.RULE_selector_expression)
        try:
            self.state = 2388
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,274,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 2371
                self.match(Swift3Parser.T__105)
                self.state = 2372
                self.match(Swift3Parser.LPAREN)
                self.state = 2373
                self.expression()
                self.state = 2374
                self.match(Swift3Parser.RPAREN)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 2376
                self.match(Swift3Parser.T__105)
                self.state = 2377
                self.match(Swift3Parser.LPAREN)
                self.state = 2378
                self.match(Swift3Parser.T__106)
                self.state = 2379
                self.expression()
                self.state = 2380
                self.match(Swift3Parser.RPAREN)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 2382
                self.match(Swift3Parser.T__105)
                self.state = 2383
                self.match(Swift3Parser.LPAREN)
                self.state = 2384
                self.match(Swift3Parser.T__107)
                self.state = 2385
                self.expression()
                self.state = 2386
                self.match(Swift3Parser.RPAREN)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Key_path_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(Swift3Parser.ExpressionContext,0)


        def getRuleIndex(self):
            return Swift3Parser.RULE_key_path_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterKey_path_expression" ):
                listener.enterKey_path_expression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitKey_path_expression" ):
                listener.exitKey_path_expression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitKey_path_expression" ):
                return visitor.visitKey_path_expression(self)
            else:
                return visitor.visitChildren(self)




    def key_path_expression(self):

        localctx = Swift3Parser.Key_path_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 460, self.RULE_key_path_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2390
            self.match(Swift3Parser.T__108)
            self.state = 2391
            self.match(Swift3Parser.LPAREN)
            self.state = 2392
            self.expression()
            self.state = 2393
            self.match(Swift3Parser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Postfix_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return Swift3Parser.RULE_postfix_expression


        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class Function_call_expression_with_closureContext(Postfix_expressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a Swift3Parser.Postfix_expressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def postfix_expression(self):
            return self.getTypedRuleContext(Swift3Parser.Postfix_expressionContext,0)

        def trailing_closure(self):
            return self.getTypedRuleContext(Swift3Parser.Trailing_closureContext,0)

        def function_call_argument_clause(self):
            return self.getTypedRuleContext(Swift3Parser.Function_call_argument_clauseContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunction_call_expression_with_closure" ):
                listener.enterFunction_call_expression_with_closure(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunction_call_expression_with_closure" ):
                listener.exitFunction_call_expression_with_closure(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunction_call_expression_with_closure" ):
                return visitor.visitFunction_call_expression_with_closure(self)
            else:
                return visitor.visitChildren(self)


    class Function_call_expressionContext(Postfix_expressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a Swift3Parser.Postfix_expressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def postfix_expression(self):
            return self.getTypedRuleContext(Swift3Parser.Postfix_expressionContext,0)

        def function_call_argument_clause(self):
            return self.getTypedRuleContext(Swift3Parser.Function_call_argument_clauseContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunction_call_expression" ):
                listener.enterFunction_call_expression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunction_call_expression" ):
                listener.exitFunction_call_expression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunction_call_expression" ):
                return visitor.visitFunction_call_expression(self)
            else:
                return visitor.visitChildren(self)


    class Explicit_member_expression1Context(Postfix_expressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a Swift3Parser.Postfix_expressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def postfix_expression(self):
            return self.getTypedRuleContext(Swift3Parser.Postfix_expressionContext,0)

        def Pure_decimal_digits(self):
            return self.getToken(Swift3Parser.Pure_decimal_digits, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExplicit_member_expression1" ):
                listener.enterExplicit_member_expression1(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExplicit_member_expression1" ):
                listener.exitExplicit_member_expression1(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExplicit_member_expression1" ):
                return visitor.visitExplicit_member_expression1(self)
            else:
                return visitor.visitChildren(self)


    class Initializer_expressionContext(Postfix_expressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a Swift3Parser.Postfix_expressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def postfix_expression(self):
            return self.getTypedRuleContext(Swift3Parser.Postfix_expressionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInitializer_expression" ):
                listener.enterInitializer_expression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInitializer_expression" ):
                listener.exitInitializer_expression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInitializer_expression" ):
                return visitor.visitInitializer_expression(self)
            else:
                return visitor.visitChildren(self)


    class Postfix_self_expressionContext(Postfix_expressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a Swift3Parser.Postfix_expressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def postfix_expression(self):
            return self.getTypedRuleContext(Swift3Parser.Postfix_expressionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPostfix_self_expression" ):
                listener.enterPostfix_self_expression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPostfix_self_expression" ):
                listener.exitPostfix_self_expression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPostfix_self_expression" ):
                return visitor.visitPostfix_self_expression(self)
            else:
                return visitor.visitChildren(self)


    class Initializer_expression_with_argsContext(Postfix_expressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a Swift3Parser.Postfix_expressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def postfix_expression(self):
            return self.getTypedRuleContext(Swift3Parser.Postfix_expressionContext,0)

        def argument_names(self):
            return self.getTypedRuleContext(Swift3Parser.Argument_namesContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInitializer_expression_with_args" ):
                listener.enterInitializer_expression_with_args(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInitializer_expression_with_args" ):
                listener.exitInitializer_expression_with_args(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInitializer_expression_with_args" ):
                return visitor.visitInitializer_expression_with_args(self)
            else:
                return visitor.visitChildren(self)


    class Dynamic_typeContext(Postfix_expressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a Swift3Parser.Postfix_expressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def dynamic_type_expression(self):
            return self.getTypedRuleContext(Swift3Parser.Dynamic_type_expressionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDynamic_type" ):
                listener.enterDynamic_type(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDynamic_type" ):
                listener.exitDynamic_type(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDynamic_type" ):
                return visitor.visitDynamic_type(self)
            else:
                return visitor.visitChildren(self)


    class Subscript_expressionContext(Postfix_expressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a Swift3Parser.Postfix_expressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def postfix_expression(self):
            return self.getTypedRuleContext(Swift3Parser.Postfix_expressionContext,0)

        def expression_list(self):
            return self.getTypedRuleContext(Swift3Parser.Expression_listContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSubscript_expression" ):
                listener.enterSubscript_expression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSubscript_expression" ):
                listener.exitSubscript_expression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSubscript_expression" ):
                return visitor.visitSubscript_expression(self)
            else:
                return visitor.visitChildren(self)


    class Explicit_member_expression2Context(Postfix_expressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a Swift3Parser.Postfix_expressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def postfix_expression(self):
            return self.getTypedRuleContext(Swift3Parser.Postfix_expressionContext,0)

        def declaration_identifier(self):
            return self.getTypedRuleContext(Swift3Parser.Declaration_identifierContext,0)

        def generic_argument_clause(self):
            return self.getTypedRuleContext(Swift3Parser.Generic_argument_clauseContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExplicit_member_expression2" ):
                listener.enterExplicit_member_expression2(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExplicit_member_expression2" ):
                listener.exitExplicit_member_expression2(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExplicit_member_expression2" ):
                return visitor.visitExplicit_member_expression2(self)
            else:
                return visitor.visitChildren(self)


    class Explicit_member_expression3Context(Postfix_expressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a Swift3Parser.Postfix_expressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def postfix_expression(self):
            return self.getTypedRuleContext(Swift3Parser.Postfix_expressionContext,0)

        def declaration_identifier(self):
            return self.getTypedRuleContext(Swift3Parser.Declaration_identifierContext,0)

        def argument_names(self):
            return self.getTypedRuleContext(Swift3Parser.Argument_namesContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExplicit_member_expression3" ):
                listener.enterExplicit_member_expression3(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExplicit_member_expression3" ):
                listener.exitExplicit_member_expression3(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExplicit_member_expression3" ):
                return visitor.visitExplicit_member_expression3(self)
            else:
                return visitor.visitChildren(self)


    class Explicit_member_expression4Context(Postfix_expressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a Swift3Parser.Postfix_expressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def postfix_expression(self):
            return self.getTypedRuleContext(Swift3Parser.Postfix_expressionContext,0)

        def argument_names(self):
            return self.getTypedRuleContext(Swift3Parser.Argument_namesContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExplicit_member_expression4" ):
                listener.enterExplicit_member_expression4(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExplicit_member_expression4" ):
                listener.exitExplicit_member_expression4(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExplicit_member_expression4" ):
                return visitor.visitExplicit_member_expression4(self)
            else:
                return visitor.visitChildren(self)


    class Postfix_operationContext(Postfix_expressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a Swift3Parser.Postfix_expressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def postfix_expression(self):
            return self.getTypedRuleContext(Swift3Parser.Postfix_expressionContext,0)

        def postfix_operator(self):
            return self.getTypedRuleContext(Swift3Parser.Postfix_operatorContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPostfix_operation" ):
                listener.enterPostfix_operation(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPostfix_operation" ):
                listener.exitPostfix_operation(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPostfix_operation" ):
                return visitor.visitPostfix_operation(self)
            else:
                return visitor.visitChildren(self)


    class PrimaryContext(Postfix_expressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a Swift3Parser.Postfix_expressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def primary_expression(self):
            return self.getTypedRuleContext(Swift3Parser.Primary_expressionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrimary" ):
                listener.enterPrimary(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrimary" ):
                listener.exitPrimary(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrimary" ):
                return visitor.visitPrimary(self)
            else:
                return visitor.visitChildren(self)



    def postfix_expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = Swift3Parser.Postfix_expressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 462
        self.enterRecursionRule(localctx, 462, self.RULE_postfix_expression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2398
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,275,self._ctx)
            if la_ == 1:
                localctx = Swift3Parser.PrimaryContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 2396
                self.primary_expression()
                pass

            elif la_ == 2:
                localctx = Swift3Parser.Dynamic_typeContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 2397
                self.dynamic_type_expression()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 2450
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,279,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 2448
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,278,self._ctx)
                    if la_ == 1:
                        localctx = Swift3Parser.Postfix_operationContext(self, Swift3Parser.Postfix_expressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_postfix_expression)
                        self.state = 2400
                        if not self.precpred(self._ctx, 12):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 12)")
                        self.state = 2401
                        self.postfix_operator()
                        pass

                    elif la_ == 2:
                        localctx = Swift3Parser.Function_call_expressionContext(self, Swift3Parser.Postfix_expressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_postfix_expression)
                        self.state = 2402
                        if not self.precpred(self._ctx, 11):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 11)")
                        self.state = 2403
                        self.function_call_argument_clause()
                        pass

                    elif la_ == 3:
                        localctx = Swift3Parser.Function_call_expression_with_closureContext(self, Swift3Parser.Postfix_expressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_postfix_expression)
                        self.state = 2404
                        if not self.precpred(self._ctx, 10):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 10)")
                        self.state = 2406
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if _la==Swift3Parser.LPAREN:
                            self.state = 2405
                            self.function_call_argument_clause()


                        self.state = 2408
                        self.trailing_closure()
                        pass

                    elif la_ == 4:
                        localctx = Swift3Parser.Initializer_expressionContext(self, Swift3Parser.Postfix_expressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_postfix_expression)
                        self.state = 2409
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 2410
                        self.match(Swift3Parser.DOT)
                        self.state = 2411
                        self.match(Swift3Parser.T__48)
                        pass

                    elif la_ == 5:
                        localctx = Swift3Parser.Initializer_expression_with_argsContext(self, Swift3Parser.Postfix_expressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_postfix_expression)
                        self.state = 2412
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 2413
                        self.match(Swift3Parser.DOT)
                        self.state = 2414
                        self.match(Swift3Parser.T__48)
                        self.state = 2415
                        self.match(Swift3Parser.LPAREN)
                        self.state = 2416
                        self.argument_names()
                        self.state = 2417
                        self.match(Swift3Parser.RPAREN)
                        pass

                    elif la_ == 6:
                        localctx = Swift3Parser.Explicit_member_expression1Context(self, Swift3Parser.Postfix_expressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_postfix_expression)
                        self.state = 2419
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 2420
                        self.match(Swift3Parser.DOT)
                        self.state = 2421
                        self.match(Swift3Parser.Pure_decimal_digits)
                        pass

                    elif la_ == 7:
                        localctx = Swift3Parser.Explicit_member_expression2Context(self, Swift3Parser.Postfix_expressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_postfix_expression)
                        self.state = 2422
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 2423
                        self.match(Swift3Parser.DOT)
                        self.state = 2424
                        self.declaration_identifier()
                        self.state = 2426
                        self._errHandler.sync(self)
                        la_ = self._interp.adaptivePredict(self._input,277,self._ctx)
                        if la_ == 1:
                            self.state = 2425
                            self.generic_argument_clause()


                        pass

                    elif la_ == 8:
                        localctx = Swift3Parser.Explicit_member_expression3Context(self, Swift3Parser.Postfix_expressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_postfix_expression)
                        self.state = 2428
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 2429
                        self.match(Swift3Parser.DOT)
                        self.state = 2430
                        self.declaration_identifier()
                        self.state = 2431
                        self.match(Swift3Parser.LPAREN)
                        self.state = 2432
                        self.argument_names()
                        self.state = 2433
                        self.match(Swift3Parser.RPAREN)
                        pass

                    elif la_ == 9:
                        localctx = Swift3Parser.Explicit_member_expression4Context(self, Swift3Parser.Postfix_expressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_postfix_expression)
                        self.state = 2435
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 2436
                        self.match(Swift3Parser.LPAREN)
                        self.state = 2437
                        self.argument_names()
                        self.state = 2438
                        self.match(Swift3Parser.RPAREN)
                        pass

                    elif la_ == 10:
                        localctx = Swift3Parser.Postfix_self_expressionContext(self, Swift3Parser.Postfix_expressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_postfix_expression)
                        self.state = 2440
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 2441
                        self.match(Swift3Parser.DOT)
                        self.state = 2442
                        self.match(Swift3Parser.T__100)
                        pass

                    elif la_ == 11:
                        localctx = Swift3Parser.Subscript_expressionContext(self, Swift3Parser.Postfix_expressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_postfix_expression)
                        self.state = 2443
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 2444
                        self.match(Swift3Parser.LBRACK)
                        self.state = 2445
                        self.expression_list()
                        self.state = 2446
                        self.match(Swift3Parser.RBRACK)
                        pass


                self.state = 2452
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,279,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Function_call_argument_clauseContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def function_call_argument_list(self):
            return self.getTypedRuleContext(Swift3Parser.Function_call_argument_listContext,0)


        def getRuleIndex(self):
            return Swift3Parser.RULE_function_call_argument_clause

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunction_call_argument_clause" ):
                listener.enterFunction_call_argument_clause(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunction_call_argument_clause" ):
                listener.exitFunction_call_argument_clause(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunction_call_argument_clause" ):
                return visitor.visitFunction_call_argument_clause(self)
            else:
                return visitor.visitChildren(self)




    def function_call_argument_clause(self):

        localctx = Swift3Parser.Function_call_argument_clauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 464, self.RULE_function_call_argument_clause)
        try:
            self.state = 2459
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,280,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 2453
                self.match(Swift3Parser.LPAREN)
                self.state = 2454
                self.match(Swift3Parser.RPAREN)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 2455
                self.match(Swift3Parser.LPAREN)
                self.state = 2456
                self.function_call_argument_list()
                self.state = 2457
                self.match(Swift3Parser.RPAREN)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Function_call_argument_listContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def function_call_argument(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Swift3Parser.Function_call_argumentContext)
            else:
                return self.getTypedRuleContext(Swift3Parser.Function_call_argumentContext,i)


        def getRuleIndex(self):
            return Swift3Parser.RULE_function_call_argument_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunction_call_argument_list" ):
                listener.enterFunction_call_argument_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunction_call_argument_list" ):
                listener.exitFunction_call_argument_list(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunction_call_argument_list" ):
                return visitor.visitFunction_call_argument_list(self)
            else:
                return visitor.visitChildren(self)




    def function_call_argument_list(self):

        localctx = Swift3Parser.Function_call_argument_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 466, self.RULE_function_call_argument_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2461
            self.function_call_argument()
            self.state = 2466
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==Swift3Parser.COMMA:
                self.state = 2462
                self.match(Swift3Parser.COMMA)
                self.state = 2463
                self.function_call_argument()
                self.state = 2468
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Function_call_argumentContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(Swift3Parser.ExpressionContext,0)


        def label_identifier(self):
            return self.getTypedRuleContext(Swift3Parser.Label_identifierContext,0)


        def operator(self):
            return self.getTypedRuleContext(Swift3Parser.OperatorContext,0)


        def getRuleIndex(self):
            return Swift3Parser.RULE_function_call_argument

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunction_call_argument" ):
                listener.enterFunction_call_argument(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunction_call_argument" ):
                listener.exitFunction_call_argument(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunction_call_argument" ):
                return visitor.visitFunction_call_argument(self)
            else:
                return visitor.visitChildren(self)




    def function_call_argument(self):

        localctx = Swift3Parser.Function_call_argumentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 468, self.RULE_function_call_argument)
        try:
            self.state = 2479
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,282,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 2469
                self.expression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 2470
                self.label_identifier()
                self.state = 2471
                self.match(Swift3Parser.COLON)
                self.state = 2472
                self.expression()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 2474
                self.operator()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 2475
                self.label_identifier()
                self.state = 2476
                self.match(Swift3Parser.COLON)
                self.state = 2477
                self.operator()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Trailing_closureContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def closure_expression(self):
            return self.getTypedRuleContext(Swift3Parser.Closure_expressionContext,0)


        def getRuleIndex(self):
            return Swift3Parser.RULE_trailing_closure

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTrailing_closure" ):
                listener.enterTrailing_closure(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTrailing_closure" ):
                listener.exitTrailing_closure(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTrailing_closure" ):
                return visitor.visitTrailing_closure(self)
            else:
                return visitor.visitChildren(self)




    def trailing_closure(self):

        localctx = Swift3Parser.Trailing_closureContext(self, self._ctx, self.state)
        self.enterRule(localctx, 470, self.RULE_trailing_closure)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2481
            self.closure_expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Argument_namesContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def argument_name(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Swift3Parser.Argument_nameContext)
            else:
                return self.getTypedRuleContext(Swift3Parser.Argument_nameContext,i)


        def getRuleIndex(self):
            return Swift3Parser.RULE_argument_names

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArgument_names" ):
                listener.enterArgument_names(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArgument_names" ):
                listener.exitArgument_names(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArgument_names" ):
                return visitor.visitArgument_names(self)
            else:
                return visitor.visitChildren(self)




    def argument_names(self):

        localctx = Swift3Parser.Argument_namesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 472, self.RULE_argument_names)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2483
            self.argument_name()
            self.state = 2487
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << Swift3Parser.T__0) | (1 << Swift3Parser.T__1) | (1 << Swift3Parser.T__2) | (1 << Swift3Parser.T__3) | (1 << Swift3Parser.T__6) | (1 << Swift3Parser.T__7) | (1 << Swift3Parser.T__8) | (1 << Swift3Parser.T__9) | (1 << Swift3Parser.T__10) | (1 << Swift3Parser.T__11) | (1 << Swift3Parser.T__12) | (1 << Swift3Parser.T__13) | (1 << Swift3Parser.T__14) | (1 << Swift3Parser.T__15) | (1 << Swift3Parser.T__16) | (1 << Swift3Parser.T__17) | (1 << Swift3Parser.T__18) | (1 << Swift3Parser.T__19) | (1 << Swift3Parser.T__20) | (1 << Swift3Parser.T__25) | (1 << Swift3Parser.T__26) | (1 << Swift3Parser.T__27) | (1 << Swift3Parser.T__29) | (1 << Swift3Parser.T__30) | (1 << Swift3Parser.T__32) | (1 << Swift3Parser.T__33) | (1 << Swift3Parser.T__34) | (1 << Swift3Parser.T__35) | (1 << Swift3Parser.T__36) | (1 << Swift3Parser.T__37) | (1 << Swift3Parser.T__38) | (1 << Swift3Parser.T__39) | (1 << Swift3Parser.T__40) | (1 << Swift3Parser.T__41) | (1 << Swift3Parser.T__42) | (1 << Swift3Parser.T__43) | (1 << Swift3Parser.T__44) | (1 << Swift3Parser.T__45) | (1 << Swift3Parser.T__46) | (1 << Swift3Parser.T__47) | (1 << Swift3Parser.T__48) | (1 << Swift3Parser.T__49) | (1 << Swift3Parser.T__50) | (1 << Swift3Parser.T__51) | (1 << Swift3Parser.T__52) | (1 << Swift3Parser.T__53) | (1 << Swift3Parser.T__54) | (1 << Swift3Parser.T__55) | (1 << Swift3Parser.T__56) | (1 << Swift3Parser.T__57) | (1 << Swift3Parser.T__58) | (1 << Swift3Parser.T__59) | (1 << Swift3Parser.T__60) | (1 << Swift3Parser.T__61) | (1 << Swift3Parser.T__62))) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & ((1 << (Swift3Parser.T__63 - 64)) | (1 << (Swift3Parser.T__64 - 64)) | (1 << (Swift3Parser.T__65 - 64)) | (1 << (Swift3Parser.T__66 - 64)) | (1 << (Swift3Parser.T__67 - 64)) | (1 << (Swift3Parser.T__68 - 64)) | (1 << (Swift3Parser.T__69 - 64)) | (1 << (Swift3Parser.T__70 - 64)) | (1 << (Swift3Parser.T__71 - 64)) | (1 << (Swift3Parser.T__72 - 64)) | (1 << (Swift3Parser.T__73 - 64)) | (1 << (Swift3Parser.T__74 - 64)) | (1 << (Swift3Parser.T__75 - 64)) | (1 << (Swift3Parser.T__76 - 64)) | (1 << (Swift3Parser.T__77 - 64)) | (1 << (Swift3Parser.T__78 - 64)) | (1 << (Swift3Parser.T__79 - 64)) | (1 << (Swift3Parser.T__80 - 64)) | (1 << (Swift3Parser.T__81 - 64)) | (1 << (Swift3Parser.T__82 - 64)) | (1 << (Swift3Parser.T__83 - 64)) | (1 << (Swift3Parser.T__86 - 64)) | (1 << (Swift3Parser.T__93 - 64)) | (1 << (Swift3Parser.T__94 - 64)) | (1 << (Swift3Parser.T__95 - 64)) | (1 << (Swift3Parser.T__96 - 64)) | (1 << (Swift3Parser.T__98 - 64)) | (1 << (Swift3Parser.T__100 - 64)) | (1 << (Swift3Parser.T__101 - 64)) | (1 << (Swift3Parser.T__102 - 64)) | (1 << (Swift3Parser.T__109 - 64)) | (1 << (Swift3Parser.T__110 - 64)) | (1 << (Swift3Parser.T__111 - 64)) | (1 << (Swift3Parser.T__112 - 64)) | (1 << (Swift3Parser.T__113 - 64)) | (1 << (Swift3Parser.T__115 - 64)) | (1 << (Swift3Parser.T__116 - 64)) | (1 << (Swift3Parser.T__117 - 64)) | (1 << (Swift3Parser.T__118 - 64)) | (1 << (Swift3Parser.T__119 - 64)) | (1 << (Swift3Parser.T__120 - 64)) | (1 << (Swift3Parser.T__121 - 64)) | (1 << (Swift3Parser.T__122 - 64)) | (1 << (Swift3Parser.T__123 - 64)) | (1 << (Swift3Parser.T__124 - 64)) | (1 << (Swift3Parser.T__125 - 64)) | (1 << (Swift3Parser.T__126 - 64)))) != 0) or ((((_la - 128)) & ~0x3f) == 0 and ((1 << (_la - 128)) & ((1 << (Swift3Parser.T__127 - 128)) | (1 << (Swift3Parser.T__128 - 128)) | (1 << (Swift3Parser.Identifier - 128)))) != 0):
                self.state = 2484
                self.argument_name()
                self.state = 2489
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Argument_nameContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def label_identifier(self):
            return self.getTypedRuleContext(Swift3Parser.Label_identifierContext,0)


        def getRuleIndex(self):
            return Swift3Parser.RULE_argument_name

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArgument_name" ):
                listener.enterArgument_name(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArgument_name" ):
                listener.exitArgument_name(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArgument_name" ):
                return visitor.visitArgument_name(self)
            else:
                return visitor.visitChildren(self)




    def argument_name(self):

        localctx = Swift3Parser.Argument_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 474, self.RULE_argument_name)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2490
            self.label_identifier()
            self.state = 2491
            self.match(Swift3Parser.COLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Dynamic_type_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(Swift3Parser.ExpressionContext,0)


        def getRuleIndex(self):
            return Swift3Parser.RULE_dynamic_type_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDynamic_type_expression" ):
                listener.enterDynamic_type_expression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDynamic_type_expression" ):
                listener.exitDynamic_type_expression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDynamic_type_expression" ):
                return visitor.visitDynamic_type_expression(self)
            else:
                return visitor.visitChildren(self)




    def dynamic_type_expression(self):

        localctx = Swift3Parser.Dynamic_type_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 476, self.RULE_dynamic_type_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2493
            self.match(Swift3Parser.T__109)
            self.state = 2494
            self.match(Swift3Parser.LPAREN)
            self.state = 2495
            self.match(Swift3Parser.T__110)
            self.state = 2496
            self.match(Swift3Parser.COLON)
            self.state = 2497
            self.expression()
            self.state = 2498
            self.match(Swift3Parser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class TypeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return Swift3Parser.RULE_type


        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class The_metatype_protocol_typeContext(TypeContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a Swift3Parser.TypeContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def type(self):
            return self.getTypedRuleContext(Swift3Parser.TypeContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterThe_metatype_protocol_type" ):
                listener.enterThe_metatype_protocol_type(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitThe_metatype_protocol_type" ):
                listener.exitThe_metatype_protocol_type(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitThe_metatype_protocol_type" ):
                return visitor.visitThe_metatype_protocol_type(self)
            else:
                return visitor.visitChildren(self)


    class The_function_typeContext(TypeContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a Swift3Parser.TypeContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def function_type(self):
            return self.getTypedRuleContext(Swift3Parser.Function_typeContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterThe_function_type" ):
                listener.enterThe_function_type(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitThe_function_type" ):
                listener.exitThe_function_type(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitThe_function_type" ):
                return visitor.visitThe_function_type(self)
            else:
                return visitor.visitChildren(self)


    class The_implicitly_unwrapped_optional_typeContext(TypeContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a Swift3Parser.TypeContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def type(self):
            return self.getTypedRuleContext(Swift3Parser.TypeContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterThe_implicitly_unwrapped_optional_type" ):
                listener.enterThe_implicitly_unwrapped_optional_type(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitThe_implicitly_unwrapped_optional_type" ):
                listener.exitThe_implicitly_unwrapped_optional_type(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitThe_implicitly_unwrapped_optional_type" ):
                return visitor.visitThe_implicitly_unwrapped_optional_type(self)
            else:
                return visitor.visitChildren(self)


    class The_dictionary_typeContext(TypeContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a Swift3Parser.TypeContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def dictionary_type(self):
            return self.getTypedRuleContext(Swift3Parser.Dictionary_typeContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterThe_dictionary_type" ):
                listener.enterThe_dictionary_type(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitThe_dictionary_type" ):
                listener.exitThe_dictionary_type(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitThe_dictionary_type" ):
                return visitor.visitThe_dictionary_type(self)
            else:
                return visitor.visitChildren(self)


    class The_optional_typeContext(TypeContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a Swift3Parser.TypeContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def type(self):
            return self.getTypedRuleContext(Swift3Parser.TypeContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterThe_optional_type" ):
                listener.enterThe_optional_type(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitThe_optional_type" ):
                listener.exitThe_optional_type(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitThe_optional_type" ):
                return visitor.visitThe_optional_type(self)
            else:
                return visitor.visitChildren(self)


    class The_tuple_typeContext(TypeContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a Swift3Parser.TypeContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def tuple_type(self):
            return self.getTypedRuleContext(Swift3Parser.Tuple_typeContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterThe_tuple_type" ):
                listener.enterThe_tuple_type(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitThe_tuple_type" ):
                listener.exitThe_tuple_type(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitThe_tuple_type" ):
                return visitor.visitThe_tuple_type(self)
            else:
                return visitor.visitChildren(self)


    class The_self_typeContext(TypeContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a Swift3Parser.TypeContext
            super().__init__(parser)
            self.copyFrom(ctx)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterThe_self_type" ):
                listener.enterThe_self_type(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitThe_self_type" ):
                listener.exitThe_self_type(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitThe_self_type" ):
                return visitor.visitThe_self_type(self)
            else:
                return visitor.visitChildren(self)


    class The_array_typeContext(TypeContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a Swift3Parser.TypeContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def array_type(self):
            return self.getTypedRuleContext(Swift3Parser.Array_typeContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterThe_array_type" ):
                listener.enterThe_array_type(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitThe_array_type" ):
                listener.exitThe_array_type(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitThe_array_type" ):
                return visitor.visitThe_array_type(self)
            else:
                return visitor.visitChildren(self)


    class The_metatype_type_typeContext(TypeContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a Swift3Parser.TypeContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def type(self):
            return self.getTypedRuleContext(Swift3Parser.TypeContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterThe_metatype_type_type" ):
                listener.enterThe_metatype_type_type(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitThe_metatype_type_type" ):
                listener.exitThe_metatype_type_type(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitThe_metatype_type_type" ):
                return visitor.visitThe_metatype_type_type(self)
            else:
                return visitor.visitChildren(self)


    class The_protocol_composition_typeContext(TypeContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a Swift3Parser.TypeContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def protocol_composition_type(self):
            return self.getTypedRuleContext(Swift3Parser.Protocol_composition_typeContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterThe_protocol_composition_type" ):
                listener.enterThe_protocol_composition_type(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitThe_protocol_composition_type" ):
                listener.exitThe_protocol_composition_type(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitThe_protocol_composition_type" ):
                return visitor.visitThe_protocol_composition_type(self)
            else:
                return visitor.visitChildren(self)


    class The_any_typeContext(TypeContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a Swift3Parser.TypeContext
            super().__init__(parser)
            self.copyFrom(ctx)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterThe_any_type" ):
                listener.enterThe_any_type(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitThe_any_type" ):
                listener.exitThe_any_type(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitThe_any_type" ):
                return visitor.visitThe_any_type(self)
            else:
                return visitor.visitChildren(self)


    class The_type_identifierContext(TypeContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a Swift3Parser.TypeContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def type_identifier(self):
            return self.getTypedRuleContext(Swift3Parser.Type_identifierContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterThe_type_identifier" ):
                listener.enterThe_type_identifier(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitThe_type_identifier" ):
                listener.exitThe_type_identifier(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitThe_type_identifier" ):
                return visitor.visitThe_type_identifier(self)
            else:
                return visitor.visitChildren(self)



    def type(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = Swift3Parser.TypeContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 478
        self.enterRecursionRule(localctx, 478, self.RULE_type, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2509
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,284,self._ctx)
            if la_ == 1:
                localctx = Swift3Parser.The_array_typeContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 2501
                self.array_type()
                pass

            elif la_ == 2:
                localctx = Swift3Parser.The_dictionary_typeContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 2502
                self.dictionary_type()
                pass

            elif la_ == 3:
                localctx = Swift3Parser.The_function_typeContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 2503
                self.function_type()
                pass

            elif la_ == 4:
                localctx = Swift3Parser.The_type_identifierContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 2504
                self.type_identifier()
                pass

            elif la_ == 5:
                localctx = Swift3Parser.The_tuple_typeContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 2505
                self.tuple_type()
                pass

            elif la_ == 6:
                localctx = Swift3Parser.The_protocol_composition_typeContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 2506
                self.protocol_composition_type()
                pass

            elif la_ == 7:
                localctx = Swift3Parser.The_any_typeContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 2507
                self.match(Swift3Parser.T__113)
                pass

            elif la_ == 8:
                localctx = Swift3Parser.The_self_typeContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 2508
                self.match(Swift3Parser.T__101)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 2523
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,286,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 2521
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,285,self._ctx)
                    if la_ == 1:
                        localctx = Swift3Parser.The_optional_typeContext(self, Swift3Parser.TypeContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_type)
                        self.state = 2511
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 2512
                        self.match(Swift3Parser.QUESTION)
                        pass

                    elif la_ == 2:
                        localctx = Swift3Parser.The_implicitly_unwrapped_optional_typeContext(self, Swift3Parser.TypeContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_type)
                        self.state = 2513
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 2514
                        self.match(Swift3Parser.BANG)
                        pass

                    elif la_ == 3:
                        localctx = Swift3Parser.The_metatype_type_typeContext(self, Swift3Parser.TypeContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_type)
                        self.state = 2515
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 2516
                        self.match(Swift3Parser.DOT)
                        self.state = 2517
                        self.match(Swift3Parser.T__111)
                        pass

                    elif la_ == 4:
                        localctx = Swift3Parser.The_metatype_protocol_typeContext(self, Swift3Parser.TypeContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_type)
                        self.state = 2518
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 2519
                        self.match(Swift3Parser.DOT)
                        self.state = 2520
                        self.match(Swift3Parser.T__112)
                        pass


                self.state = 2525
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,286,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Type_annotationContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type(self):
            return self.getTypedRuleContext(Swift3Parser.TypeContext,0)


        def attributes(self):
            return self.getTypedRuleContext(Swift3Parser.AttributesContext,0)


        def getRuleIndex(self):
            return Swift3Parser.RULE_type_annotation

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterType_annotation" ):
                listener.enterType_annotation(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitType_annotation" ):
                listener.exitType_annotation(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitType_annotation" ):
                return visitor.visitType_annotation(self)
            else:
                return visitor.visitChildren(self)




    def type_annotation(self):

        localctx = Swift3Parser.Type_annotationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 480, self.RULE_type_annotation)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2526
            self.match(Swift3Parser.COLON)
            self.state = 2528
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,287,self._ctx)
            if la_ == 1:
                self.state = 2527
                self.attributes()


            self.state = 2531
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==Swift3Parser.T__114:
                self.state = 2530
                self.match(Swift3Parser.T__114)


            self.state = 2533
            self.type(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Type_identifierContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_name(self):
            return self.getTypedRuleContext(Swift3Parser.Type_nameContext,0)


        def generic_argument_clause(self):
            return self.getTypedRuleContext(Swift3Parser.Generic_argument_clauseContext,0)


        def type_identifier(self):
            return self.getTypedRuleContext(Swift3Parser.Type_identifierContext,0)


        def getRuleIndex(self):
            return Swift3Parser.RULE_type_identifier

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterType_identifier" ):
                listener.enterType_identifier(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitType_identifier" ):
                listener.exitType_identifier(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitType_identifier" ):
                return visitor.visitType_identifier(self)
            else:
                return visitor.visitChildren(self)




    def type_identifier(self):

        localctx = Swift3Parser.Type_identifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 482, self.RULE_type_identifier)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2535
            self.type_name()
            self.state = 2537
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,289,self._ctx)
            if la_ == 1:
                self.state = 2536
                self.generic_argument_clause()


            self.state = 2541
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,290,self._ctx)
            if la_ == 1:
                self.state = 2539
                self.match(Swift3Parser.DOT)
                self.state = 2540
                self.type_identifier()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Type_nameContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declaration_identifier(self):
            return self.getTypedRuleContext(Swift3Parser.Declaration_identifierContext,0)


        def getRuleIndex(self):
            return Swift3Parser.RULE_type_name

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterType_name" ):
                listener.enterType_name(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitType_name" ):
                listener.exitType_name(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitType_name" ):
                return visitor.visitType_name(self)
            else:
                return visitor.visitChildren(self)




    def type_name(self):

        localctx = Swift3Parser.Type_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 484, self.RULE_type_name)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2543
            self.declaration_identifier()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Tuple_typeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def tuple_type_element_list(self):
            return self.getTypedRuleContext(Swift3Parser.Tuple_type_element_listContext,0)


        def getRuleIndex(self):
            return Swift3Parser.RULE_tuple_type

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTuple_type" ):
                listener.enterTuple_type(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTuple_type" ):
                listener.exitTuple_type(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTuple_type" ):
                return visitor.visitTuple_type(self)
            else:
                return visitor.visitChildren(self)




    def tuple_type(self):

        localctx = Swift3Parser.Tuple_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 486, self.RULE_tuple_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2545
            self.match(Swift3Parser.LPAREN)
            self.state = 2547
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << Swift3Parser.T__0) | (1 << Swift3Parser.T__1) | (1 << Swift3Parser.T__2) | (1 << Swift3Parser.T__3) | (1 << Swift3Parser.T__6) | (1 << Swift3Parser.T__7) | (1 << Swift3Parser.T__8) | (1 << Swift3Parser.T__9) | (1 << Swift3Parser.T__10) | (1 << Swift3Parser.T__11) | (1 << Swift3Parser.T__12) | (1 << Swift3Parser.T__13) | (1 << Swift3Parser.T__14) | (1 << Swift3Parser.T__15) | (1 << Swift3Parser.T__16) | (1 << Swift3Parser.T__17) | (1 << Swift3Parser.T__18) | (1 << Swift3Parser.T__19) | (1 << Swift3Parser.T__20) | (1 << Swift3Parser.T__25) | (1 << Swift3Parser.T__26) | (1 << Swift3Parser.T__27) | (1 << Swift3Parser.T__29) | (1 << Swift3Parser.T__30) | (1 << Swift3Parser.T__32) | (1 << Swift3Parser.T__33) | (1 << Swift3Parser.T__34) | (1 << Swift3Parser.T__35) | (1 << Swift3Parser.T__36) | (1 << Swift3Parser.T__37) | (1 << Swift3Parser.T__38) | (1 << Swift3Parser.T__39) | (1 << Swift3Parser.T__40) | (1 << Swift3Parser.T__41) | (1 << Swift3Parser.T__42) | (1 << Swift3Parser.T__43) | (1 << Swift3Parser.T__44) | (1 << Swift3Parser.T__45) | (1 << Swift3Parser.T__46) | (1 << Swift3Parser.T__47) | (1 << Swift3Parser.T__48) | (1 << Swift3Parser.T__49) | (1 << Swift3Parser.T__50) | (1 << Swift3Parser.T__51) | (1 << Swift3Parser.T__52) | (1 << Swift3Parser.T__53) | (1 << Swift3Parser.T__54) | (1 << Swift3Parser.T__55) | (1 << Swift3Parser.T__56) | (1 << Swift3Parser.T__57) | (1 << Swift3Parser.T__58) | (1 << Swift3Parser.T__59) | (1 << Swift3Parser.T__60) | (1 << Swift3Parser.T__61) | (1 << Swift3Parser.T__62))) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & ((1 << (Swift3Parser.T__63 - 64)) | (1 << (Swift3Parser.T__64 - 64)) | (1 << (Swift3Parser.T__65 - 64)) | (1 << (Swift3Parser.T__66 - 64)) | (1 << (Swift3Parser.T__67 - 64)) | (1 << (Swift3Parser.T__68 - 64)) | (1 << (Swift3Parser.T__69 - 64)) | (1 << (Swift3Parser.T__70 - 64)) | (1 << (Swift3Parser.T__71 - 64)) | (1 << (Swift3Parser.T__72 - 64)) | (1 << (Swift3Parser.T__73 - 64)) | (1 << (Swift3Parser.T__74 - 64)) | (1 << (Swift3Parser.T__75 - 64)) | (1 << (Swift3Parser.T__76 - 64)) | (1 << (Swift3Parser.T__77 - 64)) | (1 << (Swift3Parser.T__78 - 64)) | (1 << (Swift3Parser.T__79 - 64)) | (1 << (Swift3Parser.T__80 - 64)) | (1 << (Swift3Parser.T__81 - 64)) | (1 << (Swift3Parser.T__82 - 64)) | (1 << (Swift3Parser.T__83 - 64)) | (1 << (Swift3Parser.T__86 - 64)) | (1 << (Swift3Parser.T__93 - 64)) | (1 << (Swift3Parser.T__94 - 64)) | (1 << (Swift3Parser.T__95 - 64)) | (1 << (Swift3Parser.T__96 - 64)) | (1 << (Swift3Parser.T__98 - 64)) | (1 << (Swift3Parser.T__100 - 64)) | (1 << (Swift3Parser.T__101 - 64)) | (1 << (Swift3Parser.T__102 - 64)) | (1 << (Swift3Parser.T__109 - 64)) | (1 << (Swift3Parser.T__110 - 64)) | (1 << (Swift3Parser.T__111 - 64)) | (1 << (Swift3Parser.T__112 - 64)) | (1 << (Swift3Parser.T__113 - 64)) | (1 << (Swift3Parser.T__115 - 64)) | (1 << (Swift3Parser.T__116 - 64)) | (1 << (Swift3Parser.T__117 - 64)) | (1 << (Swift3Parser.T__118 - 64)) | (1 << (Swift3Parser.T__119 - 64)) | (1 << (Swift3Parser.T__120 - 64)) | (1 << (Swift3Parser.T__121 - 64)) | (1 << (Swift3Parser.T__122 - 64)) | (1 << (Swift3Parser.T__123 - 64)) | (1 << (Swift3Parser.T__124 - 64)) | (1 << (Swift3Parser.T__125 - 64)) | (1 << (Swift3Parser.T__126 - 64)))) != 0) or ((((_la - 128)) & ~0x3f) == 0 and ((1 << (_la - 128)) & ((1 << (Swift3Parser.T__127 - 128)) | (1 << (Swift3Parser.T__128 - 128)) | (1 << (Swift3Parser.Identifier - 128)) | (1 << (Swift3Parser.LPAREN - 128)) | (1 << (Swift3Parser.LBRACK - 128)) | (1 << (Swift3Parser.AT - 128)))) != 0):
                self.state = 2546
                self.tuple_type_element_list()


            self.state = 2549
            self.match(Swift3Parser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Tuple_type_element_listContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def tuple_type_element(self):
            return self.getTypedRuleContext(Swift3Parser.Tuple_type_elementContext,0)


        def tuple_type_element_list(self):
            return self.getTypedRuleContext(Swift3Parser.Tuple_type_element_listContext,0)


        def getRuleIndex(self):
            return Swift3Parser.RULE_tuple_type_element_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTuple_type_element_list" ):
                listener.enterTuple_type_element_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTuple_type_element_list" ):
                listener.exitTuple_type_element_list(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTuple_type_element_list" ):
                return visitor.visitTuple_type_element_list(self)
            else:
                return visitor.visitChildren(self)




    def tuple_type_element_list(self):

        localctx = Swift3Parser.Tuple_type_element_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 488, self.RULE_tuple_type_element_list)
        try:
            self.state = 2556
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,292,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 2551
                self.tuple_type_element()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 2552
                self.tuple_type_element()
                self.state = 2553
                self.match(Swift3Parser.COMMA)
                self.state = 2554
                self.tuple_type_element_list()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Tuple_type_elementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def element_name(self):
            return self.getTypedRuleContext(Swift3Parser.Element_nameContext,0)


        def type_annotation(self):
            return self.getTypedRuleContext(Swift3Parser.Type_annotationContext,0)


        def type(self):
            return self.getTypedRuleContext(Swift3Parser.TypeContext,0)


        def getRuleIndex(self):
            return Swift3Parser.RULE_tuple_type_element

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTuple_type_element" ):
                listener.enterTuple_type_element(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTuple_type_element" ):
                listener.exitTuple_type_element(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTuple_type_element" ):
                return visitor.visitTuple_type_element(self)
            else:
                return visitor.visitChildren(self)




    def tuple_type_element(self):

        localctx = Swift3Parser.Tuple_type_elementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 490, self.RULE_tuple_type_element)
        try:
            self.state = 2562
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,293,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 2558
                self.element_name()
                self.state = 2559
                self.type_annotation()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 2561
                self.type(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Element_nameContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def label_identifier(self):
            return self.getTypedRuleContext(Swift3Parser.Label_identifierContext,0)


        def getRuleIndex(self):
            return Swift3Parser.RULE_element_name

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterElement_name" ):
                listener.enterElement_name(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitElement_name" ):
                listener.exitElement_name(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElement_name" ):
                return visitor.visitElement_name(self)
            else:
                return visitor.visitChildren(self)




    def element_name(self):

        localctx = Swift3Parser.Element_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 492, self.RULE_element_name)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2564
            self.label_identifier()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Function_typeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def function_type_argument_clause(self):
            return self.getTypedRuleContext(Swift3Parser.Function_type_argument_clauseContext,0)


        def arrow_operator(self):
            return self.getTypedRuleContext(Swift3Parser.Arrow_operatorContext,0)


        def type(self):
            return self.getTypedRuleContext(Swift3Parser.TypeContext,0)


        def attributes(self):
            return self.getTypedRuleContext(Swift3Parser.AttributesContext,0)


        def getRuleIndex(self):
            return Swift3Parser.RULE_function_type

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunction_type" ):
                listener.enterFunction_type(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunction_type" ):
                listener.exitFunction_type(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunction_type" ):
                return visitor.visitFunction_type(self)
            else:
                return visitor.visitChildren(self)




    def function_type(self):

        localctx = Swift3Parser.Function_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 494, self.RULE_function_type)
        self._la = 0 # Token type
        try:
            self.state = 2584
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,297,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 2567
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==Swift3Parser.AT:
                    self.state = 2566
                    self.attributes()


                self.state = 2569
                self.function_type_argument_clause()
                self.state = 2571
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,295,self._ctx)
                if la_ == 1:
                    self.state = 2570
                    self.match(Swift3Parser.T__43)


                self.state = 2573
                self.arrow_operator()
                self.state = 2574
                self.type(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 2577
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==Swift3Parser.AT:
                    self.state = 2576
                    self.attributes()


                self.state = 2579
                self.function_type_argument_clause()
                self.state = 2580
                self.match(Swift3Parser.T__44)
                self.state = 2581
                self.arrow_operator()
                self.state = 2582
                self.type(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Function_type_argument_clauseContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def function_type_argument_list(self):
            return self.getTypedRuleContext(Swift3Parser.Function_type_argument_listContext,0)


        def range_operator(self):
            return self.getTypedRuleContext(Swift3Parser.Range_operatorContext,0)


        def getRuleIndex(self):
            return Swift3Parser.RULE_function_type_argument_clause

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunction_type_argument_clause" ):
                listener.enterFunction_type_argument_clause(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunction_type_argument_clause" ):
                listener.exitFunction_type_argument_clause(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunction_type_argument_clause" ):
                return visitor.visitFunction_type_argument_clause(self)
            else:
                return visitor.visitChildren(self)




    def function_type_argument_clause(self):

        localctx = Swift3Parser.Function_type_argument_clauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 496, self.RULE_function_type_argument_clause)
        try:
            self.state = 2595
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,299,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 2586
                self.match(Swift3Parser.LPAREN)
                self.state = 2587
                self.match(Swift3Parser.RPAREN)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 2588
                self.match(Swift3Parser.LPAREN)
                self.state = 2589
                self.function_type_argument_list()
                self.state = 2591
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,298,self._ctx)
                if la_ == 1:
                    self.state = 2590
                    self.range_operator()


                self.state = 2593
                self.match(Swift3Parser.RPAREN)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Function_type_argument_listContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def function_type_argument(self):
            return self.getTypedRuleContext(Swift3Parser.Function_type_argumentContext,0)


        def function_type_argument_list(self):
            return self.getTypedRuleContext(Swift3Parser.Function_type_argument_listContext,0)


        def getRuleIndex(self):
            return Swift3Parser.RULE_function_type_argument_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunction_type_argument_list" ):
                listener.enterFunction_type_argument_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunction_type_argument_list" ):
                listener.exitFunction_type_argument_list(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunction_type_argument_list" ):
                return visitor.visitFunction_type_argument_list(self)
            else:
                return visitor.visitChildren(self)




    def function_type_argument_list(self):

        localctx = Swift3Parser.Function_type_argument_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 498, self.RULE_function_type_argument_list)
        try:
            self.state = 2602
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,300,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 2597
                self.function_type_argument()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 2598
                self.function_type_argument()
                self.state = 2599
                self.match(Swift3Parser.COMMA)
                self.state = 2600
                self.function_type_argument_list()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Function_type_argumentContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type(self):
            return self.getTypedRuleContext(Swift3Parser.TypeContext,0)


        def attributes(self):
            return self.getTypedRuleContext(Swift3Parser.AttributesContext,0)


        def argument_label(self):
            return self.getTypedRuleContext(Swift3Parser.Argument_labelContext,0)


        def type_annotation(self):
            return self.getTypedRuleContext(Swift3Parser.Type_annotationContext,0)


        def getRuleIndex(self):
            return Swift3Parser.RULE_function_type_argument

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunction_type_argument" ):
                listener.enterFunction_type_argument(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunction_type_argument" ):
                listener.exitFunction_type_argument(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunction_type_argument" ):
                return visitor.visitFunction_type_argument(self)
            else:
                return visitor.visitChildren(self)




    def function_type_argument(self):

        localctx = Swift3Parser.Function_type_argumentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 500, self.RULE_function_type_argument)
        self._la = 0 # Token type
        try:
            self.state = 2614
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,303,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 2605
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,301,self._ctx)
                if la_ == 1:
                    self.state = 2604
                    self.attributes()


                self.state = 2608
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==Swift3Parser.T__114:
                    self.state = 2607
                    self.match(Swift3Parser.T__114)


                self.state = 2610
                self.type(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 2611
                self.argument_label()
                self.state = 2612
                self.type_annotation()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Argument_labelContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def label_identifier(self):
            return self.getTypedRuleContext(Swift3Parser.Label_identifierContext,0)


        def getRuleIndex(self):
            return Swift3Parser.RULE_argument_label

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArgument_label" ):
                listener.enterArgument_label(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArgument_label" ):
                listener.exitArgument_label(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArgument_label" ):
                return visitor.visitArgument_label(self)
            else:
                return visitor.visitChildren(self)




    def argument_label(self):

        localctx = Swift3Parser.Argument_labelContext(self, self._ctx, self.state)
        self.enterRule(localctx, 502, self.RULE_argument_label)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2616
            self.label_identifier()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Array_typeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type(self):
            return self.getTypedRuleContext(Swift3Parser.TypeContext,0)


        def getRuleIndex(self):
            return Swift3Parser.RULE_array_type

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArray_type" ):
                listener.enterArray_type(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArray_type" ):
                listener.exitArray_type(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_type" ):
                return visitor.visitArray_type(self)
            else:
                return visitor.visitChildren(self)




    def array_type(self):

        localctx = Swift3Parser.Array_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 504, self.RULE_array_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2618
            self.match(Swift3Parser.LBRACK)
            self.state = 2619
            self.type(0)
            self.state = 2620
            self.match(Swift3Parser.RBRACK)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Dictionary_typeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Swift3Parser.TypeContext)
            else:
                return self.getTypedRuleContext(Swift3Parser.TypeContext,i)


        def getRuleIndex(self):
            return Swift3Parser.RULE_dictionary_type

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDictionary_type" ):
                listener.enterDictionary_type(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDictionary_type" ):
                listener.exitDictionary_type(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDictionary_type" ):
                return visitor.visitDictionary_type(self)
            else:
                return visitor.visitChildren(self)




    def dictionary_type(self):

        localctx = Swift3Parser.Dictionary_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 506, self.RULE_dictionary_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2622
            self.match(Swift3Parser.LBRACK)
            self.state = 2623
            self.type(0)
            self.state = 2624
            self.match(Swift3Parser.COLON)
            self.state = 2625
            self.type(0)
            self.state = 2626
            self.match(Swift3Parser.RBRACK)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Protocol_composition_typeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def protocol_identifier(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Swift3Parser.Protocol_identifierContext)
            else:
                return self.getTypedRuleContext(Swift3Parser.Protocol_identifierContext,i)


        def getRuleIndex(self):
            return Swift3Parser.RULE_protocol_composition_type

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProtocol_composition_type" ):
                listener.enterProtocol_composition_type(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProtocol_composition_type" ):
                listener.exitProtocol_composition_type(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProtocol_composition_type" ):
                return visitor.visitProtocol_composition_type(self)
            else:
                return visitor.visitChildren(self)




    def protocol_composition_type(self):

        localctx = Swift3Parser.Protocol_composition_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 508, self.RULE_protocol_composition_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2628
            self.protocol_identifier()
            self.state = 2631
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 2629
                    self.match(Swift3Parser.AND)
                    self.state = 2630
                    self.protocol_identifier()

                else:
                    raise NoViableAltException(self)
                self.state = 2633
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,304,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Protocol_identifierContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_identifier(self):
            return self.getTypedRuleContext(Swift3Parser.Type_identifierContext,0)


        def getRuleIndex(self):
            return Swift3Parser.RULE_protocol_identifier

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProtocol_identifier" ):
                listener.enterProtocol_identifier(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProtocol_identifier" ):
                listener.exitProtocol_identifier(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProtocol_identifier" ):
                return visitor.visitProtocol_identifier(self)
            else:
                return visitor.visitChildren(self)




    def protocol_identifier(self):

        localctx = Swift3Parser.Protocol_identifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 510, self.RULE_protocol_identifier)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2635
            self.type_identifier()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Type_inheritance_clauseContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def class_requirement(self):
            return self.getTypedRuleContext(Swift3Parser.Class_requirementContext,0)


        def type_inheritance_list(self):
            return self.getTypedRuleContext(Swift3Parser.Type_inheritance_listContext,0)


        def getRuleIndex(self):
            return Swift3Parser.RULE_type_inheritance_clause

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterType_inheritance_clause" ):
                listener.enterType_inheritance_clause(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitType_inheritance_clause" ):
                listener.exitType_inheritance_clause(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitType_inheritance_clause" ):
                return visitor.visitType_inheritance_clause(self)
            else:
                return visitor.visitChildren(self)




    def type_inheritance_clause(self):

        localctx = Swift3Parser.Type_inheritance_clauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 512, self.RULE_type_inheritance_clause)
        try:
            self.state = 2646
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,305,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 2637
                self.match(Swift3Parser.COLON)
                self.state = 2638
                self.class_requirement()
                self.state = 2639
                self.match(Swift3Parser.COMMA)
                self.state = 2640
                self.type_inheritance_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 2642
                self.match(Swift3Parser.COLON)
                self.state = 2643
                self.class_requirement()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 2644
                self.match(Swift3Parser.COLON)
                self.state = 2645
                self.type_inheritance_list()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Type_inheritance_listContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_identifier(self):
            return self.getTypedRuleContext(Swift3Parser.Type_identifierContext,0)


        def type_inheritance_list(self):
            return self.getTypedRuleContext(Swift3Parser.Type_inheritance_listContext,0)


        def getRuleIndex(self):
            return Swift3Parser.RULE_type_inheritance_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterType_inheritance_list" ):
                listener.enterType_inheritance_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitType_inheritance_list" ):
                listener.exitType_inheritance_list(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitType_inheritance_list" ):
                return visitor.visitType_inheritance_list(self)
            else:
                return visitor.visitChildren(self)




    def type_inheritance_list(self):

        localctx = Swift3Parser.Type_inheritance_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 514, self.RULE_type_inheritance_list)
        try:
            self.state = 2653
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,306,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 2648
                self.type_identifier()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 2649
                self.type_identifier()
                self.state = 2650
                self.match(Swift3Parser.COMMA)
                self.state = 2651
                self.type_inheritance_list()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Class_requirementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return Swift3Parser.RULE_class_requirement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterClass_requirement" ):
                listener.enterClass_requirement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitClass_requirement" ):
                listener.exitClass_requirement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClass_requirement" ):
                return visitor.visitClass_requirement(self)
            else:
                return visitor.visitChildren(self)




    def class_requirement(self):

        localctx = Swift3Parser.Class_requirementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 516, self.RULE_class_requirement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2655
            self.match(Swift3Parser.T__35)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Declaration_identifierContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Identifier(self):
            return self.getToken(Swift3Parser.Identifier, 0)

        def keyword_as_identifier_in_declarations(self):
            return self.getTypedRuleContext(Swift3Parser.Keyword_as_identifier_in_declarationsContext,0)


        def getRuleIndex(self):
            return Swift3Parser.RULE_declaration_identifier

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclaration_identifier" ):
                listener.enterDeclaration_identifier(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclaration_identifier" ):
                listener.exitDeclaration_identifier(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclaration_identifier" ):
                return visitor.visitDeclaration_identifier(self)
            else:
                return visitor.visitChildren(self)




    def declaration_identifier(self):

        localctx = Swift3Parser.Declaration_identifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 518, self.RULE_declaration_identifier)
        try:
            self.state = 2659
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [Swift3Parser.Identifier]:
                self.enterOuterAlt(localctx, 1)
                self.state = 2657
                self.match(Swift3Parser.Identifier)
                pass
            elif token in [Swift3Parser.T__25, Swift3Parser.T__26, Swift3Parser.T__27, Swift3Parser.T__29, Swift3Parser.T__30, Swift3Parser.T__39, Swift3Parser.T__40, Swift3Parser.T__41, Swift3Parser.T__42, Swift3Parser.T__45, Swift3Parser.T__46, Swift3Parser.T__52, Swift3Parser.T__54, Swift3Parser.T__55, Swift3Parser.T__57, Swift3Parser.T__58, Swift3Parser.T__59, Swift3Parser.T__60, Swift3Parser.T__61, Swift3Parser.T__62, Swift3Parser.T__63, Swift3Parser.T__64, Swift3Parser.T__65, Swift3Parser.T__66, Swift3Parser.T__67, Swift3Parser.T__68, Swift3Parser.T__69, Swift3Parser.T__71, Swift3Parser.T__72, Swift3Parser.T__73, Swift3Parser.T__74, Swift3Parser.T__79, Swift3Parser.T__80, Swift3Parser.T__81, Swift3Parser.T__93, Swift3Parser.T__94, Swift3Parser.T__95, Swift3Parser.T__96, Swift3Parser.T__98, Swift3Parser.T__109, Swift3Parser.T__110, Swift3Parser.T__111, Swift3Parser.T__112, Swift3Parser.T__115, Swift3Parser.T__116, Swift3Parser.T__117, Swift3Parser.T__118, Swift3Parser.T__119, Swift3Parser.T__120, Swift3Parser.T__121, Swift3Parser.T__122, Swift3Parser.T__123, Swift3Parser.T__124, Swift3Parser.T__125]:
                self.enterOuterAlt(localctx, 2)
                self.state = 2658
                self.keyword_as_identifier_in_declarations()
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

    class Label_identifierContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Identifier(self):
            return self.getToken(Swift3Parser.Identifier, 0)

        def keyword_as_identifier_in_labels(self):
            return self.getTypedRuleContext(Swift3Parser.Keyword_as_identifier_in_labelsContext,0)


        def getRuleIndex(self):
            return Swift3Parser.RULE_label_identifier

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLabel_identifier" ):
                listener.enterLabel_identifier(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLabel_identifier" ):
                listener.exitLabel_identifier(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLabel_identifier" ):
                return visitor.visitLabel_identifier(self)
            else:
                return visitor.visitChildren(self)




    def label_identifier(self):

        localctx = Swift3Parser.Label_identifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 520, self.RULE_label_identifier)
        try:
            self.state = 2663
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [Swift3Parser.Identifier]:
                self.enterOuterAlt(localctx, 1)
                self.state = 2661
                self.match(Swift3Parser.Identifier)
                pass
            elif token in [Swift3Parser.T__0, Swift3Parser.T__1, Swift3Parser.T__2, Swift3Parser.T__3, Swift3Parser.T__6, Swift3Parser.T__7, Swift3Parser.T__8, Swift3Parser.T__9, Swift3Parser.T__10, Swift3Parser.T__11, Swift3Parser.T__12, Swift3Parser.T__13, Swift3Parser.T__14, Swift3Parser.T__15, Swift3Parser.T__16, Swift3Parser.T__17, Swift3Parser.T__18, Swift3Parser.T__19, Swift3Parser.T__20, Swift3Parser.T__25, Swift3Parser.T__26, Swift3Parser.T__27, Swift3Parser.T__29, Swift3Parser.T__30, Swift3Parser.T__32, Swift3Parser.T__33, Swift3Parser.T__34, Swift3Parser.T__35, Swift3Parser.T__36, Swift3Parser.T__37, Swift3Parser.T__38, Swift3Parser.T__39, Swift3Parser.T__40, Swift3Parser.T__41, Swift3Parser.T__42, Swift3Parser.T__43, Swift3Parser.T__44, Swift3Parser.T__45, Swift3Parser.T__46, Swift3Parser.T__47, Swift3Parser.T__48, Swift3Parser.T__49, Swift3Parser.T__50, Swift3Parser.T__51, Swift3Parser.T__52, Swift3Parser.T__53, Swift3Parser.T__54, Swift3Parser.T__55, Swift3Parser.T__56, Swift3Parser.T__57, Swift3Parser.T__58, Swift3Parser.T__59, Swift3Parser.T__60, Swift3Parser.T__61, Swift3Parser.T__62, Swift3Parser.T__63, Swift3Parser.T__64, Swift3Parser.T__65, Swift3Parser.T__66, Swift3Parser.T__67, Swift3Parser.T__68, Swift3Parser.T__69, Swift3Parser.T__70, Swift3Parser.T__71, Swift3Parser.T__72, Swift3Parser.T__73, Swift3Parser.T__74, Swift3Parser.T__75, Swift3Parser.T__76, Swift3Parser.T__77, Swift3Parser.T__78, Swift3Parser.T__79, Swift3Parser.T__80, Swift3Parser.T__81, Swift3Parser.T__82, Swift3Parser.T__83, Swift3Parser.T__86, Swift3Parser.T__93, Swift3Parser.T__94, Swift3Parser.T__95, Swift3Parser.T__96, Swift3Parser.T__98, Swift3Parser.T__100, Swift3Parser.T__101, Swift3Parser.T__102, Swift3Parser.T__109, Swift3Parser.T__110, Swift3Parser.T__111, Swift3Parser.T__112, Swift3Parser.T__113, Swift3Parser.T__115, Swift3Parser.T__116, Swift3Parser.T__117, Swift3Parser.T__118, Swift3Parser.T__119, Swift3Parser.T__120, Swift3Parser.T__121, Swift3Parser.T__122, Swift3Parser.T__123, Swift3Parser.T__124, Swift3Parser.T__125, Swift3Parser.T__126, Swift3Parser.T__127, Swift3Parser.T__128]:
                self.enterOuterAlt(localctx, 2)
                self.state = 2662
                self.keyword_as_identifier_in_labels()
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

    class Keyword_as_identifier_in_declarationsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return Swift3Parser.RULE_keyword_as_identifier_in_declarations

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterKeyword_as_identifier_in_declarations" ):
                listener.enterKeyword_as_identifier_in_declarations(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitKeyword_as_identifier_in_declarations" ):
                listener.exitKeyword_as_identifier_in_declarations(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitKeyword_as_identifier_in_declarations" ):
                return visitor.visitKeyword_as_identifier_in_declarations(self)
            else:
                return visitor.visitChildren(self)




    def keyword_as_identifier_in_declarations(self):

        localctx = Swift3Parser.Keyword_as_identifier_in_declarationsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 522, self.RULE_keyword_as_identifier_in_declarations)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2665
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << Swift3Parser.T__25) | (1 << Swift3Parser.T__26) | (1 << Swift3Parser.T__27) | (1 << Swift3Parser.T__29) | (1 << Swift3Parser.T__30) | (1 << Swift3Parser.T__39) | (1 << Swift3Parser.T__40) | (1 << Swift3Parser.T__41) | (1 << Swift3Parser.T__42) | (1 << Swift3Parser.T__45) | (1 << Swift3Parser.T__46) | (1 << Swift3Parser.T__52) | (1 << Swift3Parser.T__54) | (1 << Swift3Parser.T__55) | (1 << Swift3Parser.T__57) | (1 << Swift3Parser.T__58) | (1 << Swift3Parser.T__59) | (1 << Swift3Parser.T__60) | (1 << Swift3Parser.T__61) | (1 << Swift3Parser.T__62))) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & ((1 << (Swift3Parser.T__63 - 64)) | (1 << (Swift3Parser.T__64 - 64)) | (1 << (Swift3Parser.T__65 - 64)) | (1 << (Swift3Parser.T__66 - 64)) | (1 << (Swift3Parser.T__67 - 64)) | (1 << (Swift3Parser.T__68 - 64)) | (1 << (Swift3Parser.T__69 - 64)) | (1 << (Swift3Parser.T__71 - 64)) | (1 << (Swift3Parser.T__72 - 64)) | (1 << (Swift3Parser.T__73 - 64)) | (1 << (Swift3Parser.T__74 - 64)) | (1 << (Swift3Parser.T__79 - 64)) | (1 << (Swift3Parser.T__80 - 64)) | (1 << (Swift3Parser.T__81 - 64)) | (1 << (Swift3Parser.T__93 - 64)) | (1 << (Swift3Parser.T__94 - 64)) | (1 << (Swift3Parser.T__95 - 64)) | (1 << (Swift3Parser.T__96 - 64)) | (1 << (Swift3Parser.T__98 - 64)) | (1 << (Swift3Parser.T__109 - 64)) | (1 << (Swift3Parser.T__110 - 64)) | (1 << (Swift3Parser.T__111 - 64)) | (1 << (Swift3Parser.T__112 - 64)) | (1 << (Swift3Parser.T__115 - 64)) | (1 << (Swift3Parser.T__116 - 64)) | (1 << (Swift3Parser.T__117 - 64)) | (1 << (Swift3Parser.T__118 - 64)) | (1 << (Swift3Parser.T__119 - 64)) | (1 << (Swift3Parser.T__120 - 64)) | (1 << (Swift3Parser.T__121 - 64)) | (1 << (Swift3Parser.T__122 - 64)) | (1 << (Swift3Parser.T__123 - 64)) | (1 << (Swift3Parser.T__124 - 64)) | (1 << (Swift3Parser.T__125 - 64)))) != 0)):
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

    class Keyword_as_identifier_in_labelsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return Swift3Parser.RULE_keyword_as_identifier_in_labels

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterKeyword_as_identifier_in_labels" ):
                listener.enterKeyword_as_identifier_in_labels(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitKeyword_as_identifier_in_labels" ):
                listener.exitKeyword_as_identifier_in_labels(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitKeyword_as_identifier_in_labels" ):
                return visitor.visitKeyword_as_identifier_in_labels(self)
            else:
                return visitor.visitChildren(self)




    def keyword_as_identifier_in_labels(self):

        localctx = Swift3Parser.Keyword_as_identifier_in_labelsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 524, self.RULE_keyword_as_identifier_in_labels)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2667
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << Swift3Parser.T__0) | (1 << Swift3Parser.T__1) | (1 << Swift3Parser.T__2) | (1 << Swift3Parser.T__3) | (1 << Swift3Parser.T__6) | (1 << Swift3Parser.T__7) | (1 << Swift3Parser.T__8) | (1 << Swift3Parser.T__9) | (1 << Swift3Parser.T__10) | (1 << Swift3Parser.T__11) | (1 << Swift3Parser.T__12) | (1 << Swift3Parser.T__13) | (1 << Swift3Parser.T__14) | (1 << Swift3Parser.T__15) | (1 << Swift3Parser.T__16) | (1 << Swift3Parser.T__17) | (1 << Swift3Parser.T__18) | (1 << Swift3Parser.T__19) | (1 << Swift3Parser.T__20) | (1 << Swift3Parser.T__25) | (1 << Swift3Parser.T__26) | (1 << Swift3Parser.T__27) | (1 << Swift3Parser.T__29) | (1 << Swift3Parser.T__30) | (1 << Swift3Parser.T__32) | (1 << Swift3Parser.T__33) | (1 << Swift3Parser.T__34) | (1 << Swift3Parser.T__35) | (1 << Swift3Parser.T__36) | (1 << Swift3Parser.T__37) | (1 << Swift3Parser.T__38) | (1 << Swift3Parser.T__39) | (1 << Swift3Parser.T__40) | (1 << Swift3Parser.T__41) | (1 << Swift3Parser.T__42) | (1 << Swift3Parser.T__43) | (1 << Swift3Parser.T__44) | (1 << Swift3Parser.T__45) | (1 << Swift3Parser.T__46) | (1 << Swift3Parser.T__47) | (1 << Swift3Parser.T__48) | (1 << Swift3Parser.T__49) | (1 << Swift3Parser.T__50) | (1 << Swift3Parser.T__51) | (1 << Swift3Parser.T__52) | (1 << Swift3Parser.T__53) | (1 << Swift3Parser.T__54) | (1 << Swift3Parser.T__55) | (1 << Swift3Parser.T__56) | (1 << Swift3Parser.T__57) | (1 << Swift3Parser.T__58) | (1 << Swift3Parser.T__59) | (1 << Swift3Parser.T__60) | (1 << Swift3Parser.T__61) | (1 << Swift3Parser.T__62))) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & ((1 << (Swift3Parser.T__63 - 64)) | (1 << (Swift3Parser.T__64 - 64)) | (1 << (Swift3Parser.T__65 - 64)) | (1 << (Swift3Parser.T__66 - 64)) | (1 << (Swift3Parser.T__67 - 64)) | (1 << (Swift3Parser.T__68 - 64)) | (1 << (Swift3Parser.T__69 - 64)) | (1 << (Swift3Parser.T__70 - 64)) | (1 << (Swift3Parser.T__71 - 64)) | (1 << (Swift3Parser.T__72 - 64)) | (1 << (Swift3Parser.T__73 - 64)) | (1 << (Swift3Parser.T__74 - 64)) | (1 << (Swift3Parser.T__75 - 64)) | (1 << (Swift3Parser.T__76 - 64)) | (1 << (Swift3Parser.T__77 - 64)) | (1 << (Swift3Parser.T__78 - 64)) | (1 << (Swift3Parser.T__79 - 64)) | (1 << (Swift3Parser.T__80 - 64)) | (1 << (Swift3Parser.T__81 - 64)) | (1 << (Swift3Parser.T__82 - 64)) | (1 << (Swift3Parser.T__83 - 64)) | (1 << (Swift3Parser.T__86 - 64)) | (1 << (Swift3Parser.T__93 - 64)) | (1 << (Swift3Parser.T__94 - 64)) | (1 << (Swift3Parser.T__95 - 64)) | (1 << (Swift3Parser.T__96 - 64)) | (1 << (Swift3Parser.T__98 - 64)) | (1 << (Swift3Parser.T__100 - 64)) | (1 << (Swift3Parser.T__101 - 64)) | (1 << (Swift3Parser.T__102 - 64)) | (1 << (Swift3Parser.T__109 - 64)) | (1 << (Swift3Parser.T__110 - 64)) | (1 << (Swift3Parser.T__111 - 64)) | (1 << (Swift3Parser.T__112 - 64)) | (1 << (Swift3Parser.T__113 - 64)) | (1 << (Swift3Parser.T__115 - 64)) | (1 << (Swift3Parser.T__116 - 64)) | (1 << (Swift3Parser.T__117 - 64)) | (1 << (Swift3Parser.T__118 - 64)) | (1 << (Swift3Parser.T__119 - 64)) | (1 << (Swift3Parser.T__120 - 64)) | (1 << (Swift3Parser.T__121 - 64)) | (1 << (Swift3Parser.T__122 - 64)) | (1 << (Swift3Parser.T__123 - 64)) | (1 << (Swift3Parser.T__124 - 64)) | (1 << (Swift3Parser.T__125 - 64)) | (1 << (Swift3Parser.T__126 - 64)))) != 0) or _la==Swift3Parser.T__127 or _la==Swift3Parser.T__128):
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

    class Assignment_operatorContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return Swift3Parser.RULE_assignment_operator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignment_operator" ):
                listener.enterAssignment_operator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignment_operator" ):
                listener.exitAssignment_operator(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignment_operator" ):
                return visitor.visitAssignment_operator(self)
            else:
                return visitor.visitChildren(self)




    def assignment_operator(self):

        localctx = Swift3Parser.Assignment_operatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 526, self.RULE_assignment_operator)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2669
            if not SwiftSupport.isBinaryOp(_input):
                from antlr4.error.Errors import FailedPredicateException
                raise FailedPredicateException(self, "SwiftSupport.isBinaryOp(_input)")
            self.state = 2670
            self.match(Swift3Parser.EQUAL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Negate_prefix_operatorContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return Swift3Parser.RULE_negate_prefix_operator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNegate_prefix_operator" ):
                listener.enterNegate_prefix_operator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNegate_prefix_operator" ):
                listener.exitNegate_prefix_operator(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNegate_prefix_operator" ):
                return visitor.visitNegate_prefix_operator(self)
            else:
                return visitor.visitChildren(self)




    def negate_prefix_operator(self):

        localctx = Swift3Parser.Negate_prefix_operatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 528, self.RULE_negate_prefix_operator)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2672
            if not SwiftSupport.isPrefixOp(_input):
                from antlr4.error.Errors import FailedPredicateException
                raise FailedPredicateException(self, "SwiftSupport.isPrefixOp(_input)")
            self.state = 2673
            self.match(Swift3Parser.SUB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Compilation_condition_ANDContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return Swift3Parser.RULE_compilation_condition_AND

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCompilation_condition_AND" ):
                listener.enterCompilation_condition_AND(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCompilation_condition_AND" ):
                listener.exitCompilation_condition_AND(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCompilation_condition_AND" ):
                return visitor.visitCompilation_condition_AND(self)
            else:
                return visitor.visitChildren(self)




    def compilation_condition_AND(self):

        localctx = Swift3Parser.Compilation_condition_ANDContext(self, self._ctx, self.state)
        self.enterRule(localctx, 530, self.RULE_compilation_condition_AND)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2675
            if not SwiftSupport.isOperator(_input,"&&"):
                from antlr4.error.Errors import FailedPredicateException
                raise FailedPredicateException(self, "SwiftSupport.isOperator(_input,\"&&\")")
            self.state = 2676
            self.match(Swift3Parser.AND)
            self.state = 2677
            self.match(Swift3Parser.AND)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Compilation_condition_ORContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return Swift3Parser.RULE_compilation_condition_OR

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCompilation_condition_OR" ):
                listener.enterCompilation_condition_OR(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCompilation_condition_OR" ):
                listener.exitCompilation_condition_OR(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCompilation_condition_OR" ):
                return visitor.visitCompilation_condition_OR(self)
            else:
                return visitor.visitChildren(self)




    def compilation_condition_OR(self):

        localctx = Swift3Parser.Compilation_condition_ORContext(self, self._ctx, self.state)
        self.enterRule(localctx, 532, self.RULE_compilation_condition_OR)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2679
            if not SwiftSupport.isOperator(_input,"||"):
                from antlr4.error.Errors import FailedPredicateException
                raise FailedPredicateException(self, "SwiftSupport.isOperator(_input,\"||\")")
            self.state = 2680
            self.match(Swift3Parser.OR)
            self.state = 2681
            self.match(Swift3Parser.OR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Compilation_condition_GEContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return Swift3Parser.RULE_compilation_condition_GE

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCompilation_condition_GE" ):
                listener.enterCompilation_condition_GE(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCompilation_condition_GE" ):
                listener.exitCompilation_condition_GE(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCompilation_condition_GE" ):
                return visitor.visitCompilation_condition_GE(self)
            else:
                return visitor.visitChildren(self)




    def compilation_condition_GE(self):

        localctx = Swift3Parser.Compilation_condition_GEContext(self, self._ctx, self.state)
        self.enterRule(localctx, 534, self.RULE_compilation_condition_GE)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2683
            if not SwiftSupport.isOperator(_input,">="):
                from antlr4.error.Errors import FailedPredicateException
                raise FailedPredicateException(self, "SwiftSupport.isOperator(_input,\">=\")")
            self.state = 2684
            self.match(Swift3Parser.GT)
            self.state = 2685
            self.match(Swift3Parser.EQUAL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Arrow_operatorContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return Swift3Parser.RULE_arrow_operator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArrow_operator" ):
                listener.enterArrow_operator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArrow_operator" ):
                listener.exitArrow_operator(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrow_operator" ):
                return visitor.visitArrow_operator(self)
            else:
                return visitor.visitChildren(self)




    def arrow_operator(self):

        localctx = Swift3Parser.Arrow_operatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 536, self.RULE_arrow_operator)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2687
            if not SwiftSupport.isOperator(_input,"->"):
                from antlr4.error.Errors import FailedPredicateException
                raise FailedPredicateException(self, "SwiftSupport.isOperator(_input,\"->\")")
            self.state = 2688
            self.match(Swift3Parser.SUB)
            self.state = 2689
            self.match(Swift3Parser.GT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Range_operatorContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return Swift3Parser.RULE_range_operator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRange_operator" ):
                listener.enterRange_operator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRange_operator" ):
                listener.exitRange_operator(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRange_operator" ):
                return visitor.visitRange_operator(self)
            else:
                return visitor.visitChildren(self)




    def range_operator(self):

        localctx = Swift3Parser.Range_operatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 538, self.RULE_range_operator)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2691
            if not SwiftSupport.isOperator(_input,"..."):
                from antlr4.error.Errors import FailedPredicateException
                raise FailedPredicateException(self, "SwiftSupport.isOperator(_input,\"...\")")
            self.state = 2692
            self.match(Swift3Parser.DOT)
            self.state = 2693
            self.match(Swift3Parser.DOT)
            self.state = 2694
            self.match(Swift3Parser.DOT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Same_type_equalsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return Swift3Parser.RULE_same_type_equals

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSame_type_equals" ):
                listener.enterSame_type_equals(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSame_type_equals" ):
                listener.exitSame_type_equals(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSame_type_equals" ):
                return visitor.visitSame_type_equals(self)
            else:
                return visitor.visitChildren(self)




    def same_type_equals(self):

        localctx = Swift3Parser.Same_type_equalsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 540, self.RULE_same_type_equals)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2696
            if not SwiftSupport.isOperator(_input,"=="):
                from antlr4.error.Errors import FailedPredicateException
                raise FailedPredicateException(self, "SwiftSupport.isOperator(_input,\"==\")")
            self.state = 2697
            self.match(Swift3Parser.EQUAL)
            self.state = 2698
            self.match(Swift3Parser.EQUAL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Binary_operatorContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def operator(self):
            return self.getTypedRuleContext(Swift3Parser.OperatorContext,0)


        def getRuleIndex(self):
            return Swift3Parser.RULE_binary_operator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBinary_operator" ):
                listener.enterBinary_operator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBinary_operator" ):
                listener.exitBinary_operator(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBinary_operator" ):
                return visitor.visitBinary_operator(self)
            else:
                return visitor.visitChildren(self)




    def binary_operator(self):

        localctx = Swift3Parser.Binary_operatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 542, self.RULE_binary_operator)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2700
            if not SwiftSupport.isBinaryOp(_input):
                from antlr4.error.Errors import FailedPredicateException
                raise FailedPredicateException(self, "SwiftSupport.isBinaryOp(_input)")
            self.state = 2701
            self.operator()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Prefix_operatorContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def operator(self):
            return self.getTypedRuleContext(Swift3Parser.OperatorContext,0)


        def getRuleIndex(self):
            return Swift3Parser.RULE_prefix_operator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrefix_operator" ):
                listener.enterPrefix_operator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrefix_operator" ):
                listener.exitPrefix_operator(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrefix_operator" ):
                return visitor.visitPrefix_operator(self)
            else:
                return visitor.visitChildren(self)




    def prefix_operator(self):

        localctx = Swift3Parser.Prefix_operatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 544, self.RULE_prefix_operator)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2703
            if not SwiftSupport.isPrefixOp(_input):
                from antlr4.error.Errors import FailedPredicateException
                raise FailedPredicateException(self, "SwiftSupport.isPrefixOp(_input)")
            self.state = 2704
            self.operator()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Postfix_operatorContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def operator(self):
            return self.getTypedRuleContext(Swift3Parser.OperatorContext,0)


        def getRuleIndex(self):
            return Swift3Parser.RULE_postfix_operator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPostfix_operator" ):
                listener.enterPostfix_operator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPostfix_operator" ):
                listener.exitPostfix_operator(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPostfix_operator" ):
                return visitor.visitPostfix_operator(self)
            else:
                return visitor.visitChildren(self)




    def postfix_operator(self):

        localctx = Swift3Parser.Postfix_operatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 546, self.RULE_postfix_operator)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2706
            if not SwiftSupport.isPostfixOp(_input):
                from antlr4.error.Errors import FailedPredicateException
                raise FailedPredicateException(self, "SwiftSupport.isPostfixOp(_input)")
            self.state = 2707
            self.operator()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class OperatorContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def operator_head(self):
            return self.getTypedRuleContext(Swift3Parser.Operator_headContext,0)


        def operator_character(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Swift3Parser.Operator_characterContext)
            else:
                return self.getTypedRuleContext(Swift3Parser.Operator_characterContext,i)


        def dot_operator_head(self):
            return self.getTypedRuleContext(Swift3Parser.Dot_operator_headContext,0)


        def dot_operator_character(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Swift3Parser.Dot_operator_characterContext)
            else:
                return self.getTypedRuleContext(Swift3Parser.Dot_operator_characterContext,i)


        def getRuleIndex(self):
            return Swift3Parser.RULE_operator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOperator" ):
                listener.enterOperator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOperator" ):
                listener.exitOperator(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOperator" ):
                return visitor.visitOperator(self)
            else:
                return visitor.visitChildren(self)




    def operator(self):

        localctx = Swift3Parser.OperatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 548, self.RULE_operator)
        try:
            self.state = 2725
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [Swift3Parser.LT, Swift3Parser.GT, Swift3Parser.BANG, Swift3Parser.QUESTION, Swift3Parser.AND, Swift3Parser.SUB, Swift3Parser.EQUAL, Swift3Parser.OR, Swift3Parser.DIV, Swift3Parser.ADD, Swift3Parser.MUL, Swift3Parser.MOD, Swift3Parser.CARET, Swift3Parser.TILDE, Swift3Parser.Operator_head_other]:
                self.enterOuterAlt(localctx, 1)
                self.state = 2709
                self.operator_head()
                self.state = 2714
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,309,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 2710
                        if not _input.get(_input.index()-1).getType()!=WS:
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "_input.get(_input.index()-1).getType()!=WS")
                        self.state = 2711
                        self.operator_character()
                    self.state = 2716
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,309,self._ctx)

                pass
            elif token in [Swift3Parser.DOT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 2717
                self.dot_operator_head()
                self.state = 2722
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,310,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 2718
                        if not _input.get(_input.index()-1).getType()!=WS:
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "_input.get(_input.index()-1).getType()!=WS")
                        self.state = 2719
                        self.dot_operator_character()
                    self.state = 2724
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,310,self._ctx)

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

    class Operator_characterContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def operator_head(self):
            return self.getTypedRuleContext(Swift3Parser.Operator_headContext,0)


        def Operator_following_character(self):
            return self.getToken(Swift3Parser.Operator_following_character, 0)

        def getRuleIndex(self):
            return Swift3Parser.RULE_operator_character

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOperator_character" ):
                listener.enterOperator_character(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOperator_character" ):
                listener.exitOperator_character(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOperator_character" ):
                return visitor.visitOperator_character(self)
            else:
                return visitor.visitChildren(self)




    def operator_character(self):

        localctx = Swift3Parser.Operator_characterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 550, self.RULE_operator_character)
        try:
            self.state = 2729
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [Swift3Parser.LT, Swift3Parser.GT, Swift3Parser.BANG, Swift3Parser.QUESTION, Swift3Parser.AND, Swift3Parser.SUB, Swift3Parser.EQUAL, Swift3Parser.OR, Swift3Parser.DIV, Swift3Parser.ADD, Swift3Parser.MUL, Swift3Parser.MOD, Swift3Parser.CARET, Swift3Parser.TILDE, Swift3Parser.Operator_head_other]:
                self.enterOuterAlt(localctx, 1)
                self.state = 2727
                self.operator_head()
                pass
            elif token in [Swift3Parser.Operator_following_character]:
                self.enterOuterAlt(localctx, 2)
                self.state = 2728
                self.match(Swift3Parser.Operator_following_character)
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

    class Operator_headContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Operator_head_other(self):
            return self.getToken(Swift3Parser.Operator_head_other, 0)

        def getRuleIndex(self):
            return Swift3Parser.RULE_operator_head

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOperator_head" ):
                listener.enterOperator_head(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOperator_head" ):
                listener.exitOperator_head(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOperator_head" ):
                return visitor.visitOperator_head(self)
            else:
                return visitor.visitChildren(self)




    def operator_head(self):

        localctx = Swift3Parser.Operator_headContext(self, self._ctx, self.state)
        self.enterRule(localctx, 552, self.RULE_operator_head)
        self._la = 0 # Token type
        try:
            self.state = 2733
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [Swift3Parser.LT, Swift3Parser.GT, Swift3Parser.BANG, Swift3Parser.QUESTION, Swift3Parser.AND, Swift3Parser.SUB, Swift3Parser.EQUAL, Swift3Parser.OR, Swift3Parser.DIV, Swift3Parser.ADD, Swift3Parser.MUL, Swift3Parser.MOD, Swift3Parser.CARET, Swift3Parser.TILDE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 2731
                _la = self._input.LA(1)
                if not(((((_la - 142)) & ~0x3f) == 0 and ((1 << (_la - 142)) & ((1 << (Swift3Parser.LT - 142)) | (1 << (Swift3Parser.GT - 142)) | (1 << (Swift3Parser.BANG - 142)) | (1 << (Swift3Parser.QUESTION - 142)) | (1 << (Swift3Parser.AND - 142)) | (1 << (Swift3Parser.SUB - 142)) | (1 << (Swift3Parser.EQUAL - 142)) | (1 << (Swift3Parser.OR - 142)) | (1 << (Swift3Parser.DIV - 142)) | (1 << (Swift3Parser.ADD - 142)) | (1 << (Swift3Parser.MUL - 142)) | (1 << (Swift3Parser.MOD - 142)) | (1 << (Swift3Parser.CARET - 142)) | (1 << (Swift3Parser.TILDE - 142)))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                pass
            elif token in [Swift3Parser.Operator_head_other]:
                self.enterOuterAlt(localctx, 2)
                self.state = 2732
                self.match(Swift3Parser.Operator_head_other)
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

    class Dot_operator_headContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return Swift3Parser.RULE_dot_operator_head

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDot_operator_head" ):
                listener.enterDot_operator_head(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDot_operator_head" ):
                listener.exitDot_operator_head(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDot_operator_head" ):
                return visitor.visitDot_operator_head(self)
            else:
                return visitor.visitChildren(self)




    def dot_operator_head(self):

        localctx = Swift3Parser.Dot_operator_headContext(self, self._ctx, self.state)
        self.enterRule(localctx, 554, self.RULE_dot_operator_head)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2735
            self.match(Swift3Parser.DOT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Dot_operator_characterContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def operator_character(self):
            return self.getTypedRuleContext(Swift3Parser.Operator_characterContext,0)


        def getRuleIndex(self):
            return Swift3Parser.RULE_dot_operator_character

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDot_operator_character" ):
                listener.enterDot_operator_character(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDot_operator_character" ):
                listener.exitDot_operator_character(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDot_operator_character" ):
                return visitor.visitDot_operator_character(self)
            else:
                return visitor.visitChildren(self)




    def dot_operator_character(self):

        localctx = Swift3Parser.Dot_operator_characterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 556, self.RULE_dot_operator_character)
        try:
            self.state = 2739
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [Swift3Parser.DOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 2737
                self.match(Swift3Parser.DOT)
                pass
            elif token in [Swift3Parser.LT, Swift3Parser.GT, Swift3Parser.BANG, Swift3Parser.QUESTION, Swift3Parser.AND, Swift3Parser.SUB, Swift3Parser.EQUAL, Swift3Parser.OR, Swift3Parser.DIV, Swift3Parser.ADD, Swift3Parser.MUL, Swift3Parser.MOD, Swift3Parser.CARET, Swift3Parser.TILDE, Swift3Parser.Operator_head_other, Swift3Parser.Operator_following_character]:
                self.enterOuterAlt(localctx, 2)
                self.state = 2738
                self.operator_character()
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

    class LiteralContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def numeric_literal(self):
            return self.getTypedRuleContext(Swift3Parser.Numeric_literalContext,0)


        def string_literal(self):
            return self.getTypedRuleContext(Swift3Parser.String_literalContext,0)


        def boolean_literal(self):
            return self.getTypedRuleContext(Swift3Parser.Boolean_literalContext,0)


        def nil_literal(self):
            return self.getTypedRuleContext(Swift3Parser.Nil_literalContext,0)


        def getRuleIndex(self):
            return Swift3Parser.RULE_literal

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLiteral" ):
                listener.enterLiteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLiteral" ):
                listener.exitLiteral(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiteral" ):
                return visitor.visitLiteral(self)
            else:
                return visitor.visitChildren(self)




    def literal(self):

        localctx = Swift3Parser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 558, self.RULE_literal)
        try:
            self.state = 2745
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,315,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 2741
                self.numeric_literal()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 2742
                self.string_literal()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 2743
                self.boolean_literal()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 2744
                self.nil_literal()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Numeric_literalContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def integer_literal(self):
            return self.getTypedRuleContext(Swift3Parser.Integer_literalContext,0)


        def negate_prefix_operator(self):
            return self.getTypedRuleContext(Swift3Parser.Negate_prefix_operatorContext,0)


        def Floating_point_literal(self):
            return self.getToken(Swift3Parser.Floating_point_literal, 0)

        def getRuleIndex(self):
            return Swift3Parser.RULE_numeric_literal

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNumeric_literal" ):
                listener.enterNumeric_literal(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNumeric_literal" ):
                listener.exitNumeric_literal(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNumeric_literal" ):
                return visitor.visitNumeric_literal(self)
            else:
                return visitor.visitChildren(self)




    def numeric_literal(self):

        localctx = Swift3Parser.Numeric_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 560, self.RULE_numeric_literal)
        try:
            self.state = 2755
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,318,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 2748
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,316,self._ctx)
                if la_ == 1:
                    self.state = 2747
                    self.negate_prefix_operator()


                self.state = 2750
                self.integer_literal()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 2752
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,317,self._ctx)
                if la_ == 1:
                    self.state = 2751
                    self.negate_prefix_operator()


                self.state = 2754
                self.match(Swift3Parser.Floating_point_literal)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Boolean_literalContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return Swift3Parser.RULE_boolean_literal

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBoolean_literal" ):
                listener.enterBoolean_literal(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBoolean_literal" ):
                listener.exitBoolean_literal(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBoolean_literal" ):
                return visitor.visitBoolean_literal(self)
            else:
                return visitor.visitChildren(self)




    def boolean_literal(self):

        localctx = Swift3Parser.Boolean_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 562, self.RULE_boolean_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2757
            _la = self._input.LA(1)
            if not(_la==Swift3Parser.T__126 or _la==Swift3Parser.T__128):
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

    class Nil_literalContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return Swift3Parser.RULE_nil_literal

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNil_literal" ):
                listener.enterNil_literal(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNil_literal" ):
                listener.exitNil_literal(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNil_literal" ):
                return visitor.visitNil_literal(self)
            else:
                return visitor.visitChildren(self)




    def nil_literal(self):

        localctx = Swift3Parser.Nil_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 564, self.RULE_nil_literal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2759
            self.match(Swift3Parser.T__127)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Integer_literalContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Binary_literal(self):
            return self.getToken(Swift3Parser.Binary_literal, 0)

        def Octal_literal(self):
            return self.getToken(Swift3Parser.Octal_literal, 0)

        def Decimal_literal(self):
            return self.getToken(Swift3Parser.Decimal_literal, 0)

        def Pure_decimal_digits(self):
            return self.getToken(Swift3Parser.Pure_decimal_digits, 0)

        def Hexadecimal_literal(self):
            return self.getToken(Swift3Parser.Hexadecimal_literal, 0)

        def getRuleIndex(self):
            return Swift3Parser.RULE_integer_literal

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInteger_literal" ):
                listener.enterInteger_literal(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInteger_literal" ):
                listener.exitInteger_literal(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInteger_literal" ):
                return visitor.visitInteger_literal(self)
            else:
                return visitor.visitChildren(self)




    def integer_literal(self):

        localctx = Swift3Parser.Integer_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 566, self.RULE_integer_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2761
            _la = self._input.LA(1)
            if not(((((_la - 161)) & ~0x3f) == 0 and ((1 << (_la - 161)) & ((1 << (Swift3Parser.Binary_literal - 161)) | (1 << (Swift3Parser.Octal_literal - 161)) | (1 << (Swift3Parser.Decimal_literal - 161)) | (1 << (Swift3Parser.Pure_decimal_digits - 161)) | (1 << (Swift3Parser.Hexadecimal_literal - 161)))) != 0)):
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

    class String_literalContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Static_string_literal(self):
            return self.getToken(Swift3Parser.Static_string_literal, 0)

        def Interpolated_string_literal(self):
            return self.getToken(Swift3Parser.Interpolated_string_literal, 0)

        def getRuleIndex(self):
            return Swift3Parser.RULE_string_literal

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterString_literal" ):
                listener.enterString_literal(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitString_literal" ):
                listener.exitString_literal(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitString_literal" ):
                return visitor.visitString_literal(self)
            else:
                return visitor.visitChildren(self)




    def string_literal(self):

        localctx = Swift3Parser.String_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 568, self.RULE_string_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2763
            _la = self._input.LA(1)
            if not(_la==Swift3Parser.Static_string_literal or _la==Swift3Parser.Interpolated_string_literal):
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



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[3] = self.statements_impl_sempred
        self._predicates[49] = self.compilation_condition_sempred
        self._predicates[173] = self.pattern_sempred
        self._predicates[189] = self.any_punctuation_for_balanced_token_sempred
        self._predicates[231] = self.postfix_expression_sempred
        self._predicates[239] = self.type_sempred
        self._predicates[263] = self.assignment_operator_sempred
        self._predicates[264] = self.negate_prefix_operator_sempred
        self._predicates[265] = self.compilation_condition_AND_sempred
        self._predicates[266] = self.compilation_condition_OR_sempred
        self._predicates[267] = self.compilation_condition_GE_sempred
        self._predicates[268] = self.arrow_operator_sempred
        self._predicates[269] = self.range_operator_sempred
        self._predicates[270] = self.same_type_equals_sempred
        self._predicates[271] = self.binary_operator_sempred
        self._predicates[272] = self.prefix_operator_sempred
        self._predicates[273] = self.postfix_operator_sempred
        self._predicates[274] = self.operator_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def statements_impl_sempred(self, localctx:Statements_implContext, predIndex:int):
            if predIndex == 0:
                return SwiftSupport.isSeparatedStatement(_input, localctx.indexBefore)


    def compilation_condition_sempred(self, localctx:Compilation_conditionContext, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)


            if predIndex == 2:
                return self.precpred(self._ctx, 1)


    def pattern_sempred(self, localctx:PatternContext, predIndex:int):
            if predIndex == 3:
                return self.precpred(self._ctx, 2)


    def any_punctuation_for_balanced_token_sempred(self, localctx:Any_punctuation_for_balanced_tokenContext, predIndex:int):
            if predIndex == 4:
                return SwiftSupport.isPrefixOp(_input)


            if predIndex == 5:
                return SwiftSupport.isPostfixOp(_input)


    def postfix_expression_sempred(self, localctx:Postfix_expressionContext, predIndex:int):
            if predIndex == 6:
                return self.precpred(self._ctx, 12)


            if predIndex == 7:
                return self.precpred(self._ctx, 11)


            if predIndex == 8:
                return self.precpred(self._ctx, 10)


            if predIndex == 9:
                return self.precpred(self._ctx, 9)


            if predIndex == 10:
                return self.precpred(self._ctx, 8)


            if predIndex == 11:
                return self.precpred(self._ctx, 7)


            if predIndex == 12:
                return self.precpred(self._ctx, 6)


            if predIndex == 13:
                return self.precpred(self._ctx, 5)


            if predIndex == 14:
                return self.precpred(self._ctx, 4)


            if predIndex == 15:
                return self.precpred(self._ctx, 3)


            if predIndex == 16:
                return self.precpred(self._ctx, 1)


    def type_sempred(self, localctx:TypeContext, predIndex:int):
            if predIndex == 17:
                return self.precpred(self._ctx, 7)


            if predIndex == 18:
                return self.precpred(self._ctx, 6)


            if predIndex == 19:
                return self.precpred(self._ctx, 4)


            if predIndex == 20:
                return self.precpred(self._ctx, 3)


    def assignment_operator_sempred(self, localctx:Assignment_operatorContext, predIndex:int):
            if predIndex == 21:
                return SwiftSupport.isBinaryOp(_input)


    def negate_prefix_operator_sempred(self, localctx:Negate_prefix_operatorContext, predIndex:int):
            if predIndex == 22:
                return SwiftSupport.isPrefixOp(_input)


    def compilation_condition_AND_sempred(self, localctx:Compilation_condition_ANDContext, predIndex:int):
            if predIndex == 23:
                return SwiftSupport.isOperator(_input,"&&")


    def compilation_condition_OR_sempred(self, localctx:Compilation_condition_ORContext, predIndex:int):
            if predIndex == 24:
                return SwiftSupport.isOperator(_input,"||")


    def compilation_condition_GE_sempred(self, localctx:Compilation_condition_GEContext, predIndex:int):
            if predIndex == 25:
                return SwiftSupport.isOperator(_input,">=")


    def arrow_operator_sempred(self, localctx:Arrow_operatorContext, predIndex:int):
            if predIndex == 26:
                return SwiftSupport.isOperator(_input,"->")


    def range_operator_sempred(self, localctx:Range_operatorContext, predIndex:int):
            if predIndex == 27:
                return SwiftSupport.isOperator(_input,"...")


    def same_type_equals_sempred(self, localctx:Same_type_equalsContext, predIndex:int):
            if predIndex == 28:
                return SwiftSupport.isOperator(_input,"==")


    def binary_operator_sempred(self, localctx:Binary_operatorContext, predIndex:int):
            if predIndex == 29:
                return SwiftSupport.isBinaryOp(_input)


    def prefix_operator_sempred(self, localctx:Prefix_operatorContext, predIndex:int):
            if predIndex == 30:
                return SwiftSupport.isPrefixOp(_input)


    def postfix_operator_sempred(self, localctx:Postfix_operatorContext, predIndex:int):
            if predIndex == 31:
                return SwiftSupport.isPostfixOp(_input)


    def operator_sempred(self, localctx:OperatorContext, predIndex:int):
            if predIndex == 32:
                return _input.get(_input.index()-1).getType()!=WS


            if predIndex == 33:
                return _input.get(_input.index()-1).getType()!=WS





