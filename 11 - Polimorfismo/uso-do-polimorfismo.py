# POLIMORFISMO
# É a capacidade quem um objeto possui de ser referenciado de várias formas. 

class Funcionario:
    def __init__(self, nome, cpf, salario):
        self._nome = nome
        self._cpf = cpf 
        self._salario = salario
        
    def mostra_bonus(self):
        return self._salario  * 0.10 
    
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

    def mostra_bonus(self):
        return self._salario  * 0.10  + self._qtd_subordinados*0.10
    
class Secretaria(Funcionario):
    def __init__(self, nome, cpf, salario, senha, qtd_gerentes):
        super().__init__(nome, cpf, salario) # SEM SELF
        self._senha = senha 
        self._qtd_gerentes = qtd_gerentes

    def mostra_bonus(self):
        return self._salario  * 0.10  + self._qtd_gerentes*0.10

class GestaoDeBonus:
    # Uma classe que vai gerenciar objetos do tipo funcionario
    def __init__(self, total_bonificacoes=0):
        self._total_bonificacoes = total_bonificacoes

    #mostra_bonus existe para varios tipos de funcionarios
    # toda vez que adiciona um funcionario, é contabilizado nessa funcao de registro
    # pega cada um dos objetos, acessa sua funcao especifica e realiza calculo
    def registra(self, funcionario):
        self._total_bonificacoes += funcionario.mostra_bonus()

    @property
    def total_bonificacoes(self):
        return self._total_bonificacoes

# print(f'Bonus da Gerente: {g1.mostra_bonus()}') #560
# print(f'Bonus da Secretaria: {s1.mostra_bonus()}') #400


g1 = Gerente('Lucas', 987, 5600, 1234, 10)
s1 = Secretaria('Renata', 345, 4000, 789, 5)

gestao = GestaoDeBonus()
gestao.registra(g1)
gestao.registra(s1)

print(f'Total de bonificações: {gestao.total_bonificacoes}')

s2 = Secretaria('Julia', 345, 4000, 789, 5)
gestao.registra(s2)
print(f'Total de bonificações: {gestao.total_bonificacoes}')