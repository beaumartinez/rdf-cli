# Retweet Dem Faves™

> Ever wanted to retweet your favourite tweets? Chosen at random? Well now you can.

Retweet Dem Faves™ uses [Tweepy][tweepy] and exposes a simple API.

## Usage

    from rdf.api import FaveRetweeter

    # Create a Twitter app at https://dev.twitter.com/apps to get the appropriate OAuth credentials
    retweeter = FaveRetweeter(consumer_key, consumer_secret, access_token, access_token_secret)
    favorite = retweeter.retweet_favorite()

    print favorite.id

[tweepy]: http://pypi.python.org/pypi/tweepy
