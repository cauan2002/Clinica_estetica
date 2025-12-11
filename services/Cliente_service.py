from Model.cliente import Cliente
from DAO.cliente_DAO import Cliente_DAO


class cliente_service():

    def __init__(self):
        self.cliente_dao = Cliente_DAO()

    def cadastrar(self, nome , CPF, telefone, genero):
        from DataBase.database import db
        novo_cliente=Cliente(nome=nome , CPF=CPF, telefone=telefone, genero=genero)
        
        db.session.add(novo_cliente)
        db.session.commit()
        return novo_cliente   
    
    def Listar_todos(self):
        return self.cliente_dao.mostrar_todos()
    
    def mostrar_por_id(self, id):
        return self.cliente_dao.mostrar_por_id(id)
       
    
    def atualizar(self,id, novos_dados:dict):
        return self.cliente_dao.atualizar(id, novos_dados)
    
    def delete(self, id):
        return self.cliente_dao.deletar(id)
    
    


    