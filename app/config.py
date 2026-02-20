import os

class Config:
    DEBUG = False
    TESTING = False
    SECRET_KEY = os.getenv('SECRET_KEY', 'dev_secret_key')

    #Future DB/Redis configurations can be added here
    MONGO_URI = os.getenv('MONGO_URI', 'mongodb://localhost:27017/pricing_db')
    REDIS_URL = os.getenv('REDIS_URL', 'redis://localhost:6379/0')

class DevelopmentConfig(Config):
    DEBUG = True

class TestingConfig(Config):
    TESTING = True

class ProductionConfig(Config):
    DEBUG = False