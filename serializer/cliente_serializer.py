class ClienteSerializer:

    @staticmethod
    def serialize_cliente(c): 
        return {
            'id': c.id,
            'nome': getattr(c, 'nome', None),
            'CPF': getattr(c, 'CPF', None),
            'telefone': getattr(c, 'telefone', None),
            'genero': getattr(c, 'genero', None)
    }