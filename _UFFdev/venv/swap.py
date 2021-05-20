def swap():
    global a
    global b
    temp = b
    b = a
    a = temp
    print("valor de a dentro: %d" %a)
    print("valor de b dentro: %d" %b)

a = 4
b = 2

swap()
print("valor de a depois: %d" %a)
print("valor de b depois: %d" %b)