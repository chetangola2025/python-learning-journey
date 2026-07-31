# Write a program to find the greatest of 4 numbers entered by the user.

a = float(input("Enter your first number: "))
b = float(input("Enter your second number: "))
c = float(input("Enter your third number: "))
d = float(input("Enter your fourth number: "))
if(a >=b and a >=c and a>=d):
    print("First number is the greatest: ", a)
elif(b >=a and b>=c and b>=d):
    print("Second number is the greatest: ", b)

elif(c >=a and c >=b and c>= d):
    print("Third number is the Greatest: ", c)
else:
    print("Fourth number is the greatest: ", d)
