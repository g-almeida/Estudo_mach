def romanos(x):
    romano = ''
    dic = {1000 : 'M' , 900 : 'CM' , 500 : 'D', 400 : 'CD' , 100: 'C', 90: 'XC' , 50 : 'L', 40 : 'XL' , 10: 'X' ,
           9: 'IX', 5: 'V', 4: 'IV', 1: 'I' }
    for Chave in dic.keys():
        while x >= Chave:
            romano += dic[Chave]
            x -= Chave
    return romano



numero = int(input("entre com um numero de 1 a 3999: "))
resultado = romanos(numero)
print(resultado)
