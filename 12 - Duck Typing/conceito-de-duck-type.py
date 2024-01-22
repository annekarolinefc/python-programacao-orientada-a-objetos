# O que é Duck Typing (evita acoplamento excessivo)
# é uma caracteristicas de tipos em que a semântica de uma classe é 
# determinada pela sua capacidade de responder a alguma mensagem

# DUCK TYPING evita testes: type(), isintace() e hasattr()
# No lugar, usa (Pythonica): try/except

def Funcionario():
     ...


def registra(self, funcionario):
    try:
        self._total_bonus += obj.mostra_bonus()
    except AttributeError as e:
        print(e)