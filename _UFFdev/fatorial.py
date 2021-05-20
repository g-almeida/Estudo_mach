print("programa fatorial de n")

n = float(input("entre com o valor de n:"))
r = n
while n > 1:
    r = r * (n-1)
    n = n-1
print (r)
