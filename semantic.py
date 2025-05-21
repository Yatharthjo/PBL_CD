import json

def semantic_check(ast):
    with open("symbol_table.json") as f:
        symtab = json.load(f)

    for stmt in ast:
        if stmt[0] == 'assign':
            var = stmt[1]
            if var not in symtab:
                raise Exception(f"Semantic Error: Variable '{var}' not declared.")
        elif stmt[0] == 'builtin_call':
            for arg in stmt[2]:
                if arg.startswith('"') or arg.startswith('%') or arg.startswith('&'):
                    continue
                if arg not in symtab:
                    raise Exception(f"Semantic Error: Argument variable '{arg}' not declared.")
