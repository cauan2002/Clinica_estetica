from services.agendamentos_service import Agendamentos_service
from flask import Blueprint, request, jsonify

# agendamentos_bp = Blueprint('agendamentos_bp', __name__, url_prefix=' ')


    
def serialize_agendamento(a):
         
        return {
        'id': a.id,
        'data_hora': a.data_hora,
        'cliente_id': a.cliente_id,
        'procedimento_id': a.procedimento_id
    }
class Rotas_Agendamentos():

    agendamentos_bp = Blueprint('agendamentos_bp', __name__, url_prefix=' ')

    @staticmethod
    def AgdmtByClienteId(cliente_id):
        service=Agendamentos_service()
        agendamentos=service.mostrar_por_cliente_id(cliente_id)
        return agendamentos


    @staticmethod
    @agendamentos_bp.route('/', methods=['GET'])
    def listar_agendamentos():
        service = Agendamentos_service()
        agendamentos = service.Listar_todos()
        return jsonify([serialize_agendamento(a) for a in agendamentos]), 200

    @staticmethod
    @agendamentos_bp.route('/<int:id>', methods=['GET'])
    def obter_agendamento(id):
        service = Agendamentos_service()
        a = service.mostrar_por_id(id)
        if not a:
            return jsonify({'error': 'Agendamento não encontrado'}), 404
        return jsonify(serialize_agendamento(a)), 200

    @staticmethod
    @agendamentos_bp.route('/', methods=['POST'])
    def criar_agendamento():
        service = Agendamentos_service()
        data = request.get_json() or {}

        data_hora = data.get('data_hora')
        cliente_id = data.get('cliente_id')
        procedimento_id = data.get('procedimento_id')

        if not (data_hora and cliente_id and procedimento_id):
            print('Dados incompletos para criar agendamento')
            return jsonify({'error': 'data_hora, cliente_id e procedimento_id são obrigatórios'}), 400

        try:
            agendamento = service.cadastrar(data_hora, cliente_id, procedimento_id)
            return jsonify(serialize_agendamento(agendamento)), 201
        
        except Exception as e:
            print('Erro ao criar agendamento:', e)
            return jsonify({'error': str(e)}), 500