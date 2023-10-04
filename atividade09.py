import random

def remover_acentos(palavra):
    acentos = {'á':'a', 'é':'e', 'í':'i', 'ó':'o', 'ú':'u', 'ã':'a', 'õ':'o', 'â':'a', 'ê':'e', 'ô':'o'}
    return ''.join(acentos[i] if i in acentos else i for i in palavra)

agenda = []

def adicionar_contato(nome, telefone, email):
    agenda.append((nome, telefone, email))

def listar_contatos():
    for contato in agenda:
        print(f"Nome: {contato[0]}, Telefone: {contato[1]}, email: {contato[2]}")

def pesquisar_contato():
    print("1 - Pesquisar por nome")
    print("2 - Pesquisar por telefone")
    print("3 - Pesquisar por email")
    
    opcao = input("Escolha uma opção: ")
    
    if opcao == '1':
        nome = input("Digite o nome do contato a ser pesquisado: ")
        for contato in agenda:
            if remover_acentos(contato[0].lower()) == remover_acentos(nome.lower()):
                return contato
    elif opcao == '2':
        telefone = input("Digite o telefone do contato a ser pesquisado: ")
        for contato in agenda:
            if contato[1] == telefone:
                return contato
    elif opcao == '3':
        email = input("Digite o email do contato a ser pesquisado: ")
        for contato in agenda:
            if contato[2] == email:
                return contato

    return None

while True:
    print("1 - Adicionar contato")
    print("2 - Listar contatos")
    print("3 - Pesquisar contato")
    print("4 - Sair")
    
    opcao = input("Escolha uma opção: ")
    
    if opcao == '1':
        nome = input("Digite o nome do contato: ")
        telefone = input("Digite o telefone do contato: ")
        email = input("Digite o email do contato: ")
        adicionar_contato(nome, telefone, email)
    elif opcao == '2':
        listar_contatos()
    elif opcao == '3':
        contato = pesquisar_contato()
        if contato:
            print(f"Nome: {contato[0]}, Telefone: {contato[1]}, email: {contato[2]}")
        else:
            print("Contato não encontrado.")
    elif opcao == '4':
        break
