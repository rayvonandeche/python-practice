#Compute factorial using a loop.

num = int(input("Enter a number: "))
product = 1

for i in range(1, num):
    product = product * (i + 1)

print(f"Factorial of {num} is {product}")