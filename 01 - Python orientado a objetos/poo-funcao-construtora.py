class Televisao():
    def __init__(self): # self é um argumento obrigatório
        print(f"O OBJETO {self} FOI CONSTRUÍDO")

tv_1  = Televisao()
print(tv_1) # posicao da memoria onde se encontra o objeto
print(type(tv_1)) # visualizando o tipo do objeto

tv_2  = Televisao()
print(tv_2)