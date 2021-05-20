print("função somatório 2^n")

def somatório(n):

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

n = float(input("entre com o valor de n:"))

somatorioFinal = somatório(n)
print(somatorioFinal)