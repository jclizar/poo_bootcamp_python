from pessoa import Pessoa

class Autor(Pessoa):
    def __init__(self, nome):
        super().__init__(nome)

    def __repr__(self):
        return f'{self.nome}'