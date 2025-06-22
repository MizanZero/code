from flask import Flask, render_template, request
import numpy as np


def checkInputValid(*eqs):
    invalIndex = []
    
    for i in range(len(eqs)):
        for j in range(i):
            if not eqs[i][j].isnumeric():
                invalIndex.append((i,j))
    if invalIndex: return False
    else: return True

def solutionOf(*eqs):
    eq1, eq2, eq3 = eqs

    eq1 = list(map(float, eq1))
    eq2 = list(map(float, eq2))
    eq3 = list(map(float, eq3))

    v = eq1[:-1] + eq2[:-1] + eq3[:-1]
    c = eq1[-1:] + eq2[-1:] + eq3[-1:]
    c = list(map(lambda x: -x, c))

    print(f"\n\n\nFunction works, c={c}\n\n\n") # eq1[-1] + eq2[-1] adds the values instead of making a list 

    v = np.array(v)
    c = np.array(c)

    v = np.reshape(v, shape=(3,3))
    c = np.reshape(c, shape=(3,1))

    print(f"\n\n\nc = {c} \n v = {v}\n\n\n")

    result = np.linalg.solve(v, c)
    x, y, z = (round(e, 3) for r in result for e in r)
    return x,y,z

app = Flask(__name__)


@app.route('/')
def index():
    eq1 = eq2 = eq3 = [0,0,0,0]
    return render_template('home.html', eq = (eq1, eq2, eq3), result=('',''), varNm = ('x', 'y', 'z'))

@app.route('/calculate', methods = ['POST'])
def calculate():
    x=float()
    y=float()

    if request.method == 'POST':
        eq1 = [0 for _ in range(4)]
        eq2 = [0 for _ in range(4)]
        eq3 = [0 for _ in range(4)]

        eq1 = request.form.getlist('eq1')
        eq2 = request.form.getlist('eq2')
        eq3 = request.form.getlist('eq3')

        if checkInputValid(eq1, eq2, eq3):
            x,y,z = solutionOf(eq1, eq2, eq3)
            if x == 0: x = 0.0
        else:
            x,y,z = ['','','']
            

    return render_template('home.html', result=(x,y,z), eq = (eq1, eq2, eq3), varNm = ('x', 'y', 'z'))
    
app.run(debug=True)