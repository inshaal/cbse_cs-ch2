"""FUNCTION OVERLOADING IS NOT POSSIBLE IN PYTHON"""
"""However, if it was possible, the following code would work."""
def volume(a):
    volume=a**3
    return volume
def volume(a,b,c): #b-height
    volume=a*b*c
    return volume
def volume(a,b): #a-radius|b-height
    from math import pi
    volume= pi*(a**2)*b
    return volume
a=raw_input("Enter dimension1: ")
b=raw_input("Enter dimension2: ")
c=raw_input("Enter dimension3: ")
ta=bool(a)
tb=bool(b)
tc=bool(c)
if ta:
    a=float(a)
    if not (tb and tc):
        volume(a)
    elif tb and (not tc):
        b=float(b)
        volume(a,b)
    elif (tb and tc):
        b=float(b)
        c=float(c)
        volume(a,b,c)




"""It's possible using module/s: https://pypi.python.org/pypi/overload"""
