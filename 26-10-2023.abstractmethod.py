from abc import ABC, abstractmethod

# Definindo a interface Vendavel
class Vendavel(ABC):
    @abstractmethod
    def calcular_preco(self):
        pass

# Classe para representar Livro
class Livro(Vendavel):
    def __init__(self, titulo, preco_base, desconto, imposto):
        self.titulo = titulo
        self.preco_base = preco_base
        self.desconto = desconto
        self.imposto = imposto

    def calcular_preco(self):
        # Cálculo do preço do livro com desconto e imposto
        preco_com_desconto = self.preco_base * (1 - self.desconto)
        preco_final = preco_com_desconto * (1 + self.imposto)
        return preco_final

# Classe para representar Produto Eletrônico
class Eletronico(Vendavel):
    def __init__(self, nome, preco_base, desconto, imposto):
        self.nome = nome
        self.preco_base = preco_base
        self.desconto = desconto
        self.imposto = imposto

    def calcular_preco(self):
        # Cálculo do preço do eletrônico com desconto e imposto
        preco_com_desconto = self.preco_base * (1 - self.desconto)
        preco_final = preco_com_desconto * (1 + self.imposto)
        return preco_final

# Classe para representar Roupa
class Roupa(Vendavel):
    def __init__(self, descricao, preco_base, desconto, imposto):
        self.descricao = descricao
        self.preco_base = preco_base
        self.desconto = desconto
        self.imposto = imposto

    def calcular_preco(self):
        # Cálculo do preço da roupa com desconto e imposto
        preco_com_desconto = self.preco_base * (1 - self.desconto)
        preco_final = preco_com_desconto * (1 + self.imposto)
        return preco_final

# Solicitar ao usuário os valores dos produtos
titulo_livro = input("Insira o título do livro: ")
preco_base_livro = float(input("Insira o preço base do livro: ").replace(',', '.'))
desconto_livro = float(input("Insira o desconto do livro (em decimal): ").replace(',', '.'))
imposto_livro = float(input("Insira o imposto do livro (em decimal): ").replace(',', '.'))

nome_eletronico = input("Insira o nome do produto eletrônico: ")
preco_base_eletronico = float(input("Insira o preço base do produto eletrônico: ").replace(',', '.'))
desconto_eletronico = float(input("Insira o desconto do produto eletrônico (em decimal): ").replace(',', '.'))
imposto_eletronico = float(input("Insira o imposto do produto eletrônico (em decimal): ").replace(',', '.'))

descricao_roupa = input("Insira a descrição da roupa: ")
preco_base_roupa = float(input("Insira o preço base da roupa: ").replace(',', '.'))
desconto_roupa = float(input("Insira o desconto da roupa (em decimal): ").replace(',', '.'))
imposto_roupa = float(input("Insira o imposto da roupa (em decimal): ").replace(',', '.'))

# Criar instâncias das classes de produtos com os valores inseridos
livro = Livro(titulo_livro, preco_base_livro, desconto_livro, imposto_livro)
eletronico = Eletronico(nome_eletronico, preco_base_eletronico, desconto_eletronico, imposto_eletronico)
roupa = Roupa(descricao_roupa, preco_base_roupa, desconto_roupa, imposto_roupa)

# Calculando os preços dos produtos
preco_livro = livro.calcular_preco()
preco_eletronico = eletronico.calcular_preco()
preco_roupa = roupa.calcular_preco()

# Exibindo os preços calculados
print(f"Preço do Livro: R${preco_livro:.2f}")
print(f"Preço do Eletrônico: R${preco_eletronico:.2f}")
print(f"Preço da Roupa: R${preco_roupa:.2f}")




