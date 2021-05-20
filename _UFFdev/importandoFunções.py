from bibliotecaFunções import *
"""
palavra = str(input("Escolha uma palavra para saber seu número de vogais:"))
x = numeroDeVogais(palavra)

print(x)


print("calcule o somatório 2^n sendo n = 87")
n = float(input("entre com um valor para n:"))
y = somatorio2n(n)
print(y)


print("Area do triangulo, entre com base e altura:")
base = float(input("base:"))
altura = float(input("altura:"))
area = areaTriang(base,altura)
print(area)


print("Função do 2 grau, entre com a, b e c:")
a = float(input("a:"))
b = float(input("b:"))
c = float(input("c:"))
raizes = funcao2Grau( a, b, c )
print(raizes)
raiz1 = raizes[0]
raiz2 = raizes[1]

print("a primeira raíz é:" , raiz1)
print("a segunda raíz é:", raiz2)
"""

def soma(m,n):
    soma = m+n
    return soma

print("teste")
a = int(input("a:"))
b = int(input("b:"))
f = funçãoComp(a,b,soma)
print (f)