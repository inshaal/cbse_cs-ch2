    """FUNCTION OVERLOADING IS NOT POSSIBLE IN PYTHON"""
"""However, if it was possible, the following code would work."""
def area(a):
    from math import pi
    area= pi*(r**2)
    return area

def area(a,b):
    area= a*b
    return area

def area(a,b,c):
    s= (a+b+c)/2.0
    area= (s(s-a)(s-b)(s-c))^0.5
    return area

a= raw_input("Enter side1: ")
b= raw_input("Enter side2: ")
c= raw_input("Enter side3: ")
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


"""It's possible using module/s: https://pypi.python.org/pypi/overload"""
