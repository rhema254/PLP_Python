# This assignment is all about arithmetic operations and user input.


a = int(input("Enter a number:  "))
print(a)
b = int(input("Enter your second operand:  "))
print(b)
operator = input("Enter your operator:  ")
print(operator)


if operator == "+":
    operation = a + b
elif operator == "-":
    operation = a-b
elif operator == "/":
    operation = a/b
elif operator == "*":
    operation = a * b
else:
    print("Invalid operator")    

print(a, operator, b , "=" , operation)