from flask import Blueprint, request, jsonify
from services.Cliente_service import cliente_service
from serializer.cliente_serializer import ClienteSerializer


cliente_bp = Blueprint('cliente_bp', __name__,url_prefix=' ')






@cliente_bp.route('/', methods=['GET'])# Listar todos os clientes
def listar_clientes():
    service = cliente_service()
    clientes = service.Listar_todos()
    return jsonify([ClienteSerializer.serializeCliente(c) for c in clientes]), 200


@cliente_bp.route('/<int:id>', methods=['GET']) # Obter cliente por ID
def obter_cliente(id):
    service = cliente_service()
    c = service.mostrar_por_id(id)
    if not c:
        return jsonify({'error': 'Cliente não encontrado'}), 404
    return jsonify(ClienteSerializer.serializeCliente(c)), 200

@staticmethod
@cliente_bp.route('/', methods=['POST']) # Criar novo cliente
def criar_cliente():

    service = cliente_service()
    data = request.get_json() or {}
    

    try:
        result,status = service.cadastrar(data)
        return jsonify(result), status
    
    except ValueError as ve:
        return jsonify({'error': str(ve)}), 400
    
    except Exception as e:
        print('Erro ao criar cliente:', e)
        return jsonify({'error': 'Erro ao criar cliente'}), 500
    

    


@cliente_bp.route('/<int:id>', methods=['PUT']) # Atualizar cliente
def atualizar_cliente(id):
    service = cliente_service()
    data = request.get_json() or {}
    Query_result = service.atualizar(id, data)
    if Query_result is None:
        return jsonify({'error': 'Cliente não encontrado'}), 404
    return jsonify(ClienteSerializer.serializeCliente(Query_result)), 200


@cliente_bp.route('/<int:id>', methods=['DELETE'])
def deletar_cliente(id):
    service = cliente_service()
    resultado = service.delete(id)
    if resultado is False:
        return jsonify({'error': 'Cliente não encontrado'}), 404
    return jsonify({'message': resultado}), 200
