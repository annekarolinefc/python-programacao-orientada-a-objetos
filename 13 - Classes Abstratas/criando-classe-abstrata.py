#from abc import ABC # abstract base classes

# NÃO É CLASSE ABSTRATA
# import abc 
# class Funcionario(abc.ABC):
#     pass 

# f = Funcionario()


import abc 
class Funcionario(abc.ABC):

    @abc.abstractmethod
    def nome(self):
        print('Nome')

    @abc.abstractmethod
    def senha(self):
        print('Senha')


# INTERFACE
# Classe funcionario se tornou uma interface - nao posso instancias
class Atendente(Funcionario):
    def nome(self):
        print('Nome')
    def senha(self):
        print('Senha')

a = Atendente()
print(a)
print(a.senha())