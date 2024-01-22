# Classes Abstratas ou ABS 

# Complementa a ideia de Duck Typing
# - Projeto para outras classe
# - Reforçar a implementação da interface (métodos) (classes filhas)
# - Obriga a criação de métodos
# - Uma classe abstrata não pode ser instanciada
# - Deve conter pelo menos um método abstrato

# Um método abstrato possui uma declaralçao, mas não uma implementação. 
# Para transformar um método em abstrato - decorar: @abstractmethod

from abc import ABC # abstract base classes
from collections.abc import MutableSequence 

# class ClubeSecretarias(MutableSequence):
#     def __delitem__(self, item):
#         print('delete')
#     def __getitem__(self, item):
#         print('coleta')

class ClubeSecretarias(MutableSequence):
    # INTERFACE OBRIGATÓRIA
    def __delitem__(self, item):
        print('delete')
    def __getitem__(self, item):
        print('coleta')
    def __len__(self, item):
        print('tamanho')
    def __setitem__(self, item):
        print('setar')
    def insert(self, item): # não é metodo magico
        print('inserir')

cs = ClubeSecretarias()