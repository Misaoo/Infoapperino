import os, sys
from flask import Flask, flash, redirect, render_template, request, session
import os
import time
import config



app = Flask(__name__)

@app.route('/')
def home():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        return render_template("blogpost.html")

@app.route('/login', methods=['POST', 'GET'])
def do_admin_login():
    if request.method == 'POST':
        POST_USERNAME = str(request.form["username"])
        POST_PASSWORD = str(request.form["password"])

        query = "SELECT email, password, firstname FROM admin WHERE email=%s"

        config.cur.execute(query, (POST_USERNAME,))

        result = config.cur.fetchall()
        for i in result:

            if i[0] == POST_USERNAME and i[1] == POST_PASSWORD:
                session['logged_in'] = True
                return home()
            elif POST_PASSWORD != i[1]:
                return "Wrong Password"
    elif request.method == 'GET':
        return render_template("login.html")



@app.route("/blogpost", methods=['POST', 'GET'])
def create_post():

    if request.method == 'POST' and session.get('logged_in') == True:

        post_heading = request.form["heading"]
        post_text = request.form["text"]

        print request.form["heading"]

        query = "INSERT INTO post (headline, text) VALUES (%s, %s)"

        print query

        config.cur.execute(query, (post_heading, post_text))

        return render_template("blogpost.html")


    elif request.method == 'GET':
        return render_template("blogpost.html")

@app.route('/index', methods=['POST', 'GET'])
def index_troll():
    return render_template("index.html")

@app.route("/logout")
def logout():
    session['logged_in'] = False
    return home()


if __name__ == "__main__":
    app.secret_key = os.urandom(12)
    app.run(debug=True)
