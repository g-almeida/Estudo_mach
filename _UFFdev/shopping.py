"""
TRY TO SOLVE BEFORE LOOKING AT THE CODE
Ask for the order information (name, price and quantity)
Print the name of the product and the total value after applying some ruled discounts based on the quantity
Discount Rules:
A) 11 to 20 units: 10% of discount
B) 21 to 50 units: 20% of discount
C) more than 50 units: 30% of discount
"""

print("Enter the order information")
nome = str(input("Product:"))
p = float(input("Price:"))
qtd = int(input("Quantity:"))
print(nome, "price =", p, "quantity =", qtd)

if qtd <= 10:
    print("the price stays the same, no discount. Price = ", p)
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
    print("The unit price after applying discount rules is: ", p)
total = p*qtd
print(total)
