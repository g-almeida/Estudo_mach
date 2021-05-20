print("premio de vendas")
salario  = float(input("salario é:"))
vendas = int(input("total de vendas é:"))
if vendas > 1000 and vendas <= 5000:
    salario += 500
elif vendas > 5000 and vendas <= 7500:
    salario += 700
elif vendas > 7500:
    salario += 1000
else:
    print("nenhum premio")
print("salario final é:" , salario)