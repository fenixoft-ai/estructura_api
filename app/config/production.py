'''Configuración específica para el entorno de producción.'''

# Se heredan las configuraciones base y se añaden configuraciones específicas
# para el entorno de producción
from . import Config

class ProductionConfig(Config):
    DEBUG = False