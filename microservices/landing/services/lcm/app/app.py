from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class LCM(Resource):

	def lcm(self, num1, num2):
		if num1 > num2:  
			greater = num1  
		else:  
			greater = num2  
		while(True):  
			if((greater % num1 == 0) and (greater % num2 == 0)):  
				lcm = greater  
				break  
			greater += 1  
		return lcm 

	def get(self, num1, num2, s1, s2):
		if(s1==1):
			num1=num1*-1
		if(s2==1):
			num2=num2*-1
		return {'result': self.lcm(num1,num2)}


	

api.add_resource(LCM, '/calculator/lcm/<int:num1>/<int:num2>/<int:s1>/<int:s2>')

if __name__ == '__main__':
	app.run(host = '0.0.0.0', port = 5005, debug = True)

