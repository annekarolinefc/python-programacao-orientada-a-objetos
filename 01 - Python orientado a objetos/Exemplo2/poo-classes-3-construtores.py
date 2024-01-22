# PYTHON OBJECT-ORIENTED PROGRAMMING 
# CLASSES
    # Utilizadas para criar objetos (instances)
    # OBJETOS sao partes dentro de uma Class
    # Utilizadas para agrupar dados e funções, podendo reutilizar

# CLASS: frutas
# Objects: Abacate, Banana
from datetime import datetime

class Funcionario:
    def __init__(self, nome, sobrenome, ano_nascimento):
        self.nome = nome
        self.sobrenome = sobrenome 
        self.ano_nascimento = ano_nascimento

    def nome_completo(self):
        return self.nome + ' ' + self.sobrenome
    
    def idade_funcionario(self):
        ano_atual = datetime.now().year
        self.ano_nascimento = int(ano_atual - self.ano_nascimento)
        return self.ano_nascimento

usuario1 = Funcionario('Ana', 'Paula', 2020)
print(usuario1.nome_completo())
print(usuario1.idade_funcionario())