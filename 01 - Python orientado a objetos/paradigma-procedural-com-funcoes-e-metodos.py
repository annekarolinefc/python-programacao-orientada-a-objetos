def cria_tv(ano, marca, preco, n_canais):
    tv = {'ano': ano, 'marca': marca, 'preco': preco, 'n_canais':n_canais}
    return tv 

t1 = cria_tv(ano = 2023, marca = 'LG', preco = 1200 ,n_canais = 30)
t2 = cria_tv(ano = 2024, marca = 'Samsung', preco = 1500, n_canais = 50)

print(t1)
print(t1.keys())

# aumentar canal
def aumentar_canais(tv, valor):
    tv['n_canais'] += valor

print('Aumentando Canais')    
print(t1)
aumentar_canais(t1, 5)
print(t1)

# diminuir canal
def diminuir_canais(tv, valor):
    tv['n_canais'] -= valor

print('Diminuindo Canais')    
print(t1)
diminuir_canais(t1, 5)
print(t1)