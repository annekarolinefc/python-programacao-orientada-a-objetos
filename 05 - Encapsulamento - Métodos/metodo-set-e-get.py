# ATRIBUTOS PRIVADOS - somente usados dentro da classe

class Televisao():
    # METODO CONSTRUTOR - COM ATRIBUTOS
    def __init__(self, marca, ano, preco, n_canais): # self é um argumento obrigatório
        #print(f"O OBJETO {self} FOI CONSTRUÍDO")
        self.marca = marca
        self.ano = ano
        self.n_canais = n_canais
        self.preco = preco
        self.__ligada = False # tornar privada o atributo

    # METODOS PARA MODIFICAR OS ATRIBUTOS
    def aumentar_canal(self):
        self.n_canais+=1

    def diminuir_canal(self):
        self.n_canais-=1

    # ACESSANDO ATRIBUTO PRIVADO DENTRO DA PROPRIA CLASSE
    def liga_tv(self):
        self.__ligada = True
        print(f'TV LIGADA! {self.__ligada}')

    def desliga_tv(self):
        self.__ligada = False
        print(f'TV DESLIGADA! {self.__ligada}')

    # SET E GET- MÉTODOS DE ACESSO
    def getMarca(self):
        return self.marca
    
    # def setMarca(self, marca_):
    #     self.marca = marca_.title()
    def setMarca(self, marca_):
        if len(marca_) > 5:
            self.marca = marca_.title()
        else:
            self.marca = marca_.upper()

    # SET E GET- MÉTODOS DE ACESSO PARA ATRIBUTOS PRIVADOS
    def getLigada(self):
        return self.__ligada 
    
    def setLigada(self,valor):
        self.__ligada = valor        
    

b1 = Televisao('AOC', 2023, 500, 43)
#print(b1) # temos um objeto na memoria

# NÃO É UMA BOA PRATICA - ALTERAR ATRIBUTO NESSA FORMA
# print(b1.marca)
# b1.marca = 'SAMSUNG'
# print(b1.marca)

# USANDO OS METODOS DE ACESSO
print(b1.marca)
b1.setMarca('SAMSUNG')
print(b1.marca)
b1.setMarca('lg')
print(b1.marca)
b1.setMarca('essa é uma marca de tv')
print(b1.marca)
b1.setMarca('aoc')
print(b1.marca)

print(b1.getMarca())