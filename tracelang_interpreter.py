# tracelang_interpreter.py
import sys


class TraceSystem:
    """System for tracking variable history"""

    def __init__(self):
        self.traces = {}  # {var_name: [history of values]}
        self.trace_vars = set()  # Set of variables marked for tracing
        self.call_stack = ["Main"]  # Track function calls
        self.trace_output = []  # Store trace output lines

    def mark_traced(self, var_name):
        """Mark a variable for tracing"""
        self.trace_vars.add(var_name)
        if var_name not in self.traces:
            self.traces[var_name] = []

    def update(self, var_name, value):
        """Update trace history for a variable"""
        if var_name in self.trace_vars:
            self.traces[var_name].append(value)
            # Format trace output
            context = " -> ".join(self.call_stack)
            iteration = len(self.traces[var_name]) - 1
            if iteration > 0:
                line = f"{context}@{iteration} {var_name} {value}"
            else:
                line = f"{context} -> {var_name} {value}"
            self.trace_output.append(line)

    def push_context(self, func_name):
        """Push a new function context"""
        self.call_stack.append(func_name)

    def pop_context(self):
        """Pop function context"""
        if len(self.call_stack) > 1:
            self.call_stack.pop()

    def write_trace_file(self, filename="Trace.txt"):
        """Write trace output to file"""
        if self.trace_output:
            with open(filename, "w", encoding="utf-8") as f:
                f.write("=" * 38 + "\n")
                f.write("Trace.txt:\n\n")
                for line in self.trace_output:
                    f.write(line + "\n")
                f.write("\n")
                # Write final values
                for var_name in sorted(self.trace_vars):
                    if self.traces[var_name]:
                        final_value = self.traces[var_name][-1]
                        f.write(f"{var_name}: {final_value}\n")
            print(f"\nTrace output written to {filename}")


class Environment:
    """Environment for variable storage"""

    def __init__(self, parent=None):
        self.vars = {}
        self.parent = parent

    def get(self, name):
        if name in self.vars:
            return self.vars[name]
        elif self.parent:
            return self.parent.get(name)
        else:
            raise NameError(f"Variable '{name}' is not defined")

    def set(self, name, value):
        self.vars[name] = value

    def update(self, name, value):
        """Update existing variable"""
        if name in self.vars:
            self.vars[name] = value
        elif self.parent:
            self.parent.update(name, value)
        else:
            raise NameError(f"Variable '{name}' is not defined")

    def exists(self, name):
        return name in self.vars or (self.parent and self.parent.exists(name))


class ReturnException(Exception):
    """Exception to handle return statements"""

    def __init__(self, value):
        self.value = value


