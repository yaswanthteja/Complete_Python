
# Import the dis module which supports the analysis of CPython bytecode
import dis

# Define a simple function to illustrate Python's internals
def greet(name):
    # A simple print statement that is more complex than it looks
    print(f'Hello, {name}!')

# Disassemble the greet function to see what's happening under the hood
def disassemble_function():
    dis.dis(greet)

# Call the disassemble function
disassemble_function()