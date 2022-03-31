from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class Add(Resource):

    def get(self, num1, num2, s1, s2):
        if(s1==1):
            num1=num1*-1
        if(s2==1):
            num2=num2*-1
        return {'result': num1+num2}

api.add_resource(Add, '/calculator/add/<int:num1>/<int:num2>/<int:s1>/<int:s2>')

if __name__ == '__main__':
	app.run(host = '0.0.0.0', port = 5000, debug = True)
        
