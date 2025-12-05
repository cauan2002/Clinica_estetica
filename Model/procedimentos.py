from DataBase.database import db

class Procedimentos(db.Model):
    
    
    __tablename__ = 'procedimentos'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome_procedimento = db.Column(db.String(100), nullable=False)
    preco = db.Column(db.Float, nullable=False)
    observacoes = db.Column(db.Text, nullable=True)

    def __init__(self, nome_procedimento=None, preco=0.0, observacoes=None):
        
        self.nome_procedimento = nome_procedimento
        self.preco = preco
        self.observacoes = observacoes


    # @property
    # def nome_procedimento(self):
    #     return self.nome_procedimento

    # @nome_procedimento.setter
    # def nome_procedimento(self, nome_procedimento):
    #     self.nome_procedimento = nome_procedimento

    # @property
    # def preco(self):
    #     return self.preco

    # @preco.setter
    # def preco(self, preco):
    #     self.preco = preco  

    # @property
    # def observacoes(self):
    #     return self.observacoes

    # @observacoes.setter
    # def observacoes(self, observacoes):
    #     self.observacoes = observacoes

if __name__ == "__main__":
   pass