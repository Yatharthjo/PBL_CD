temp_counter = 0

def new_temp():
    global temp_counter
    temp = f"t{temp_counter}"
    temp_counter += 1
    return temp

def eval_expr(expr, code):
   
    if isinstance(expr, tuple):
        op = expr[0]
        left = expr[1]
        right = expr[2]

   
        left_temp = eval_expr(left, code)
        right_temp = eval_expr(right, code)

        temp = new_temp()
        code.append(f"{temp} = {left_temp} {op} {right_temp}")
        return temp
    else:
        return expr

 
def generate_TAC(ast):
    code = []
    for stmt in ast:
        if stmt[0] == 'assign':
            var_name = stmt[1]
            expr = stmt[2]

            result = eval_expr(expr, code)   
            code.append(f"{var_name} = {result}")  

        elif stmt[0] == 'builtin_call':
            func = stmt[1]
            args = stmt[2]

            
            final_args = [eval_expr(arg, code) for arg in args]
            code.append(f"call {func}({', '.join(final_args)})")

    return code
