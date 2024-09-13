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
print(logo)
def add(n1, n2):
    """Adding two number"""
    return n1 + n2

def subtract(n1, n2):
    """Subtracting one number from another"""
    return n1 - n2

def multiply(n1, n2):
    """Multiply two number"""
    return n1 * n2

def divide(n1, n2):
    """Divide one number form another number"""
    return n1 / n2

calculater = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide
}
result = 0
is_continue = True
start_with_new = True
while is_continue:

    if start_with_new:
        number1 = int(input("give a number 1: "))
    else:
        number1 = result
    for symbol in calculater:
        print(symbol)
    sign = input("enter the operation: ")
    number2 = int(input("give a number 2: "))

    result = calculater[sign](number1,number2)
    print(f"{number1} {sign} {number2} = {result}")
    ans = input("Start with result 'y', Start with new 'n', Exit program 'exit' ").lower()
    if ans == "y":
        start_with_new=False
    elif ans == "n":
        start_with_new=True
        result=0
        print("\n" * 20)
    elif ans == "exit":
        is_continue = False
    else:
        print("Invalid Choice")
        is_continue = False








