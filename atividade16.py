import random

class Ataque:
    def __init__(self, nome, dano, tipo):
        self.nome = nome
        self.dano = dano
        self.tipo = tipo

    def toString(self):
        return f"{self.nome} {self.dano} {self.tipo}"

class AtaqueRapido(Ataque):
    def __init__(self, ataqueRapido, nome, dano, tipo, energiaConsumida):
        super().__init__(nome, dano, tipo)
        self.__ataqueRapido = ataqueRapido
        self.energiaConsumida = energiaConsumida

    def toString(self):
        return f"{self.__ataqueRapido} {super().toString()}"

class AtaqueCarregado(Ataque):
    def __init__(self, ataqueCarregado, nome, dano, tipo, energiaConsumida):
        super().__init__(nome, dano, tipo)
        self.__ataqueCarregado = ataqueCarregado
        self.energiaConsumida = energiaConsumida

    def toString(self):
        return f"{self.__ataqueCarregado} {super().toString()}"

class Pokemon:
    def __init__(self, nome, hp, iv, tipos, ataqueRapido, ataquesCarregado):
        self.nome = nome
        self.hp = hp
        self.iv = iv
        self.tipos = tipos
        self.ataqueRapido = ataqueRapido
        self.energiaAcumulada = 0
        self.ataquesCarregado = ataquesCarregado

    def toString(self):
        return f"{self.nome} {self.hp} {self.iv} {self.tipos} {self.ataqueRapido.toString()} {[ataque.toString() for ataque in self.ataquesCarregado]}"

    def atacar(self, outro_pokemon):
        ordem_ataque = [self, outro_pokemon]
        random.shuffle(ordem_ataque)  # Embaralha a ordem de ataque

        while self.hp > 0 and outro_pokemon.hp > 0:
            ordem_ataque[0].realizar_ataque(ordem_ataque[1])
            if ordem_ataque[1].hp <= 0:
                break
            ordem_ataque[1].realizar_ataque(ordem_ataque[0])

        if self.hp <= 0:
            print(f"{outro_pokemon.nome} venceu!")
        else:
            print(f"{self.nome} venceu!")

    def realizar_ataque(self, outro_pokemon):
        if self.energiaAcumulada >= 50:
            ataque = random.choice(self.ataquesCarregado)
            print(f"{self.nome} usou o ataque carregado {ataque.nome}")
            outro_pokemon.hp -= ataque.dano
            self.energiaAcumulada -= ataque.energiaConsumida
        else:
            print(f"{self.nome} usou o ataque rápido {self.ataqueRapido.nome}")
            outro_pokemon.hp -= self.ataqueRapido.dano
            self.energiaAcumulada += self.ataqueRapido.energiaConsumida

# Manipulando a classe Ataque
# ataqueRapido, nome, dano, tipo
caudaDeDragao = AtaqueRapido("Ataque Rápido", "Cauda de Dragão", 13, "Dragão", 20)
cachoeira = AtaqueRapido("Ataque Rápido", "Cachoeira", 16, "Água", 15)
nevasca = AtaqueCarregado("AtaqueCarregado", "Nevasca", 140, "Gelo", 50)
jatoDeAgua = AtaqueCarregado("AtaqueCarregado", "Jato de Água", 130, "Água", 50)
meteoroDoDragao = AtaqueCarregado("AtaqueCarregado", "Meteoro do Dragão", 150, "Dragão", 50)
garraDeDragao = AtaqueCarregado("AtaqueCarregado", "Garra de Dragão", 50, "Dragão", 33)

# Manipulando a classe Pokemon
kyogre = Pokemon("Kyogre", 174, 45, ["Água"], cachoeira, [jatoDeAgua, nevasca])
dragonite = Pokemon("Dragonite", 177, 44, ["Dragão", "Voador"], caudaDeDragao, [meteoroDoDragao, garraDeDragao])

# Chama a função toString para imprimir as informações dos Pokémon
#print(kyogre.toString())
#print(dragonite.toString())

# Iniciar a batalha
kyogre.atacar(dragonite)
