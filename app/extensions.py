from flask_restx import Api

authorizations = {
    'Bearer Auth': {
        'type': 'apiKey',
        'in': 'header',
        'name': 'Authorization',
        'description': "Type in the *'Value'* input box below: **'Bearer &lt;JWT&gt;'**, where JWT is the token"
    }
}

api = Api(version='1.0',
    title='Example API',
    description='An example of an API',
    authorizations=authorizations,
    security='apiKey'
)