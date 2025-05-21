# lexer.py

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

tok_regex = '|'.join('(?P<%s>%s)' % pair for pair in token_spec)

def lexer(code):
    tokens = []
    symbol_table = {}
    current_type = None

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

        elif kind == 'OP' and value == '=':
            if len(tokens) > 0 and tokens[-1][0] == 'ID':
                var = tokens[-1][1]
                if var in symbol_table:
                    symbol_table[var]['initialized'] = True

        if kind not in {'SKIP', 'NEWLINE'}:
            tokens.append((kind, value))

    with open("symbol_table.json", "w") as f:
        json.dump(symbol_table, f, indent=2)

    return tokens
