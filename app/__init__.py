'''Este archivo inicializa la aplicación Flask y registra las configuraciones y blueprints'''

from flask import Flask
from .config import Config
from .extensions import api
# from .apis import blueprint as api_blueprint
from .apis.main.controllers import ns_main
from .apis.namespace1.controllers import ns1
from .apis.namespace2.controllers import ns2

import logging

def create_app(config_class=Config):
    
    # Create Flask app
    app = Flask(__name__)

    # load configurations from config
    app.config.from_object(config_class)

    # Initialize MariaDB connection
    # init_mariadb(app)
    api.init_app(app)


    logging.basicConfig(filename = 'documents.log' ,
                       level = logging.DEBUG,
                       format = '%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s')

    # Register blueprints
    # app.register_blueprint(api_blueprint, url_prefix='/api')
    api.add_namespace(ns_main)
    api.add_namespace(ns1)
    api.add_namespace(ns2)

    # Log the routes registered
    for rule in app.url_map.iter_rules():
        logging.info(f"Route registered: {rule}")

    return app
