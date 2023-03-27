n = int(input("Digite o valor de n: "))
fatorial = n

if n == 0:
    fatorial = 1
else:
    for qq in range(n-1):
        n -= 1
        fatorial = fatorial * n
print(fatorial)


