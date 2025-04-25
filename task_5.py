#Factorial(Recursive)

def factorial(num):
    if num == 0:
        return 1
    else:
        num = num * factorial(num - 1)
        return num
        
print(factorial(5))