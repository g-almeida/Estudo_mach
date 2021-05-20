print("Identificando Vogais!")

def NumeroDeVogais(palavra):
    palavra = palavra.lower()
    y = palavra.count("a" "e" "i")
    x = palavra.count("o" "u")


    numeroVogais = x+y

    return numeroVogais

palavra = str(input("entre com uma palavra:"))
numeroVogais = NumeroDeVogais(palavra)
print (numeroVogais)

