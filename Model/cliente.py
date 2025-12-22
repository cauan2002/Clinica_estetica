from DataBase.database import db

class Cliente(db.Model):

    __tablename__ = 'clientes'
    genero_options = ['Masculino', 'Feminino', 'Outro']

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    
    nome = db.Column(db.String(100), nullable=False)
    CPF = db.Column(db.String(11), unique=True, nullable=False)
    telefone = db.Column(db.String(15), nullable=False)
    genero = db.Column(db.String(20), nullable=True)


    
    
    


if __name__ == "__main__":
    pass

