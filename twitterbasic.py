import tweepy as tw

consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''

# login or authenticate to twitter
auth = tw.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tw.API(auth, wait_on_rate_limit=True)

# api.update_status('hello world from cipete')

search_words = "#jokowi"
date_since = "2019-08-01"

tweets = tw.Cursor(api.search, q=search_words, lang="en", since=date_since).items(1)

for t in tweets:
    print(t.text + ' at ' + t.user.location)
    print(t.user.description)




