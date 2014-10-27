from tweepy.streaming import StreamListener
from mapping.models import Tweets
from mapping.util import isValidTweet
from dateutil import parser
import json


class StdOutListener(StreamListener):
    """ A listener handles tweets are the received from the stream.
    This is a basic listener that just prints received tweets to stdout.

    """
    def __init__(self,count,keyword,api=None):
        StreamListener.__init__(self,api=api)
        self.count = count
        self.keyword = keyword
    def on_data(self, data):
        if self.count>0:
            tt = json.loads(data)
            if isValidTweet(tt):
                self.count -= 1
                print tt['text']
                tweet = Tweets(longitude=tt['coordinates']['coordinates'][0],\
                               latitude=tt['coordinates']['coordinates'][1],\
                               keywords=self.keyword,\
                               post_time=parser.parse(tt['created_at'])
                               )
                tweet.save()#write data into database
        else:
            return False
    def on_error(self, status):
        print status
        return False


