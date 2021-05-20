print("Identificando Vogais!")

def NumeroDeVogais(palavra):
    palavra = palavra.lower()
    A = palavra.count("a")
    E = palavra.count("e")
    I = palavra.count("i")
    O = palavra.count("o")
    U = palavra.count("u")

    numeroVogais = A + E + I + O + U

    return numeroVogais

palavra = str(input("entre com uma palavra:"))
numeroVogais = NumeroDeVogais(palavra)
print (numeroVogais)


