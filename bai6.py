a=float(input("Input length 1: "))
b=float(input("Input length 2: "))
c=float(input("Input length 3: "))
sumab=a+b
sumbc=b+c
sumac=a+c
if sumab>c and sumbc>a and sumac>b:
    print("The 3 line segments can form a triangle.") 
else:
    print("The 3 line segments cannot form a triangle.")
