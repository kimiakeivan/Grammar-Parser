import re

# Read the grammar from the input file
with open('Grammar.txt', 'r') as f:
    grammar = f.read()


# Extract the variables, terminals, and rules from the grammar
variables = re.findall(r'Variables:\s*(.*)', grammar)[0].split(', ')
terminals = re.findall(r'Terminals:\s*(.*)', grammar)[0].split(', ')
start_var = re.findall(r'Start_Var:\s*(.*)', grammar)[0]
ruleslist = re.findall(r'Rules:\s*(.*)', grammar, re.DOTALL)[0].split('\n')

rules = {}
for i in ruleslist:
    lhs, rhs = i.strip().split(', ')
    if lhs not in rules:
        rules[lhs] = []
    rules[lhs].append(rhs.split())


# Define a function to parse a given string using the grammar
def parse_string(inp_str):
    stack = [start_var]
    index = 0
    while stack and index < len(inp_str):
        head = stack.pop()
        if head in variables:
            for rhs in rules.get(head, []):
                if rhs[0][0] == inp_str[index] or rhs[0][0] == "0":
                    for sym in rhs:
                        stack.extend(reversed(sym))
                    break
            else:
                return False

        elif head == inp_str[index]:
                index += 1

    return len(stack) == 0


# Test the parser with input strings from console
while True:
    input_string = input("Enter a string (or 'end' to quit): ")
    if input_string == 'end':
        break
    if parse_string(input_string):
        print("The input string is accepted.")
    else:
        print("The input string is not accepted.")
