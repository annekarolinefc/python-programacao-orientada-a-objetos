# class Pessoa:
#     _num_pessoa = 0

#     def __init__(self, idade):
#         self.__idade= idade
#         self._num_pessoa +=1

#     def get_num_pessoas():
#         return Pessoa._num_pessoa
    

class Pessoa:
    _num_pessoas = 0

    def __init__(self, idade):
        self.__idade= idade
        Pessoa._num_pessoas+=1 # contabilizando informação de criação
    
    def get_num_pessoas(self):
        return Pessoa._num_pessoas

p1 = Pessoa(20)
p2 = Pessoa(30)
p3 = Pessoa(60)
p4 = Pessoa(60)
#print(p1.num_pessoas)
print(Pessoa.get_num_pessoas(p1))
print(p1.get_num_pessoas())