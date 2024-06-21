'''Define los controladores del namespace namespace1.'''

from flask_restx import Resource, Namespace
from http import HTTPStatus
#from app.utils.db_utils import example_get

ns1 = Namespace('namespace1', description='namespace1')

@ns1.route('/example1/<int:id>')
class ExampleResource(Resource):
    def get(self, id):
        return {'id': id}

 