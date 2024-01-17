class Televisao():
    def __init__(self): # self é um argumento obrigatório
        #print(f"O OBJETO {self} FOI CONSTRUÍDO")
        self.marca = 'LG'
        self.ano = 2023
        self.n_canais = 30
        self.preco = 1200

tv_1  = Televisao()
print(tv_1) # posicao da memoria onde se encontra o objeto
print(type(tv_1)) # visualizando o tipo do objeto
print(tv_1.ano)
print(tv_1.marca)
print(tv_1.n_canais)
print(tv_1.preco)