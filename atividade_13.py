import random

class MonstroMinecraft:
    def __init__(self, saude, nome, habito):
        self.saude = saude
        self.nome = nome
        self.habito = habito
        self.posicaoX = random.randint(0, 10)
        self.posicaoY = random.randint(0, 10)

    def correr(self, jogador):
        direcaoX = random.choice([-1, 0, 1])
        direcaoY = random.choice([-1, 0, 1])

        self.posicaoX += direcaoX
        self.posicaoY += direcaoY

class CreeperMinecraft(MonstroMinecraft):
    def __init__(self, saude, raioExplosao, raioPerseguicao , velocidade, nome, habito, explosaoSilenciosa):
        super().__init__(saude, nome, habito)
        self.raioExplosao = raioExplosao
        self.raioPerseguicao = raioPerseguicao
        self.velocidade = velocidade
        self.explosaoSilenciosa = explosaoSilenciosa

    def __str__(self):
        return f"Nome: {self.nome}\nSaúde: {self.saude}\nRaio de Explosão: {self.raioExplosao}\nRaio de Perseguição: {self.raioPerseguicao}\nVelocidade: {self.velocidade}\nHábito: {self.habito}\nExplosão Silenciosa: {self.explosaoSilenciosa}\nPosição X: {self.posicaoX}\nPosição Y: {self.posicaoY}"

class EsqueletoMinecraft(MonstroMinecraft):
    def __init__(self, saude, arco, flechas, nome, habito, armadura, raioPerseguicao ,ataqueDistancia):
        super().__init__(saude, nome, habito)
        self.arco = arco
        self.flechas = flechas
        self.armadura = armadura
        self.ataqueDistancia = ataqueDistancia
        self.raioPerseguicao = raioPerseguicao

    def __str__(self):
        return f"Nome: {self.nome}\nSaúde: {self.saude}\nArco: {self.arco}\nFlechas: {self.flechas}\nHábito: {self.habito}\nArmadura: {self.armadura}\nRaio de Perseguição: {self.raioPerseguicao}\nPrecisão de Ataque à Distância: {self.ataqueDistancia}\nPosição X: {self.posicaoX}\nPosição Y: {self.posicaoY}"

    def atirar(self):
        if self.flechas > 0 and random.random() < 0.5:
            print(f"{self.nome} atirou uma flecha!")
            self.flechas -= 1

class Jogador:
    def __init__(self, nome, saude=20):
        self.nome = nome
        self.saude = saude
        self.posicaoX = random.randint(0, 10)
        self.posicaoY = random.randint(0, 10)
        
nome_jogador = input("Digite o nome do jogador: ")

jogador = Jogador(nome_jogador)

creeper = CreeperMinecraft(20, "3 blocos"," 16 Blocos ", 2, "Creeper", "Diurno e Noturno", False)

print(creeper)

esqueleto = EsqueletoMinecraft(20, "Arco de Ferro", 10, "Esqueleto", "Noturno", "Nenhuma", "15 blocos" , "16 blocos")

print(esqueleto)

creeper.correr(jogador)

esqueleto.atirar()
