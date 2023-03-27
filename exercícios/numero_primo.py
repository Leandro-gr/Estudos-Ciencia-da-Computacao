n = int(input("Digite um número inteiro: "))
primos = [2, 3, 5, 7, 11, 13]
valores = [int(val) for val in primos]
nao_e_primo = False
for numero in valores:
    if n == 1:
        nao_e_primo = True
    elif n == numero:
        pass
    else:
        confirma = n % numero == 0
        if confirma == True:
            nao_e_primo = True
if nao_e_primo == True:
    print("não primo")
else:
    print("primo")
