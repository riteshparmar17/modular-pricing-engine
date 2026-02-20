import os
from app import create_app
from app.config import DevelopmentConfig, ProductionConfig

env = os.getenv('FLASK_ENV', 'development')

if env == 'production':
    app = create_app(ProductionConfig)
else:
    app = create_app(DevelopmentConfig)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)