def mdc(a, b):
    if b == 0:
        return a
    else:
        return mdc(b, a % b)

def mmc(a, b):
    divisor = mdc(a, b)
    if divisor == 0:
        return 0
    else:
        return abs(a*b) // divisor

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

resultado = mmc(num1, num2)
print(f"O MMC de {num1} e {num2} é {resultado}")
