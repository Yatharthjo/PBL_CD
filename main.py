from lexer import lexer
from parser import simple_parser
from semantic import semantic_check
from tac_generator import generate_TAC

def main():
    with open("test_cases/input1.c") as f:
        source_code = f.read()

    print(" Lexical Analysis:")
    tokens = lexer(source_code)
    print(tokens)

    print("\n Syntax Analysis:")
    ast = simple_parser(tokens)
    print(ast)

    print("\n Semantic Analysis:")
    semantic_check(ast)
    print("No semantic errors found.")

    print("\n Three-Address Code:")
    tac = generate_TAC(ast)
    for line in tac:
        print(line)

if __name__ == "__main__":
    main()
