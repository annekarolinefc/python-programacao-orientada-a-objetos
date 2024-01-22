# ERROS
    # Excelente para testes
    # Não realiza o 'stop' no programa
    # Mensagens customizadas quando encontra um erro 
try: 
    valor = int(input('Digite o valor do seu produto: '))
    print(valor)
except ValueError:
    print('Favor digitar um valor em numeros.')
else:
    print('Usuario digitou um valor correto')
    resultado = valor * 2
    print(f'Resultado (valor * 2): {resultado}')
finally:
    print(f'Codigo OK. (Esse trecho sempre será executado)')