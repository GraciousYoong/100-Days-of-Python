import calc_pics

def clear_screen():
    print("\n" * 100)

def add(first_num: float, second_num: float) -> float:
    return first_num + second_num

def substract(first_num: float, second_num: float) -> float:
    return first_num - second_num

def multiply(first_num: float, second_num: float) -> float:
    return first_num * second_num

def divide(first_num: float, second_num: float) -> float:
    return first_num / second_num

def calculation() -> None:
    print(calc_pics.logo)
    operations = {
    "+":add,
    "-":substract,
    "*":multiply,
    "/":divide
    }
    first_num = float(input("What is the first number?: "))
    for symbol in operations:
        print(symbol)
    should_continue = True
    while should_continue == True:
        operation_symbol = input("Pick an  operation: ")
        while operation_symbol != "+" and operation_symbol  != "-" and operation_symbol != "*" and operation_symbol != "/":
            print("Please pick ONE: '+', '-', '*' and '/'")
            operation_symbol = input("Pick an  operation: ")
        next_num = float(input("What is the next number?: "))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(first_num, next_num)
        print(f"{first_num} {operation_symbol} {next_num} = {answer}")
        if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ") == "y":
            first_num = answer
        else:
            should_continue = False
            clear_screen()
            calculation()
calculation()


## Alternative way:
# def calc():
#     print(calc_pics.logo)
#     first_num = int(input("What is the first number?: "))
#     answer = operation(first_num)
#     to_continue = True
#     while to_continue == True:
#         user_input = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ")
#         if user_input == "y":
#             answer = operation(answer)
#         else:
#             to_continue = False
#             clear_screen()
#             calc()

# def operation(first_num: int) -> int:
#     print('''+
# -
# *
# /''')
#     operation = input("Pick an  operation: ")
#     while operation != "+" and operation  != "-" and operation != "*" and operation != "/":
#         print("Please pick ONE: '+', '-', '*' and '/'")
#         operation = input("Pick an  operation: ")
#     next_num = int(input("What is the next number?: "))
#     if operation == "+":
#         answer = first_num + next_num
#     elif operation == "-":
#         answer = first_num - next_num
#     elif operation == "*":
#         answer = first_num * next_num
#     elif operation == "/":
#         answer = first_num / next_num
#     print(f"{first_num} + {next_num} = {answer}")
#     return answer

# calc()