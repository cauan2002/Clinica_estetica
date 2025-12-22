from flask import jsonify
from Model.cliente import Cliente
from DAO.cliente_DAO import Cliente_DAO
from validator.cliente_validate import validate_cliente
from serializer.cliente_serializer import ClienteSerializer as SerializerC


class cliente_service():

    def __init__(self):
        self.cliente_dao = Cliente_DAO()

    def cadastrar(self, payload):
    
           validate_cliente.validate_data(payload)

           

           Nome = payload.get('nome')
           CPF = payload.get('CPF')
           telefone = payload.get('telefone')
           genero = payload.get('genero')

           novo_cliente=Cliente_DAO.cadastrar(nome=Nome,
                                      CPF=CPF, 
                                      telefone=telefone, 
                                      genero=genero)


           return SerializerC.serializeCliente(novo_cliente), 201
    
    
       

    
    
    def Listar_todos(self):
        return self.cliente_dao.mostrar_todos()
    
    def mostrar_por_id(self, id):
        return self.cliente_dao.mostrar_por_id(id)
       
    
    def atualizar(self,id, novos_dados:dict):
        return self.cliente_dao.atualizar(id, novos_dados)
    
    def delete(self, id):
        return self.cliente_dao.deletar(id)
    
    


    