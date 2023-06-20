import os

# Env configurations

class BaseConfig():
   API_PREFIX = '/api'
   TESTING = False
   DEBUG = False

class DevConfig(BaseConfig):
   FLASK_ENV = 'development'
   DEBUG = True
   SQLALCHEMY_DATABASE_URI = 'postgresql://{}:{}@{}:5432/flask-deploy'.format(os.environ['DB_USER'], os.environ['DB_PASS'], os.environ['DB_NAME'])
   CELERY_BROKER = 'pyamqp://{}:{}@broker-rabbitmq//'.format(os.environ['RABBITMQ_USER'], os.environ['RABBITMQ_PASS'])
   CELERY_RESULT_BACKEND = 'rpc://{}:{}@broker-rabbitmq//'.format(os.environ['RABBITMQ_USER'], os.environ['RABBITMQ_PASS'])

class ProductionConfig(BaseConfig):
   FLASK_ENV = 'production'
   SQLALCHEMY_DATABASE_URI = 'postgresql://{}:{}@{}:5432/flask-deploy'.format(os.environ['DB_USER'], os.environ['DB_PASS'], os.environ['DB_NAME'])
   CELERY_BROKER = 'pyamqp://{}:{}@broker-rabbitmq//'.format(os.environ['RABBITMQ_USER'], os.environ['RABBITMQ_PASS'])
   CELERY_RESULT_BACKEND = 'rpc://{}:{}@broker-rabbitmq//'.format(os.environ['RABBITMQ_USER'], os.environ['RABBITMQ_PASS'])

class TestConfig(BaseConfig):
   FLASK_ENV = 'development'
   TESTING = True
   DEBUG = True
   CELERY_ALWAYS_EAGER = True # Make celery execute tasks synchronously in the same process