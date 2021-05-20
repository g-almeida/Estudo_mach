dic = {}
while True:
    nome = str(input("nome:"))
    nota = float(input("nota:"))
    dic[nome] = nota
    resposta = str(input("deseja continuar?"))
    if resposta == 'nao':
        break
print (dic)

for cadaChave in dic:
    #print(cadaChave)
    if dic[cadaChave] >= 7:
       print(cadaChave, "passou")
    else:
        print(cadaChave, "kbço")
