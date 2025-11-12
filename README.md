# TraceLang - Procedural Programming Language with Memory Tracing

TraceLang is a procedural programming language designed to simplify memory management and variable tracking. The language's main feature is the ability to automatically track variable history and access previously computed values without additional code complexity.

## Key Features

### 1. Automatic Memory Tracing

TraceLang's unique feature is the `trace` keyword, which automatically tracks all changes to a variable throughout program execution. This allows you to:

- Monitor how variables change over time
- Debug algorithms by seeing the history of calculations
- Understand program flow without manual logging

### 2. Complete Type System

- **int** - Integer numbers
- **float** - Floating-point numbers
- **string** - Text strings
- **bool** - Boolean values (true/false)
- **array<T>** - Arrays of any type

### 3. Control Structures

- **if/else** - Conditional statements
- **while** - While loops
- **for** - For loops with initialization, condition, and update

### 4. Functions

- Function declarations with return types
- Parameters with type declarations
- Return statements

### 5. Operators

- **Arithmetic**: `+`, `-`, `*`, `/`, `%`
- **Comparison**: `==`, `!=`, `<`, `>`, `<=`, `>=`
- **Logical**: `&&`, `||`, `!`
- **Assignment**: `=`, `+=`, `-=`, `*=`, `/=`
- **Increment/Decrement**: `++`, `--`

## Installation

### Prerequisites

- Python 3.6 or higher
- PLY (Python Lex-Yacc) library

### Setup

```bash
# Install PLY
pip install ply

# Clone or download the TraceLang repository
cd tracelang
```

## Usage

### Running a TraceLang Program

```bash
python tracelang_compiler.py <source_file.tl>
```

### Example

```bash
python tracelang_compiler.py examples/fibonacci.tl
```

## Language Syntax

### Variable Declarations

```tracelang
// Basic declarations
int x = 5;
float pi = 3.14159;
string name = "TraceLang";
bool isActive = true;

// Traced variables (automatically tracked)
trace int counter = 0;
trace float result = 0.0;
```

### Control Structures

#### If/Else

```tracelang
int age = 18;
if (age >= 18) {
    print("Adult");
} else {
    print("Minor");
}
```

#### While Loop

```tracelang
int count = 0;
while (count < 5) {
    print("Count: " + count);
    count++;
}
```

#### For Loop

```tracelang
for (int i = 0; i < 10; i++) {
    print("i = " + i);
}
```

### Functions

```tracelang
function int add(int a, int b) {
    return a + b;
}

function float multiply(float x, float y) {
    return x * y;
}

int result = add(5, 3);
print("Result: " + result);
```

### Arrays

```tracelang
// Array declaration
array<int> numbers = [1, 2, 3, 4, 5];

// Array access
int first = numbers[0];
print("First element: " + first);

// Array length
int len = length(numbers);

// Array modification
numbers[2] = 10;

// Array iteration
for (int i = 0; i < length(numbers); i++) {
    print("numbers[" + i + "] = " + numbers[i]);
}
```

### Comments

```tracelang
// This is a single-line comment
int x = 5; // Comments can also be at the end of a line
```

## The Trace Feature

The trace feature is TraceLang's most powerful capability. By marking variables with the `trace` keyword, you automatically track their entire history.

### Example: Fibonacci with Trace

```tracelang
function int fibonacci(int n) {
    if (n <= 1) {
        return n;
    }

    trace int prev = 0;
    trace int curr = 1;

    int i = 2;
    while (i <= n) {
        trace int temp = curr + prev;
        prev = curr;
        curr = temp;
        i++;
    }

    return curr;
}

trace int result = fibonacci(6);
print("Fibonacci(6) = " + result);
```

### Trace Output

When you run a program with traced variables, TraceLang automatically generates a `Trace.txt` file:

