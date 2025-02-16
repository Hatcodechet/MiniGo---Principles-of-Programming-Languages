grammar MiniGo;

@lexer::header {
from lexererr import *
}

@lexer::members {

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
}

options{
	language = Python3;
}

program: NEWLINE* declared (declared | NEWLINE)* EOF;

literal
    : INT_LIT
    | REAL
    | STRING_LIT
    | HEX_LIT
    | OCT_LIT
    | TRUE
    | FALSE
    | array_literal
    | struct_literal
    | BIN_LIT
    | NIL
    ;
literal1
    : INT_LIT
    | REAL
    | STRING_LIT
    | HEX_LIT
    | OCT_LIT
    | TRUE
    | FALSE
    | array_literal
    | struct_literal
    | BIN_LIT
    | NIL
    ;

literal3
    : INT_LIT
    | REAL
    | STRING_LIT
    | HEX_LIT
    | OCT_LIT
    | TRUE
    | FALSE
    | struct_literal3
    | BIN_LIT
    | NIL
    | ID
    ;

literal4
    : INT_LIT
    | ID
    ;
array_literal
    : '[' literal4 ']' array_literal_rest
    ;

array_literal_rest
    : '[' literal4 ']' array_literal_rest
    | type_spec arraySupport
    ;
arraySupport: '{' literal3List '}' ;
literal3List
    : literal3
    | literal3 COMMA literal3List
    | arraySupport
    | arraySupport COMMA literal3List
    ;
    
struct_literalSP: (ID LBRACE (literal3| field_init_list) RBRACE);
struct_literal
    :    struct_literalSP 
    ;
struct_literal3
    :   LBRACE* struct_literalSP RBRACE*
    ;

field_init_list
    : field_init ',' field_init_list
    | field_init
    | // empty 
    ;


field_init
    : ID ':' expression
    ;
list_expression
    : expression ',' list_expression
    | expression
    ;


expression
    : logicalOrExpr;
// -------------------- BOOLEAN (LOGICAL) OPERATORS --------------------
logicalOrExpr: logicalOrExpr OR logicalAndExpr | logicalAndExpr;
logicalAndExpr: logicalAndExpr AND equalityExpr | equalityExpr;
// -------------------- RELATIONAL OPERATORS --------------------
// ==, !=, <, >, <=, >=
equalityExpr
    : equalityExpr ('==' | '!=') relationalExpr
    | relationalExpr
    ;
relationalExpr
    : relationalExpr ('<' | '>' | '<=' | '>=') additiveExpr
    | additiveExpr
    ;
// -------------------- ARITHMETIC OPERATORS --------------------
// +, -, *, /, %
additiveExpr
    : additiveExpr ('+' | '-') multiplicativeExpr
    | multiplicativeExpr
    ;
multiplicativeExpr
    : multiplicativeExpr ('*' | '/' | '%') unaryExpr
    | unaryExpr
    ;
// -------------------- UNARY OPERATORS --------------------
// For example, logical negation (!).
unaryExpr
    : ('!'|'-') unaryExpr
    | primaryExpr
    ;
// -------------------- PRIMARY EXPRESSIONS --------------------
// At the "lowest" level, we parse literals, identifiers, parentheses,
// plus array/struct access, which can chain together.
primaryExpr
    : basePrimary postfixOps
    ;

primaryExpr1: basePrimary1 postfixOps;


postfixOps
    : postfixOp postfixOps
    | 
    ;

basePrimary
   : literal1
   | ID
   | '(' expression ')'
   ;

basePrimary1
   :  ID
   //| '(' expression ')'
   ;


postfixOp
    : arrayAccess
    | memberAccess
    | functionCall
    ;

arrayAccess
    : '[' expression ']' postfixOp
    | '[' expression ']' 
    ;

memberAccess
    : DOT ID arrayAccess NEWLINE*
    | DOT ID 
    ;

functionCall
    : '(' argumentList ')' postfixOp
    | '(' argumentList ')'
    ;

argumentList
    : expression (',' expression)*
    | 
    ;


list_statement: statement list_statement | statement;
statement:
	(
		declared_statement
		| assign_statement
		| if_statement
		| for_statement
		| break_statement
		| continue_statement
		| call_statement
		| return_statement
	);

