#Escreva	 um	 programa	 que	 transforme	 o	 valor	 correspondente	 a	 um
#intervalo	 temporal,	 expresso	 em	 horas,	 minutos	 e	 segundos,	 no	 valor
#correspondente	em	segundos.	\

print("horas,minutos,segundos")
h = int(input("entre com o valor em horas:"))
m = int(input("entre com o valor em minutos:"))
s = int(input("entre com o valor em segundos:"))

print(h,":",m,":",s)

a = h*60*60
b = m*60
c = a+b+s
print(c,"segundos")

