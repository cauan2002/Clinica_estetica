from flask import jsonify
from DAO.procedimentosDAO import procedimentos_DAO
from Model.procedimentos import Procedimentos
from validator.validate_procedimentos import validateProcedimentos as ValidatorP
from serializer.procedimentos_serializer import procedimentosSerializer as SerializerP

class procedimento_service():

    def __init__(self):
        self.procedimento_dao = procedimentos_DAO()

    def cadastrarProcedimento(self, payload):
        
        ValidatorP.validate_data(payload)

        nome_procedimento = payload.get('nome_procedimento')
        preco = payload.get('preco')    
        observacoes = payload.get('observacoes')

        # novo_procedimento = procedimentos_DAO.criarProcedimento(
        #     nome_procedimento=nome_procedimento,
        #     preco=preco,
        #     observacoes=observacoes
        # )

        procedimento = Procedimentos(
            nome_procedimento=nome_procedimento,
            preco=preco,
            observacoes=observacoes
        
        )

        procedimento_salvo = procedimentos_DAO.criarProcedimento(procedimento)

        return jsonify(SerializerP.serialize_procedimento(procedimento_salvo)), 201
    


    
    def Listar_todos(self):
        return self.procedimento_dao.mostrar_todos()
    


    
    def mostrar_por_id(self, id):
        return self.procedimento_dao.mostrar_por_id(id)
       
    
    def atualizar(self,id, novos_dados:dict):
        return self.procedimento_dao.atualizar(id, novos_dados)
    
    def delete(self, id):
        return self.procedimento_dao.deletar(id)