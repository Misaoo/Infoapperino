import os, sys
from flask import Flask, flash, redirect, render_template, request, session
import os
import time
import config
import authenticate
import json

app = Flask(__name__)

@app.route('/')
def home(name=None):
    return render_template('index.html', name=name)

@app.route('/loggain')
def logga_in():
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
                return render_template('blogpost.html')
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


    if request.method == 'GET' and session.get("logged_in") == True:
        return render_template("blogpost.html")
    else:
        return redirect('/login')

@app.route('/blogg', methods=['POST', 'GET'])
def blogg():
    bloggPosts = []
    limit = 3

    if request.method == 'POST':
        limit = int(request.form['limit']) + 3

    query = "SELECT headline, text, date FROM post ORDER BY date DESC LIMIT %s "
    config.cur.execute(query, (limit,))
    result = config.cur.fetchall()

    for i in result:
        bloggPosts.append(i)

    return render_template("posts.html", bloggPosts=bloggPosts, limit = limit)

@app.route("/logout")
def logout():
    session['logged_in'] = False
    return logga_in()

@app.route('/schema')
def schema(name=None):

    return render_template('schema.html', name=name)


@app.route('/yt')
def yt(name=None):

    return render_template('yt.html', name=name)


@app.route('/iframe')
def iframe(name=None):

    return render_template('iframe.html', name=name)


@app.route('/twittergalleri')
def twittergalleri():

    return render_template("twittergalleri.html", findtweet=findtweet())


@app.route('/Images')
def findtweet():
    images = []
    for tweet in authenticate.tweepy.Cursor(authenticate.api.search, q="#BTHSkate", include_entities=True).items(20):
        if 'media' in tweet.entities:
            for image in tweet.entities['media']:
                images.append(image['media_url'])
                print(image['media_url'])

    print(images)
    print (len(images))
    return json.dumps(images)



if __name__ == "__main__":
    app.secret_key = os.urandom(12)
    app.run(debug=True)
