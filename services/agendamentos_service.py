from Model.agendamentos import Agendamentos
from DAO.agendamentos_DAO import Agendamentos_DAO

class Agendamentos_service():

    def __init__(self):
        self.agendamentos_dao = Agendamentos_DAO()

    def cadastrar(self, data_hora, cliente_id, procedimento_id):
        from DataBase.database import db
        novo_agendamento = Agendamentos(data_hora=data_hora, cliente_id=cliente_id, procedimento_id=procedimento_id)
        
        db.session.add(novo_agendamento)
        db.session.commit()
        return novo_agendamento   
    
    def Listar_todos(self):
        return self.agendamentos_dao.mostrar_todos()
    
    def mostrar_por_id(self, id):
        return self.agendamentos_dao.mostrar_por_id(id)
    
    def mostrar_por_cliente_id(self, cliente_id):
        return self.agendamentos_dao.mostrar_por_cliente_id(cliente_id)
       
    
    def atualizar(self,id, novos_dados:dict):
        return self.agendamentos_dao.atualizar(id, novos_dados)
    
    def delete(self, id):
        return self.agendamentos_dao.deletar(id)