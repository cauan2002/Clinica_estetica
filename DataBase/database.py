# Initialize database and migration objects
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


db = SQLAlchemy()
migrate = Migrate()



# Importa os models apenas após a inicialização do objeto `db` para evitar
# import circular (models importam `db` de app). Isso também garante que
# Flask-Migrate veja os models.