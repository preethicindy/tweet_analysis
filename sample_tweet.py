from twikit import Client
from configparser import ConfigParser
from datetime import datetime
import asyncio
import csv
import time

# Extrating tweets from Twitter 

async def tweepyAnalysis():
    MIN_TWEETS = 30
    tweet_count = 0 
    QUERY="deepseek"
    config = ConfigParser()
    config.read('config.ini')
    username = config['X']['username']
    email = config['X']['email']
    password = config['X']['password']
    
    with open("tweets.csv", 'w', newline='') as file:
        csv_writer = csv.writer(file)
        csv_writer.writerow(["Tweet Count", "Username", "Tweet text", "Retweets", "Likes"])

    client = Client('en-US')
    try:
        await client.login(auth_info_1=username, auth_info_2=email, password=password)
        client.save_cookies('cookies.json')
     #  client.load_cookies('cookies.json')
        print("Yaay, I'm in X")

        tweets = None
        while tweet_count < MIN_TWEETS:
            if tweets is None:
                print(f'{datetime.now()} - Getting tweets...')
                tweets = await client.search_tweet(QUERY,product='Latest')
            else:
                wait_time = 8
                print(f'{datetime.now()} - Getting more tweets after {wait_time} seconds...')
                time.sleep(wait_time)
                tweets = await tweets.next()
            if not tweets:
                print(f'{datetime.now()} - No more tweets found...')
                break

            for tweet in tweets:
                tweet_count +=1
                tweet_data = [tweet_count, tweet.user.name, tweet.text, tweet.retweet_count, tweet.favorite_count]
                
                with open("tweets.csv", 'a', newline='') as file:
                    csv_writer = csv.writer(file)
                    csv_writer.writerow(tweet_data)

            print(f'{datetime.now()} - Got {tweet_count} tweets...')
        
        print(f'{datetime.now()} - Done! Got {tweet_count} tweets...')
            
    except Exception as e:
        print(f'Something went wrong! {e}')


    

asyncio.run(tweepyAnalysis())