def calculator(num1, num2, operator):  # method or function or procedure declaration
    result = 0
    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
        result = num1 / num2
    else:
        print("Input operator is not recognized! ")
    print(result)


num1 = int(input("Enter your first number: "))
num2 = int(input("Enter your second number: "))

print("Enter which operator woud you like to perform? ")

operator = input("Enter any of these value for specific operation +,- ,*,/ : ")

result = calculator(num1, num2, operator) # Metod or procedure or function call

#calculator(num1,num2,operator)
