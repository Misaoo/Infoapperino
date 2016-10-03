
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import time

ckey = 
csecret = 
atoken = 
asecret = 


class listener(StreamListener):
    def on_data(self, data):
        try:
            #print (data)

            tweet = data.split(',"media_url":"')[1].split('","media_url_https')[0]
            tweet = tweet.replace("\\", "")
            images = '<img src=' + tweet +' style="width:150px;height:150px;">'
            print (tweet)
            
            saveFile = open('twitDB.txt' , 'a')
            saveFile.write(images)
            saveFile.write('\n')
            saveFile.close()
            return True
        except BaseException as e:
            print ('failed ondata.' ,str(e))
            time.sleep(5)

    def on_error(self, status):
        print (status)

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
twitterStream = Stream(auth, listener())
twitterStream.filter(track=["Photos"])

