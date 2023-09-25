n = int(input("Entre com um número: "))

fatorial = 1

for i in range(n, 0, -1):
    fatorial = fatorial * i

print(f'{n}! = {fatorial}')