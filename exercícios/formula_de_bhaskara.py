import math

a = int(input("Digite o valor de 'a': "))
b = int(input("Digite o valor de 'b': "))
c = int(input("Digite o valor de 'c': "))

#calcula valor de delta.
delta = b ** 2 - 4 * a * c

#verifica se valor de delta e menor igual ou maior que 0, e calcula a raiz do delta.
if delta < 0:
    print("esta equação não possui raízes reais")

elif delta > 0:
    x1 = (-b + math.sqrt(delta)) / (2 * a) 
    x2 = (-b - math.sqrt(delta)) / (2 * a)
    if x1 > x2:
        print(f"as raízes da equação são {x2} e {x1}")
    else:
        print(f"as raízes da equação são {x1} e {x2}")
else:
    x = (-b + math.sqrt(delta)) / (2 * a) 
    print(f"a raiz desta equação é {x}")