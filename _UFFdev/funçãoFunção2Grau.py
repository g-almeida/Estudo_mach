print("Função de resolver funções 2 grau\n")



def funcaoR1(a,b,c):

    d = (b*b) - (4*a*c)
    if d < 0:
        #print("raízes irracionais")
        return "raízes irracionais"
    else:
        r1 = (-b + (d ** (1/2)))/2*a

    return r1
def funcaoR2(a,b,c):

    d = (b * b) - (4 * a * c)
    if d < 0:
        # print("raízes irracionais")
        return "raízes irracionais"
    else:
        r2 = (-b - (d ** (1 / 2))) / 2 * a

    return r2

a = float(input("entre com o valor de a:"))
b = float(input("entre com o valor de b:"))
c = float(input("entre com o valor de c:"))

R1 = funcaoR1(a,b,c)
R2 = funcaoR2(a,b,c)
print("as raízes são:",R1, "e", R2)