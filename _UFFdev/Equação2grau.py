#Determine as raízes de uma equação de 2º grau: ax2 + bx + c = 0 (recordar que o discriminante
#Δ =b2 – 4ac, e que a raiz r = (–b ± √Δ)/2a)

print("Equação do 2 grau")
a = float(input("entre com um valor para a"))
b = float(input("entre com um valor para b"))
c = float(input("entre com um valor para c"))
d = (b*b) - (4*a*c)
print ("Delta =" , d)
if d<0:
    print("raízes irracionais")
else:

    x1 = ( -b + (d ** (1/2)) ) / (2*a)
    print("x1=" , x1)
    x2 = ( -b - (d ** (1/2)) ) / (2*a)
    print("x2=" , x2)



