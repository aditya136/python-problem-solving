#Factorail code


#Using function
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)
    
number = int(input("Factorial Number: "))
n = number
print(factorial(n))




#We can also do it with the help of for loop
def factorial(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    
    result = 1
    for i in range(1, n + 1):
        result *= i
    
    return result


number = int(input("Factorial Number: "))
n = number
print(factorial(n))