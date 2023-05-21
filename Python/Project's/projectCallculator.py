logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
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
#Add
def add(n1, n2):
    return n1 + n2
#Subtract
def substract(n1, n2):
    return n1 - n2
#Multiply
def multiply(n1, n2):
    return n1 * n2
#Divide
def divide(n1, n2):
    return n1 / n2
operations = {
    "+": add,
    "-": substract,
    "*": multiply,
    "/": divide
}

def calculator():
    print(logo)
    num1 = float(input("What's the first number?: "))
    continueCalculating = False
    while not continueCalculating:
        for symbol in operations:
            print(symbol)
        operationSymbol = input("Pick an operation from the line above: ")

        if operationSymbol not in operations:
            print("Invalid operation")
            continue
        else:
            num2 = float(input("What's the next number?: "))
            function = operations[operationSymbol]
            answer = function(num1, num2)
            print(f"{num1} {operationSymbol} {num2} = {answer}")
            anOther = input(f"Type 'y' to continue calculating with {answer}, \
or type 'n' to exit the calculator: ")
            if anOther == "n":
                continueCalculating = True
            else:
                num1 = answer

calculator()