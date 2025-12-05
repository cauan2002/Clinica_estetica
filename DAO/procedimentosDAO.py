from Model.procedimentos import Procedimentos

class procedimentos_DAO():

    def criarProcedimento(self, nome_procedimento, preco, observacoes=None):
        from DataBase.database import db
        novo_procedimento = Procedimentos(nome_procedimento=nome_procedimento, preco=preco, observacoes=observacoes)
        
        db.session.add(novo_procedimento)
        db.session.commit()
        return novo_procedimento

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