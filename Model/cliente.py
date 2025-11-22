from DataBase.database import db

class Cliente(db.Model):

    __tablename__ = 'clientes'
    genero_options = ['Masculino', 'Feminino', 'Outro']

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(100), nullable=False)
    CPF = db.Column(db.String(11), unique=True, nullable=False)
    telefone = db.Column(db.String(15), nullable=False)
    genero = db.Column(db.String(20), nullable=True)


    def __init__(self, id,nome,CPF,telefone,genero):
        self.id = id
        self.nome = nome
        self.CPF = CPF
        self.telefone = telefone
        self.genero = genero
    
    @property
    def name_cliente(self):
        return self.nome

    @name_cliente.setter
    def nome_cliente(self, nome):
        self.nome = nome

    @property
    def cpf_cliente(self):
        return self.CPF

    @cpf_cliente.setter
    def cpf_cliente(self, CPF):
        self.CPF = CPF

    @property
    def telefone_cliente(self):
        return self.telefone

    @telefone_cliente.setter
    def telefone_cliente(self, telefone):
        self.telefone = telefone

    @property
    def genero_cliente(self):
        return self.genero



    @genero_cliente.setter
    def genero_cliente(self, genero):
        if genero not in self.genero_options:
            raise ValueError(f'genero invalido. descreva de acordo com as seguintes opcoes: {self.genero_options}')
        self.genero = genero


if __name__ == "__main__":
    pass

