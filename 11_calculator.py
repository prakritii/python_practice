def add(num_1, num_2):
    return num_1 + num_2

def subtraction(num_1, num_2):
    return num_1 - num_2

def multiplication(num_1, num_2):
    return num_1 * num_2

def division(num_1, num_2):
    if num_2 == 0:
        print("Cannot divided by 0")
        return " "
    return num_1 / num_2

num1 = int(input("Enter the first number: "))
operator = input("Enter the mathmatical sign(+,-,*,/): ")
num2 = int(input("Enter the second number: "))

if operator == "+":
    print(add(num_1=num1, num_2=num2))
elif operator == "-":
    print(subtraction(num_1=num1, num_2=num2))
elif operator == "*":
    print(multiplication(num_1=num1, num_2=num2))
elif operator == "/":
    print(division(num_1=num1, num_2=num2))
else:
    print("Envalid operator")