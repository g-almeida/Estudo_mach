#Calcule a distância entre dois pontos num espaço de 3 dimensões
# D= raiz de ( ((x2-x1)**2) + ((y2-y1)**2) + ((z2-z1)**2) )

print("Distancia entre 2 pontos no espaço")

print("entre com as coordenadas de P1")
x1 = float(input("entre com o eixo x para P1"))
y1 = float(input("entre com o eixo y para P1"))
z1 = float(input("entre com o eixo z para P1"))
print("(", x1 , "," , y1 , "," , z1 , ")")

print("entre com as coordenadas de P2")
x2 = float(input("entre com o eixo x para P2"))
y2 = float(input("entre com o eixo y para P2"))
z2 = float(input("entre com o eixo z para P2"))
print("(", x2 , "," , y2 , "," , z2 , ")")

d = ( ((x2-x1)**2) + ((y2-y1)**2) + ((z2-z1)**2) ) ** (1/2)

print (d)