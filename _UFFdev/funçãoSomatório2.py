print("função somatório 2^n")

def somatório(n):
    soma = 0

    while n >= 0 :
        soma = soma + 2**n
        n = n-1

    return soma

n = float(input("entre com o valor de n:"))

somatorioFinal = somatório(n)
print(somatorioFinal)