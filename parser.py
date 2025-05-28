
def simple_parser(tokens):
    ast = []
    i = 0

    print("Starting Syntax Analysis...\n")

    while i < len(tokens):
        token = tokens[i]

        if token[0] == 'ID' and i + 2 < len(tokens) and tokens[i+1][1] == '=':
            var = tokens[i][1]
            val = tokens[i+2][1]
            ast.append(('assign', var, val))
            print(f"Parsed Assignment: {var} = {val}")
            i += 4 

        elif token[0] == 'BUILTIN_FUNC':
            func = token[1]
            args = []
            i += 2  
            while tokens[i][1] != ')':
                if tokens[i][0] not in ('SYMBOL', 'SKIP'):
                    args.append(tokens[i][1])
                i += 1
            ast.append(('builtin_call', func, args))
            print(f"Parsed Function Call: {func} with args {args}")
            i += 2  

        else:
            i += 1

    print("\n AST (Abstract Syntax Tree) Created.\n")
    return ast
