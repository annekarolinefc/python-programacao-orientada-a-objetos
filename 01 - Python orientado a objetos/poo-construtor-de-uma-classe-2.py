class Televisao():
    def __init__(self, marca, ano, preco, n_canais): # self é um argumento obrigatório
        #print(f"O OBJETO {self} FOI CONSTRUÍDO")
        self.marca = marca
        self.ano = ano
        self.n_canais = n_canais
        self.preco = preco

tv_1  = Televisao('LG', 2023, 100, 23)
#print(tv_1) # posicao da memoria onde se encontra o objeto
#print(type(tv_1)) # visualizando o tipo do objeto
print(tv_1.ano)
print(tv_1.marca)
print(tv_1.n_canais)
print(tv_1.preco)