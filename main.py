import time
import tweepy
import ssl

ssl._create_default_https_context = ssl._create_unverified_context
# Oauth keys
consumer_key = "API_KEY"
consumer_secret = "API_SECRET_KEY"
access_token = "ACCESS_TOKEN"
access_token_secret = "ACCESS_TOKEN_SECRET"

# Authentication with Twitter
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Tweet Url : https://twitter.com/ZarTweety/status/1420971733444608008
# Structure :    TWITTER_DOMAIN  /@USERNAME/status/     TWEET_ID
name = 'ZarTweety'  # @USERNAME
tweet_id = '1420971733444608008'  # TWEET_ID

# If duplicates are required:
#   repeat = True
# else:
#   repeat = False
repeat = False
counter = 1
repliesUserId = []

for tweet in tweepy.Cursor(api.search, q='to:' + name, result_type='recent', timeout=9999999).items(100000):
    if hasattr(tweet, 'in_reply_to_status_id_str'):
        if tweet.in_reply_to_status_id_str == tweet_id:
            value = tweet.user.id

            # Check for duplicates user.id
            valueIs = value in repliesUserId

            if (valueIs and repeat) or not valueIs:
                repliesUserId.append(value)
                print('{} - {}'.format(counter, value))
                print(tweet)
                counter += 1

    # set sleep for unlimited Twitter API
    time.sleep(1)
