from flask import Flask, render_template, request, redirect, url_for, flash, session
import csv
from flask_bcrypt import Bcrypt

from config import config

app = Flask(__name__)
bcrypt = Bcrypt(app)

def read_users_from_csv():
    users = []
    with open('users.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            users.append(row)
    return users

@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method=='POST':
        print(request.form['email'])
        print(request.form['password'])
        return render_template('user.html')
    else:
        return render_template('auth/login.html')
    #     username = request.form['username']
    #     password = request.form['password']
    #     users = read_users_from_csv()
    #     user = next((u for u in users if u['username'] == username), None)
    #     if user and bcrypt.check_password_hash(user['password'], password):
    #         # Iniciar sesión almacenando el username y el rol en la sesión
    #         session['username'] = user['username']
    #         session['role'] = user['role']
    #         flash('Login successful!', 'success')
    #         return redirect(url_for('home'))
    #     else:
    #         flash('Login unsuccessful. Please check your username and password.', 'danger')
    # return render_template('login.html')

if __name__ == '__main__':
    app.config.from_object(config['development'])
    app.run()