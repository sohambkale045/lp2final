from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def calculator():
    result = ''
    if request.method == 'POST':
        try:
            n1 = float(request.form['num1'])
            n2 = float(request.form['num2'])
            op = request.form['operation']

            if op == 'add':
                result = n1 + n2
            elif op == 'sub':
                result = n1 - n2
            elif op == 'mul':
                result = n1 * n2
            elif op == 'div':
                result = n1 / n2 if n2 != 0 else 'Error (division by zero)'
        except Exception as e:
            result = f'Error: {e}'

    return render_template('index.html', result=result)
