from flask import jsonify

class validate_agendamentos:
    def validate_data(data):
        Data = data.get('data')
        Hora = data.get('hora')
        cpf= data.get('CPF')
        procedimento_nome = data.get('procedimento')

        if not (Data and Hora  and cpf and procedimento_nome):
            print('Dados incompletos para criar agendamento')
            return jsonify({'error': 'data, hora, cpf e procedimento são obrigatórios'}), 400