from flask import Flask, jsonify
from configurações import config
from DataBase.database import db, migrate


class APP_inicilize():

    @staticmethod
    def create_app():

        # Initialize Flask app and configure database
        app = Flask(__name__)
        app.config.from_object('configurações.config.Config')

        db.init_app(app)
        migrate.init_app(app, db)
        # Import models to register them with SQLAlchemy

        with app.app_context():
          from Model.cliente import Cliente
          from Model.procedimentos import Procedimentos
          from Model.agendamentos import Agendamentos


        """try:
            with app.app_context():
                from Model import cliente, procedimentos, agendamentos
            except Exception:
                pass"""

        if app.config.get("CREATE_DB_ON_STARTUP", False):

            try:
                with app.app_context():
                    print('criando tabelas')
                    db.create_all() # Cria todas as tabelas definidas nos modelos
                    print('algumas tabelas ja existiam ou foram criadas!')
                    print('banco sincronizado com o Models!')

            except Exception as e:

                print('erro ao sincronizar com banco', e)

        APP_inicilize.registrar_blueprints(app)

        return app
    @staticmethod
    def registrar_blueprints(app):

        # Registrar rotas (blueprints)
        try:
            from routes import cliente_routes
            
            app.register_blueprint(cliente_routes.cliente_bp, url_prefix="/api/clientes")

        except Exception as e:
            print('Erro ao registrar blueprint:', e) # Se houver erro ao importar/registrar o blueprint, imprime o erro para debug
            
if __name__ == '__main__':
    
    app=APP_inicilize.create_app()
    app.run(host='127.0.0.1', port=5000, debug=True) # Executa a aplicação localmente para desenvolvimento


# Expose database engine and session
# engine= db.engine
# session = db.session
# no need to expose engine and session if not used directly
