def div(a,b):
    return a/b

num_1 = int(input("Write the first number: "))
num_2 = int(input("Write the second number: "))

result = div(num_1, num_2)

if num_1 == 0:
    print("Error")
else:
    print(f"The division of {num_1} and {num_2} is {result}")
