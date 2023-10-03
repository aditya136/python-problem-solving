#2+4+6+8+10          == red circle in Nyon da's copy book
s = 0
for i in range(2, 11, 2):
    s += i
print(s)



#1+3+5+7+9           == blue circle in Nyon da's copy book
s = 0
for i in range(1, 11, 2):
    s += i
print(s)



#1.5 + 2.5 + 3.5 + 4.5 + 5.5 + 6.5 + 7.5 + 8.5 + 9.5 + 10.5                     == yellow circle in Nyon da's copy book
s = 0 
for i in range(1, 11):
    s += i + 0.5
print(s)



#1^2 + 2^2 + 3^2 + 4^2 + 5^2 + 6^2 + 7^2 + 8^2 + 9^2 + 10^2                 == green circle in Nyon da's copy book
s = 0
for i in range(1, 11):
    s += i * i 
print(s)



#1^3 + 2^3 + 3^3 + 4^3 + 5^3 + 6^3 + 7^3 + 8^3 + 9^3 + 10^3                         == orange circle in Nyon da's copy book
s = 0
for i in range(1,11):
    s += i * i * i 
print(s)



#1 + 1/2 + 1/3 + 1/4 + 1/5 + 1/6 + 1/7 + 1/8 + 1/9 + 1/10                    == ass/white circle in Nyon da's copy book
s = 0
for i in range(1,11):
    s += 1/i 
print(s)



# #1*2 + 2*3 + 3*4 + 4*5 + 5*6 + 6*7 + 7*8 + 8*9 + 9*10                        == sky circle in Nyon da's copy book
s = 0
for i in range(1,6):
    s += i*(i+1)
print(s)