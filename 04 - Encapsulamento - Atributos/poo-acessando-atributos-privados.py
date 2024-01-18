# ATRIBUTOS PRIVADOS - somente usados dentro da classe

class Televisao():
    def __init__(self, marca, ano, preco, n_canais): # self é um argumento obrigatório
        #print(f"O OBJETO {self} FOI CONSTRUÍDO")
        self.marca = marca
        self.ano = ano
        self.n_canais = n_canais
        self.preco = preco
        self.__ligada = False # tornar privada o atributo

    def aumentar_canal(self):
        self.n_canais+=1

    def diminuir_canal(self):
        self.n_canais-=1

    def liga_tv(self):
        self.__ligada = True
        print(f'TV LIGADA! {self.__ligada}')

    def desliga_tv(self):
        self.__ligada = False
        print(f'TV DESLIGADA! {self.__ligada}')

TV  = Televisao('LG', 2023, 1000, 23)
print(TV) # temos um objeto na memoria

print(f'\nACESSANDO ATRIBUTOS PRIVADOS')
print(TV._Televisao__ligada)