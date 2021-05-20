print("pares e impares")

x = 1
pares = 0
impares = 0

while x <= 10:
    A = int(input("entre com um numero inteiro"))
    if A % 2 == 0:
        pares += 1
    else:
        impares += 1
    x += 1
print ("pares:", pares , "\nimpares:", impares)

