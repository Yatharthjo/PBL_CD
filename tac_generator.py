temp_counter = 0

def new_temp():
    global temp_counter
    temp = f"t{temp_counter}"
    temp_counter += 1
    return temp

def generate_TAC(ast):
    code = []
    for stmt in ast:
        if stmt[0] == 'assign':
            temp = new_temp()
            code.append(f"{temp} = {stmt[2]}")
            code.append(f"{stmt[1]} = {temp}")
        elif stmt[0] == 'builtin_call':
            func, args = stmt[1], stmt[2]
            code.append(f"call {func}({', '.join(args)})")
    return code
