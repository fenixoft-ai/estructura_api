'''Define los controladores del namespace namespace2.'''

from flask_restx import Resource, Namespace

ns2 = Namespace('namespace2', description='namespace2')

@ns2.route('/sample/<int:id>')
class SampleResource(Resource):
    def get(self, id):
        return {'sample': id}
