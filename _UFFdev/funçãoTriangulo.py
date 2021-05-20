print("função area do triangulo\n")

def areaTriang(x,y):

    area = (x*y)/2

    return area

base = float(input("base:"))
altura = float(input("altura:"))

trianguloArea = areaTriang(base, altura)

print(trianguloArea)