statement2:
	(
		declared_statement2
		| if_statement
        | assign_statement
		| for_statement
		| break_statement
		| continue_statement
		| call_statement
		| return_statement
	);

statement3:
	(
		declared_statement2
		| if_statement
		| for_statement
		| break_statement
		| continue_statement
		| call_statement
		| return_statement
	);

declared_statement
    : variables_declared 
    | constants_declared 
    ;

declared_statement2
    : variables_declared
    | constants_declared2
    ;
assign_statement
    : assignable ASSIGN expression (SEMI|NEWLINE)+
    | assignable ADD_ASSIGN expression (SEMI|NEWLINE)+
    | assignable SUB_ASSIGN expression (SEMI|NEWLINE)+
    | assignable MUL_ASSIGN expression (SEMI|NEWLINE)+
    | assignable DIV_ASSIGN expression (SEMI|NEWLINE)+
    | assignable MOD_ASSIGN expression (SEMI|NEWLINE)+
    | assignable COLON_ASSIGN expression (SEMI|NEWLINE)+
    | ID
    ;

assign_statement2
    : assignable2 ASSIGN expression (SEMI|NEWLINE)+
    | assignable2 ADD_ASSIGN expression (SEMI|NEWLINE)+
    | assignable2 SUB_ASSIGN expression (SEMI|NEWLINE)+
    | assignable2 MUL_ASSIGN expression (SEMI|NEWLINE)+
    | assignable2 DIV_ASSIGN expression (SEMI|NEWLINE)+
    | assignable2 MOD_ASSIGN expression (SEMI|NEWLINE)+
    | assignable2 COLON_ASSIGN expression (SEMI|NEWLINE)+
    | ID
    ;
assignable2
    : ID
    ;
assignable
    : ID tail
    ;
tail
    : DOT ID tail
    | LBRACK expression RBRACK tail
    | 
    | return_type
    ;
tail2
    : DOT ID tail2
    | 
    | type_spec
    ;

if_block: if_statement1 else_if_statement* else_statement?;
if_statement1:
	IF LPAREN expression RPAREN NEWLINE* conditional_body_block;
else_statement: ELSE NEWLINE* bodyBLOCK;
bodyBLOCK: LBRACE NEWLINE* statement_with_newlines NEWLINE* RBRACE;

else_if_statement:
	ELSE IF LPAREN expression RPAREN NEWLINE* conditional_body_block;
conditional_body_block:
	LBRACE NEWLINE* statement2  RBRACE;



if_statement
    : IF LPAREN expression RPAREN NEWLINE*  blockIF (ELSE if_statement) // `else if`
    | IF LPAREN expression RPAREN NEWLINE*  blockIF (ELSE NEWLINE* blockIF2)*        // `else`
    | IF LPAREN expression RPAREN NEWLINE*  blockIF2
    ;



block
    : LBRACE NEWLINE* statement2* RBRACE (SEMI|NEWLINE)* // Khối lệnh, có thể chứa nhiều statement
    ;

blockIF
    : LBRACE NEWLINE* statement2* (SEMI|NEWLINE)?  RBRACE // Khối lệnh, có thể chứa nhiều statement
    ;
blockIF2
    : LBRACE NEWLINE* statement2*  RBRACE NEWLINE+ // Khối lệnh, có thể chứa nhiều statement
    ;

for_statement
    : FOR expression block
    | FOR VAR? assign_statement2 expression (SEMI|NEWLINE)+ ID (ADD_ASSIGN|SUB_ASSIGN|MUL_ASSIGN|DIV_ASSIGN|COLON_ASSIGN| ASSIGN) expression block
    | FOR VAR? assign_statement2 COMMA ID COLON_ASSIGN? RANGE literal? ID? return_type? block
    | FOR VAR assign_statement expression (SEMI|NEWLINE)+ ID (ADD_ASSIGN|SUB_ASSIGN|MUL_ASSIGN|DIV_ASSIGN|COLON_ASSIGN| ASSIGN) expression block
    ;

break_statement
    : BREAK (SEMI | NEWLINE)+
    ;

continue_statement
    : CONTINUE (SEMI | NEWLINE)+
    ;

