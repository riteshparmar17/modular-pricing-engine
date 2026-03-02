import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Config:

    """
    Base configuration.
    Reads values from environment variables.
    """

    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY')
    #Future DB/Redis configurations can be added here
    MONGO_URI = os.getenv('MONGO_URI')
    REDIS_URL = os.getenv('REDIS_URL')
    PORT = int(os.getenv('PORT', 5000))

    DEBUG = False
    TESTING = False

class DevelopmentConfig(Config):
    DEBUG = True

class TestingConfig(Config):
    TESTING = True

class ProductionConfig(Config):
    DEBUG = False

config_by_name = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig
}