import perguntas_ao_cliente  
import json
import os

CAMINHO_BASE = os.path.dirname(__file__)
USUARIOS = os.path.join(CAMINHO_BASE, 'arquivos.json', 'usuarios.json')

class Usuario():
    

    def __init__(self, nome, senha, cpf, email, ano_de_nascimento, telefone, endereco):
        self._nome = nome.title()
        self._senha = senha
        self._cpf = cpf
        self._email = email
        self._ano_de_nascimento = str(ano_de_nascimento)
        self._telefone = telefone
        self._endereco = endereco

    @property
    def nome(self):
        return self._nome
    @property
    def senha(self):
        return self._senha
    @property
    def cpf(self):
        return self._cpf
    @property
    def email(self):
        return self._email
    @property
    def ano(self):
        return self._ano_de_nascimento
    @property
    def telefone(self):
        return self._telefone
    @property
    def endereco(self):
        return self._endereco
    
    def para_dict(self):
        return {
            "nome": self.nome,
            "senha": self.senha,
            "cpf": self.cpf,
            "email": self.email,
            "ano": self.ano,
            "telefone": self.telefone,
            "endereco": self.endereco
        }