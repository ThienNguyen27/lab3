from turtle import *
a=float(input("Input length 1: "))
b=float(input("Input length 2: "))
c=float(input("Input length 3: "))
sumab=a+b
sumbc=b+c
sumac=a+c
ch1=a**2+b**2
ch2=b**2+c**2
ch3=a**2+c**2
if sumab>c and sumbc>a and sumac>b: # tam giac
    
    if ch1==c**2 or ch2==a**2 or ch3==b**2: # tam giac vuong
        print("The 3 line segments can form a right triangle.")
    else:
            if a==b==c: # tam giac deu
                print("The 3 line segments can form an equilateral triangle.")
                for tamgiacdeu in range(3):
                    fd(a)
                    lt(120)
                mainloop()
            else: #tam giac binh thuong
                print("The 3 line segments can form a triangle.")
else: #khong phai tam giac
    print("The 3 line segments cannot form a triangle.")

