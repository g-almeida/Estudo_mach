"""
TRY TO SOLVE BEFORE LOOKING AT THE CODE
Determine the roots of the second degree equation: ax2 + bx + c = 0 
remember that:
    delta: 
        Δ =b2 – 4ac , 
    and the roots are:
        r = (–b ± √Δ)/2a)
"""

print("Second degree equations")
a = float(input("input the 'a' value:"))
b = float(input("input the 'b' value:"))
c = float(input("input the 'c' value:"))
d = (b*b) - (4*a*c)
print ("Delta =" , d)
if d<0:
    print("irrational roots")
else:
    x1 = ( -b + (d ** (1/2)) ) / (2*a)
    print("x1=" , x1)
    x2 = ( -b - (d ** (1/2)) ) / (2*a)
    print("x2=" , x2)


def equation(a, b, c):
    d = (b*b) - (4*a*c)
    print("Delta =" , d)
    if d<0:
        print("irrational roots")
    else:
        x1 = ( -b + (d ** (1/2)) ) / (2*a)
        print("x1=" , x1)
        x2 = ( -b - (d ** (1/2)) ) / (2*a)
        print("x2=" , x2)
    return x1, x2        
