from flask import Flask, render_template, request

app = Flask(__name__)


class calc:
    global np
    import numpy as np
    def add(a,b):
        A = np.array(a)
        B = np.array(b)

        result = (A+B).reshape((3,3))
        print(result)
        return result
    def sub(a,b):
        A = np.array(a)
        B = np.array(b)

        result = (A-B).reshape((3,3))
        print(result)
        return result
    def mul(a,b):
        A = np.array(a)
        B = np.array(b)

        result = (A*B).reshape((3,3))
        print(result)
        return result
    def zero():
        return np.zeros((3,3))


@app.route('/', methods=['GET', 'POST'])

def index():
    result = None
    error = None

    if request.method == 'POST':
        try:
            a_ = request.form.getlist('a[]')
            b_ = request.form.getlist('b[]')
            op = request.form.get('op')

            print(a_)
            print(b_)
            print(op)

            a = [0 for _ in range(9)]
            b = a.copy()

            a = [float(x) for x in a_]
            b = [float(x) for x in b_]

            error = False

            if op == '+':
                result = calc.add(a,b)
            elif op == '-':
                result = calc.sub(a,b)
            elif op == '*':
                result = calc.mul(a,b)
            else:
                error = True


        except Exception as e:
            error = True
            error = str(e)

    print (result)
    print()
    return render_template("index.html", result=result, error=error, Z=calc.zero())

app.run(debug=True)