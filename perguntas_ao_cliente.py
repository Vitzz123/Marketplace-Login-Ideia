import json
import os
from cliente import Usuario #importa o objeto do arquivo cliente.py

#esses códigos bem da biblioteca 'os'
#servem para que indepedente de onde o arquio estiver(pensando em portabilidade)
CAMINHO_BASE = os.path.dirname(__file__)
USUARIOS = os.path.join(CAMINHO_BASE, 'arquivos.json', 'usuarios.json')

def carregar_usuarios():  
    try:
        with open(USUARIOS, 'r') as usuarios:
            return json.load(usuarios)
    except FileNotFoundError:
        return []  

def salvar_usuarios(lista_usuarios): 
    os.makedirs(os.path.dirname(USUARIOS), exist_ok=True)
    with open(USUARIOS, 'w') as usuarios:
        json.dump(lista_usuarios, usuarios, indent=5)

def cadastrar_usuario():
    import main
    main.titulo()
    print('\n=== CADASTRO DE USUÁRIO ===\n')
    
    #deixa as variáveis em aberto para depois fazer a verificação delas
    nome = ''
    senha = ''
    cpf = ''
    email = ''
    ano_de_nascimento = ''
    telefone = ''
    endereco = ''

    #sequências de while que criam um laço de repetição que continuam pedindo a variável caso ela não tenha sido inserida corretamente
    while not nome.strip():#".strip" faz com que inputs de espaço também não computem no sistema
        nome = input('Digite seu nome completo: ')
        if not nome.strip():
            print('\n⚠️  Nome é obrigatório.\n')
        #esse if será repetido também todas as vezes que os objetivos não forem atingidos.
    while not senha.strip():
        senha = input('Digite sua senha: ')
        if not senha.strip():
            print('\n⚠️  Senha é obrigatória!\n')

    while not cpf.strip():
        cpf = input('Digite seu CPF: ')
        if not cpf.strip():
            print('\n⚠️  CPF é obrigatório!\n')

    while not email.strip():
        email = input('Digite seu email: ')
        if not email.strip():
            print('\n⚠️  Email é obrigatório!\n')

    while not ano_de_nascimento.strip():
        ano_de_nascimento = input('Digite seu ano de nascimento: ')
        if not ano_de_nascimento.strip():
            print('\n⚠️  Ano de nascimento é obrigatório\n')

    while not telefone.strip():
        telefone = input('Digite seu telefone: ')
        if not telefone.strip():
            print('\n⚠️  Telefone é obrigatório\n')

    while not endereco.strip():
        endereco = input('Digite seu endereço completo: ')
        if not endereco.strip():
            print('\n⚠️  Endereço é obrigatório\n')

    #variável     #objeto (instâncias desse objeto)
    usuario_obj = Usuario(nome, senha, cpf, email, ano_de_nascimento, telefone, endereco)
    #cria o perfil de cada usuário em um dicionário. 
    perfil_usuario = usuario_obj.para_dict()
    #transpoe essas informações para o objeto que com um método transformará as informações em dicionário e assim salvará em um .JSON

    #usuario é uma variável temporária, porque quando se dá um .append ele salva o que estava na memória, mas ao adicionar no .JSON ele o sobreescreverá sem as informações que estavam lá antes.
    usuarios = carregar_usuarios() #salva na memoria o que estava no .JSON
    usuarios.append(perfil_usuario) #adiciona o perfil_usuario na memória agora
    salvar_usuarios(usuarios) #salva tudo junto no .JSON

    print('Usuário cadastrado com sucesso!')
    input('\nPressione ENTER para continuar...')

