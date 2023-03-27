n = int(input("Digite um número inteiro: "))
soma = 0

if n <= 10:
    soma = n
else:
    while n > 0:
        soma += n % 10
        n = n // 10
        
print(soma)