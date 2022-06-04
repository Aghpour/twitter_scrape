import snscrape.modules.twitter as sntwitter
import pandas as pd
import time
import os
from datetime import datetime

t1 = time.perf_counter()
# Creating list to append tweet data to
tweets_list = []
keyword = 'بورس'
start_date = '2022-05-15'
end_date = '2022-06-04'
lang = 'fa'

# Using TwitterSearchScraper to scrape data and append tweets to list
for i,tweet in enumerate(sntwitter.TwitterSearchScraper(f'{keyword} lang:{lang} since:{start_date} until:{end_date}').get_items()):
    if i>5000000:
        break
    elif keyword in tweet.content:
        tweets_list.append([tweet.date, tweet.content, tweet.likeCount, tweet.replyCount, tweet.retweetCount, tweet.quoteCount,
                        tweet.user.username, tweet.user.displayname, tweet.user.followersCount, tweet.user.friendsCount])
        os.system('cls')  # clear terminal output. only for windows os
        print(f'{i+1}, {tweet.user.username}')
    
# Creating dataframe
tweets_df = pd.DataFrame(tweets_list, columns=['Datetime', 'Tweet_Text', 'Like_Count', 'Reply_Count', 'Retweet_Count',
                                               'Quote_Count', 'Username', 'Display_Name', 'Followers_Count', 'Following_Count'])

now = datetime.today().strftime('%Y-%m-%d_%H-%M')
filename = f'{keyword}_{now}'
tweets_df.to_csv(f'{filename}.csv', index = False, encoding='utf-8')

t2 = time.perf_counter() - t1
tweets_count = len(tweets_list)
os.system('cls')
if t2 <= 60:
    seconds = t2
    print(f'It took {seconds:0.1f} seconds to download {tweets_count} tweets and exported to "{filename}.csv" file.')
else:
    minutes = t2/60
    print(f'It took {minutes:0.1f} minutes to download {tweets_count} tweets and exported to "{filename}.csv" file.')
