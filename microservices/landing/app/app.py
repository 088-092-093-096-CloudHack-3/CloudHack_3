
from flask import Flask, render_template, request, flash, redirect, url_for

import requests
import os
import json

app = Flask(__name__ , template_folder='.')
app.secret_key = 'thisisjustarandomstring'

@app.route('/', methods=['POST', 'GET'])
def index():
    number_1 = request.form.get("first")
    number_2 = request.form.get('second')
    operation = request.form.get('operation')
    print(number_1, number_2)
    result = 0
    try:
        num1=int(number_1)
        num2=int(number_2)
        s1=s2=0
        if num1<0:
            s1=1
            number_1=num1*-1
        if(num2<0):
            s2=1
            number_2=num2*-1
        if operation == 'add':
            res = requests.get('http://add-service:5000/calculator/add/'+str(number_1)+'/'+str(number_2)+'/'+str(s1)+'/'+str(s2))
            print(res)
            a=(res.json())
            result=a['result']
        elif operation == 'minus':
            res =  requests.get('http://subtract-service:5001/calculator/subtract/'+str(number_1)+'/'+str(number_2)+'/'+str(s1)+'/'+str(s2))
            a = (res.json())
            result = a['result']
        elif operation == 'multiply':
            res = requests.get('http://multiply-service:5002/calculator/multiply/'+str(number_1)+'/'+str(number_2)+'/'+str(s1)+'/'+str(s2))
            a = (res.json())
            result = a['result']
        elif operation == 'divide':
            if(number_2==0):
                raise ZeroDivisionError
            res = requests.get('http://divide-service:5003/calculator/divide/'+str(number_1)+'/'+str(number_2)+'/'+str(s1)+'/'+str(s2))
            a=(res.json())
            result=a['result']
        elif operation == 'gcd':
            res = requests.get('http://gcd-service:5004/calculator/gcd/'+str(number_1)+'/'+str(number_2)+'/'+str(s1)+'/'+str(s2))
            a=(res.json())
            result=a['result']
        elif operation == 'lcm':
            res = requests.get('http://lcm-service:5005/calculator/lcm/'+str(number_1)+'/'+str(number_2)+'/'+str(s1)+'/'+str(s2))
            a=(res.json())
            result=a['result']
        elif operation == 'exponent':
            res = requests.get('http://exponent-service:5006/calculator/exponent/'+str(number_1)+'/'+str(number_2))
            a=(res.json())
            result=a['result']
        e=f'The result of operation {operation} on {num1} and {num2} is {result}'
    except ValueError:
        e="Invalid entry"
    except ZeroDivisionError:
        e="Cannot divide by zero" 
    except Exception as exp:
        e=exp
    flash(e)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(
    debug=True,
    port=5050,
    host="0.0.0.0"
)
