from flask import jsonify



class validate_cliente:
    def validate_data(data):

        nome = data.get('nome')
        CPF = data.get('CPF')
        telefone = data.get('telefone')
        genero = data.get('genero')
        genero_options = ['Masculino', 'Feminino', 'Outro']


        if genero not in genero_options:
            raise ValueError(f'genero invalido. descreva de acordo com as seguintes opcoes: {genero_options}')
        genero = genero



        if not (nome and CPF and telefone):
          print('Dados incompletos para criar cliente')
          return jsonify({'error': 'nome, CPF e telefone são obrigatórios'}), 400

       
    