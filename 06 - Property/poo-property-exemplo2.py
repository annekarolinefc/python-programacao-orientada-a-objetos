class Televisao():
    # METODO CONSTRUTOR - COM ATRIBUTOS
    def __init__(self, marca, ano, preco, n_canais): 
        self.__marca = marca
        self.__ano = ano
        self.n_canais = n_canais
        self.preco = preco
        self.__ligada = False # tornar privada o atributo

    # PROPERTY NO GET
    @property
    def marca(self):
        return self.__marca # a variavel privada esta sendo usada dentro da funcao
    
    @marca.setter
    # PROPERTY NO SET
    def marca(self, nova_marca):
        self.__marca = nova_marca
    
    def setAno(self, novo_ano):
        self.__ano = novo_ano

    def getAno(self):
        return self.__ano

    ano = property(fget=getAno, fset=setAno)

b1 = Televisao('AOC', 2023, 500, 43)
# print(b1.getAno())
# #b1.marca = 'LG' # NAO PODE SER FEITO DIRETAMENTE. PRECISA USAR O SET
# b1.setAno(2010)
# print(b1.getAno())

print(b1.ano)
b1.ano=2020
print(b1.ano)