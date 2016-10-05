from flask import Flask
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
from tweepy import api
import tweepy
import time
import json
import pprint

app = Flask(__name__)

ckey = 'lpgoKPoAgQ2G5DOxdDqP63SIG'
csecret = 'W4zTAiIaLuWuwBLV7ApIV8QDb9nuq4deEgpzZMAj2Ag3l4l3Bz'
atoken = '468737134-N1LHgVGyjyRIVCghgPxu1DmFgNoQ0CRAEDJU3flk'
asecret = 'XJTg9p70CmRVAhTyXupBtJhErWgPy8tNqXhsxqbFEYn0C'


class listener(StreamListener):
    def on_data(self, data):
        try:

            #json_tweet = json.loads(data)
            tweet = data.split(',"media_url":"')[1].split('","media_url_https')[0]
            tweet = tweet.replace("\\", "")
            images = '<img src2=' + tweet + ' style="width:150px;height:150px;">'
            print(tweet)

            #print (json_tweet['text'])


            saveFile = open('twitDB.html' , 'a')
            saveFile.write(images)
            saveFile.write('\n')
            saveFile.close()
            return True

        except BaseException as e:
            #print(json_tweet['text'])
            print ('failed ondata.' ,str(e))
            time.sleep(0.5)

    def on_error(self, status):
        print (status)


auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
twitterStream = Stream(auth, listener())
twitterStream.filter(track=['Photos'])











