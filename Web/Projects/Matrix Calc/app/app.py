from flask import Flask, render_template, request
import numpy as np


def calc(a:list[float], op:list[float], b:list[float]): #return noError:bool, result: list
    print(a)
    print(op)
    print(b)

    opInd = '+-*'.index(op)
    print(opInd, '\n')

    if opInd not in [0,1,2] or len(op)!=1:
        print("Invalid operator:",op)
        return False, [0 for _ in range(9)]
    
    a = np.array(a) ; b = np.array(b)
    a = np.reshape(a,(3,3)) ; b = np.reshape(b, (3,3))

    if opInd == 0: result = a+b
    elif opInd == 1: result = a-b
    elif opInd == 2: result = a*b

    print(a,op,b, '\n')

    return True, [e for r in result for e in r]




app = Flask(__name__)
@app.route('/', methods=['GET','POST'])
def index():
    result = [0 for _ in range(9)]
    noError = False

    if request.method == 'POST':
        try:
            a = list(map(float, request.form.getlist('a[]')))
            op = request.form.get('op')
            b = list(map(float, request.form.getlist('b[]')))

            print(a,op,b,'\n')

            noError, result = calc(a,op,b)

        except:
            noError = False

    return render_template('index.html', result=result, noError=noError, Z=np.zeros((3,3))) 

app.run(debug=True)

