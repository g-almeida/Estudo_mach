""" Churrasco direito """
print("Churrasco Direito")
print("Responda com 'sim' ou 'nao' ")

bebida = float(input("Custo da bebida"))
comida = float(input("Custo da comida"))
bebCount = 0
comCount = 0

orc = {}
print("Diga quem entrou e quanto gastou:")

while True:
    nome = str(input("Nome:"))
    gasto = float(input("Gastos:"))
    beb = str(input("Entrou na bebida?"))
    if beb == 'sim':
        bebCount +=1
    com = str(input("Entrou na comida?"))
    if com == 'sim':
        comCount +=1

    orc[nome]= gasto
    continuar = str(input("Deseja continuar?"))
    if continuar == 'nao':
        break

print (orc)
print ("Pessoas bebendo:", bebCount)
print ("Pessoas comendo", comCount)

cadaBebendo = bebida/bebCount
cadaComendo = comida/comCount

print("/nCada um que bebeu deve gastar:", cadaBebendo)
print("Cada um que comeu deve gastar:", cadaComendo)




