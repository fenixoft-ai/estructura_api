'''Configuración específica para el entorno de pruebas.'''

# Se heredan las configuraciones base y se añaden configuraciones específicas
# para el entorno de pruebas.
from . import Config

class TestingConfig(Config):
    TESTING = True
    WTF_CSRF_ENABLED = False