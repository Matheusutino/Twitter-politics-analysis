import tweepy
import requests
import pandas as pd
import os
import credentials

def getData(queryTopic, max_results = 100):
    query = queryTopic + ' -is:retweet lang:pt'


    tweets = client.search_recent_tweets(query, max_results = max_results)

    # Save data as dictionary
    tweets_dict = tweets.json() 

    # Extract "data" value from dictionary
    tweets_data = tweets_dict['data'] 

    # Transform to pandas Dataframe
    df = pd.json_normalize(tweets_data)

    return df 

def classifier(df):
    label = []

    for i in range(0, len(df)):
        print(df['text'][i])
        category = input()
        label.append(category)
        os.system('cls')
        
    return label

client = tweepy.Client( bearer_token=credentials.bearer_token, 
                        consumer_key=credentials.consumer_key, 
                        consumer_secret=credentials.consumer_secret, 
                        access_token=credentials.access_token, 
                        access_token_secret=credentials.access_token_secret, 
                        return_type = requests.Response,
                        wait_on_rate_limit=True)

topics = ['candidato']

for topic in topics:
    df = getData(topic, 100)
    label = classifier(df)
    df['label'] = label
    df.to_csv(topic + '.csv',index=False)
