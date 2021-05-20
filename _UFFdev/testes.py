"""
frase = "Oi Tudo Bem?"
print(frase)
print(frase[0:12])
print(len(frase))
f = list(frase)
print(f)
f[0]= "a"
print(frase)
print(f)
s = "".join(f)
print(s)

maiusculas = frase.upper()
print(maiusculas)

bem = "bem??"

formatada = "{0} tudo {4}".format("Oi","qlq","a","b",bem)
print(formatada)

vogais ="aeiou"
V=list(vogais)
print(vogais)
print(V)
print(V[1])
"""
x = int(input("entre com x:"))
y = int(input("entre com y:"))

def soma(x, y ):
    soma = x+y
    return soma
def imprime ( x,y,soma):
    print(soma(x,y))
#def impri (a, b, subt):
 #   print (subt()

print (imprime(x,y,soma))



