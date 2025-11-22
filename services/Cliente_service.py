from Model import cliente
from DAO.cliente_DAO import Cliente_DAO


class cliente_service():

    def __init__(self):
        self.cliente_dao = Cliente_DAO()

    def cadastrar(self):
        return self.cliente_dao.cadastrar()    
    
    def Listar_todos(self):
        return self.cliente_dao.mostrar_todos()
    
    def mostrar_por_id(self):
        return self.cliente_dao.mostrar_por_id()
    
    def atualizar(self):
        return self.cliente_dao.atualizar()
    
    def delete(self):
        return self.cliente_dao.deletar()
    
    


    