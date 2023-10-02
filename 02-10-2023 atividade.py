import random

def remover_acentos(palavra):
    acentos = {'á':'a', 'é':'e', 'í':'i', 'ó':'o', 'ú':'u', 'ã':'a', 'õ':'o', 'â':'a', 'ê':'e', 'ô':'o'}
    return ''.join(acentos[i] if i in acentos else i for i in palavra)

def jogar(limiteDeErros, numJogadores):
    palavras_dicas = {'casa': 'Lugar onde moramos', 
                      'carro': 'Meio de transporte', 
                      'python': 'Linguagem de programação', 
                      'jogo': 'Passatempo divertido', 
                      'computador': 'Máquina que processa informações'}
    pontos = [0 for _ in range(numJogadores)]
    nomes = [input('Digite o nome do jogador {}: '.format(i+1)) for i in range(numJogadores)]
    rodada = 0

    while True:
        palavra = random.choice(list(palavras_dicas.keys()))
        dica = palavras_dicas[palavra]
        palavraSemAcentos = remover_acentos(palavra)
        acertos = ['_' for _ in palavra]
        erros = [0 for _ in range(numJogadores)]
        jogadorAtual = 0
        alguem_acertou = False  # Variável para controlar se alguém acertou a palavra inteira

        print('Dica:', dica)

        while max(erros) < limiteDeErros and '_' in acertos:
            print('Jogador', nomes[jogadorAtual])
            print('Palavra:', ' '.join(acertos))
            letra = input('Digite uma letra ou a palavra inteira: ').lower()
            if len(letra) > 1:  # o usuário tentou adivinhar a palavra inteira
                if letra == palavra:
                    if acertos.count('_') >= 3:
                        pontos[jogadorAtual] += 5 * len(palavra)
                    else:
                        pontos[jogadorAtual] += len(palavra)
                    print('Parabéns! Você acertou a palavra:', palavra)
                    alguem_acertou = True  # Alguém acertou a palavra inteira
                    break
                else:
                    print('Você errou! A palavra era:', palavra)
                    erros[jogadorAtual] = limiteDeErros
            elif letra in palavraSemAcentos:
                for i in range(len(palavraSemAcentos)):
                    if palavraSemAcentos[i] == letra:
                        acertos[i] = palavra[i]
                        pontos[jogadorAtual] += 1
            else:
                erros[jogadorAtual] += 1
                print('Erros:', erros[jogadorAtual])

            jogadorAtual = (jogadorAtual + 1) % numJogadores

        if not alguem_acertou and '_' in acertos:
            print('Ninguém acertou! A palavra era:', palavra)

        rodada += 1
        print('Pontuação após a rodada {}:'.format(rodada))
        for i in range(numJogadores):
            print(nomes[i], ':', pontos[i])

        if rodada % 3 == 0 and numJogadores > 1:
            minPontos = min(pontos)
            for i in range(numJogadores):
                if pontos[i] == minPontos:
                    if i == jogadorAtual:
                        jogadorAtual = (jogadorAtual + 1) % numJogadores
                    print('O jogador', nomes[i], 'foi eliminado por ter menos pontos!')
                    del pontos[i]
                    del nomes[i]
                    numJogadores -= 1
                    break

        if numJogadores == 1:
            break

    print('O vencedor é o jogador', nomes[pontos.index(max(pontos))], '! Parabéns!')

limiteDeErros = int(input('Digite o limite de erros: '))
numJogadores = int(input('Digite o número de jogadores: '))
jogar(limiteDeErros, numJogadores)

