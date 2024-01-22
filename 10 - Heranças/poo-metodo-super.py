# HERANÇA
# Evitar repetir código

class Funcionario:
    def __init__(self, nome, cpf, salario):
        self._nome = nome
        self._cpf = cpf 
        self._salario = salario
        
class Gerente(Funcionario):
    def __init__(self, nome, cpf, salario, senha, qtd_subordinados):
        Funcionario.__init__(self, nome, cpf, salario)
        self._senha = senha 
        self._qtd_subordinados = qtd_subordinados
    
    def validacao(self, senha):
        if self._senha == senha:
            print('Acesso permitido')
            return True
        else:
            print('Acesse não permitido')
            return False

class Secretaria(Funcionario):
    def __init__(self, nome, cpf, salario, senha, qtd_gerentes):
        super().__init__(nome, cpf, salario) # SEM SELF
        self._senha = senha 
        self._qtd_gerentes = qtd_gerentes

print(f'Usando metodo super')
s1 = Secretaria('Julia', 159, 1500, 123456, 5)
print(f'Nome: {s1._nome}')