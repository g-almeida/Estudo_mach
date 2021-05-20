def numeroDeVogais(palavra):
    palavra = palavra.lower()
    A = palavra.count("a")
    E = palavra.count("e")
    I = palavra.count("i")
    O = palavra.count("o")
    U = palavra.count("u")

    numeroVogais = A + E + I + O + U

    return numeroVogais

def somatorio2n(n):

    if n >=0:
        soma = 0
        i=0
        while i <= n :
            soma = soma + 2**i
            i = i+1
    else:
        soma = 0
        while n <=0:
            soma = soma + 2**n
            n = n+1


    return soma

def areaTriang(x,y):

    area = (x*y)/2

    return area

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

def funcao2Grau(a,b,c):

    d = (b * b) - (4 * a * c)
    print("Delta =", d)
    if d < 0:
        print("raízes irracionais")
    else:

        x1 = (-b + (d ** (1 / 2))) / (2 * a)

        x2 = (-b - (d ** (1 / 2))) / (2 * a)


    resultados = [x1,x2]

    return resultados

def fatorial(n):
    fat = n
    while n > 1:
        fat = fat * (n - 1)
        n = n - 1
    return fat