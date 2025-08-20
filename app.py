from flask import Flask, render_template, request, redirect, session, url_for
import os

app = Flask(__name__)
app.secret_key = os.getenv("FLASK_SECRET_KEY", "defaultsecretkey")  # For session security

# Environment variables for sensitive info
USERNAME = os.getenv('MY_USERNAME', 'user')
PASSWORD = os.getenv('MY_PASSWORD', 'pass')
API_KEY = os.getenv('MY_API_KEY', 'this_is_an_api_key')

@app.route('/', methods=['GET', 'POST'])
def login():
    error = ""
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if username == USERNAME and password == PASSWORD:
            session['user'] = username
            return redirect(url_for('dashboard'))
        else:
            error = "Incorrect username or password"
    return render_template('login.html', error=error)

@app.route('/dashboard')
def dashboard():
    if 'user' in session:
        user_ip = request.remote_addr
        return render_template(
            'dashboard.html',
            username=session['user'],
            ip=user_ip,
            api_key=API_KEY
        )
    return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)

