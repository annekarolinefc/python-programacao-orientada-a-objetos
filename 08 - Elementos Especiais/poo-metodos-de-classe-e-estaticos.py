# METODOS DE CLASSE E ESTATICOS
# Ambos nao são ligados a instâncuia, mas sim a classe

class Pessoa:
    _num_pessoas = 0

    def __init__(self, idade):
        self.__idade= idade
        Pessoa._num_pessoas+=1 # contabilizando informação de criação

    # METODO DE CLASSE -> usa cls
    @classmethod
    def get_num_pessoas(cls):
        return cls._num_pessoas

p1 = Pessoa(20)
p2 = Pessoa(30)

print(f'USANDO METODOS ESTATICOS')
print("Pegando a nivel de classe:")
print(Pessoa.get_num_pessoas())
print("Pegando a nivel de instância:")
print(p1.get_num_pessoas())