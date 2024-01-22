# HERANÇA
# Evitar repetir código

class Funcionario:
    def __init__(self, nome, cpf, salario):
        self._nome = nome
        self._cpf = cpf 
        self._salario = salario
        
class Gerente:
    def __init__(self, nome, cpf, salario, senha, qtd_subordinados):
        self._nome = nome
        self._cpf = cpf 
        self._salario = salario
        self._senha = senha 
        self._qtd_subordinados = qtd_subordinados
    
    def validacao(self, senha):
        if self._senha == senha:
            print('Acesso permitido')
            return True
        else:
            print('Acesse não permitido')
            return False

class Secretaria:
    def __init__(self, nome, cpf, salario, senha, qtd_gerentes):
        self._nome = nome
        self._cpf = cpf 
        self._salario = salario
        self._senha = senha 
        self._qtd_gerentes = qtd_gerentes