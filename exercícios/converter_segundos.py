segundos = int(input("Por favor, entre com o número de segundos que deseja converter: "))

d = segundos % 60
d2 = segundos // 60

c  = d2 % 60
c2 = d2 // 60

b = c2  % 24 
b2 = c2 // 24

a = b2

print(f'{a} dias, {b} horas, {c} minutos, {d} segundos.')