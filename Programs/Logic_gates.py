def get_boolean_input(prompt):
    while True:
        response = input(prompt)
        if response.lower() in ['true', 't', 'yes', 'y', '1']:
            return True
        elif response.lower() in ['false', 'f', 'no', 'n', '0']:
            return False
        else:
            print("Invalid input. Please enter 'true', 't', 'yes', 'y', '1', 'false', 'f', 'no', 'n', or '0'.")

# Testing the XNOR gate with user input
input1 = get_boolean_input("Enter a boolean value for input 1 (true/false/t/f/yes/no/1/0): ")
input2 = get_boolean_input("Enter a boolean value for input 2 (true/false/t/f/yes/no/1/0): ")




def and_gate(input1, input2):
    return input1 and input2

def or_gate(input1, input2):
    return input1 or input2

def not_gate(input):
    return not input

def nor_gate(input1, input2):
    return not (input1 or input2)

def nand_gate(input1, input2):
    return not (input1 and input2)

def xor_gate(input1, input2):
    return (input1 and not input2) or (not input1 and input2)

def xnor_gate(input1, input2):
    return not (input1 ^ input2)

print(xnor_gate(input1, input2))