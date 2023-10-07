alunos = {}

def calcular_media(notas):
    return sum(notas) / len(notas)

def verificar_aprovacao(media, frequencia):
    if media >= 6 and frequencia >= 75:
        return "Aprovado", "Parabéns! Você foi aprovado"
    elif media >= 6 and frequencia < 75:
        return "Reprovado", "Reprovado! Você teve boas notas mas infelizmente teve muitas faltas."
    elif media < 6 and frequencia >= 75:
        return "Reprovado", "Reprovado! Você teve boa frequência de aulas mas não alcançou a nota necessária."
    else:
        return "Reprovado", "Reprovado!"

while True:
    nome = input("Digite o nome do aluno (ou digite 'sair' para ver os resultados): ")
    if nome.lower() == 'sair':
        break

    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))
    nota3 = float(input("Digite a terceira nota: "))
    frequencia = [float(input("Digite a frequência (0-100): "))] 

    alunos[nome] = [nota1, nota2, nota3, frequencia]

for nome, info in alunos.items():
    notas = info[:-1]  
    frequencia = info[-1][0]  
    media = calcular_media(notas)
    status, mensagem = verificar_aprovacao(media, frequencia)
    print(f"O Aluno: {nome}, obteve a Média de: {media} e a Frequência de: {frequencia}, sua situação é: {mensagem}")
