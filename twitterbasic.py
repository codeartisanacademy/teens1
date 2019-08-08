import tweepy as tw

consumer_key = '3AJlDF2sOLiacWfTwB4kfQ'
consumer_secret = 'N0BoMJRjiixJo7IHdqupdqx7gYCksgRsAGF9gHWYTI'
access_token = '14128035-vJOHnsTqjD8gOcyysOAvDHCOiLMZ8ZyKL1v6ZguXQ'
access_token_secret = 'XkEEdb2MH2OJVGYQtiV7eyXZrGpHzsuz7dRQek1j4'

# login or authenticate to twitter
auth = tw.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tw.API(auth, wait_on_rate_limit=True)

# api.update_status('hello world from cipete')


















'''
consumer_key = '3AJlDF2sOLiacWfTwB4kfQ'
consumer_secret = 'N0BoMJRjiixJo7IHdqupdqx7gYCksgRsAGF9gHWYTI'
access_token = '14128035-vJOHnsTqjD8gOcyysOAvDHCOiLMZ8ZyKL1v6ZguXQ'
access_token_secret = 'XkEEdb2MH2OJVGYQtiV7eyXZrGpHzsuz7dRQek1j4'

auth = tw.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tw.API(auth, wait_on_rate_limit=True)

# api.update_status('hello world #python')

search_words = "#quotes"
date_since = "2019-08-01"

tweets = tw.Cursor(api.search, q=search_words, lang="en", since=date_since).items(5)

for t in tweets:
    print(t.text)
    print('-'*10)
    
'''



