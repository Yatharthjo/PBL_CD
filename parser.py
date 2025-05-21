# parser.py

def simple_parser(tokens):
    ast = []
    i = 0

    while i < len(tokens):
        token = tokens[i]

        # Variable assignment: a = 10;
        if token[0] == 'ID' and i + 2 < len(tokens) and tokens[i+1][1] == '=':
            var_name = tokens[i][1]
            value = tokens[i+2][1]
            ast.append(('assign', var_name, value))
            i += 4  # Skip ; too

        # Built-in function call: printf("x=%d", x);
        elif token[0] == 'BUILTIN_FUNC':
            func = token[1]
            args = []
            i += 2  # skip function name and '('
            while tokens[i][1] != ')':
                if tokens[i][0] not in ('SYMBOL', 'SKIP'):
                    args.append(tokens[i][1])
                i += 1
            ast.append(('builtin_call', func, args))
            i += 2  # Skip ')' and ';'

        else:
            i += 1

    return ast
