def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)  #didn't understand what happend here

the_num = int(input("Enter the number: "))
print(fibonacci(the_num))