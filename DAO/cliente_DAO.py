from Model.cliente import Cliente

"""Evita import circular importando `db` localmente dentro dos métodos.
    Assim `DAO` não importa `app` no topo do módulo.
"""

class Cliente_DAO:

    def cadastrar(self, cliente:Cliente): # Recebe um objeto Cliente
        from DataBase.database import db
        db.session.add(cliente) # cadastra o objeto no banco de dados
        db.session.commit() # Confirma a transacao no banco de dados

    def mostrar_todos(self):
        from DataBase.database import db
        return Cliente.query.all()
    
    def mostrar_por_id(self, id):
        from DataBase.database import db
        return Cliente.query.get(id)
    
    def atualizar(self, id, novos_dados:dict):
        from DataBase.database import db
        cliente = Cliente.query.get(id)
                                      
        if not cliente:
            return None
        
        # forma de alterar manualmente cada campo, mas menos eficiente e mais verboso

        #cliente.nome = novos_dados.get('nome', cliente.nome) # Atualiza o nome se fornecido
        #cliente.CPF = novos_dados.get('CPF', cliente.CPF) # Atualiza o CPF se fornecido
        #cliente.telefone = novos_dados.get('telefone', cliente.telefone) # Atualiza o telefone se fornecido

        for campo, valor in novos_dados.items():
            if hasattr(cliente, campo): # Verifica se o atributo existe no objeto
                setattr(cliente, campo, valor) # Atualiza o atributo dinamicamente

        from app import db
        db.session.commit() # Confirma as alterações no banco de dados
        return cliente # Retorna o cliente atualizado
    
    def deletar(self, id):
        from DataBase.database import db
        cliente = Cliente.query.get(id)
        if not cliente:
            return False
        from app import db
        db.session.delete(cliente)
        db.session.commit()

        return 'Cliente deletado com sucesso'