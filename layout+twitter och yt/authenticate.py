from tweepy import OAuthHandler
import tweepy



ckey = 'lpgoKPoAgQ2G5DOxdDqP63SIG'
csecret = 'W4zTAiIaLuWuwBLV7ApIV8QDb9nuq4deEgpzZMAj2Ag3l4l3Bz'
atoken = '468737134-N1LHgVGyjyRIVCghgPxu1DmFgNoQ0CRAEDJU3flk'
asecret = 'XJTg9p70CmRVAhTyXupBtJhErWgPy8tNqXhsxqbFEYn0C'

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
api = tweepy.API(auth)