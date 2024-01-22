# HERANÇA MULTIPLA
# - Classe que herda de várias outras
# - PROBLEMA:
    # Duas superclasses podem possuir o mesmo método ou atributo
    # Classes podem possuir o mesmo método

class A:
    def m1(self):
        print('metodo de A')


class B(A):
    def m2(self):
        print('metodo de B')

        
class C(A):
    def m2(self):
        print('metodo de C')

class D(B, C):
    pass

d = D()
print(f'{d.m1()}')
print(f'{d.m2()}')

# MRO - METHOD RESOLUTION ORDER - Ordem de Resolução de Métodos
# toda classe tem o atributo __mro__: retorna uma tupla de referencias das superclasses na ordem MRO
print(D.mro())
print(B.mro())