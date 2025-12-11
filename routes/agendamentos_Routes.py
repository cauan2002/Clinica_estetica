from Model.cliente import Cliente
from Model.procedimentos import Procedimentos
from services.agendamentos_service import Agendamentos_service
from serializer.agendamentos_serializer import AgendamentosSerializer as SerializerA
from flask import Blueprint, request, jsonify



class Rotas_Agendamentos():

    agendamentos_bp = Blueprint('agendamentos_bp', __name__, url_prefix=' ')

    @staticmethod
    @agendamentos_bp.route('/cliente/<int:cliente_id>', methods=['GET'])    
    def AgdmtByClienteId(cliente_id):

        service=Agendamentos_service()
        agendamentos=service.mostrar_por_cliente_id(cliente_id)
        return agendamentos
    


    @staticmethod
    @agendamentos_bp.route('/', methods=['GET'])
    def listar_agendamentos():
        service = Agendamentos_service()
        agendamentos = service.Listar_todos()
        
        return jsonify([SerializerA.serializeAgendamento(a) for a in agendamentos]), 200
    




    @staticmethod
    @agendamentos_bp.route('/<int:id>', methods=['GET'])
    def obter_agendamento(id):
        service = Agendamentos_service()
        a = service.mostrar_por_id(id)
        if not a:
            return jsonify({'error': 'Agendamento não encontrado'}), 404
        return jsonify(SerializerA.serializeAgendamento(a)), 200



    @staticmethod
    @agendamentos_bp.route('/', methods=['POST'])
    def criar_agendamento():

        data = request.get_json() or {}
        service = Agendamentos_service()
    
        result,status = service.cadastrar(data)

        return jsonify(result), status
     
        
        
    @staticmethod
    @agendamentos_bp.route('/<int:id>', methods=['DELETE'])
    def deletar_agendamento(id):
        service = Agendamentos_service()
        sucesso = service.delete(id)
        if not sucesso:
            return jsonify({'error': 'Agendamento não encontrado'}), 404
        return jsonify({'message': 'Agendamento deletado com sucesso'}), 200