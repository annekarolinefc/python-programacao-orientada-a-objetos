
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
        if(isinstance(funcionario, Funcionario)):
            self._total_bonificacoes += funcionario.mostra_bonus()
        else:
            print(f'O objeto {self.__class__.__name__} nao tem implementado o método mostra_bonus()')
    @property
    def total_bonificacoes(self):
        return self._total_bonificacoes

class Engenheiro:
    def __init__(self, nome):
        self._nome = nome 

# TRANSFORMAR CLASSE EM UMA LISTA
class ClubeGerentes(): # SE PARECE A UMA LISTA
#class ClubeGerentes(list): 
    # funcionarios será uma lista de funcionario
    def __init__(self, nome, funcionarios):
        self.nome = nome 
        self._funcionarios = funcionarios 
    
    def __getitem__(self, item):
        return self._funcionarios[item]
    
    def __len__(self):
        return len(self._funcionarios)
    
    def add_item(self, item):
        self._funcionarios.append(item)

    def listagem(self):
        return self._funcionarios 

    def tamanho(self):
        return len(self._funcionarios)
    
g1 = Gerente('Lucas', 876, 1200, 123, 10)
g2 = Gerente('Pedro', 444, 1900, 123, 20)
g3 = Gerente('Ricardo', 333, 1400, 123, 12)
g4 = Gerente('Fabiano', 222, 1700, 123, 16)

lista_gerentes = [g1, g2, g3, g4]
clube = ClubeGerentes('Clube de Gerentes', lista_gerentes)
for g in clube:
    print(g._nome)

g5 = Gerente('Rafael', 444, 1900, 123, 20)
clube.add_item(g5)

print(f'Tamanho: {clube.tamanho()}')
print(f'Tamanho: {len(clube)}')
print(f'{clube[4]._nome}')

# DUNDER METHODS