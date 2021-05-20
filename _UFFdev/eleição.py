'''
Em uma eleição presidencial existem quatro candidatos. Os votos são informados através de
códigos. Os dados utilizados para a contagem dos votos obedecem à seguinte codificação:
1,2,3,4 = voto para os respectivos candidatos;
5 = voto nulo;
6 = voto em branco;
Elabore um programa que leia o código votado por vários eleitores. Como finalizador da entrada de
dados, considere o código zero. Ao final, calcule e escreva:
- total de votos para cada candidato;
- total de votos nulos;
- total de votos em branco;
'''

print("Eleicoes. \nCandidatos: 1, 2, 3, 4. 5 = nulo e 6 = branco. \nEncerre as eleições votando 0\n")

voto = 10
contadorVotos = 0
candidato1 = 0
candidato2 = 0
candidato3 = 0
candidato4 = 0
contadorNulo = 0
contadorBranco = 0

while voto != 0:
    voto = int(input("Vote no seu candidato:"))
    contadorVotos = contadorVotos + 1
    if voto == 1:
        candidato1 = candidato1 + 1
    elif voto == 2:
        candidato2 = candidato2 + 1
    elif voto == 3:
        candidato3 = candidato3 + 1
    elif voto == 4:
        candidato4 = candidato4 + 1
    elif voto == 5:
        contadorNulo = contadorNulo + 1
    else:
        contadorBranco = contadorBranco + 1
somaVotos = candidato1  + candidato2 + candidato3 + candidato4 + contadorBranco + contadorNulo

print("\nFim das eleições!")
print("\ntotal de votos:", contadorVotos)
print(candidato1 , "para o candidato 1")
print(candidato2 , "para o candidato 2")
print(candidato3 , "para o candidato 3")
print(candidato4 , "para o candidato 4")
print("total de votos nulos:", contadorNulo)
print("total de votos brancos:", contadorBranco)
print("confirmação da soma dos votos", somaVotos)



