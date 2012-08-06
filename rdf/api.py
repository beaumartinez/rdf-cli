from math import ceil
from random import choice, randrange

from tweepy import API, OAuthHandler

def _retweet(tweet, user):
    retweets = tweet.retweets()

    if tweet.retweeted:
        # Already retweeted. Unretweet and tweet again

        for retweet in retweets:
            if retweet.user.id == user.id:
                retweet.destroy()

                break

    tweet.retweet()

class FaveRetweeter(object):

    def __init__(self, consumer_key, consumer_secret, access_token, access_token_secret):
        self.consumer_key = consumer_key
        self.consumer_secret = consumer_secret

        self.access_token = access_token
        self.access_token_secret = access_token_secret

        self._authorize()

    def _authorize(self):
        oauth_handler = OAuthHandler(self.consumer_key, self.consumer_secret)
        oauth_handler.set_access_token(self.access_token, self.access_token_secret)

        self.tweepy = API(oauth_handler)

    def retweet_fave(self):
        me = self.tweepy.me()

        favorite_count = me.favourites_count
        page = randrange(favorite_count)

        favorites = self.tweepy.favorites(count=1, page=page)
        favorite = favorites[0]

        _retweet(favorite, me)
