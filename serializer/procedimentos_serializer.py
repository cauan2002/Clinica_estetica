class procedimentosSerializer:
    @staticmethod
    def serialize_procedimento(p):
      
      return {
        'ID': p.id,
        'nome_procedimento': getattr(p, 'nome_procedimento', None),
        'preco': getattr(p, 'preco', None),
        'observacoes': getattr(p, 'observacoes', None)
    }