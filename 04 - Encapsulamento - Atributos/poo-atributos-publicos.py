class Televisao():
    def __init__(self, marca, ano, preco, n_canais): # self é um argumento obrigatório
        #print(f"O OBJETO {self} FOI CONSTRUÍDO")
        self.marca = marca
        self.ano = ano
        self.n_canais = n_canais
        self.preco = preco
        self.ligada = False

    def aumentar_canal(self):
        self.n_canais+=1

    def diminuir_canal(self):
        self.n_canais-=1

TV  = Televisao('LG', 2023, 1000, 23)
print(TV) # temos um objeto na memoria
print(TV.ligada)
TV.ligada = True
print('Modificando o atributo')
print(f'Ligando a TV com TV.ligada=True: {TV.ligada}')