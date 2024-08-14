from datetime import datetime,timedelta

class Emprestimo:
    def __init__(self, livro, usuario,exemplar, ndays):
        self.livro = livro
        self.usuario = usuario
        self.dta_emprestimo = datetime.now()
        self.dta_devolucao = datetime.now() + timedelta(days=ndays)
        self.estado_exemplar = 'emprestado' #devolvido
        self.exemplar = exemplar
        self.count_renovacao = 0

    def devolver(self):
        self.estado_exemplar = 'devolvido'

    def renovar(self):
        if self.livro.max_renovacao == self.count_renovacao:
            self.devolver()
            print("Número máximo de renovações atingida\nDevolver livro!")
        else:
            self.count_renovacao +=1
            self.dta_emprestimo = datetime.now()
            #quando renova em sequencia pode ficar no máximo 1 semana
            self.dta_devolucao = datetime.now() + timedelta(days=7)


    


