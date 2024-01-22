'''
IF, ELIF, ELSE

Criar um programa que dependendo da temperatura (em celsius) dos steak, ele retorna o ponto de cozimento em portugues. 
O usuário deverá fornecer a temperatura.

Temperatura - Cozimento
120ºf ou 48ºc - Rare (selada)
130ºf ou 54ºc - Medium rare (Ao ponto para o mal)
140ºf ou 60ºc - Medium (Ao ponto)
150ºf ou 65ºc - Medium well (Ao ponto para o bem)
160ºf ou 71ºc - Well done (Bem passada)
'''

temp = int(input('Insira o valor da temperatura da carne: '))
if temp < 48:
    print('Cozinhar por mais alguns minutos.')
elif temp in range(48, 53):
    print('Rare (selada)')
elif temp in range(54, 59):
    print('Medium rare (Ao ponto para o mal)') 
elif temp in range(60, 65):
    print('Medium (Ao ponto)') 
elif temp in range(65, 70):
    print('Medium well (Ao ponto para o bem)')
else:
    print('Well done (Bem passada)')