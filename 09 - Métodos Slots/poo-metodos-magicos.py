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
print('Visualizando metodos magicos...')
print(dir(p1))

print('METODO __NEW__')
pessoa = object.__new__(Pessoa)