from DAO.procedimentosDAO import procedimentos_DAO
from Model.procedimentos import Procedimentos

class procedimento_service():

    def __init__(self):
        self.procedimento_dao = procedimentos_DAO()

    def cadastrarProcedimento(self, nome_procedimento, preco, observacoes=None):
        return self.procedimento_dao.criarProcedimento(nome_procedimento, preco, observacoes)  
    


    
    def Listar_todos(self):
        return self.procedimento_dao.mostrar_todos()
    


    
    def mostrar_por_id(self, id):
        return self.procedimento_dao.mostrar_por_id(id)
       
    
    def atualizar(self,id, novos_dados:dict):
        return self.procedimento_dao.atualizar(id, novos_dados)
    
    def delete(self, id):
        return self.procedimento_dao.deletar(id)