```
======================================
Trace.txt:

Main -> Fibonacci -> prev 0
Main -> Fibonacci -> curr 1
Main -> Fibonacci -> temp 1
Main -> Fibonacci@1 prev 1
Main -> Fibonacci@1 curr 1
Main -> Fibonacci@1 temp 2
Main -> Fibonacci@2 prev 1
Main -> Fibonacci@2 curr 2
Main -> Fibonacci@2 temp 3
Main -> Fibonacci@3 prev 2
Main -> Fibonacci@3 curr 3
Main -> Fibonacci@3 temp 5
Main -> Fibonacci@4 prev 3
Main -> Fibonacci@4 curr 5
Main -> Fibonacci@4 temp 8
Main -> Fibonacci@5 prev 5
Main -> Fibonacci@5 curr 8
Main -> result 8

curr: 8
prev: 5
result: 8
temp: 8
```

The trace output shows:

- **Context**: Which function the variable is in (e.g., `Main -> Fibonacci`)
- **Iteration**: How many times the variable has been updated (e.g., `@1`, `@2`)
- **Variable name and value**: The current value after each update
- **Final values**: Summary of all traced variables at the end

## Built-in Functions

### `print(expression)`

Outputs a value to the console. Automatically converts all types to strings.

```tracelang
print("Hello, World!");
print(42);
print(3.14);
print(true);
```

### `length(array)`

Returns the length of an array.

```tracelang
array<int> nums = [1, 2, 3, 4, 5];
int len = length(nums);
print("Length: " + len); // Output: Length: 5
```

## Examples

The `examples/` directory contains several demonstration programs:

1. **fibonacci.tl** - Fibonacci sequence with trace feature
2. **trace_demo.tl** - Various trace feature demonstrations
3. **complete_demo.tl** - Comprehensive feature showcase
4. **array_demo.tl** - Array operations and manipulation

## Project Structure

```
tracelang/
├── tracelang_lexer.py       # Lexical analyzer (tokenization)
├── tracelang_parser.py      # Syntax analyzer (parsing)
├── tracelang_interpreter.py # Interpreter and trace system
├── tracelang_compiler.py    # Main compiler entry point
├── examples/                # Example programs
│   ├── fibonacci.tl
│   ├── trace_demo.tl
│   ├── complete_demo.tl
│   └── array_demo.tl
└── README.md               # This file
```

## Technical Details

### Implementation

- **Language**: Python 3
- **Parser Generator**: PLY (Python Lex-Yacc)
- **Execution Model**: Tree-walking interpreter

### Components

1. **Lexer** (`tracelang_lexer.py`): Tokenizes the source code
2. **Parser** (`tracelang_parser.py`): Builds an Abstract Syntax Tree (AST)
3. **Interpreter** (`tracelang_interpreter.py`): Executes the AST with trace tracking
4. **Compiler** (`tracelang_compiler.py`): Coordinates the compilation and execution

### Trace System

The trace system uses:

- **TraceSystem class**: Manages variable history and trace output
- **Environment class**: Handles variable scoping
- **Call stack tracking**: Records function call context
- **Automatic file generation**: Creates `Trace.txt` with formatted output

## Why TraceLang?

### Traditional Debugging

```python
# Python - Manual logging
x = 0
print(f"x = {x}")
x = 5
print(f"x = {x}")
x = 10
print(f"x = {x}")
```

### TraceLang Debugging

```tracelang
// TraceLang - Automatic tracking
trace int x = 0;
x = 5;
x = 10;
// Trace.txt automatically generated!
```

## Advantages

1. **Automatic History Tracking**: No need to manually log variable changes
2. **Algorithm Analysis**: Easily understand how algorithms work
3. **Debugging**: Quickly identify where variables get incorrect values
4. **Educational**: Great for learning programming and understanding algorithms
5. **Clean Code**: No debugging code polluting your source files

## Limitations

- Tracing uses additional memory to store variable history
- Not suitable for production systems where memory is critical
- Best used for debugging, learning, and algorithm analysis

## Future Enhancements

Potential future additions to TraceLang:

- [ ] Structs/records for custom data types
- [ ] More built-in functions (min, max, sort, etc.)
- [ ] File I/O operations
- [ ] Error handling (try/catch)
- [ ] Interactive trace viewer
- [ ] Trace filtering and querying
- [ ] Performance profiling

## Contributing

TraceLang is an educational project. Suggestions and improvements are welcome!

## License

This project is for educational purposes.

## Author

Created as a demonstration of programming language design and implementation.

---

**TraceLang** - Making memory tracking simple and automatic! 🚀
