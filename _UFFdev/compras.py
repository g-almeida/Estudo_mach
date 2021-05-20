#. Leia os dados de uma compra (nome do produto, preço e quantidade), escreva o nome do produto
#comprado e o valor total a ser pago naquele produto, considerando que são oferecidos descontos
#pelo número de unidades compradas, segundo a tabela abaixo:
#a. Até 10 unidades: valor total
#b. de 11 a 20 unidades: 10% de desconto
#c. de 21 a 50 unidades: 20% de desconto
#d. acima de 50 unidades: 25% de desconto

print("Entre com os dados da compra")
nome = str(input("Nome do produto:"))
p = float(input("Preço do produto:"))
qtd = int(input("Quantidade do produto:"))
print(nome , "preço =", p ,"quantidade =", qtd )

if qtd <= 10:
    print("o preço é o mesmo, sem desconto. Preço = ", p)
else:
    if qtd >= 11 and qtd <= 20:
        p = p*0.9
        #print("o preço do produto com desconto é", p)
    elif qtd >= 21 and qtd <= 50:
        p = p*0.80
        #print("o preço do produto com desconto é", p)
    else:
        p = p*0.75
        #print("o preço do produto com desconto é", p)
    print("o preço do produto com desconto é", p)
total = p*qtd
print(total)
