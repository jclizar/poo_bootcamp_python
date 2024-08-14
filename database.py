from usuario import Usuario
from livro import Livro
from autor import Autor

def get_usaurios():
    return [
        Usuario("Livia","+55159988999900","Brasileira"),
        Usuario("Nicola","+55119988999901","Brasileira"),
        Usuario("Michelle","+55169988999902","Brasileira"),
        Usuario("Nadi","+58169988999903","Venezuelana"),
        Usuario("Raquel","+55169988999904","Brasileira"),
        Usuario("Leticia","+55769988999905","Brasileira"),
        Usuario("Jessica","+55139988999906","Brasileira")
    ]

def get_livros():
    return [
        Livro(
            lista_autor=[Autor('Josh Starmer PhD')],
            titulo='The StatQuest Illustrated Guide to Machine Learning!!!',
            editora='Packt Publishing',
            lista_genero=['Machine Learning','Statiscs'],
            lista_exemplar=['#01'],
            max_renovacao=1
        ),
        Livro(
            lista_autor=[Autor('Luciano Ramalho')],
            titulo='Python Fluente: Programação Clara, Concisa e Eficaz',
            editora='Novatec',
            lista_genero=['Programação'],
            lista_exemplar=['#01','#02'],
            max_renovacao=1
        ),
        Livro(
            lista_autor=[Autor('Robert C. Martin')],
            titulo='Código Limpo: Habilidades Práticas do Agile',
            editora='Alta Books',
            lista_genero=['Computação','Informática'],
            lista_exemplar=['#01','#02','#03'],
            max_renovacao=2
        )
    ]