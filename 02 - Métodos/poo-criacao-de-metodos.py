class Televisao():
    def __init__(self, marca, ano, preco, n_canais): # self é um argumento obrigatório
        #print(f"O OBJETO {self} FOI CONSTRUÍDO")
        self.marca = marca
        self.ano = ano
        self.n_canais = n_canais
        self.preco = preco

    def aumentar_canal(self):
        self.n_canais+=1

    def diminuir_canal(self):
        self.n_canais-=1

tv_1  = Televisao('LG', 2023, 1000, 23)
print(tv_1.ano)
print(tv_1.marca)
print(tv_1.n_canais)
print(tv_1.preco)

print(f'\nDiminuindo o canal')
print(tv_1.n_canais)
tv_1.diminuir_canal()
print(f'Diminuindo o canal')
tv_1.diminuir_canal()
print(tv_1.n_canais)
print(f'\nAumentando o canal')
tv_1.aumentar_canal()
print(tv_1.n_canais)
# tv_2  = Televisao('Samsung', 2024, 1400, 25)
# print(tv_2.ano)
# print(tv_2.marca)
# print(tv_2.n_canais)
# print(tv_2.preco)