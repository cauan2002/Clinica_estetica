
from DataBase.database import db

class Agendamentos(db.Model):
    __tablename__ = 'agendamentos'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_cliente = db.Column(db.Integer, db.ForeignKey('clientes.id'))
    id_procedimento = db.Column(db.Integer, db.ForeignKey('procedimentos.id'))
    data = db.Column(db.Date, nullable=False)
    hora = db.Column(db.Time, nullable=False)
    status = db.Column(db.Enum('confirmado', 'concluido', 'cancelado', 'pendente'), nullable=False)

    status_options = ['confirmado', 'concluido', 'cancelado','pendente']

    def __init__(self, id, id_cliente, id_procedimento, data, hora, status):
        self.id = id
        self.id_cliente = id_cliente
        self.id_procedimento = id_procedimento
        self.data = data
        self.hora =hora
        self.status = status

    @property
    def id_agendamento(self):
        return self.id
    @id_agendamento.setter
    def id_agendamento(self, id):
        self.id = id

    @property
    def id_cliente(self):
        return self.id_cliente
    @id_cliente.setter
    def id_cliente(self, id_cliente):
        self.id_cliente = id_cliente

    @property
    def id_procedimento(self):
        return self.id_procedimento
    @id_procedimento.setter
    def id_procedimento(self, id_procedimento):
        self.id_procedimento = id_procedimento

    @property
    def data(self):
        return self.data
    @data.setter
    def data(self, data):
        self.data = data

    @property
    def hora(self):
        return self.hora
    @hora.setter
    def hora(self, hora):
        self.hora = hora

    @property
    def status(self):
        return self.status
    @status.setter
    def status(self, status):
        if status.lower() not in self.status_options:
            raise ValueError(f'status invalido, escolha entre: {", ".join(self.status_options)}')


        self.status = status