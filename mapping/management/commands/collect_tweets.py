from django.core.management.base import BaseCommand, CommandError
from tweepy import OAuthHandler
from tweepy import Stream
from _private import StdOutListener
# Go to http://dev.twitter.com and create an app.
# The consumer key and secret will be generated for you after
consumer_key="cDU40spi8UOc9Tv1sUrsH2Y58"
consumer_secret="GZ51gpTPGRgJWkAxRqMSCtI0PzdD5LNWxVJ922Enuv8ZcMUvyG"

# After the step above, you will be redirected to your app's page.
# Create an access token under the the "Your access token" section
access_token="2840641954-vpsxGA6Hl1a4eO3UE2FcJkJ0CjCFsw15PAvHPU9"
access_token_secret="1SBtwLoUbeounR6Qs5FZZfrveJBFUu5ZRmMpCnzRwAKgR"

class Command(BaseCommand):
    def handle(self, *args, **options):
        #this part could be further improved for the command line
        keyword = args[1]
        l = StdOutListener(int(args[0]),keyword)
        auth = OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)

        stream = Stream(auth, l)
        #stream.sample(languages=['en'])
        stream.filter(track=[keyword])