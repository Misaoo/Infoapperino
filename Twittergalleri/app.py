from flask import Flask, render_template
import authenticate
import json



app = Flask(__name__)

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



@app.route('/')
def index():
    return render_template("index.html", findtweet=findtweet())




if __name__ == "__main__":
    app.run(debug=True)
