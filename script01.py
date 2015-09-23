#!/usr/bin/python
#Author=Yeswanth
# Print greater Number amount 3 numbers, if all number are equal than print noting.


print ("Enter 3 numbers")
x = int(raw_input('enter a number X:'))
y = int(raw_input('enter a number Y:'))
z = int(raw_input('enter a number Z:'))

if x > y and x > z:
    print("{} is greater than {},{}") .format(x,y,z)
    pass
elif y > x and y > z:
    print("{} is greater than {},{}") .format(y,x,z)
elif z > x and z > y:
    print("{} is greater than {},{}") .format(z,x,y)
#elif x == y == z:   print("Nothing to do, all numbers are equal\n")  ### insterd of "elif" we can give "else" as shown in below
else:
    print ("Nothing to do, all numbers are equal")
