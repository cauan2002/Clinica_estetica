from DataBase.database import db

class Procedimentos(db.Model):
    
    
    __tablename__ = 'procedimentos'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome_procedimento = db.Column(db.String(100), nullable=False)
    preco = db.Column(db.Float, nullable=False)
    observacoes = db.Column(db.Text, nullable=True)

    # nao ha necessidade de criar o construtor (__init__) explicitamente
    # o SQLAlchemy ja faz isso automaticamente



if __name__ == "__main__":
   pass