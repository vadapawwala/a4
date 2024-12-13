from flask import Flask, render_template, request, abort

app = Flask(__name__, template_folder='./templates')

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
    
        if not username or not password:
            abort(400, 'Username and password are required')

        if len(password) < 8:
            abort(400, 'Password must be at least 8 characters long')

        if not username.isalnum():
            abort(400, 'Username can only contain letters and numbers')

       
        if username.lower() == 'admin':
            abort(403)

        return 'Form submitted successfully!'
    
    return render_template('register.html')


if __name__ == '__main__':
    app.run(host='localhost', port=5003)

