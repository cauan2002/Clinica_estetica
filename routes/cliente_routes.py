from flask import Blueprint, request, jsonify
from services.Cliente_service import cliente_service


cliente_bp = Blueprint('cliente_bp', __name__,url_prefix=' ')



def serialize_cliente(c):
    return {
        'id': c.id,
        'nome': getattr(c, 'nome', None),
        'CPF': getattr(c, 'CPF', None),
        'telefone': getattr(c, 'telefone', None),
        'genero': getattr(c, 'genero', None)
    }

# Listar todos os clientes
@cliente_bp.route('/', methods=['GET'])
def listar_clientes():
    service = cliente_service()
    clientes = service.Listar_todos()
    return jsonify([serialize_cliente(c) for c in clientes]), 200

# Obter cliente por ID
@cliente_bp.route('/<int:id>', methods=['GET'])
def obter_cliente(id):
    service = cliente_service()
    c = service.mostrar_por_id(id)
    if not c:
        return jsonify({'error': 'Cliente não encontrado'}), 404
    return jsonify(serialize_cliente(c)), 200

# Criar novo cliente
@cliente_bp.route('/', methods=['POST'])
def criar_cliente():

    service = cliente_service()
    data = request.get_json() or {}

    nome = data.get('nome')
    CPF = data.get('CPF')
    telefone = data.get('telefone')
    genero = data.get('genero')

    if not (nome and CPF and telefone):
        print('Dados incompletos para criar cliente')
        return jsonify({'error': 'nome, CPF e telefone são obrigatórios'}), 400

    try:
        cliente = service.cadastrar( nome, CPF, telefone, genero)
        return jsonify(serialize_cliente(cliente)), 201
    
    except Exception as e:
        print('Erro ao criar cliente:', e)
        return jsonify({'error': str(e)}), 500

    

# Atualizar cliente
@cliente_bp.route('/<int:id>', methods=['PUT'])
def atualizar_cliente(id):
    service = cliente_service()
    data = request.get_json() or {}
    Query_result = service.atualizar(id, data)
    if Query_result is None:
        return jsonify({'error': 'Cliente não encontrado'}), 404
    return jsonify(serialize_cliente(Query_result)), 200

# Deletar cliente
@cliente_bp.route('/<int:id>', methods=['DELETE'])
def deletar_cliente(id):
    service = cliente_service()
    resultado = service.delete(id)
    if resultado is False:
        return jsonify({'error': 'Cliente não encontrado'}), 404
    return jsonify({'message': resultado}), 200
