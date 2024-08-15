import uuid
import random

rd = random.Random()
rd.seed(123)

class Livro:
    def __init__(self, lista_autor, titulo, editora, lista_genero, lista_exemplar, max_renovacao):
        self.__lista_autor = lista_autor
        self.__titulo = titulo
        self.__editora = editora
        self.__lista_genero = lista_genero
        self.lista_exemplar = lista_exemplar  # Usando o setter aqui
        self.max_renovacao = max_renovacao  # Usando o setter aqui
        self.__id = str(uuid.UUID(int=rd.getrandbits(128), version=4))

    @property
    def max_renovacao(self):
        return self.__max_renovacao
    
    @max_renovacao.setter
    def max_renovacao(self, value):
        if value < 0:
            raise ValueError("O número máximo de renovações deve ser positivo.")
        self.__max_renovacao = value

    @property
    def lista_exemplar(self):
        return self.__lista_exemplar

    @lista_exemplar.setter
    def lista_exemplar(self, value):
        if not isinstance(value, list):
            raise TypeError("A lista de exemplares deve ser uma lista.")
        self.__lista_exemplar = value

    @property
    def id(self):
        return self.__id

    def __repr__(self):
        return f'Livro | ID: {self.__id}, Titulo: {self.__titulo}, Autores: {self.__lista_autor}, Lista exemplares: {self.__lista_exemplar}, Lista generos: {self.__lista_genero}, Editora: {self.__editora} \n'
