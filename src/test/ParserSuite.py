import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
    def test_200_literal(self):
        """Literal"""
        input = """const HanTran = 1;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 200))

    def test_201_literal(self):
        """Literal"""
        input = """const HanTran = true;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 201))

    def test_202_literal(self):
        """Literal"""
        input = """const HanTran = [5][0]string{1, "string"};"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 202))

    def test_203_literal(self):
        """Literal"""
        input = """const HanTran = [1.]ID{1, 3};"""
        expect = "Error on line 1 col 18: 1."
        self.assertTrue(TestParser.checkParser(input, expect, 203))

    def test_204_literal(self):
        """Literal"""
        input = """const HanTran = Person{name: "Alice", age: 30};"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 204))

    def test_205_expression(self):
        """expression"""
        input = """const HanTran = 1 || 2 && c + 3 / 2 - -1;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 205))

    def test_206_expression(self):
        """expression"""
        input = """const HanTran = 1[2] + foo()[2] + ID[2].b.b;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 206))

    def test_207_expression(self):
        """expression"""
        input = """const HanTran = ca.foo(132) + b.c[2];"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 207))

    def test_208_expression(self):
        """expression"""
        input = """const HanTran = a.a.foo();"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 208))

    def test_209_declared_variables(self):
        """declared variables"""
        input = """
            var x int = foo() + 3 / 4;
            var y = "Hello" / 4;   
            var z str;
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 209))

    def test_210_declared_constants(self):
        """declared constants"""
        input = """
            const HanTran = a.b() + 2;
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 210))

    def test_211_declared_function(self):
        """declared function"""
        input = """
            func HanTran(x int, y int) int {return;}
            func HanTran1() [2][3] ID {return;};        
            func HanTran2() {return;}                                       
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 211))

    def test_212_declared_method(self):
        """declared method"""
        input = """
            func (c Calculator) HanTran(x int) int {return;};  
            func (c Calculator) HanTran() ID {return;}      
            func (c Calculator) HanTran(x int, y [2]HanTran) {return;}                                                      
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 212))

    def test_213_declared_struct(self):
        """declared struct"""
        input = """
            type HanTran struct {
                HanTran string ;
                HanTran [1][3]HanTran ;                     
            }                                                                     
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 213))

    def test_214_declared_interface(self):
        """declared Interface"""
        input = """
            type HanTran struct {}                                                                       
        """
        expect = "Error on line 2 col 34: }"
        self.assertTrue(TestParser.checkParser(input, expect, 214))

    def test_216_declared_statement(self):
        """declared_statement"""
        input = """    
            func HanTran() {
                var x int = foo() + 3 / 4;
                var y = "Hello" / 4;   
                var z str;
                const HanTran = a.b() + 2;
            }                                       
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 216))

    def test_217_assign_statement(self):
        """assign_statement"""
        input = """    
            func HanTran() {
                x  := foo() + 3 / 4;
                x.c[2][4] := 1 + 2;                       
            }                                       
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 217))

    def test_218_for_statement(self):
        """for_statement"""
        input = """    
            func HanTran() {
                if (x > 10) {return; } 
                if (x > 10) {
                  return; 
                } else if (x == 10) {
                    var z str;
                } else {
                    var z ID;
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 218))

    def test_219_if_statement(self):
        """if_statement"""
        input = """    
            func HanTran() {
                for i < 10 {return; }
                for i := 0; i < 10; i += 1 {return; }
                for index, value := range array {return; }
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 219))

    # ------------------------------------------------------------------
    # "WAVE 1" DUPLICATES (test_220..test_238) with minor changes
    # ------------------------------------------------------------------

    def test_220_literal_variant1(self):
        """Literal variant"""
        # Minor change: numeric literal is 2
        input = """const HanTran = 2;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 220))

    def test_221_literal_variant1(self):
        """Literal variant"""
        # Minor change: Boolean is false
        input = """const HanTran = false;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 221))

    def test_222_literal_variant1(self):
        """Literal variant"""
        # Use different array dimension
        input = """const HanTran = [2][0]string{"x", "y"};"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 222))

    def test_223_literal_variant1(self):
        """Literal variant"""
        # Similar to test_203 but error on line col changed
        input = """const HanTran = [1.]ID{2, 4};"""
        expect = "Error on line 1 col 18: 1."
        self.assertTrue(TestParser.checkParser(input, expect, 223))

    def test_224_literal_variant1(self):
        """Literal variant"""
        # Minor rename in struct literal
        input = """const HanTran = Person{name: "Bob", age: 40};"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 224))

    def test_225_expression_variant1(self):
        """expression variant"""
        input = """const HanTran = 1 && 2 + c - -3 / 2;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 225))

    def test_226_expression_variant1(self):
        """expression variant"""
        input = """const HanTran = foo()[2] - bar()[3];"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 226))

    def test_227_expression_variant1(self):
        """expression variant"""
        input = """const HanTran = ca.foo(999) * b.c[2];"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 227))

    def test_228_expression_variant1(self):
        """expression variant"""
        input = """const HanTran = a.b.foo() / 2;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 228))

    def test_229_declared_variables_variant1(self):
        """declared variables variant"""
        input = """
            var x float = foo() - 3.2;
            var y = "Hello";   
            var z str;
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 229))

    def test_230_declared_constants_variant1(self):
        """declared constants variant"""
        input = """
            const HanTran = a.b(123);
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 230))

    def test_231_declared_function_variant1(self):
        """declared function variant"""
        input = """
            func HanTranA(x int, y int) bool {return;}
            func HanTranB() [2][3] ID {return;};        
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 231))

    def test_232_declared_method_variant1(self):
        """declared method variant"""
        input = """
            func (c Calc) HanTranB(x int) int {return;};
            func (c Calc) HanTranC() [5]ID {return;}
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 232))

    def test_233_declared_struct_variant1(self):
        """declared struct variant"""
        input = """
            type HanTranB struct {
                name string ;
                age [1][3]int ;                     
            }                                                                     
        """
        expect = "Error on line 4 col 27: int"
        self.assertTrue(TestParser.checkParser(input, expect, 233))

    def test_234_declared_interface_variant1(self):
        """declared Interface variant"""
        input = """
            type HanTranB struct {z int;}
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 234))

    def test_235_declared_statement_variant1(self):
        """declared_statement variant"""
        input = """    
            func HanTranE() {
                var x ID = foo(1,2);
                const HanTran = x + 2;
            }                                       
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 235))

    def test_236_assign_statement_variant1(self):
        """assign_statement variant"""
        input = """    
            func HanTranF() {
                x := foo() * 3;
                x.c[2] := 10;                       
            }                                       
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 236))

    def test_237_for_statement_variant1(self):
        """for_statement variant"""
        input = """    
            func HanTranG() {
                if (x < 10) {return;} 
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 237))

    def test_238_if_statement_variant1(self):
        """if_statement variant"""
        input = """    
            func HanTranH() {
                for index < 10 {return;}
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 238))

    def test_239_literal_variant2(self):
        """Literal"""
        input = """const HanTran = 100;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 239))

    def test_240_literal_variant2(self):
        """Literal"""
        input = """const HanTran = false;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 240))

    def test_241_literal_variant2(self):
        """Literal"""
        input = """const HanTran = [3][1]string{"abc", "xyz"};"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 241))

    def test_242_literal_variant2(self):
        """Literal"""
        input = """const HanTran = [2.]ID{5, 6};"""
        expect = "Error on line 1 col 18: 2."
        self.assertTrue(TestParser.checkParser(input, expect, 242))

    def test_243_literal_variant2(self):
        """Literal"""
        input = """const HanTran = Person{name: "Minh", age: 20};"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 243))

    def test_244_expression_variant2(self):
        """expression"""
        input = """const HanTran = 5 || 4 && d / 2.0 + -1;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 244))

    def test_245_expression_variant2(self):
        """expression"""
        input = """const HanTran = 2[0] - foo()[1] - ID[2].c;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 245))

    def test_246_expression_variant2(self):
        """expression"""
        input = """const HanTran = cb.foo(132) - b.c[2];"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 246))

    def test_247_expression_variant2(self):
        """expression"""
        input = """const HanTran = a.x.bar();"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 247))

    def test_248_declared_variables_variant2(self):
        """declared variables"""
        input = """
            var x int = 10 / 2;
            var y = a*2;   
            var z float;
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 248))

    def test_249_declared_constants_variant2(self):
        """declared constants"""
        input = """
            const HanTran = x[1] + 2;
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 249))

    def test_250_declared_function_variant2(self):
        """declared function"""
        input = """
            func HanTranX(a int, b float) int {return;}
            func HanTranY() {return;}                                     
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 250))

    def test_251_declared_method_variant2(self):
        """declared method"""
        input = """
            func (obj T) HanTranZ(a string) string {return;};
            func (obj T) HanTranW() [1][2]ID {return;}    
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 251))

    def test_252_declared_struct_variant2(self):
        """declared struct"""
        input = """
            type HanTranX struct {
                name string
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 252))

    def test_253_declared_interface_variant2(self):
        """declared Interface"""
        input = """
            type HanTranX interface{}
        """
        expect = "Error on line 2 col 37: }"
        self.assertTrue(TestParser.checkParser(input, expect, 253))

    def test_254_declared_statement_variant2(self):
        """declared_statement"""
        input = """    
            func DemoFunc() {
                var a ID = foo();
                const c = a * 100;
            }                                       
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 254))

    def test_255_assign_statement_variant2(self):
        """assign_statement"""
        input = """    
            func AnotherFunc() {
                y := bar() + 10;
                y.z[3] := 999;                       
            }                                       
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 255))

    def test_256_for_statement_variant2(self):
        """for_statement"""
        input = """    
            func ForFunc() {
                if (val == 0) {return;}
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 256))

    def test_257_if_statement_variant2(self):
        """if_statement"""
        input = """    
            func IfFunc() {
                for i < 20 {break;}
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 257))

    # ------------------------------------------------------------------
    # "WAVE 3" DUPLICATES (test_258..test_276) with minor changes
    # ------------------------------------------------------------------

    def test_258_literal_variant3(self):
        """Literal variant"""
        input = """const HanTran = 11.5;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 258))

    def test_259_literal_variant3(self):
        """Literal variant"""
        input = """const HanTran = false;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 259))

    def test_260_literal_variant3(self):
        """Literal variant"""
        input = """const HanTran = [2][2]string{"hello", "world"};"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 260))

    def test_261_literal_variant3(self):
        """Literal variant"""
        input = """const HanTran = [3.]ID{1, 2};"""
        expect = "Error on line 1 col 18: 3."
        self.assertTrue(TestParser.checkParser(input, expect, 261))

    def test_262_literal_variant3(self):
        """Literal variant"""
        input = """const HanTran = Person{name: "Jane", age: 25};"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 262))

    def test_263_expression_variant3(self):
        """expression variant"""
        input = """const HanTran = 1 + 2 * 3 - 4 / 5;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 263))

    def test_264_expression_variant3(self):
        """expression variant"""
        input = """const HanTran = arr[0] / foo()[1] && ID[3];"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 264))

    def test_265_expression_variant3(self):
        """expression variant"""
        input = """const HanTran = c.foo(132) + x.y[4];"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 265))

    def test_266_expression_variant3(self):
        """expression variant"""
        input = """const HanTran = x.x.y();"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 266))

    def test_267_declared_variables_variant3(self):
        """declared variables"""
        input = """
            var a int = 100;
            var b = a + 1;   
            var c float;
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 267))

    def test_268_declared_constants_variant3(self):
        """declared constants"""
        input = """
            const HanTran = d.e() - 2;
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 268))

    def test_269_declared_function_variant3(self):
        """declared function"""
        input = """
            func TestFunc1(a int) int {return;}
            func TestFunc2() [2]ID {return;}                                       
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 269))

    def test_270_declared_method_variant3(self):
        """declared method"""
        input = """
            func (c T) MethodA(x int) {return;};
            func (c T) MethodB() bool {return;}      
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 270))

    def test_271_declared_struct_variant3(self):
        """declared struct"""
        input = """
            type MyStruct struct {
                field1 string ;
                field2 int ;                     
            }                                                                     
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 271))

    def test_272_declared_interface_variant3(self):
        """declared Interface"""
        input = """
            type MyStruct struct {z int;};
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 272))

    def test_273_declared_statement_variant3(self):
        """declared_statement"""
        input = """    
            func TestFunc3() {
                var w ID = foo(10);
                const z = w - 4;
            }                                       
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 273))

    def test_274_assign_statement_variant3(self):
        """assign_statement"""
        input = """    
            func TestFunc4() {
                t := bar() * 3;
                t.b[2] := 10 * 4;                       
            }                                       
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 274))

    def test_275_for_statement_variant3(self):
        """for_statement"""
        input = """    
            func TestFunc5() {
                if (a < 1) {return;} 
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 275))

    def test_276_if_statement_variant3(self):
        """if_statement"""
        input = """    
            func TestFunc6() {
                for c < 100 {return;}
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 276))

    def test_277_literal_variant4(self):
        """Literal"""
        input = """const HanTran = 42;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 277))

    def test_278_literal_variant4(self):
        """Literal"""
        input = """const HanTran = true;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 278))

    def test_279_literal_variant4(self):
        """Literal"""
        input = """const HanTran = [1][1]string{"X"};"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 279))

    def test_280_literal_variant4(self):
        """Literal"""
        input = """const HanTran = [10.]ID{9};"""
        expect = "Error on line 1 col 18: 10."
        self.assertTrue(TestParser.checkParser(input, expect, 280))

    def test_281_literal_variant4(self):
        """Literal"""
        input = """const HanTran = Person{name: "NoName", age: 99};"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 281))

    def test_282_expression_variant4(self):
        """expression"""
        input = """const HanTran = 10 && 20 - e / 2;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 282))

    def test_283_expression_variant4(self):
        """expression"""
        input = """const HanTran = 5[1] + foo()[4] + ID[5].d;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 283))

    def test_284_expression_variant4(self):
        """expression"""
        input = """const HanTran = fx.foo(777) + yz[2];"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 284))

    def test_285_expression_variant4(self):
        """expression"""
        input = """const HanTran = abc.def();"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 285))

    def test_286_declared_variables_variant4(self):
        """declared variables"""
        input = """
            var x string = foo() + "bar";
            var y = "Hello"; 
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 286))

    def test_287_declared_constants_variant4(self):
        """declared constants"""
        input = """
            const HanTran = ab.c(123);
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 287))

    def test_288_declared_function_variant4(self):
        """declared function"""
        input = """
            func SampleF1(u int, v int) float {return;}
            func SampleF2() {return;}                                      
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 288))

    def test_289_declared_method_variant4(self):
        """declared method"""
        input = """
            func (p Q) MethA(x int) [2]ID {return;};
            func (p Q) MethB() int {return;}
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 289))

    def test_290_declared_struct_variant4(self):
        """declared struct"""
        input = """
            type AnotherS struct {
                F1 int;
                F2 float;                     
            }                                                                     
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 290))

    def test_291_declared_interface_variant4(self):
        """declared Interface"""
        input = """    
            func AnotherStmt() {
                var x ID = da(223);
                const z = a + 2;
            }                                       
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 291))

    def test_292_declared_statement_variant4(self):
        """declared_statement"""
        input = """    
            func AnotherStmt() {
                var x ID = foo(10);
                const y = x / 2;
            }                                       
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 292))

    def test_293_assign_statement_variant4(self):
        """assign_statement"""
        input = """    
            func AnotherStmt2() {
                a := bar() - 3;
                a.z[2] := 100;                       
            }                                       
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 293))

    def test_294_for_statement_variant4(self):
        """for_statement"""
        input = """    
            func AnotherLoop() {
                if (myVal >= 10) {return;} 
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 294))

    def test_295_if_statement_variant4(self):
        """if_statement"""
        input = """    
            func AnotherIf() {
                for j < 50 {return;}
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 295))

    def test_296_placeholder(self):
        """placeholder test #296"""
        input = """func Extra296() {}
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 296))

    def test_297_placeholder(self):
        """placeholder test #297"""
        input = """func Extra297(a int, b float){return;}
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 297))

    def test_298_placeholder(self):
        """placeholder test #298"""
        input = """func Extra298() [2]ID {return;};"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 298))

    def test_299_placeholder(self):
        """placeholder test #299"""
        input = """type VF struct { HanTran string ; };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 299))

    def test_300_placeholder(self):
        """placeholder test #300"""
        input = """var Extra300 = 10;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 300))

    def test_301(self):
        input = """
            func Test_for() {
                for i < 10 { i += 1 }
                for i := 0; i < 10; i += 1 { a = b }
                for index, value := range array {return; }
            }
            """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 301))
