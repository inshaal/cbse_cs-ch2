"""FUNCTION OVERLOADING IS NOT POSSIBLE IN PYTHON"""
"""However, if it was possible, the following code would work."""
def volume(a): #For volume of cube
    vol=a**3
    print vol, "is volume of cube"
def volume(a,b,c): #volume of cuboid |b-height
    vol=a*b*c
    print vol, "is volume of cuboid" 
def volume(a,b): #volume of cylinder |a-radius|b-height
    from math import pi
    vol= pi*(a**2)*b
    print vol, "is volume of cylinder"
a=raw_input("Enter dimension1: ")
b=raw_input("Enter dimension2: ")
c=raw_input("Enter dimension3: ")
volume(a,b,c)

'''
Notice Python takes the latest definition of that function. So if all three values are provided for a,b & c Python will give an error
stating it takes only 2 arguments but 3 given.
'''

'''
EXTRA PART FOR - (Not Required)
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
'''



"""It's possible using module/s: https://pypi.python.org/pypi/overload"""
