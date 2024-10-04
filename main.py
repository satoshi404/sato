import sys

iota_counter = 0
def iota(reset = False):
    global iota_counter
    if reset: iota_counter = 0
    result = iota_counter
    iota_counter += 1
    return result

PUSH = iota(True)
PLUS = iota()
OUT  = iota()

stack = []

out_pos = -1
def program_to_op(program):
    if program.isdigit():
        return (PUSH, int(program),0)
    elif program == "+":
        return (PLUS, 0, 0)
    elif program == "out":
        global out_pos
        out_pos += 1
        return (OUT, 0, out_pos)
    
    else:
        assert False, f"Systax invalid! {program}"
        exit(1)

def compiler_mode():
   with open(sys.argv[1] ,"r") as file:
       program = file.read()
       for prog in program.split():
           op, value, pos= program_to_op(prog)
           if op == PUSH:
               stack.append(value)
           elif op == PLUS:
               a = stack.pop()
               b = stack.pop()
               stack.append(a + b)
           elif op == OUT:
               print(stack[pos])


if __name__ == "__main__":
    compiler_mode()
    
