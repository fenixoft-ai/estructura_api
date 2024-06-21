'''Define los controladores del namespace main.'''

from flask_restx import Resource, Namespace

ns_main = Namespace('main', description='Main operations')

@ns_main.route('/user/')
class UserResource(Resource):
    def get(self):
        return {'hello': 'world'}
