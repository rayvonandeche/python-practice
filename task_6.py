#Sum of digits of a number

num = str(input("Enter number: "))
sum_of_digits = 0

for i in range(len(num)):
    sum_of_digits += int(num[i])

print(sum_of_digits)