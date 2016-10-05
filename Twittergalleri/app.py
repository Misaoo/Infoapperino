from flask import Flask, render_template
import authenticate
import tweepy
from tweepy import OAuthHandler


app = Flask(__name__)

@app.route('/')
def findtweet():

    images = []

    for tweet in authenticate.tweepy.Cursor(authenticate.api.search, q="#BTHSkate", include_entities=True).items(3):
        if 'media' in tweet.entities:
            for image in tweet.entities['media']:
                images.append(image['media_url'])
                print(image['media_url'])
    #images.append(image['media_url'])
    print(images)
    print (len(images))
    return render_template("index.html", images=images)

if __name__ == "__main__":
    app.run(debug=True)
