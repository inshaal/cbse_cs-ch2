"""FUNCTION OVERLOADING IS NOT POSSIBLE IN PYTHON""" 
"""However, if it was possible, the following code would work."""
def area(a): #Area of circle
    from math import pi
    sol=pi*(r**2)
    print sol, "is area of circle"

def area(a,b): #Area of rectangle
    sol= a*b
    print sol, "is area of rectangle"

def area(a,b,c): #Area of triangle
    s= (a+b+c)/2.0
    sol= (s(s-a)(s-b)(s-c))^0.5
    print sol, "is area of triangle"

a= input("Enter a: ")
b= input("Enter b: ")
c= input("Enter c: ")

#Error will come if only a and b are given because python takes the latest definiton of function. so only area of triangle can be calculated.

'''
#EXTRA
ta= bool(a)
tb= bool(b)
tc= bool(c)

if ta:
    a= float(a)
    if not (tb and tc):
        area(a)
    elif tb and (not tc):
        b= float(b)
        area(a,b)
    elif (tb and tc):
        b= float(b)
        c= float(c)
        area(a,b,c)
'''

"""It's possible using module/s: https://pypi.python.org/pypi/overload"""
