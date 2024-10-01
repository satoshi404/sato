import sys

## Try build a compiler in python sato

iota_counter = 0
def iota(reset = False):
    global iota_counter
    if reset: iota_counter ^= iota_counter
    result = iota_counter
    iota_counter += 1
    return result

PUSH = iota(True)
PLUS = iota()
DUMP = iota()
POP  = iota()

stack = [] 

def push(value):
    return (PUSH, value)
def plus():
    return (PLUS,0)
def dump():
    return (DUMP,0)

program = [ push(14520), push(5457), plus(), dump() ] ## This is 10 + 7 = 17 sure

def interpreter_mode():
    for prog in program:
        if prog[0] == PUSH:
            stack.append(prog[1])
        elif prog[0] == PLUS:
            a = stack.pop()
            b = stack.pop()
            stack.append(a + b)
        elif prog[0] == DUMP:
            print(stack[0])
      
def usage():
    print("Usage: python3 sato.py <command> ./exemple.s \nCommands:\n\t-i - interpreter mode\n\t-c - compiler mode\n")
    exit(1)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        usage()
    elif "-i" in sys.argv:
        interpreter_mode()
    elif "-c" in sys.argv:
        usage()
    else:
        usage()
