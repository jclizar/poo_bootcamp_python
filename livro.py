import uuid
import random

rd = random.Random()
rd.seed(123) 

class Livro:
    def __init__(self,lista_autor,titulo,editora,lista_genero,lista_exemplar,max_renovacao):
        self.__lista_autor=lista_autor
        self.__titulo=titulo
        self.__editora=editora
        self.__lista_genero=lista_genero
        self.__lista_exemplar=lista_exemplar
        self.__max_renovacao=max_renovacao
        self.__id = str(uuid.UUID(int=rd.getrandbits(128), version=4))

    @property
    def max_renovacao(self):
        return self.__max_renovacao
    
    @property
    def id(self):
        return self.__id

    @property
    def lista_exemplar(self):
        return self.__lista_exemplar

    def __repr__(self):
        return f'Livro | ID: {self.__id}, Titulo: {self.__titulo}, Autores: {self.__lista_autor}, Lista exemplares: {self.__lista_exemplar}, Lista generos: {self.__lista_genero}, Editora: {self.__editora} \n'