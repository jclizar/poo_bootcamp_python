from pessoa import Pessoa
import uuid
import random

rd = random.Random()
rd.seed(123) 

class Usuario(Pessoa):
    def __init__(self, nome,telefone,nacionalidade):
        super().__init__(nome)
        self.telefone=telefone
        self.nacionalidade=nacionalidade
        self.__id = str(uuid.UUID(int=rd.getrandbits(128), version=4))

    def __repr__(self):
        return f'Usuario | ID: {self.__id}, Nome: {self.nome}, Telefone: {self.telefone}, Nacionaldiade: {self.nacionalidade}\n'
    
    @property
    def id(self):
        return self.__id