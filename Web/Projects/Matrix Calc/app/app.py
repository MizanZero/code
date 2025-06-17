from flask import Flask, render_template, request
import numpy as np


class mat():
    def __init__ ( self, a:list[float], shape = (3,3) ):
        self.rows = shape[0]
        self.columns = shape[1]
        self.order = shape
        self.elements = shape[0] * shape[1]
        self.value = toNp(a)


def toNp(
        a:list,
        b:list,
        shape:tuple[int, int]=(3, 3)
        ) -> tuple[np.array, np.array]:
        # shape is passed as arg default is (3,3), i keep forgetting
    rows = shape[0]
    columns = shape[1]

    a, b = np.array(a, shape=(rows, columns)), np.array(b, shape=(rows, columns))


def toList(a:np.array, b:np.array) -> tuple[list, list]:
    a, b = tuple(map(lambda l: [e for r in l for e in r]), [a,b]) 


def calc(a:mat, b:mat, op:str): #return noError:bool, result: list
    """
    takes np arrays and string:operator,
    creates index from string:op, and index
    is if-elif-elsed to perform operation
    and then returns np array (not yet, function needs editing)

    """
    a = a.value
    b = b.value

    print(a)
    print(op)
    print(b)

    opInd = '+-*'.index(op)
    print(opInd, '\n')

    if opInd not in [0,1,2] or len(op)!=1:
        print("Invalid operator:",op)
        return False, [0 for _ in range(9)]

    if opInd == 0: result = a+b
    elif opInd == 1: result = a-b
    elif opInd == 2: result = a*b

    return True, result



app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def index():
    return render_template('index.html', rows=3, columns=3) 

app.run(debug=True)