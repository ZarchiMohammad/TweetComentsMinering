# Tweet Comments Miner

Using this code snippet, you can stream all the comments of a particular tweet_

For example, we can refer to [@ZarTweety's first tweet](https://twitter.com/ZarTweety/status/1420971733444608008)


## Python Code

```python
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

# duplicates are required ? True : False
repeat = False
counter = 1
repliesUserId = []

for tweet in tweepy.Cursor(api.search, q='to:' + name, result_type='recent', timeout=9999999).items(100000):
    if hasattr(tweet, 'in_reply_to_status_id_str'):
        if tweet.in_reply_to_status_id_str == tweet_id:
            twitterUserId = tweet.user.id

            # Check for duplicates user.id
            valueIs = twitterUserId in repliesUserId

            if (valueIs and repeat) or not valueIs:
                repliesUserId.append(twitterUserId )
                print('{} - {}'.format(counter, twitterUserId ))
                counter += 1

    # set sleep for unlimited Twitter API
    time.sleep(1)
```

## More details
If you are looking for more details of users commenting in a tweet, you can get help from [statuses/lookup](https://developer.twitter.com/en/docs/twitter-api/v1/tweets/post-and-engage/api-reference/get-statuses-lookup) or look at **TweetLookup.json**

For example:
```python
twitterUserId = tweet.user.id  # 1310040128916774912
twitterUserName = tweet.user.name  # مگاهـــرتز
twitterScreenName = tweet.user.screen_name  # ZarchiMohammad
```
## TweetLookup.json
```json
{
  "created_at": "Wed Aug 11 10:19:15 +0000 2021",
  "id": 1425401417406291972,
  "id_str": "1425401417406291972",
  "text": "@ZarTweety 3rd comment for test",
  "truncated": false,
  "entities": {
    "hashtags": [],
    "symbols": [],
    "user_mentions": [
      {
        "screen_name": "ZarTweety",
        "name": "ZarTweety",
        "id": 1393057524425928710,
        "id_str": "1393057524425928710",
        "indices": [
          0,
          10
        ]
      }
    ],
    "urls": []
  },
  "metadata": {
    "iso_language_code": "en",
    "result_type": "recent"
  },
  "source": "<a href=',http://twitter.com/download/android' rel='nofollow'>Twitter for Android</a>",
  "in_reply_to_status_id": 1420971733444608008,
  "in_reply_to_status_id_str": "1420971733444608008",
  "in_reply_to_user_id": 1393057524425928710,
  "in_reply_to_user_id_str": "1393057524425928710",
  "in_reply_to_screen_name": "ZarTweety",
  "user": {
    "id": 1310040128916774912,
    "id_str": "1310040128916774912",
    "name": "مگاهـــرتز",
    "screen_name": "ZarchiMohammad",
    "location": "Islamic Republic of Iran",
    "description": "Developer of Java, PHP & Python",
    "url": "https://t.co/Isi3moIHfd",
    "entities": {
      "url": {
        "urls": [
          {
            "url": "https://t.co/Isi3moIHfd",
            "expanded_url": "https://t.me/ZarTweety",
            "display_url": "t.me/ZarTweety",
            "indices": [
              0,
              23
            ]
          }
        ]
      },
      "description": {
        "urls": []
      }
    },
    "protected": false,
    "followers_count": 2682,
    "friends_count": 2688,
    "listed_count": 5,
    "created_at": "Sun Sep 27 02:15:01 +0000 2020",
    "favourites_count": 29118,
    "utc_offset": "none",
    "time_zone": "none",
    "geo_enabled": true,
    "verified": false,
    "statuses_count": 9478,
    "lang": "none",
    "contributors_enabled": false,
    "is_translator": false,
    "is_translation_enabled": false,
    "profile_background_color": "F5F8FA",
    "profile_background_image_url": "none",
    "profile_background_image_url_https": "none",
    "profile_background_tile": false,
    "profile_image_url": "http://pbs.twimg.com/profile_images/1412404960319393793/NUfgIauz_normal.jpg",
    "profile_image_url_https": "https://pbs.twimg.com/profile_images/1412404960319393793/NUfgIauz_normal.jpg",
    "profile_banner_url": "https://pbs.twimg.com/profile_banners/1310040128916774912/1620577298",
    "profile_link_color": "1DA1F2",
    "profile_sidebar_border_color": "C0DEED",
    "profile_sidebar_fill_color": "DDEEF6",
    "profile_text_color": "333333",
    "profile_use_background_image": true,
    "has_extended_profile": true,
    "default_profile": true,
    "default_profile_image": false,
    "following": false,
    "follow_request_sent": false,
    "notifications": false,
    "translator_type": "none",
    "withheld_in_countries": []
  },
  "geo": "none",
  "coordinates": "none",
  "place": "none",
  "contributors": "none",
  "is_quote_status": false,
  "retweet_count": 0,
  "favorite_count": 0,
  "favorited": false,
  "retweeted": false,
  "lang": "en"
}
```
