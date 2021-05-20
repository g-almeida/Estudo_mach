#Construa	um	programa	que	recebe	o	número	de	cadastro	(inteiro)	de	três	clientes	de	uma	loja
#e	 o	 valor	 (em	 reais)	que	cada	um	desses	clientes	pagou	por	 sua	compra.	O	programa	deverá
#informar:
#(a) o	valor	total	pago	pelos	três	clientes
#(b) o	valor	da	compra	média efetuada
#(c) o	número	de	cadastro	dos	clientes	que	efetuaram	compras	superiores	a	100	reais
#(d) quantos	clientes	efetuaram	compras	inferiores	a	50	reais

print("cadastro inteiro de 3 clientes")
cadastro1 = int(input("entre com seu numero de cadastro"))
compra1 = float(input("quanto você gastou?"))
cadastro2 = int(input("entre com seu numero de cadastro"))
compra2 = float(input("quanto voce gastou?"))
cadastro3 = int(input("entre com seu número de cadastro"))
compra3 = float(input("quanto voce gastou?"))

#letra (A) valor total:

print("\no valor total das 3 compras foi:")
total = compra1 + compra2 + compra3
print(total)

#letra (B) compra media:

print("\nvalor da compra media efetuada")
if compra1 >= compra2 and compra1 <= compra3 or compra1 <= compra2 and compra1 >= compra3:
    print("a compra média é a do cadastro: ", cadastro1, "no valor de: ", compra1)
if compra2 >= compra1 and compra2 <= compra3 or compra2 <= compra1 and compra2 >= compra3:
    print("a compra média é a do cadastro: ", cadastro2, "no valor de: ", compra2)
if compra3 >= compra1 and compra3 <=compra2 or compra3 <= compra1 and compra3 >= compra2:
    print("a compra média é a do cadastro: ", cadastro3, "no valor de: ", compra3)

#letra (C) cadastro das compras >100

print("\nnúmero	de	cadastro	dos	clientes	que	efetuaram	compras	superiores	a	100	reais")
if compra1 > 100:
    print(cadastro1)
    if compra2 > 100:
        print(cadastro2)
    if compra3 > 100:
        print(cadastro3)
elif compra2 > 100:
    print(cadastro2)
    if compra3 > 100:
        print(cadastro3)
elif compra3 > 100:
    print(cadastro3)
else:
    print('ninguem')


#letra (D) soma dos inferiories a 50$

print("\nquantos	clientes	efetuaram	compras	inferiores	a	50	reais?")

if compra1 < 50 or compra2 < 50 or compra3 < 50:
    soma = 1
    if compra1 < 50 and compra2 < 50 or compra2 < 50 and compra3 < 50 or compra1 < 50 and compra3 < 50:
        soma = 2
    if compra1 < 50 and compra2 < 50 and compra3 < 50:
        soma = 3
    print(soma)
else:
    print("ninguem gastou menos de 50 reais")



