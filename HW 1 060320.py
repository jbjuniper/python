# JBOCK Juniper Python Homework #1 060320

import math


# homework # 1 060320
for x in range(1,3):
    print("---")





print("PROBLEM #1 - implement power and **")
x=int(input("input number to be raised by the power "))
y=int(input("input the power to raise to "))
print("   using '**' method,", x," to the power of ",y,"=",x**y)
print("   using math.pow ",x," to the power of =",y," = ",math.pow(x,y))

for x in range(1,3):
    print("---")

y=11
print("PROBLEM #2 - implement mod and %  using x%y")
x=int(input("input nunber to be divided "))
y=int(input("input number to divide by "))


flip=math.floor(x/y)*y
print(x," /",y," = ",x/y," so floor(",x,"%",y,")*",y," is ",flip," and ",x,"-",flip,"=",x-flip," therefore y%x (the remainder) is ",x%y)

for x in range(1,3):
    print("---")


print("PROBLEM #3 - implement any other math function - I elected perm")

n=0
while not int(n) in range(1,1000001) :
    n=int(input("Define n (items available) max of 1,000,000 - "))

k=0
while not int(k) in range(1,11) :
    k=int(input("Define k (items selected each time) max of 10 - "))

print("permutations of ",k," items selected from ",n,"items is ",format(math.perm(n,k),",d"))





# create a GitHub account

