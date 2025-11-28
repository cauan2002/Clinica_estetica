import os

class Config:
# Configurações em nível de módulo para que `app.config.from_object('config.config')`
# consiga ler as variáveis diretamente.
  SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:22122002jc@localhost:3306/clinica_estetica'
  SQLALCHEMY_TRACK_MODIFICATIONS = False
# Habilita o log das queries SQL no console para facilitar debug
  SQLALCHEMY_ECHO = True

  CREATE_DB_ON_STARTUP = True