def run(node, env, trace_system, functions=None):
    """Execute AST node"""
    if functions is None:
        functions = {}

    if node is None:
        return None

    nodetype = node[0]

    # Program
    if nodetype == "program":
        for stmt in node[1]:
            run(stmt, env, trace_system, functions)

    # Block
    elif nodetype == "block":
        for stmt in node[1]:
            run(stmt, env, trace_system, functions)

    # Variable declaration
    elif nodetype == "declare":
        _, var_type, name, init_value, is_traced = node
        value = (
            run(init_value, env, trace_system, functions)
            if init_value
            else get_default_value(var_type)
        )
        env.set(name, value)
        if is_traced:
            trace_system.mark_traced(name)
            trace_system.update(name, value)

    # Assignment
    elif nodetype == "assign":
        _, name, expr = node
        value = run(expr, env, trace_system, functions)
        if env.exists(name):
            env.update(name, value)
        else:
            env.set(name, value)
        # Update trace if variable is traced
        if name in trace_system.trace_vars:
            trace_system.update(name, value)

    # Array assignment
    elif nodetype == "array_assign":
        _, name, index_expr, value_expr = node
        array = env.get(name)
        index = run(index_expr, env, trace_system, functions)
        value = run(value_expr, env, trace_system, functions)
        if not isinstance(array, list):
            raise TypeError(f"'{name}' is not an array")
        if not isinstance(index, int):
            raise TypeError(f"Array index must be an integer")
        if index < 0 or index >= len(array):
            raise IndexError(f"Array index {index} out of range")
        array[index] = value

    # Compound assignment
    elif nodetype == "compound_assign":
        _, name, op, expr = node
        current = env.get(name)
        value = run(expr, env, trace_system, functions)
        if op == "+=":
            result = current + value
        elif op == "-=":
            result = current - value
        elif op == "*=":
            result = current * value
        elif op == "/=":
            result = current / value
        env.update(name, result)
        if name in trace_system.trace_vars:
            trace_system.update(name, result)

    # Increment/Decrement
    elif nodetype == "inc_dec":
        _, name, op = node
        current = env.get(name)
        result = current + 1 if op == "++" else current - 1
        env.update(name, result)
        if name in trace_system.trace_vars:
            trace_system.update(name, result)

    # If statement
    elif nodetype == "if":
        _, condition, then_stmt, else_stmt = node
        if run(condition, env, trace_system, functions):
            run(then_stmt, env, trace_system, functions)
        elif else_stmt:
            run(else_stmt, env, trace_system, functions)

    # While loop
    elif nodetype == "while":
        _, condition, body = node
        while run(condition, env, trace_system, functions):
            run(body, env, trace_system, functions)

    # For loop
    elif nodetype == "for":
        _, init, condition, update, body = node
        loop_env = Environment(env)
        if init:
            run(init, loop_env, trace_system, functions)
        while run(condition, loop_env, trace_system, functions):
            run(body, loop_env, trace_system, functions)
            if update:
                run(update, loop_env, trace_system, functions)

    # Function declaration
    elif nodetype == "function":
        _, return_type, name, params, body = node
        functions[name] = (return_type, params, body)

    # Return statement
    elif nodetype == "return":
        _, value = node
        result = run(value, env, trace_system, functions) if value else None
        raise ReturnException(result)

    # Print statement
    elif nodetype == "print":
        value = run(node[1], env, trace_system, functions)
        print(value)

    # Binary operations
    elif nodetype == "binop":
        _, op, left, right = node
        l = run(left, env, trace_system, functions)
        r = run(right, env, trace_system, functions)

        if op == "+":
            # Handle string concatenation with automatic type conversion
            if isinstance(l, str) or isinstance(r, str):
                return str(l) + str(r)
            return l + r
        elif op == "-":
            return l - r
        elif op == "*":
            return l * r
        elif op == "/":
            if r == 0:
                raise ZeroDivisionError("Division by zero")
            return l / r
        elif op == "%":
            return l % r
        elif op == "==":
            return l == r
        elif op == "!=":
            return l != r
        elif op == "<":
            return l < r
        elif op == ">":
            return l > r
        elif op == "<=":
            return l <= r
        elif op == ">=":
            return l >= r
        elif op == "&&":
            return l and r
        elif op == "||":
            return l or r

    # Unary operations
    elif nodetype == "unop":
        _, op, expr = node
        value = run(expr, env, trace_system, functions)
        if op == "!":
            return not value
        elif op == "-":
            return -value

    # Literals
    elif nodetype == "num":
        return node[1]

    elif nodetype == "float":
        return node[1]

    elif nodetype == "string":
        return node[1]

    elif nodetype == "bool":
        return node[1]

    # Variable reference
    elif nodetype == "var":
        return env.get(node[1])

    # Array literal
    elif nodetype == "array":
        _, elements = node
        return [run(elem, env, trace_system, functions) for elem in elements]

    # Array access
    elif nodetype == "array_access":
        _, name, index_expr = node
        array = env.get(name)
        index = run(index_expr, env, trace_system, functions)
        if not isinstance(array, list):
            raise TypeError(f"'{name}' is not an array")
        if not isinstance(index, int):
            raise TypeError(f"Array index must be an integer")
        if index < 0 or index >= len(array):
            raise IndexError(f"Array index {index} out of range")
        return array[index]

    # Function call
    elif nodetype == "call":
        _, func_name, args = node

        # Built-in function: length
        if func_name == "length":
            if len(args) != 1:
                raise TypeError(
                    f"length() takes exactly 1 argument ({len(args)} given)"
                )
            arr = run(args[0], env, trace_system, functions)
            if not isinstance(arr, list):
                raise TypeError("length() argument must be an array")
            return len(arr)

        # User-defined function
        if func_name not in functions:
            raise NameError(f"Function '{func_name}' is not defined")

        return_type, params, body = functions[func_name]

        if len(args) != len(params):
            raise TypeError(
                f"Function '{func_name}' takes {len(params)} arguments ({len(args)} given)"
            )

        # Create new environment for function
        func_env = Environment(env)
        for (param_type, param_name), arg in zip(params, args):
            arg_value = run(arg, env, trace_system, functions)
            func_env.set(param_name, arg_value)

        # Push function context for tracing
        trace_system.push_context(func_name.capitalize())

        try:
            run(body, func_env, trace_system, functions)
            result = None
        except ReturnException as ret:
            result = ret.value
        finally:
            trace_system.pop_context()

        return result

    else:
        print(f"Unknown node type: {nodetype}")
        return None


def get_default_value(var_type):
    """Get default value for a type"""
    if var_type == "int":
        return 0
    elif var_type == "float":
        return 0.0
    elif var_type == "string":
        return ""
    elif var_type == "bool":
        return False
    elif isinstance(var_type, tuple) and var_type[0] == "array_type":
        return []
    else:
        return None
