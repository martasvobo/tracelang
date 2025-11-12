# tracelang_interpreter.py
def run(node, env):
    nodetype = node[0]

    if nodetype == "program":
        for stmt in node[1]:
            run(stmt, env)

    elif nodetype == "assign":
        _, name, expr = node
        env[name] = run(expr, env)

    elif nodetype == "print":
        value = run(node[1], env)
        print(value)

    elif nodetype == "binop":
        _, op, left, right = node
        l = run(left, env)
        r = run(right, env)
        return l + r if op == "+" else l - r

    elif nodetype == "num":
        return node[1]

    elif nodetype == "var":
        return env.get(node[1], 0)

    else:
        print("Unknown node:", node)
