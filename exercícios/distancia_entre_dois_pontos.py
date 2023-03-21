import math

x1 = int(input("Digite a coordenadas x1: "))
y1 = int(input("Digite a coordenadas y1: "))
x2 = int(input("Digite a coordenadas x2: "))
y2 = int(input("Digite a coordenadas y2: "))

deltax = x2 - x1
deltay = y2 - y1

distancia = math.sqrt(deltax ** 2 + deltay ** 2)

if distancia >= 10:
    print("longe")
else:
    print("perto")
