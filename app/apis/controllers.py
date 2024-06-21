'''Define los controladores del namespace namespace1.'''

from flask_restx import Resource, Namespace
from http import HTTPStatus
#from app.utils.db_utils import example_get

ns2 = Namespace('namespace2', description='namespace2')

@ns2.route('/example1/<int:id>')
class ExampleResource(Resource):
    def get(self, id):
        try:
            data = ns2.payload

            if data['id']:
                return {'sample': data['id']}, 200
            else:
                return {'message': 'Sample not found'}, 404
        except Exception as e:
            return {
                'status': True,
                'message': str(e)
            }