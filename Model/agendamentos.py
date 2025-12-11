
from DataBase.database import db

class Agendamentos(db.Model):
    __tablename__ = 'agendamentos'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    hora = db.Column(db.Time, nullable=False)
    data = db.Column(db.Date, nullable=False)
    
    id_cliente = db.Column(db.Integer, db.ForeignKey('clientes.id'))
    id_procedimento = db.Column(db.Integer, db.ForeignKey('procedimentos.id'))

    cliente = db.relationship('Cliente', backref='agendamentos', lazy=True)
    procedimento = db.relationship('Procedimentos', backref='agendamentos', lazy=True)
    
    status = db.Column(db.Enum('confirmado', 'concluido', 'cancelado', 'pendente'),
                        default='pendente', 
                        nullable=False)
    status_options = ['confirmado', 'concluido', 'cancelado','pendente']

    # nao ha necessidade de criar o construtor (__init__) explicitamente
    # o SQLAlchemy ja faz isso automaticamente
    # nem os getters e setters, pois o SQLAlchemy ja gerencia os atributos

if __name__ == "__main__":
   pass