# This program acts as a calculator that can perform basic math operations for the user.


CALC_ART = """
 _____________________
|  _________________  |
| | Calculator   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

# Gets input from the user and validates the answer.
# Parameter:
#   - input_type: 
#       - "YN" for "Y" or "N"
#       - "OP" for an operation in the operations dictionary
#       - "FLOAT" for a float number
# Returns a validated string.
def get_input(input_type):
    '''Gets input from the user and validates the answer.'''

    while True:

        # Get input from user.
        # Strip it of whitespace.
        ans = input(f"> ").strip()

        if len(ans) == 0:
           print(f"Oops, you did not enter anything...\n")

        if input_type == "YN":
            if ans[0].upper() == "Y":
                return "Y"
            elif ans[0].upper() == "N":
                return "N"
            else:
                print(f"Oops, I can't accept {ans}. Please enter Y or N...\n")

        elif input_type == "OP":
            if ans in operations.keys():
                return ans
            else:
                print(f"Oops, I can't accept {ans}. Please enter one of the above operations...\n")
        
        elif input_type == "FLOAT":
            try:
                return float(ans)
            except:
                print(f"Oops, I can't accept {ans}. Please enter a number...\n")

        else:
            print(f"Error: Cannot interpret input type {input_type}.\n")
            return ""


def calculate():
    '''Asks user for two numbers and an operation to perform, then prints the calculated results.'''
        
    print("\nWhat's the first number?")
    num1 = float(get_input("FLOAT"))

    op_str = ""
    for o in operations:
        op_str += o + " "

    print(f"\nWhich operation would you like to perform?\nEnter one of these symbols: {op_str}")
        
    operation_symbol = get_input("OP")

    print("\nWhat's the second number?")
    num2 = float(get_input("FLOAT"))

    chosen_function = operations[operation_symbol]
    result = chosen_function(num1, num2)
    print(f"\nResult:  {num1} {operation_symbol} {num2} = {result}")


def main():
    '''Main function. Loops calculations until user quits.'''
    print(CALC_ART)

    quit_program = False
    while not quit_program:

        calculate()

        print("\nWould you like me to do another calculation? [Y/N]")

        if get_input("YN") == "N":
            print("\nGoodbye!\n")
            quit_program = True

        print("\n================================================")

main()
