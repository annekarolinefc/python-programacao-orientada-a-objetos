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

TV  = Televisao('LG', 2023, 1000, 23)
print(TV) # temos um objeto na memoria
TV  = Televisao('LG', 2023, 1000, 23)
print(TV) # temos um objeto na memoria

# Vai eliminar o primeiro 


LG = TV
print(TV) # temos um objeto na memoria DA tv-> PEGA O MESMO ESPAÇO DA MEORIA
LG.diminuir_canal()
print('vai diminuir em ambas as referencias')
print(LG.n_canais)
print(TV.n_canais)
print('MESMO ENDEREÇO DE MEMORIA SENDO AFETADO')