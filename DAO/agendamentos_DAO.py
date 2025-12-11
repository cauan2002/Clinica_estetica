from Model.agendamentos import Agendamentos
from DataBase.database import db

class Agendamentos_DAO():

    def agendar(self, id_cliente, id_procedimento, data, hora, status):
        
        novo_agendamento = Agendamentos(id_cliente=id_cliente, id_procedimento=id_procedimento, data=data, hora=hora, status=status)
        
        db.session.add(novo_agendamento)
        db.session.commit()
        return novo_agendamento



    def mostrar_por_cliente_id(self, cliente_id):
        
        return Agendamentos.query.filter_by(cliente_id=cliente_id).all()

    
    def mostrar_todos(self):
      
        return Agendamentos.query.all()
    
    def mostrar_por_id(self, id):
       
        return Agendamentos.query.get(id)
    
    def atualizar(self, id, novos_dados:dict):
        agendamento = Agendamentos.query.get(id)
        if not agendamento:
            return None
        
        for key, value in novos_dados.items():
            if hasattr(agendamento, key):
                setattr(agendamento, key, value)
        
        from DataBase.database import db
        db.session.commit()
        return agendamento
    
    def deletar(self, id):
        agendamento = Agendamentos.query.get(id)
        if not agendamento:
            return False
        
        from DataBase.database import db
        db.session.delete(agendamento)
        db.session.commit()
        return True