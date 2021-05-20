print("programa almoxarifado")

caderno = 10
caneta = 20
lapis = 30
borracha = 40
regua = 50

estoqueCaderno = int(input("entre com o estoque inicial de cadernos"))
estoqueCaneta = int(input("entre com o estoque inicial de canetas"))
estoqueLapis = int(input("entre com o estoque inicial de lapis"))
estoqueBorracha = int(input("entre com o estoque inicial de borrachas"))
estoqueRegua = int(input("entre com o estoque inicial de reguas"))

operacao = 0
X = 1
E = 0
S = 0
R = 0

while operacao != X:

    operacao = str(input("\nEntre com um código:\n E = entrada \n S  = saída \n R = relatorio \n X = sair \n"))

    if operacao == 'E':
        entrada = int(input("Qual e o codigo do produto?"))
        if entrada == 10:
            adicionarCadernos = int(input("quantos cadernos deseja adicionar?"))
            estoqueCaderno = estoqueCaderno + adicionarCadernos
            print(estoqueCaderno)
        if entrada == 20:
            adicionarCanetas = int(input("quantas canetas deseja adicionar?"))
            estoqueCaneta = estoqueCaneta + adicionarCanetas
            print(estoqueCaneta)
        if entrada == 30:
            adicionarLapis = int(input("quantos lapis deseja adicionar?"))
            estoqueLapis = estoqueLapis + adicionarLapis
            print(estoqueLapis)
        if entrada == 40:
            adicionarBorrachas = int(input("quantas borrachas deseja adicionar?"))
            estoqueBorracha = estoqueBorracha + adicionarBorrachas
            print (estoqueBorracha)
        if entrada == 50:
            adicionarRegua = int(input("quantas reguas deseja adicionar?"))
            estoqueRegua = estoqueRegua + adicionarRegua
            print(estoqueRegua)

    if operacao == 'S':
        entrada = int(input("Qual e o codigo do produto?"))
        if entrada == 10:
            retirarCadernos = int(input("quantos cadernos deseja retirar?"))
            if retirarCadernos > estoqueCaderno:
                break
            estoqueCaderno = estoqueCaderno - retirarCadernos
            print(estoqueCaderno)
        if entrada == 20:
            retirarCanetas = int(input("quantos canetas deseja retirar?"))
            if retirarCanetas > estoqueCaneta:
                break
            estoqueCaneta = estoqueCaneta- retirarCanetas
            print(estoqueCaneta)
        if entrada == 30:
            retirarLapis = int(input("quantos lapis deseja retirar?"))
            if retirarLapis > estoqueLapis:
                break
            estoqueLapis = estoqueLapis - retirarLapis
            print(estoqueLapis)
        if entrada == 40:
            retirarBorrachas = int(input("quantos borrachas deseja retirar?"))
            if retirarBorrachas > estoqueBorracha:
                break
            estoqueBorracha = estoqueBorracha - retirarBorrachas
            print(estoqueBorracha)
        if entrada == 50:
            retirarReguas = int(input("quantos reguas deseja retirar?"))
            if retirarReguas > estoqueRegua:
                break
            estoqueRegua = estoqueRegua - retirarReguas
            print(estoqueRegua)

    if operacao == 'R':
        print("\nEstoque cadernos", estoqueCaderno, "\nEstoque Canetas", estoqueCaneta , "\nEstoque Lapis", estoqueLapis,
              "\nEstoque Reguas" , estoqueRegua , "\nEstoque Borrachas", estoqueBorracha)

    if operacao == 'X':
        break


