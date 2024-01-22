'''
FUNÇÕES

Criar um programa que calcula a quantidade de tinta necessaria para pintar uma parede.
O usuário deverá fornecer as seguintes informações: rendimento, altura, largura.
O programa deve mostrar na tela a mensagem: 'Você necessita de x latas de tintas'
'''

def calculaArea(altura, largura):
        area = altura * largura
        return area 
    
def calculaRendimento(area, rendimento):
    rende = area / rendimento
    print(f'Será necessário {rende} latas de tintas.')
    return rende 

rendimento = int(input('Insira o rendimento da tinta (1 lata para x metros quadrados): '))
altura = int(input('Insira a altura da parede: '))
largura = int(input('Insira a largura da parede: '))

area = calculaArea(altura, largura)
rende = calculaRendimento(area, rendimento)
print(f'Area: {area} m²')
print(f'Rendimento: {rende} latas')