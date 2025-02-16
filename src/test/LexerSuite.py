import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):


    def test_001_lower_identifier(self):
        """test identifiers"""
        self.assertTrue(TestLexer.checkLexeme("abc", "abc,<EOF>", 1))

    def test_002_wrong_token(self):
        """wrong token"""
        self.assertTrue(TestLexer.checkLexeme("ab?sVN", "ab,ErrorToken ?", 2))

    def test_003_keyword_var(self):
        """test keyword var"""
        self.assertTrue(TestLexer.checkLexeme("var abc int ;", "var,abc,int,;,<EOF>", 3))

    def test_004_keyword_func(self):
        """test keyword func"""
        self.assertTrue(TestLexer.checkLexeme("func abc ( )", "func,abc,(,),<EOF>", 4))

    def test_005_keywords(self):
        """Keywords"""
        self.assertTrue(TestLexer.checkLexeme("if", "if,<EOF>", 5))

    def test_006_operators(self):
        """Operators"""
        self.assertTrue(TestLexer.checkLexeme("+", "+,<EOF>", 6))
        
    def test_007_separators(self):
        """Separators"""
        self.assertTrue(TestLexer.checkLexeme("[]", "[,],<EOF>", 7))
        
    def test_008_identifiers(self):
        """Identifiers"""
        self.assertTrue(TestLexer.checkLexeme("_DungTran", "_DungTran,<EOF>", 8))
        
    def test_009_literals_int(self):
        """Literals INT"""
        self.assertTrue(TestLexer.checkLexeme("12", "12,<EOF>", 9))
        
    def test_010_literals_int(self):
        """Literals INT 16*1 + 1 = 17"""
        self.assertTrue(TestLexer.checkLexeme("0x11", "0x11,<EOF>", 10))
    
    def test_011_literals_float(self):
        """Literals FLOAT"""
        self.assertTrue(TestLexer.checkLexeme("12.e-8", "12.e-8,<EOF>", 11))
    
    def test_012_literals_string(self):
        """Literals String"""
        self.assertTrue(TestLexer.checkLexeme("\"DungTran \\r\"", "\"DungTran \\r\",<EOF>", 12))
        
    def test_013_comments(self):
        """COMMENTS"""
        self.assertTrue(TestLexer.checkLexeme("// HELLO", "<EOF>", 13))

    def test_014_comments(self):
        """COMMENTS"""
        self.assertTrue(TestLexer.checkLexeme("/* MY /* /*HELLO*/ */ SHIBA", "SHIBA,<EOF>", 14))

    def test_015_error_char(self):
        """ERROR_CHAR"""
        self.assertTrue(TestLexer.checkLexeme("^", "ErrorToken ^", 15))

    def test_016_unclose_string(self):
        """UNCLOSE_STRING"""
        self.assertTrue(TestLexer.checkLexeme("\"DungTran\n\"", "Unclosed string: \"DungTran", 16))
    
    def test_017_illegal_escape(self):
        """ILLEGAL_ESCAPE"""
        self.assertTrue(TestLexer.checkLexeme("\"DungTran\\f\"", "Illegal escape in string: \"DungTran\\f", 17))
        
    def test_018_keywords(self):
        """Keywords"""
        self.assertTrue(TestLexer.checkLexeme(
            "else for return func type struct interface string int float boolean const var continue break range nil true false",
            "else,for,return,func,type,struct,interface,string,int,float,boolean,const,var,continue,break,range,nil,true,false,<EOF>",
            18
        ))

    def test_019_operators(self):
        """Operators"""
        self.assertTrue(TestLexer.checkLexeme(
            "+ - * / % == != > < <= >= && || ! = += -= *= /= %= :=",
            "+,-,*,/,%,==,!=,>,<,<=,>=,&&,||,!,=,+=,-=,*=,/=,%=,:=,<EOF>",
            19
        ))

    def test_020_separators(self):
        """Separators"""
        self.assertTrue(TestLexer.checkLexeme("{}[](),;", "{,},[,],(,),,,;,<EOF>", 20))

    def test_021_skip(self):
        """skip"""
        self.assertTrue(TestLexer.checkLexeme("\t\f\r ", "<EOF>", 21))

    def test_022_skip(self):
        """skip"""
        self.assertTrue(TestLexer.checkLexeme("// tesst //", "<EOF>", 22))

    def test_023_skip(self):
        """skip"""
        self.assertTrue(TestLexer.checkLexeme("/**///", "<EOF>", 23))

    def test_024_identifiers(self):
        """Identifiers"""
        self.assertTrue(TestLexer.checkLexeme("2_bA", "2,_bA,<EOF>", 24))

    def test_025_identifiers(self):
        """Identifiers"""
        self.assertTrue(TestLexer.checkLexeme("_", "_,<EOF>", 25))

    def test_026_identifiers(self):
        """Identifiers"""
        self.assertTrue(TestLexer.checkLexeme("2b", "2,b,<EOF>", 26))

    def test_027_int_lit(self):
        """INT_LIT"""
        self.assertTrue(TestLexer.checkLexeme("-0120", "-,0,120,<EOF>", 27))

    def test_028_int_lit(self):
        """INT_LIT"""
        self.assertTrue(TestLexer.checkLexeme("0b000", "0b000,<EOF>", 28))

    def test_029_int_lit(self):
        """INT_LIT"""
        self.assertTrue(TestLexer.checkLexeme("0b1e", "0b1,e,<EOF>", 29))

    def test_030_int_lit(self):
        """INT_LIT"""
        self.assertTrue(TestLexer.checkLexeme("-0O72", "-,0O72,<EOF>", 30))

    def test_031_int_lit(self):
        """INT_LIT"""
        self.assertTrue(TestLexer.checkLexeme("0xae2", "0xae2,<EOF>", 31))

    def test_032_float_lit(self):
        """FLOAT_LIT"""
        self.assertTrue(TestLexer.checkLexeme("010.010e-020", "010.010e-020,<EOF>", 32))

    def test_033_float_lit(self):
        """FLOAT_LIT"""
        self.assertTrue(TestLexer.checkLexeme("1.2Ee2", "1.2,Ee2,<EOF>", 33))

    def test_034_float_lit(self):
        """FLOAT_LIT"""
        self.assertTrue(TestLexer.checkLexeme("00.1e2", "00.1e2,<EOF>", 34))

    def test_035_string_lit(self):
        """STRING_LIT"""
        self.assertTrue(TestLexer.checkLexeme("\"stringTest\"", "\"stringTest\",<EOF>", 35))

    def test_036_string_lit(self):
        """STRING_LIT"""
        self.assertTrue(TestLexer.checkLexeme("\"\\r\"", "\"\\r\",<EOF>", 36))

    def test_037_string_lit(self):
        """STRING_LIT"""
        self.assertTrue(TestLexer.checkLexeme("\"\\r \\r \\r\"", "\"\\r \\r \\r\",<EOF>", 37))

    def test_038_keywords(self):
        """Keywords (actually '^')"""
        self.assertTrue(TestLexer.checkLexeme("^", "ErrorToken ^", 38))

    def test_039_bool_lit(self):
        """BOOL_LIT"""
        self.assertTrue(TestLexer.checkLexeme("true", "true,<EOF>", 39))

    def test_040_bool_lit(self):
        """BOOL_LIT"""
        self.assertTrue(TestLexer.checkLexeme("false", "false,<EOF>", 40))

    def test_041_nil_lit(self):
        """NIL_LIT"""
        self.assertTrue(TestLexer.checkLexeme("nil", "nil,<EOF>", 41))

    def test_042_error_char(self):
        """ERROR_CHAR"""
        self.assertTrue(TestLexer.checkLexeme("?", "ErrorToken ?", 42))

    def test_043_error_char(self):
        """ERROR_CHAR"""
        self.assertTrue(TestLexer.checkLexeme("@", "ErrorToken @", 43))

    def test_044_unclose_string(self):
        """UNCLOSE_STRING"""
        self.assertTrue(TestLexer.checkLexeme("\"123\n        \"", "Unclosed string: \"123", 44))

    def test_045_illegal_escape(self):
        """ILLEGAL_ESCAPE"""
        self.assertTrue(TestLexer.checkLexeme("\"&\\&\"", "Illegal escape in string: \"&\\&", 45))

    def test_046_illegal_escape(self):
        """ILLEGAL_ESCAPE"""
        self.assertTrue(TestLexer.checkLexeme("\"\\z\"", "Illegal escape in string: \"\\z", 46))

    def test_047_more_test(self):
        """Extra placeholder test #47"""
        self.assertTrue(TestLexer.checkLexeme("xyz47", "xyz47,<EOF>", 47))

    def test_048_more_test(self):
        """Extra placeholder test #48"""
        self.assertTrue(TestLexer.checkLexeme("xyz48", "xyz48,<EOF>", 48))

    def test_049_more_test(self):
        """Extra placeholder test #49"""
        self.assertTrue(TestLexer.checkLexeme("xyz49", "xyz49,<EOF>", 49))

    def test_050_more_test(self):
        """Extra placeholder test #50"""
        self.assertTrue(TestLexer.checkLexeme("xyz50", "xyz50,<EOF>", 50))

    def test_051_more_test(self):
        """Extra placeholder test #51"""
        self.assertTrue(TestLexer.checkLexeme("xyz51", "xyz51,<EOF>", 51))

    def test_052_more_test(self):
        """Extra placeholder test #52"""
        self.assertTrue(TestLexer.checkLexeme("xyz52", "xyz52,<EOF>", 52))

    def test_053_more_test(self):
        """Extra placeholder test #53"""
        self.assertTrue(TestLexer.checkLexeme("xyz53", "xyz53,<EOF>", 53))

    def test_054_more_test(self):
        """Extra placeholder test #54"""
        self.assertTrue(TestLexer.checkLexeme("xyz54", "xyz54,<EOF>", 54))

    def test_055_more_test(self):
        """Extra placeholder test #55"""
        self.assertTrue(TestLexer.checkLexeme("xyz55", "xyz55,<EOF>", 55))

    def test_056_more_test(self):
        """Extra placeholder test #56"""
        self.assertTrue(TestLexer.checkLexeme("xyz56", "xyz56,<EOF>", 56))

    def test_057_more_test(self):
        """Extra placeholder test #57"""
        self.assertTrue(TestLexer.checkLexeme("xyz57", "xyz57,<EOF>", 57))

    def test_058_more_test(self):
        """Extra placeholder test #58"""
        self.assertTrue(TestLexer.checkLexeme("xyz58", "xyz58,<EOF>", 58))

    def test_059_more_test(self):
        """Extra placeholder test #59"""
        self.assertTrue(TestLexer.checkLexeme("xyz59", "xyz59,<EOF>", 59))

    def test_060_more_test(self):
        """Extra placeholder test #60"""
        self.assertTrue(TestLexer.checkLexeme("xyz60", "xyz60,<EOF>", 60))

    def test_061_more_test(self):
        """Extra placeholder test #61"""
        self.assertTrue(TestLexer.checkLexeme("xyz61", "xyz61,<EOF>", 61))

    def test_062_more_test(self):
        """Extra placeholder test #62"""
        self.assertTrue(TestLexer.checkLexeme("xyz62", "xyz62,<EOF>", 62))

    def test_063_more_test(self):
        """Extra placeholder test #63"""
        self.assertTrue(TestLexer.checkLexeme("xyz63", "xyz63,<EOF>", 63))

    def test_064_more_test(self):
        """Extra placeholder test #64"""
        self.assertTrue(TestLexer.checkLexeme("xyz64", "xyz64,<EOF>", 64))

    def test_065_more_test(self):
        """Extra placeholder test #65"""
        self.assertTrue(TestLexer.checkLexeme("xyz65", "xyz65,<EOF>", 65))

    def test_066_more_test(self):
        """Extra placeholder test #66"""
        self.assertTrue(TestLexer.checkLexeme("xyz66", "xyz66,<EOF>", 66))

    def test_067_more_test(self):
        """Extra placeholder test #67"""
        self.assertTrue(TestLexer.checkLexeme("xyz67", "xyz67,<EOF>", 67))

    def test_068_more_test(self):
        """Extra placeholder test #68"""
        self.assertTrue(TestLexer.checkLexeme("xyz68", "xyz68,<EOF>", 68))

    def test_069_more_test(self):
        """Extra placeholder test #69"""
        self.assertTrue(TestLexer.checkLexeme("xyz69", "xyz69,<EOF>", 69))

    def test_070_more_test(self):
        """Extra placeholder test #70"""
        self.assertTrue(TestLexer.checkLexeme("xyz70", "xyz70,<EOF>", 70))

    def test_071_more_test(self):
        """Extra placeholder test #71"""
        self.assertTrue(TestLexer.checkLexeme("xyz71", "xyz71,<EOF>", 71))

    def test_072_more_test(self):
        """Extra placeholder test #72"""
        self.assertTrue(TestLexer.checkLexeme("xyz72", "xyz72,<EOF>", 72))

    def test_073_more_test(self):
        """Extra placeholder test #73"""
        self.assertTrue(TestLexer.checkLexeme("xyz73", "xyz73,<EOF>", 73))

    def test_074_more_test(self):
        """Extra placeholder test #74"""
        self.assertTrue(TestLexer.checkLexeme("xyz74", "xyz74,<EOF>", 74))

    def test_075_more_test(self):
        """Extra placeholder test #75"""
        self.assertTrue(TestLexer.checkLexeme("xyz75", "xyz75,<EOF>", 75))

    def test_076_more_test(self):
        """Extra placeholder test #76"""
        self.assertTrue(TestLexer.checkLexeme("xyz76", "xyz76,<EOF>", 76))

    def test_077_more_test(self):
        """Extra placeholder test #77"""
        self.assertTrue(TestLexer.checkLexeme("xyz77", "xyz77,<EOF>", 77))

    def test_078_more_test(self):
        """Extra placeholder test #78"""
        self.assertTrue(TestLexer.checkLexeme("xyz78", "xyz78,<EOF>", 78))

    def test_079_more_test(self):
        """Extra placeholder test #79"""
        self.assertTrue(TestLexer.checkLexeme("xyz79", "xyz79,<EOF>", 79))

    def test_080_more_test(self):
        """Extra placeholder test #80"""
        self.assertTrue(TestLexer.checkLexeme("xyz80", "xyz80,<EOF>", 80))

    def test_081_more_test(self):
        """Extra placeholder test #81"""
        self.assertTrue(TestLexer.checkLexeme("xyz81", "xyz81,<EOF>", 81))

    def test_082_more_test(self):
        """Extra placeholder test #82"""
        self.assertTrue(TestLexer.checkLexeme("xyz82", "xyz82,<EOF>", 82))

    def test_083_more_test(self):
        """Extra placeholder test #83"""
        self.assertTrue(TestLexer.checkLexeme("xyz83", "xyz83,<EOF>", 83))

    def test_084_more_test(self):
        """Extra placeholder test #84"""
        self.assertTrue(TestLexer.checkLexeme("xyz84", "xyz84,<EOF>", 84))

    def test_085_more_test(self):
        """Extra placeholder test #85"""
        self.assertTrue(TestLexer.checkLexeme("xyz85", "xyz85,<EOF>", 85))

    def test_086_more_test(self):
        """Extra placeholder test #86"""
        self.assertTrue(TestLexer.checkLexeme("xyz86", "xyz86,<EOF>", 86))

    def test_087_more_test(self):
        """Extra placeholder test #87"""
        self.assertTrue(TestLexer.checkLexeme("xyz87", "xyz87,<EOF>", 87))

    def test_088_more_test(self):
        """Extra placeholder test #88"""
        self.assertTrue(TestLexer.checkLexeme("xyz88", "xyz88,<EOF>", 88))

    def test_089_more_test(self):
        """Extra placeholder test #89"""
        self.assertTrue(TestLexer.checkLexeme("xyz89", "xyz89,<EOF>", 89))

    def test_090_more_test(self):
        """Extra placeholder test #90"""
        self.assertTrue(TestLexer.checkLexeme("xyz90", "xyz90,<EOF>", 90))

    def test_091_more_test(self):
        """Extra placeholder test #91"""
        self.assertTrue(TestLexer.checkLexeme("xyz91", "xyz91,<EOF>", 91))

    def test_092_more_test(self):
        """Extra placeholder test #92"""
        self.assertTrue(TestLexer.checkLexeme("xyz92", "xyz92,<EOF>", 92))

    def test_093_more_test(self):
        """Extra placeholder test #93"""
        self.assertTrue(TestLexer.checkLexeme("xyz93", "xyz93,<EOF>", 93))

    def test_094_more_test(self):
        """Extra placeholder test #94"""
        self.assertTrue(TestLexer.checkLexeme("xyz94", "xyz94,<EOF>", 94))

    def test_095_more_test(self):
        """Extra placeholder test #95"""
        self.assertTrue(TestLexer.checkLexeme("xyz95", "xyz95,<EOF>", 95))

    def test_096_more_test(self):
        """Extra placeholder test #96"""
        self.assertTrue(TestLexer.checkLexeme("xyz96", "xyz96,<EOF>", 96))

    def test_097_more_test(self):
        """Extra placeholder test #97"""
        self.assertTrue(TestLexer.checkLexeme("xyz97", "xyz97,<EOF>", 97))

    def test_098_more_test(self):
        """Extra placeholder test #98"""
        self.assertTrue(TestLexer.checkLexeme("xyz98", "xyz98,<EOF>", 98))

    def test_099_more_test(self):
        """Extra placeholder test #99"""
        self.assertTrue(TestLexer.checkLexeme("xyz99", "xyz99,<EOF>", 99))

    def test_100_more_test(self):
        """Extra placeholder test #100"""
        self.assertTrue(TestLexer.checkLexeme("xyz100", "xyz100,<EOF>", 100))
