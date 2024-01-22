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

g1 = Gerente('Lucas', 987, 5600, 1234, 10)
s1 = Secretaria('Renata', 345, 4000, 789, 5)

print(f'Bonus da Gerente: {g1.mostra_bonus()}') #560
print(f'Bonus da Secretaria: {s1.mostra_bonus()}') #400