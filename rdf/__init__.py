from random import choice, randrange

from tweepy import API, OAuthHandler

PAGE_LIMIT = 20

consumer_key = ''
consumer_secret = ''

access_token = ''
access_token_secret = ''

oauth_handler = OAuthHandler(consumer_key, consumer_secret)
oauth_handler.set_access_token(access_token, access_token_secret)

api = API(oauth_handler)
me = api.me()

favourite_count = me.favourites_count
page_count = favourite_count // PAGE_LIMIT

page = randrange(page_count)

favourites = api.favorites(limit=PAGE_LIMIT, page=page)
random_favourite = choice(favourites)

retweets = random_favourite.retweets()

if random_favourite.retweeted:
    print 'Already retweeted'

    for retweet in retweets:
        if retweet.user.id == me.id:
            retweet.destroy()

            print 'Asploded'

random_favourite.retweet()
print 'Retweeted'
