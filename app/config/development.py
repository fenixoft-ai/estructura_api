'''Configuración específica para el entorno de desarrollo.'''

# Se heredan las configuraciones base y se añaden configuraciones específicas
# para el entorno de desarrollo.
from . import Config

class DevelopmentConfig(Config):
    DEBUG = True
