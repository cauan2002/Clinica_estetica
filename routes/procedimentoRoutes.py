from services.procedimentoService import procedimento_service
from flask import Blueprint, request, jsonify
from serializer.procedimentos_serializer import procedimentosSerializer


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

        nome_procedimento = data.get('nome_procedimento')
        preco = data.get('preco')
        observacoes = data.get('observacoes')

        if not (nome_procedimento and preco is not None):
            print('Dados incompletos para criar procedimento')
            return jsonify({'error': 'nome_procedimento e preco são obrigatórios'}), 400

        try:
            procedimento = service.cadastrarProcedimento(nome_procedimento, preco, observacoes)
            return jsonify(procedimentosSerializer.serialize_procedimento(procedimento)), 201
        
        except Exception as e:
            print('Erro ao criar procedimento:', e)
            return jsonify({'error': str(e)}), 500