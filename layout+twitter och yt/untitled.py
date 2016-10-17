from flask import Flask
from flask import render_template
from flask import url_for
import authenticate
import json


app = Flask(__name__)


@app.route('/')
def hello_world(name=None):

    return render_template('index.html', name=name)


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



if __name__ == '__main__':
    app.run(debug=True)
