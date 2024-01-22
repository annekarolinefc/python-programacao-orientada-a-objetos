# ATRIBUTOS PRIVADOS - somente usados dentro da classe

class Televisao():
    # METODO CONSTRUTOR - COM ATRIBUTOS
    def __init__(self, marca, ano, preco, n_canais): # self é um argumento obrigatório
        #print(f"O OBJETO {self} FOI CONSTRUÍDO")
        self.__marca = marca
        self.ano = ano
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
    

b1 = Televisao('AOC', 2023, 500, 43)
print(b1.marca)
#b1.marca = 'LG' # NAO PODE SER FEITO DIRETAMENTE. PRECISA USAR O SET
b1.marca='LG'
print(b1.marca)