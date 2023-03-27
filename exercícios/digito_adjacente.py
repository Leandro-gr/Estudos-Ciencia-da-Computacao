n = int(input("Digite um número inteiro: "))
igual = True

while igual:    
    numero = n//10
    numero1 = n%10
    numero2 = numero%10
    if n <= 10:
        print('não')
        igual = False
    elif n > 10 and numero1 == numero2:
        print('sim')
        igual = False
    else:
        n = n//10