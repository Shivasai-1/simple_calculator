num1 = float(input("Enter first number: ")) # --> GETS INPUT FROM THE USER AND CONVERTS IT TO FLOAT

op = input("Enter operator: ") # --> GETS INPUT FROM THE USER

num2 = float(input("Enter second number: ")) # --> GETS INPUT FROM THE USER AND CONVERTS IT TO FLOAT

if op == "+": # --> IF STATEMENT TO CHECK THE OPERATOR
    print(num1 + num2)  # --> PRINTS THE SUM OF THE TWO NUMBERS

elif op == "-": # --> ELSE IF STATEMENT TO CHECK THE OPERATOR
    print(num1 - num2) # --> PRINTS THE DIFFERENCE OF THE TWO NUMBERS

elif op == "/": # --> ELSE IF STATEMENT TO CHECK THE OPERATOR
    print(num1 / num2) # --> PRINTS THE QUOTIENT OF THE TWO NUMBERS

elif op == "*": # --> ELSE IF STATEMENT TO CHECK THE OPERATOR
    print(num1 * num2) # --> PRINTS THE PRODUCT OF THE TWO NUMBERS

else:
    print("Invalid operator") # --> ELSE STATEMENT TO HANDLE INVALID OPERATOR