call_statement
    : primaryExpr1 (SEMI | NEWLINE)+
    ;

return_statement
    : 
    RETURN (expression) (SEMI | NEWLINE)+
    | RETURN (NEWLINE|SEMI)+
    ;
/*------------------------------DECLARED------------------------------*/


declared
    : function_declared
    | variables_declared
    | constants_declared
    | method_declared
    | struct_declared
    | interface_declared
    ;

declared2
    : variables_declared
    | constants_declared2
    | function_declared
    | method_declared
    | struct_declared
    | interface_declared
    ;

declared3
    : variables_declared
    | constants_declared
    | struct_declared
    | interface_declared
    ;

variables_declared
    : VAR ID type_spec ASSIGN expression (SEMI | NEWLINE)+

    | VAR ID ASSIGN expression (SEMI | NEWLINE)+

    | VAR ID type_spec (SEMI | NEWLINE)+

    | VAR ID type_spec ASSIGN ID expression (SEMI | NEWLINE)+

    | VAR ID return_type type_spec ASSIGN expression (SEMI | NEWLINE)+

    | VAR ID return_type type_spec (SEMI | NEWLINE)+
;
type_spec
    : STRING
    | FLOAT
    | BOOLEAN
    | INT
    | 'str'
    | ID
    ;

constants_declared
    : CONST ID ASSIGN constant_expression (SEMI|NEWLINE)+
    ;

constants_declared2
    : CONST ID ASSIGN constant_expression (SEMI|NEWLINE)+
    ;

constant_expression
    : expression
    ;

//FUNCTION--------------------delcared
function_declared
    : FUNC ID LPAREN parameter_list? RPAREN (return_type)? ID? function_body
    
    ;

parameter_list
    : parameter type_spec
    | parameter ',' parameter_list
    ;

parameter
    : ID parameter_type
    ;

parameter_type
    : type_spec 
    | '[' INT_LIT ']' parameter_type 
    |
    ;

return_type
    : type_spec           // Kiểu dữ liệu thông thường
    | array_type ID?          // Kiểu mảng
    ;

array_type
    : '[' INT_LIT ']' '[' INT_LIT ']' ID?  // Mảng nhiều chiều
    | '[' INT_LIT ']' ID? type_spec?
    ;

function_body
    : '{' NEWLINE* statement_with_newlines? '}' (SEMI|NEWLINE)+
    ;

//function_body2 :  '{' statement2 '}' SEMI?;
// '{' statement_with_newlines SEMI? NEWLINE* '}'

statement_with_newlines
    : statement2 statement_with_newlines
    | statement2 
    ;


statement_list
    : statement
    | statement recursive_newlines statement_list
    ;

//METHOD-------------------------------declared
method_declared
    : FUNC '(' receiver ')' ID? '(' parameter_list2? ')' return_type function_body
    | FUNC '(' receiver ')' ID? '(' parameter_list2? ')' ID function_body
    | FUNC '(' receiver ')' ID? '(' parameter_list2 ')' function_body
    | FUNC '(' receiver ')' ID? '(' parameter_list2 ')' function_body
    | FUNC '(' receiver ')' ID? '('  ')' function_body
    | FUNC ID LPAREN RPAREN function_body
    | FUNC '(' receiver2 ')' ID '(' ')' return_type function_body
    ;

parameter_list2
    : parameter2 (',' parameter2)*
    ;
parameter2
    : ID return_type?
    ;


receiver
    : ID? ID?
    ;
receiver2: ID ID
    ;
//STRUCT-----------------------------------------declared
struct_declared
    : TYPE ID STRUCT '{' NEWLINE* field+ NEWLINE* '}' (SEMI | NEWLINE) // Có thể chứa danh sách các field hoặc rỗng
    ;

field_list
    : field ( (SEMI | NEWLINE) field )* SEMI
    | return_type
    ;
field
    : ID return_type (SEMI|NEWLINE)+      
    | declared3
    ;
//INTERFACE-----------------------------------------declared
interface_declared
    : TYPE ID INTERFACE '{' NEWLINE* method_decl+ NEWLINE* '}' (SEMI|NEWLINE)+
    ;

optional_newlines
    : /* empty */
    | NEWLINE optional_newlines
    ;

