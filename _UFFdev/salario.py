#A prefeitura de uma cidade fez uma pesquisa entre seus habitantes, coletando dados sobre o
#salário e número de filhos. Faça um programa que leia o salário e o número de filhos de n
#habitantes. O final da leitura de dados se dará com a entrada de um salário negativo. Mostre na
#saída:
#a. média de salário da população;
#b. média de número de filhos;
#c. maior salário;
#d. percentual de pessoas com salário de até R$ 1000,00.

print("Pesquisa salário e n de filhos\n")
s=0
somaSalario=0
somaFilhos=0
contadorSalario=0
contadorFilhos=0
armazenamento=0
maiorSal=0
somaPercent=0
s = float(input("Entre com o valor do salário:"))

while s >= 0:

 f = int(input("Entre com o numero de filhos:"))
 print("\nO salário é " , s , "e o numero de filhos" , f , "\n")
 somaSalario = somaSalario + s
 somaFilhos = somaFilhos + f
 contadorSalario = contadorSalario + 1
 contadorFilhos = contadorFilhos + 1
 if s > maiorSal:
  maiorSal = s
 if s <= 1000:
  somaPercent = somaPercent + 1
 s = float(input("Entre com o valor do salário:"))


#Letra a e b

mediaSalario = somaSalario / contadorSalario
mediaFilhos = somaFilhos / contadorFilhos
print("\nLetra a e b:")
print("a media dos salarios inseridos e:" , mediaSalario, "\n" "e a media do numero de filhos e:", mediaFilhos)

#Letra c

print("\no maior salario e:", maiorSal)

#Letra d  OBS: percentual = 100*numerador / denominador

percent = (100*somaPercent) / contadorSalario
print("\no percentual de pessoas com salario ate 1000 reais e:" , percent, "%")






