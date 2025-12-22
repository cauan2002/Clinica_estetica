from services.procedimentoService import procedimento_service
from flask import Blueprint, request, jsonify
from serializer.procedimentos_serializer import procedimentosSerializer
from validator.validate_procedimentos import validateProcedimentos as ValidatorP


class Rotas_Procedimento(): 

    procedimento_bp = Blueprint('procedimento_bp', __name__, url_prefix=' ')

    @staticmethod
    @procedimento_bp.route('/', methods=['GET'])
    def listar_procedimentos():
        service = procedimento_service()
        procedimentos = service.Listar_todos()
        return jsonify([procedimentosSerializer.serialize_procedimento(p) for p in procedimentos]), 200

    @staticmethod
    @procedimento_bp.route('/<int:id>', methods=['GET'])
    def obter_procedimento(id):
        service = procedimento_service()
        p = service.mostrar_por_id(id)
        if not p:
            return jsonify({'error': 'Procedimento não encontrado'}), 404
        return jsonify(procedimentosSerializer.serialize_procedimento(p)), 200

    @staticmethod
    @procedimento_bp.route('/', methods=['POST'])
    def criar_procedimento():
        service = procedimento_service()
        data = request.get_json() or {}

        try:
           result,status = service.cadastrarProcedimento(data)
           return jsonify(result), status
        
        except Exception as e:
            print('Erro ao criar procedimento:', e)
            return jsonify({'error': str(e)}), 500
        
    @staticmethod
    @procedimento_bp.route('/<int:id>', methods=['PUT'])
    def atualizar_procedimento(id):
        service = procedimento_service()
        data = request.get_json() or {}
        Query_result = service.atualizar(id, data)

        if Query_result is None:
            return jsonify({'error': 'Procedimento não encontrado'}), 404
        
        return jsonify(procedimentosSerializer.serialize_procedimento(Query_result)), 200