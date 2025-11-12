# tracelang_compiler.py
import sys

from tracelang_interpreter import Environment, TraceSystem, run
from tracelang_lexer import lexer
from tracelang_parser import parser


def main():
    if len(sys.argv) < 2:
        print("Usage: python tracelang_compiler.py <sourcefile>")
        print("Example: python tracelang_compiler.py examples/demo.tl")
        return

    source_file = sys.argv[1]
    try:
        with open(source_file, "r", encoding="utf-8") as f:
            code = f.read()
    except FileNotFoundError:
        print(f"Error: File '{source_file}' not found")
        return
    except Exception as e:
        print(f"Error reading file: {e}")
        return

    # Parse the code
    try:
        ast = parser.parse(code, lexer=lexer)
        if ast is None:
            print("Error: Failed to parse code")
            return
    except Exception as e:
        print(f"Parse error: {e}")
        return

    # Execute the code
    try:
        env = Environment()
        trace_system = TraceSystem()
        functions = {}

        run(ast, env, trace_system, functions)

        # Write trace output if any traced variables exist
        if trace_system.trace_vars:
            trace_system.write_trace_file()

    except Exception as e:
        print(f"Runtime error: {e}")
        import traceback

        traceback.print_exc()
        return


if __name__ == "__main__":
    main()
