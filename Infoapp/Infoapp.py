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

        query = "INSERT INTO post (headline, text, date) VALUES (%s, %s, now())"

        print query

        config.cur.execute(query, (post_heading, post_text))

        return render_template("blogpost.html")
    else:
        return redirect('/')


    if request.method == 'GET':
        return render_template("blogpost.html")

@app.route('/blogg')
def blogg():

    bloggPosts = []

    query = "SELECT headline, text FROM post ORDER BY date DESC"
    config.cur.execute(query)
    result = config.cur.fetchall()

    for i in result:
        bloggPosts.append(i)

    print bloggPosts



    bloggHead = []
    bloggText = []

    for i in bloggPosts:
        #print i[0]
        bloggHead.append(i[0])
        bloggText.append(i[1])
    #bloggHead = bloggPosts[0][0]
    #bloggText = bloggPosts[0][1]

    print bloggHead
    print bloggText

    return render_template("posts.html", bloggPosts=bloggPosts)

@app.route("/logout")
def logout():
    session['logged_in'] = False
    return home()


if __name__ == "__main__":
    app.secret_key = os.urandom(12)
    app.run(debug=True)
