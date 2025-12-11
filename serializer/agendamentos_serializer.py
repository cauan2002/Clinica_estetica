class AgendamentosSerializer:
   
 def serializeAgendamento(a):
    return {
    'id': a.id,
    'data': a.data.isoformat() if a.data else None,                # 'YYYY-MM-DD'
    'hora': a.hora.strftime('%H:%M:%S') if a.hora else None,      # 'HH:MM:SS'
    'status': a.status,
    'id_cliente': a.id_cliente,
    'id_procedimento': a.id_procedimento,
    'cliente': {
      'id': a.cliente.id,
      'nome': getattr(a.cliente, 'nome', None),
      'CPF': getattr(a.cliente, 'CPF', None)
        } 
      
    if getattr(a, 'cliente', None) else None, 'procedimento': {          
      'id': a.procedimento.id,
      'nome': getattr(a.procedimento, 'nome', None)
    } 
        if getattr(a, 'procedimento', None) else None
    }