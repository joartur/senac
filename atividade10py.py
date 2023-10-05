def soma_sequencia_recursiva(seq):
    if len(seq) == 0:
        return 0
    else:
        return seq[0] + soma_sequencia_recursiva(seq[1:])

sequencia = [3, 8, 5, 2, 1]
resultado = soma_sequencia_recursiva(sequencia)
print(f'A soma da sequência {sequencia} é {resultado}')
