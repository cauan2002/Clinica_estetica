from Model.procedimentos import Procedimentos

class procedimentos_DAO():
    @staticmethod
    def criarProcedimento( procedimento:Procedimentos):
        from DataBase.database import db
       


        db.session.add(procedimento)
        db.session.commit()
        return procedimento

    def mostrar_todos(self):
        from DataBase.database import db
        return Procedimentos.query.all()
    
    def mostrar_por_id(self, id):
        from DataBase.database import db
        return Procedimentos.query.get(id)
    
    def atualizar(self, id, novos_dados:dict):
        procedimento = Procedimentos.query.get(id)
        if not procedimento:
            return None
        
        for key, value in novos_dados.items():
            if hasattr(procedimento, key):
                setattr(procedimento, key, value)
        
        from DataBase.database import db
        db.session.commit()
        return procedimento
    
    def deletar(self, id):
        procedimento = Procedimentos.query.get(id)
        if not procedimento:
            return False
        
        from DataBase.database import db
        db.session.delete(procedimento)
        db.session.commit()
        return True