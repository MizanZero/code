from flask import Flask, render_template, request, redirect, url_for ,session
import numpy as np
import sqlite3
import os, sys
import time

os.chdir(os.path.dirname(os.path.abspath(sys.argv[0]))) # set current dir as app dir
appDir = os.getcwd().replace('\\', '/') # store app dir as a string, windows uses '\' in folder names, replace them with '/'

def dbExecute(command: str):
    with sqlite3.connect(appDir + "/static/users.db") as connection:
        cursor = connection.cursor()
        data = cursor.execute(command)
    return data

class createUser:
    def __init__(self, ip):
        self.previousInp = None
        self.ip = ip
        dbExecute(f"INSERT INTO user VALUES('{self.ip}')")

def checkInputValid(*eqs):
    invalIndex = []
    
    for i in range(3):
        for j in range(3):
            n = eqs[i][j]
            if not n.isnumeric():
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
app.secret_key = 'dimag_me_keeday'

@app.before_request
def before_request():
    if 'last_seen' in session:
        if time.time() - session['last_seen'] > 15:
            session['status'] = 'disconnected'
            return redirect('/disconnected')

# JS sends pings on /ping
@app.route('/ping')
def ping():
    if session['status'] == 'disconnected': return before_request()
    session['last_seen'] = time.time()
    return '', 204

@app.route('/disconnected')
def disconnected():
    session['last_seen'] = time.time()
    session.clear()
    return render_template('offline.html')

@app.route('/', methods = ['POST', 'GET'])
def enter():
    return redirect('/login')

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.environ.get('HTTP_X_FORWARDED_FOR') is None:
        ip = request.environ['REMOTE_ADDR']
    else:
        ip = request.environ['HTTP_X_FORWARDED_FOR']
    ipList = dbExecute("SELECT IP FROM user").fetchall()

    session['user'] = ip
    print(f"{ip} logged in")
    if ip not in [ip[0] for ip in ipList]:
        createUser(ip)
        return render_template('login.html', ip = ip)
    else:
        return redirect('/calculate')

@app.route('/calculate', methods = ['POST', 'GET'])
def calculate():
    if request.method == 'POST':
        eq1 = [0 for _ in range(4)]
        eq2 = [0 for _ in range(4)]
        eq3 = [0 for _ in range(4)]

        eq1 = request.form.getlist('eq1')
        eq2 = request.form.getlist('eq2')
        eq3 = request.form.getlist('eq3')

        print(eq1, eq2, eq3)

        if checkInputValid(eq1, eq2, eq3):
            x,y,z = solutionOf(eq1, eq2, eq3)
            if x == int(x): x = int(x)
            if y == int(y): y = int(y)
            if z == int(z): z = int(z)
        else:
            x,y,z = ['','','']          
        return render_template('home.html', result=(x,y,z), eq = (eq1, eq2, eq3), varNm = ('x', 'y', 'z'))
    
    elif request.method == 'GET':
        eq1 = eq2 = eq3 = [0,0,0,0]
        return render_template('home.html', eq = (eq1, eq2, eq3), result=('',''), varNm=('x', 'y', 'z'))

app.run(debug=True)

print(dbExecute("SELECT IP FROM user").fetchall())