
import re
import json

keywords = {'int', 'float', 'char', 'return'}
builtin_funcs = {'printf', 'scanf'}

token_spec = [
    ('NUMBER',   r'\d+(\.\d+)?'),
    ('ID',       r'[A-Za-z_]\w*'),
    ('OP',       r'[+\-*/=]'),
    ('SYMBOL',   r'[{}();,&]'),
    ('STRING',   r'"[^"]*"'),
    ('SKIP',     r'[ \t]+'),
    ('NEWLINE',  r'\n'),
    ('MISMATCH', r'.'),
]

tok_regex = '|'.join(f'(?P<{name}>{pattern})' for name, pattern in token_spec)

def lexer(code):
    tokens = []
    symbol_table = {}
    current_type = None

    print(" Starting Lexical Analysis...\n")

    for match in re.finditer(tok_regex, code):
        kind = match.lastgroup
        value = match.group()

        if kind == 'ID':
            if value in keywords:
                kind = 'KEYWORD'
                current_type = value  
            elif value in builtin_funcs:
                kind = 'BUILTIN_FUNC'
            else:
                kind = 'ID'
                if current_type and value not in symbol_table:
                    symbol_table[value] = {
                        "type": current_type,
                        "scope": "global",
                        "initialized": False
                    }

        if kind == 'OP' and value == '=':
            if len(tokens) > 0 and tokens[-1][0] == 'ID':
                var_name = tokens[-1][1]
                if var_name in symbol_table:
                    symbol_table[var_name]["initialized"] = True

        if kind not in {'SKIP', 'NEWLINE'}:
            tokens.append((kind, value))


    for t in tokens:
        print(f"Token: {t[0]:<12} | Value: {t[1]}")

    with open("symbol_table.json", "w") as f:
        json.dump(symbol_table, f, indent=2)

    print("\nSymbol Table Generated in 'symbol_table.json'\n")
    return tokens
