#%%
import tweepy
from twitter_scrape import twitter_scrappy
from rss_feed import rss_scrappy

#All keys are hidden for personal and privacy purposes
from keys import *

#url of the rss feed
url = 'https://www.cannabisbusinesstimes.com/rss/'

#enter the usernames that you would like to scrape
users_list = [
    'garyvee',
    'kingjames'

]

tweets = twitter_scrappy(api, api_s, access, access_s, bearer, users_list)
rss = rss_scrappy(url)

# %%
import tweepy
print(tweepy.__version__)
# %%
