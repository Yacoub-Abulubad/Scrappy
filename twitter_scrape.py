import tweepy as tw
import pandas as pd
from urllib3.requests import urlopen
from bs4 import BeautifulSoup as bs

def twitter_scrappy(api_key, api_secret, access_token, access_secret, bearer_token, users_list):

    api = tw.Client(bearer_token, api_key, api_secret,access_token,access_secret, wait_on_rate_limit=True)

    users = {}

    for user in users_list:
        user_info = api.get_user(username=user)
        user_id = user_info.data.id
        users[user] = user_id
        
    tweets = {
      'Content':[],
      'Tweet URL':[],
      'Article URL':[],
      'account':[],
    }
    for user,id in users.items():
        user_tw = {}
        links = []
        texts = []
        tweet_links = []
        titles = []
        tweet = api.get_users_tweets(id,max_results=100, exclude=['retweets','replies'])
        for j in tweet[0]:
            if 'https' in j['text']:
                text, link = j['text'].rsplit('https',1)
                title = article_scrape(link)
            else:
                link = 'None'
            
            links.append(link)
            texts.append(text)
            titles.append(title)

        tweet_links = ['https://twitter.com/twitter/statuses/' + str(i['id']) for i in tweet[0]]
        

        for i in range(len(tweet[0])):
            tweets['Content'].append(texts[i])
            tweets['Tweet URL'].append(tweet_links[i])
            tweets['Article URL'].append('https' + links[i][:18])
            tweets['Article Title'].append(titles[i])
            tweets['Account'].append(user)
        

    return pd.DataFrame(tweets)

def article_scrape(url):
    #
    # fix it
    #
    #reqs = requests.get('https' + url)
    soup = bs(urlopen('https' + url))
    print(soup)
    #title = soup.find('title')
    print(soup.title)
    return soup.title.get_text()
