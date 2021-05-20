print ("A qual quadrante pertence a coordenada?")

x = float(input("entre com a coordenada x:"))
y = float(input("entre com a coordenada y:"))
print("(", x , ",", y , ")")
if x == 0 and y == 0:
    print("0")
else:
    if x == 0 or y == 0:
        print("-1")
    else:
        if x > 0 and y > 0:
            print("1 quadrante")
        elif x > 0 and y < 0:
            print("4 quadrante")
        elif x < 0 and y < 0:
            print("3 quadrante")
        else:
            print("2 quadrante")