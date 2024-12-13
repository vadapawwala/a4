from flask import Flask

app = Flask(__name__)

@app.route('/<int:n>')
def print_table(n):
    table = ''
    for i in range(1, 11):
        table += f'{n} x {i} = {n * i}<br>'
    return table

if __name__ == '__main__':
    app.run(host='localhost', port=5000)
