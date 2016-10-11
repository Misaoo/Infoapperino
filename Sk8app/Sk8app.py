# coding=utf-8
from flask import Flask, render_template,request, url_for,session,redirect, escape
from hashlib import md5
import mysql
import mysql.connector
import bcrypt

app = Flask(__name__)
if __name__ == '__main__':
    cnx = mysql.connector.connect(user='root', password='', host='localhost', database='skatefest')
    cursor = cnx.cursor()
    app.secret_key = 'hemlis'

class ServerError(Exception):pass

#query = "SELECT email FROM admin"


"""@app.route('/')
def hello_world():
    cursor.execute(query)
    results = cursor.fetchall()
    for i in results:
        print i
    return 'Hello World!'
"""
"""@app.route('/')
def home():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        return "Hello Boss!"

@app.route('/login', methods=['POST'])
def do_admin_login():
    if request.form['password'] == 'password' and request.form['username'] == 'admin':
        session['logged_in'] = True
    else:
        flash('Wrong password')
    return home()

@app.route("/logout")
def logout():
    session['logged_in'] = False
    return home()"""
@app.route('/')
def index():
    if 'username' in session:
        return redirect(url_for('index'))

    username_session = escape(session['username']).capitalize()
    return render_template('index.html', session_user_name=username_session)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if 'username' in session:
        return redirect(url_for('index'))

    error = None
    try:
        if request.method == 'POST':
            username_form = request.form['username']
            cursor.execute("SELECT COUNT(1) FROM admin WHERE email = {};"
                           .format(username_form))

            if not cursor.fetchone()[0]:
                raise ServerError('Invalid username')

            password_form = request.form['password']
            cursor.execute("SELECT password FROM admin WHERE email = {};"
                           .format(username_form))

            for row in cursor.fetchall():
                if md5(password_form).hexdigest() == row[0]:
                    session['username'] = request.form['username']
                    return redirect(url_for('index'))

            raise ServerError('Invalid password')
    except ServerError as e:
        error = str(e)
    return render_template('index.html', error=error)


@app.route('/hej')
def hej ():

    return render_template('index.html')



if __name__ == '__main__':
    app.run(debug=True)
