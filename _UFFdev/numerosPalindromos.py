print("PALÍNDROMOS")
x = 1000
while x <= 9999:
    a = str(x)
    if a[0] == a[3] and a[1] == a[2]:
        print(x)
    x += 1

    