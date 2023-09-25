n = int(input("Digite um valor:"))
soma = 0
for i in range(n , n + 1 ):
    
    if i % 2 == 0:
        soma += i

print(f"A soma dos números pares de 1 até {n} é: {soma}")

###########################################################

entrada = int(input("Digite um valor: "))
acumulador = 0


while (acumulador - 1) < entrada:
    if entrada % 2 == 0:
        acumulador += entrada 
    

print(f"A soma dos números pares de 1 até {entrada} é: {acumulador}") 