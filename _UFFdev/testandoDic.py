dicionario = {}
results = open('resultadoss')
for linha in results:
    (nome, nota) = linha.split()
    dicionario[float(nota)] = nome
print(dicionario)
'''c = 1
for cada in sorted(notas.keys(), reverse = True):
    print(f'{c} lugar foi o {notas[cada]} com {cada}' )
    c += 1'''
