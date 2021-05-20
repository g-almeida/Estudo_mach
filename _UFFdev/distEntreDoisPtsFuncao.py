def distancia(x2,x1,y2,y1,z2,z1):
    d = (((x2 - x1) ** 2) + ((y2 - y1) ** 2) + ((z2 - z1) ** 2)) ** (1 / 2)
    return d

print("Distancia entre 2 pontos no espaço")

print("entre com as coordenadas de P1")
a = float(input("entre com o eixo x para P1"))
b = float(input("entre com o eixo y para P1"))
c = float(input("entre com o eixo z para P1"))

print("entre com as coordenadas de P2")
d = float(input("entre com o eixo x para P2"))
e = float(input("entre com o eixo y para P2"))
f = float(input("entre com o eixo z para P2"))

resp = distancia(a,b,c,d,e,f)
print(resp)