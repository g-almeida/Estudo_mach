print("jogo do adivinha")
b=0
while b!=5:
    a = input("manda o número:")
    b = int(a)
    if b==5:
        print("boa")
    else:
        if b>5:
            print("muito alto")
        else:
            print("muito baixo")