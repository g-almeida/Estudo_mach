def sum():
    n = 1
    soma = 0
    while n != 0:
        n = float(input("entre com o valor:"))
        soma = soma + n
    return soma

print("Somando valores:")
somando = sum()
print(somando)

def sum2(*v):
    soma = 0
    for num in v:
        soma = soma + num
    return soma

print("somando valores")
somei = sum2(1, 2, 4, 5)
print (somei)
