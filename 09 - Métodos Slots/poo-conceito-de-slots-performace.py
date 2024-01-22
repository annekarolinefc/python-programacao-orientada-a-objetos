class Pessoa:
    _num_pessoas = 0
    #__slots__ = ['__idade', 'nome']

    def __init__(self, idade, nome):
        self.__idade= idade
        self.nome = nome
        
        Pessoa._num_pessoas+=1 # contabilizando informação de criação

    # METODO DE CLASSE -> usa cls
    @classmethod
    def get_num_pessoas(cls):
        return cls._num_pessoas

p1 = Pessoa(20, 'Pedro')

# CONSUMO DE MEMORIA 
print(vars(p1))
p1.sexo='M'
print(vars(p1))
p1.altura = 1.7
print(vars(p1))