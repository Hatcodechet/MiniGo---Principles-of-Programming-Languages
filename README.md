# MiniGo - Principles of Programming Languages

## Introduction
MiniGo is a simplified programming language designed for learning the principles of programming languages. It incorporates key concepts from Go while maintaining simplicity for easier parsing and analysis. The language is implemented using **ANTLR** to define its grammar and structure.

## Features
- **Basic data types**: Supports integers, real numbers, booleans, strings, and nil values.
- **Control structures**: Includes if-else statements, loops (for statements), and switch-case.
- **Functions**: Supports function definitions, calls, and returns.
- **Expressions and Operators**: Logical, relational, arithmetic, and unary operators.
- **Variable Declarations**: Supports variable and constant declarations.
- **Structs and Arrays**: Implements structured data and array literals.
- **Error Handling**: Custom error handling with lexing and parsing rules.

## Grammar Definition
MiniGo uses **ANTLR** for defining its grammar rules. The core grammar is structured as follows:

### Program Structure
The MiniGo program consists of:
- **Declarations** (variables, constants, functions)
- **Statements** (assignments, loops, conditionals, function calls)
- **Expressions** (arithmetic, logical, relational)
- **Literals** (integers, strings, booleans, arrays, structs)

### Key Grammar Components
#### 1. **Expressions and Operators**
Expressions follow standard precedence rules and include:
- **Arithmetic operators**: `+`, `-`, `*`, `/`, `%`
- **Logical operators**: `&&`, `||`, `!`
- **Relational operators**: `==`, `!=`, `<`, `>`, `<=`, `>=`
- **Assignment operators**: `=`, `+=`, `-=`, `*=`, `/=`, `%=`

#### 2. **Control Flow**
- **If Statements**: Nested if-else structures with block scoping.
- **For Loops**: Ranges, standard iteration, and conditional for-loops.
- **Break/Continue**: Supports breaking and continuing within loops.

#### 3. **Function Definitions**
- Supports parameterized function declarations.
- Return types are inferred or explicitly defined.
- Function calls are handled with argument lists.

#### 4. **Data Structures**
- **Arrays**: Defined using square brackets and initialized with literals.
- **Structs**: Defined with key-value pairs for complex data representation.

## Installation and Usage
1. Install **ANTLR 4.9.2** if not already installed.
2. Clone this repository and navigate to the `src/main/minigo/parser` directory.
3. Run the following command to generate the parser:
   ```bash
   antlr4 -Dlanguage=Python3 MiniGo.g4
   ```
4. Execute `run.py` to test the MiniGo interpreter.

## Error Handling
MiniGo includes custom error handling in the lexer and parser:
- **Illegal Escape Handling**: Detects incorrect string escape sequences.
- **Unrecognized Tokens**: Throws errors for invalid tokens.
- **Syntax Validation**: Ensures correct grammar structure in MiniGo scripts.

## Future Enhancements
- Implement a type checker for stricter type enforcement.
- Add support for functions with variable arguments.
- Improve error messages for better debugging.
- Extend support for additional data types and operations.

## Contributors
- **Pham Nguyen Viet Tri**
## License
This project is licensed under the MIT License.

