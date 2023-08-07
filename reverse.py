#Problem-  I have to reverse a number/word without using the built in reverse method
#Let's solve the problem-

x = input("Enter the number you want to reverse: ")
n = int(x)
s = 0
while n:         #if n == 115
    r = n % 10    #5
    n //= 10    #11
    s = s + r
    print(r)



#An another way
x = input("Enter the number you want to reverse: ")
n = int(x)
s = 0
while n:         #if n == 115
    r =n % 10  #5
    s = s * 10 + r  #5
    n //= 10 #11
    print(r)
