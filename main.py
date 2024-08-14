
# Jéssica Caroline Lizar
#%%
'''
Gerenciamento de Biblioteca:

Vamos criar um sistema orientado a objetos para representar um
sistema de biblioteca seguindo os requisitos abaixo:

✅ 1. Cada livro pode ter um ou mais autores. 
✅ 2. A biblioteca controla apenas o nome, o telefone e a nacionalidade
de cada usuário.
✅ 3. Cada livro tem um título, editora, uma lista de gêneros aos quais
pertence e uma lista de exemplares disponíveis.
✅ 4. Quando um exemplar é emprestado, ele é removido da lista de
exemplares disponíveis.
✅ 5. Alguns livros podem ter um número máximo de renovações
permitidas.
✅ 6. A biblioteca mantém um registro de todos os empréstimos
realizados, incluindo detalhes como data de empréstimo, data de
devolução e estado do exemplar (por exemplo, emprestado ou
devolvido).

Para modelar o sistema, utilize obrigatoriamente os conceitos de classe,
herança, propriedade, encapsulamento e classe abstrata.
'''

from biblioteca import Biblioteca
from usuario import Usuario
from database import get_livros, get_usaurios

#%%
# criando a biblioteca
biblioteca = Biblioteca(livros=get_livros(), usuarios=get_usaurios())

#%%
# listar usuarios
biblioteca.listar_usuarios()

#%%
# listar livros
biblioteca.listar_livros()

#%%
#Adicionando um novo usuario
novo_usuario = Usuario("Mariana","+5516977562340","Brasileira")
biblioteca.add_user(novo_usuario)
biblioteca.listar_usuarios()
#%%
#emprestimo
livro_emprestimo = biblioteca.return_livro('610e4ad5-09c4-4055-9ff4-948fe6b4f832')

biblioteca.registro_emprestimo(novo_usuario,livro_emprestimo,'#01')
biblioteca.registro_emprestimo(novo_usuario,livro_emprestimo,'#01')
biblioteca.registro_emprestimo(novo_usuario,livro_emprestimo,'#01')
biblioteca.registro_emprestimo(novo_usuario,livro_emprestimo,'#01')
