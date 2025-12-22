from flask import jsonify
from Model.agendamentos import Agendamentos
from DAO.agendamentos_DAO import Agendamentos_DAO
from Model.cliente import Cliente
from Model.procedimentos import Procedimentos
from validator.validat_agendamentos import validate_agendamentos    
from serializer.agendamentos_serializer import AgendamentosSerializer as SerializerA


class Agendamentos_service():

    def __init__(self):
        self.agendamentos_dao = Agendamentos_DAO()

    def cadastrar(self, payload):

        try:
          
          
          

           validate_agendamentos.validate_data(payload)
           dao = Agendamentos_DAO()

           Data = payload["data"]
           Hora = payload["hora"]
           cpf = payload["cpf"]
           procedimento_nome = payload["procedimento"]

           procedimento = Procedimentos.query.filter_by(nome_procedimento=procedimento_nome).first()
           if not procedimento:
               return jsonify({'error': 'Procedimento não encontrado'}), 404
        
           cliente = Cliente.query.filter_by(CPF=cpf).first()
           if not cliente:
                return jsonify({'error': 'Cliente não encontrado'}), 404
        
          
           novo_agendamento = dao.agendar(id_cliente=cliente.id, id_procedimento=procedimento.id, data=Data, hora=Hora, status = 'pendente')
          

           return SerializerA.serializeAgendamento(novo_agendamento), 201

        except ValueError as ve:
            print('Erro de validação:', ve)
            return ({'error': str(ve)}), 400
        except Exception as e:
            print('Erro ao cadastrar agendamento:', e)
            return ({'error': 'Erro ao cadastrar agendamento'}), 500

       

        
  
    
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