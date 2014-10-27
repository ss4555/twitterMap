__author__ = 'songqiaosu'

def isValidTweet(tweet):
    if not tweet or 'delete' in tweet or 'limit' in tweet or 'warning' in tweet:
        return False
    return 'coordinates' in tweet and tweet['coordinates'] \
        and 'coordinates' in tweet['coordinates'] and tweet['coordinates']['coordinates'] \
        and 'created_at' in tweet and tweet['created_at'] \
        and 'text' in tweet and tweet['text']
