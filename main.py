# Import the sys module, which provides access to some variables used or maintained by the interpreter and to functions that interact strongly with the interpreter.
import sys

# Initialize a counter variable iota_counter to 0.
iota_counter = 0

# Define a function iota that returns a unique integer each time it's called, unless the reset parameter is True, in which case it resets the counter to 0.
def iota(reset = False):
    global iota_counter
    if reset: iota_counter = 0
    result = iota_counter
    iota_counter += 1
    return result

# Use the iota function to define three constants: PUSH, PLUS, OUT, VAR, FUNC, IF, ELSE.
PUSH = iota(True)
PLUS = iota()
OUT  = iota()
VAR  = iota()
FUNC = iota()
IF   = iota()
ELSE = iota()

# Initialize an empty stack list.
stack = []

# Initialize a variable out_pos to -1, which will be used to keep track of the position of the last output operation.
out_pos = -1

# Initialize a dictionary to store variables.
variables = {}

# Define a function program_to_op that takes a program string as input and returns a tuple containing an operation code, a value, and a position.
def program_to_op(program):
    if program.isdigit():
        return (PUSH, int(program), 0)
    elif program == "+":
        return (PLUS, 0, 0)
    elif program == "out":
        global out_pos
        out_pos += 1
        return (OUT, 0, out_pos)
    elif program == "var":
        return (VAR, 'E', 0)
    # elif program == "func":
    #     return (FUNC, 0, 0)
    # elif program == "if":
    #     return (IF, 0, 0)
    # elif program == "else":
    #     return (ELSE, 0, 0)
    elif program == "push":
        return (PUSH, 0, 0)
    elif "=" in program:
        var_name, var_value = program.split("=")
        var_name = var_name.strip()
        var_value = var_value.strip()
        return (VAR, var_name, var_value)
    elif program.startswith("func "):
        func_name, *args = program.split()
        args = [int(arg) for arg in args[1:]]
        return (FUNC, func_name, args)
    elif program.startswith("if "):
        condition, body = program.split(" ", 1)
        return (IF, condition[3:], body)
    elif program.startswith("else "):
        body = program[5:]
        return (ELSE, 0, body)
    else:
        # Assume it's a variable reference
        return (VAR, 'xa', 0)

def compiler_mode():
    program = """
    var x = 5
    var y = 4
    push 3
    push 3
    + out 
    if 4 < 2
        push 10
        out
    else
        push 20
        out
    """
    # Split the program into lines and process each line
    lines = program.strip().split('\n')
    for line in lines:
        tokens = line.strip().split()
        i = 0
        while i < len(tokens):
            op, value, pos = program_to_op(tokens[i])
            if op == PUSH:
                if value == 0:
                    # This is a 'push' keyword, so we need to push the next token
                    i += 1
                    print("PUSH::",  tokens[i])
                    _, value, _ = program_to_op(tokens[i])
                stack.append(value)
            elif op == PLUS:
                b = stack.pop()
                a = stack.pop()
                print(variables)
                stack.append(int(variables['']) + int(variables['']))
            elif op == OUT:
                if i + 1 < len(tokens) and tokens[i+1] in variables:
                    print(variables[tokens[i+1]])
                    i += 1
                else:
                    print(stack[-1] if stack else None)
            elif op == VAR:
                if isinstance(value, str) and '=' not in tokens[i]:
                    # This is a variable reference
                    stack.append(variables.get(value, 0))
                else:
                    print(value)
                    # This is a variable assignment
                    var_name = value
                    print("NAME::", var_name)
                    print(int(tokens[i+1]))
                    var_value = int(tokens[i+1])
                    print(int(tokens[i+1]))
                    variables[var_name] = var_value
                    i += 1
            elif op == FUNC:
                func_name, *args = value
                if func_name == "add":
                    result = sum(args)
                    stack.append(result)
            elif op == IF:
                condition = value
                print("aa"+tokens[i+1:])
                body = tokens[i+1:]
                if eval(condition, variables):
                    compiler_mode('\n'.join(body))
                break
            elif op == ELSE:
                body = tokens[i+1:]
                compiler_mode('\n'.join(body))
                break
            i += 1

if __name__ == "__main__":
    compiler_mode()