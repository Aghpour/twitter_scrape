import snscrape.modules.twitter as sntwitter
import pandas as pd
import time

start = time.time()
t1 = time.perf_counter()
# Creating list to append tweet data to
tweets_list = []
keyword = 'بورس'
start_date = '2022-06-02'
end_date = '2022-06-03'
lang = 'fa'

# Using TwitterSearchScraper to scrape data and append tweets to list
for i,tweet in enumerate(sntwitter.TwitterSearchScraper(f'{keyword} lang:{lang} since:{start_date} until:{end_date}').get_items()):
    if i>2000000:
        break
    tweets_list.append([tweet.date, tweet.content, tweet.likeCount, tweet.replyCount, tweet.retweetCount, tweet.quoteCount,
                        tweet.user.username, tweet.user.displayname, tweet.user.followersCount, tweet.user.friendsCount])
    
# Creating dataframe
tweets_df = pd.DataFrame(tweets_list, columns=['Datetime', 'Tweet_Text', 'Like_Count', 'Reply_Count', 'Retweet_Count',
                                               'Quote_Count', 'Username', 'Display_Name', 'Followers_Count', 'Following_Count'])

tweets_df.to_csv(f'{keyword}.csv', index = False, encoding='utf-8')

t2 = time.perf_counter() - t1
tweets_count = len(tweets_list)
print(f'It took {t2:0.1f} seconds to download {tweets_count} tweets.')
