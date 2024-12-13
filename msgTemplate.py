from flask import Flask, render_template
from datetime import datetime

# Specify custom template folder
app = Flask(__name__, template_folder='./templates')

@app.route('/')
def hello():
    return render_template('hello.html')

if __name__ == '__main__':
    app.run(debug=True)
