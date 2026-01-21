import perguntas_ao_cliente
import cliente_login
import os


def titulo():
    os.system('cls')
    nome_estilizado = '''
██╗   ██╗ ██╗ ████████╗  █████████╗
██║   ██║ ██║    ██║          ██╔═╝
██║   ██║ ██║    ██║        ██╔═╝ 
╚██╗ ██╔╝ ██║    ██║      ██╔═╝
 ╚████╔╝  ██║    ██║     █████████╗
  ╚═══╝   ╚═╝    ╚═╝     ╚════════╝'''
    caixa_com_nome(nome_estilizado)
    print('-' * 40)

def caixa_com_nome(nome):
    linhas = nome.strip('\n').split('\n')
    largura_maxima = max(len(linha) for linha in linhas)
    borda = '*' * (largura_maxima + 4)

    print(borda)
    for linha in linhas:
        print(f'* {linha.ljust(largura_maxima)} *')
    print(borda)

def main():
    
    while True:
        titulo()
        print('\n1 - Cadastrar novo usuário')
        print('2 - Fazer login')
        print('3 - Sair')
        opcao = input('Escolha uma opção: ')

        if opcao == '1':
            os.system('cls')
            perguntas_ao_cliente.cadastrar_usuario()
        elif opcao == '2':
            os.system('cls')
            cliente_login.login()
        elif opcao == '3':
            os.system('cls')
            print('Saindo do Marketplace...')
            break
        else:
            print('Opção inválida, tente novamente.')
            input('\nPressione ENTER para continuar...')


if __name__ == '__main__':
    main()