method_list
    : method_decl
    ;

recursive_newlines
    : NEWLINE
    | NEWLINE recursive_newlines
    ;

method_decl
    : ID '(' parameter_list? ')' return_type? (SEMI|NEWLINE)+
    ;

method_signature
    : ID '(' parameter_list? ')' (return_type)? (SEMI)?
    ;





// Keywords
IF: 'if';
ELSE: 'else';
FOR: 'for';
RETURN: 'return';
FUNC: 'func';
TYPE: 'type';
STRUCT: 'struct';
INTERFACE: 'interface';
STRING: 'string';
INT: 'int';
FLOAT: 'float';
BOOLEAN: 'boolean';
CONST: 'const';
VAR: 'var';
CONTINUE: 'continue';
BREAK: 'break';
RANGE: 'range';
NIL: 'nil';
TRUE: 'true';
FALSE: 'false';


ADD: '+';
SUB: '-';
MUL: '*';
DIV: '/';
MOD: '%';

EQUAL: '==';
NOTEQUAL: '!=';
LESS: '<';
LESSEQUAL: '<=';
GREATER: '>';
GREATEREQUAL: '>=';

AND: '&&';
OR: '||';
NOT: '!';

ASSIGN: '=';
ADD_ASSIGN: '+=';
SUB_ASSIGN: '-=';
MUL_ASSIGN: '*=';
DIV_ASSIGN: '/=';
MOD_ASSIGN: '%=';
COLON_ASSIGN: ':=';

DOT: '.';

LPAREN: '(';
RPAREN: ')'; // Right Parenthesis
LBRACE: '{'; // Left Brace
RBRACE: '}'; // Right Brace
LBRACK: '['; // Left Bracket
RBRACK: ']'; // Right Bracket
SEMI: ';'; // Semicolon
COLON: ':'; // Semicolon
COMMA: ',';
ID: [a-zA-Z_][a-zA-Z0-9_]*;

//Decimal
INT_LIT
 : ('0' | [1-9][0-9]*); 
// Binary integers  
BIN_LIT: '0' [bB] [01]+;
// Octal integers
OCT_LIT: '0' [oO] [0-7]+;
// Hexadecimal Literals
HEX_LIT: '0' [xX] [0-9a-fA-F]+ ;


REAL
 : DIGITS '.' DIGITS? EXPONENT?     
 | '0' '.' DIGITS? EXPONENT?        
 ;

fragment DIGITS: [0-9]+;

fragment EXPONENT
 : [eE] [+\-]? DIGITS; 

fragment VALID_ESC
  : '\\' [rnt"\\]    // valid: \r, \n, \t, \", \\
  ;
fragment ESCAPE: '\\' [trn\\"];
fragment IL_ESCAPE: '\\' ~[trn\\"];
    // Rule for illegal escape sequences
ILLEGAL_ESCAPE
  : '"'
      (
        ~["\\\r\n]    // normal characters (except " or \, and no newlines)
      | VALID_ESC     // \r, \n, \t, \", \\
      )*
      
      '\\' ~[rnt"\\\r\n]   // e.g. \b, \f, \q, etc.
      .*?
    '"'
    {
      raise IllegalEscape("\"" + self.text[1:-1])  
    }
  ;

    //STRING literals
STRING_LIT
  : '"'
      (
        ~["\\\r\n]
      | VALID_ESC        // \r, \n, \t, \" or \\
      )*
    '"'
  ;
NEWLINE: '\r'? '\n' {
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
    };
WS
  : [ \t\f\r]+ -> skip;



MULTI_COMMENT: 
    '/*' ( MULTI_COMMENT | .)*? '*/' -> skip
    ;
LINE_COMMENT
  : '//' ~[\r\n]* -> skip;            



// Rule for unclosed strings
UNCLOSE_STRING
  : '"'
      ( ~[\\\n"] | VALID_ESC )*
      ( '\r'? '\n' | EOF )
    {
      if self.text[-1] == '\n':
         raise UncloseString("\"" + self.text[1:-1])
      else:
         raise UncloseString("\"" + self.text[1:])
    }
  ;

ERROR_CHAR: . {raise ErrorToken(self.text)};
