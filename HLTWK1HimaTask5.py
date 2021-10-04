#numbers = [1,2,3,4,5]
#input("choose two numebr from the numbers: ")
num1 = int(input("Enter your first number: "))
num2 = int(input("Enter your second number: "))

print ("Enter which operator woud you like to perform?")
x = input("Enter any of these value for specific operation +,- ,*,/: ")
result = 0
if x == '+' :
    result = num1 + num2
elif x == '-':
    result = num1 - num2
elif x == '*':
    result = num1 * num2
elif x == '/':
    result = num1 / num2
else:
    print("Input operator is not recognized! ")
    
print (num1, x, num2, "=", result)