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

print(f'\nLoop for para diminuir os canais -> 5 x')
print(f'Canais atuais: {tv_1.n_canais}')
for i in range(5):
    tv_1.diminuir_canal()
print(f'Canais atuais: {tv_1.n_canais}')