from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class GCD(Resource):

    def gcd(self, a, b):
        if a == 0:
            return b
        return self.gcd(b % a, a)       

    def get(self, num1, num2, s1, s2):
        if(s1==1):
            num1=num1*-1
        if(s2==1):
            num2=num2*-1
        return {'result': self.gcd(num1,num2)}
	
	 

api.add_resource(GCD, '/calculator/gcd/<int:num1>/<int:num2>/<int:s1>/<int:s2>')

if __name__ == '__main__':
	app.run(host = '0.0.0.0', port = 5004, debug = True)
        
