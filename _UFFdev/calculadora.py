operando1 = float(input("entre com o 1 operando:"))
operando2 = float(input("entre com o 2 operando:"))
operacao = str(input("qual operacao deseja? soma, subtracao, multiplicacao ou divisao?"))
if operacao  == 'soma':
    resultado = operando1 + operando2
if operacao == 'subtracao':
    resultado = operando1 - operando2
if operacao == 'multiplicacao':
    resultado = operando1 * operando2
if operacao == 'divisao':
    resultado = operando1 / operando2
print(resultado)

