class Fratura:
    def __init__(self, nf, tam, nome):
        self._nf = nf # atributo protegido
        self.tam = tam 
        self.__nome = nome # atributo privado

    def _calculaArea(self):
        return self._nf * self.tam
    
f1 = Fratura(5, 10, 'F1')
print(f1._nf)
print(dir(f1))

# Acessando um atributo privado
#print(f1.__nome)
print(f1._Fratura__nome)

# Acessando o metodo privado
print(f1._calculaArea())