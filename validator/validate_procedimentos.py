from flask import jsonify

class validateProcedimentos:
    def validate_data(data):
        nome_procedimento = data.get('nome_procedimento')
        preco = data.get('preco')
        observacoes = data.get('observacoes')

        if not (nome_procedimento and preco is not None):
            print('Dados incompletos para criar procedimento')

            return jsonify({'error': 'nome_procedimento e preco são obrigatórios'}), 400