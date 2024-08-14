from emprestimo import Emprestimo

class Biblioteca:
    def __init__(self,livros,usuarios):
        self._livros=livros
        self._exemplares=livros
        self._usuarios=usuarios
        self.dict_emprestimos = {}

    @property
    def livros(self):
        return self._livros
    
    @property
    def usuarios(self):
        return self._usuarios
        
    # Listagem
    def listar_livros(self):
        print(self.livros)

    def listar_usuarios(self):
        print(self.usuarios)

    # Adicionar
    def add_user(self,valor):
        self.usuarios.append(valor)

    # Buscar idx user_id
    def search_list_user_idx(self,id):
        for idx,user in enumerate(self.usuarios):
            if user.id == id:
                return idx
            
    # Buscar idx livro_id
    def search_livro_user_idx(self,id):
        for idx,livro in enumerate(self.livros):
            if livro.id == id:
                return idx
    
    # retornar objeto livro
    def return_livro(self,id):
        idx = self.search_livro_user_idx(id)
        if idx is None:
            print("Livro ID não encontrado")
        else:
            livro = self.livros[idx]
            return livro

    # Alterar # setter
    def alter_user(self,id,nome, telefone, nacionalidade):
        idx = self.search_list_user_idx(id)
        if idx is None:
            print("ID não encontrado")
        else:
            user = self.usuarios[idx]
            user.nome = nome
            user.telefone = telefone
            user.nacionalidade = nacionalidade
            self.usuarios[idx] = user

    # Remover
    def remove_user(self,id):
        idx = self.search_list_user_idx(id)
        if idx is None:
            print("ID não encontrado")
        else:
            self.usuarios.pop(idx)

    # Emprestimo
    def check_emprestimo(self, usuario, livro):
        return self.dict_emprestimos.get(f'{usuario.id}-{livro.id}',None)

    def registro_emprestimo(self,usuario,livro, exemplar):
        emprestimo = self.check_emprestimo(usuario,livro)
        if emprestimo is None: #posso criar o emprestimo
            id = f'{usuario.id}-{livro.id}' 
            self.dict_emprestimos[id] = Emprestimo(livro=livro,usuario = usuario
                                                    ,exemplar = exemplar
                                              ,ndays=20)    
            
            idx = self.search_livro_user_idx(livro.id)
            self._exemplares[idx].lista_exemplar.remove(exemplar)
            print('Emprestimo realizado')
        else:
            emprestimo.renovar()

    def registro_devolucao(self,usuario,livro, exemplar):
        id = f'{usuario.id}-{livro.id}' 
        self.dict_emprestimos[id].devolver()

        idx = self.search_livro_user_idx(livro.id)
        self._exemplares[idx].lista_exemplar.append(exemplar)










