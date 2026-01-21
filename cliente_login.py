import json
import os
import main

CAMINHO_BASE = os.path.dirname(__file__)
USUARIOS = os.path.join(CAMINHO_BASE, 'arquivos.json', 'usuarios.json')

def login():
    main.titulo()
    print('\n=== LOGIN ===\n')
    email_verificar = input('Email: ').strip()
    senha_verificar = input('Senha: ').strip()

    try:
        with open(USUARIOS, 'r') as arquivo:
            lista_usuarios = json.load(arquivo)
    except FileNotFoundError:
        print('Nenhum usuário cadastrado ainda.')
        input('\nPressione ENTER para continuar...')
        return

    # Procura usuário com email e senha correspondentes
    for usuario in lista_usuarios:
        if email_verificar == usuario.get("email") and senha_verificar == usuario.get("senha"):
            print(f'Bem-vindo ao Marketplace, {usuario.get("nome")}!')
            input('\nPressione ENTER para continuar...')
            main.main()
            return

    print('Email ou senha incorretos.')
    print('\n1 - Tentar novamente')
    print('2 - Voltar ao menu principal')
    opcao = input('Escolha uma opção: ')
    
    if opcao == '1':
        login()  # Chama a função novamente para tentar de novo
    else:
        return  # Volta ao menu principal
