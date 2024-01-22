'''
SETS

Cria um programa que gera 3 listas de acordo com a necessidade logo abaixo: 

Lista1 = Funcionários que tem carro e trabalham a noite
Lista2 = Funcionarios que tem carro e trabalham durante o dia
Lista3 = Funcionarios que não tem carro

'''

funcionarios = ['Ana', 'Marcos', 'Alice', 'Pedro', 'Shopia', 'Bruno', 'Melissa']
turno_dia = ['Ana', 'Marcos', 'Alice', 'Melissa']
turno_noite = ['Pedro', 'Sophia', 'Bruno']
tem_Carro = ['Marcos', 'Alice', 'Bruno', 'Melissa']

#Lista1 = Funcionários que tem carro e trabalham a noite
lista1 = set(tem_Carro).intersection(turno_noite)
print(f'Funcionários que tem carro e trabalham a noite: {lista1}')

#Lista2 = Funcionarios que tem carro e trabalham durante o dia
lista2 = set(tem_Carro).intersection(turno_dia)
print(f'Funcionarios que tem carro e trabalham durante o dia: {lista2}')

#Lista3 = Funcionarios que não tem carro
lista3 = set(funcionarios).difference(tem_Carro)
print(f'Funcionarios que não tem carro: {lista3}')