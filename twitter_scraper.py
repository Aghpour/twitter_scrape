import snscrape.modules.twitter as sntwitter
import pandas as pd
import time
import os
from IPython.display import clear_output
from datetime import datetime
###############################
dir = os.getcwd()
today = datetime.today().strftime('%Y-%m-%d')
file_counter = []
columns=['Datetime', 'Tweet_Text', 'Like_Count', 'Reply_Count', 'Retweet_Count',
         'Quote_Count', 'Username', 'Display_Name', 'Followers_Count', 'Following_Count',
         'User_Id', 'Tweet_Url', 'Tweet_Id', 'location']
###############################
def collect(keyword, start_date, end_date, lang, chunk):
  scraper = sntwitter.TwitterSearchScraper(f'{keyword} lang:{lang} since:{start_date} until:{end_date}')
  tweets_list = []
  filename = f'{keyword}_{today}'
  for i, tweet in enumerate(scraper.get_items()):
    if i >= total_twt:
      break
    else:
      tweets_list.append([tweet.date, tweet.rawContent, tweet.likeCount, tweet.replyCount, tweet.retweetCount,
                          tweet.quoteCount, tweet.user.username, tweet.user.displayname, tweet.user.followersCount,
                          tweet.user.friendsCount, tweet.user.id, tweet.url, tweet.id, tweet.user.location])
      clear_output(wait=True)
      #os.system('cls')  # clear terminal output. only for windows os
      print(f'{i+1} - {tweet.user.username}')
      if len(tweets_list) > 0 and len(tweets_list) % chunk == 0:
          tweets_df = pd.DataFrame(tweets_list, columns=columns)
          file_counter.append(len(tweets_list))
          tweets_df.to_csv(f'{filename}_{len(file_counter)}.csv', index=False, encoding='utf-8')
          tweets_list = []

  if len(tweets_list) > 0:
    tweets_df = pd.DataFrame(tweets_list, columns=columns)
    file_counter.append(len(tweets_list))
    filename = f'{keyword}_{today}'
    tweets_df.to_csv(f'{filename}_{len(file_counter)}.csv', index=False, encoding='utf-8')
    tweets_list = []
###############################
def time_counter(t):
  if t < 60:
    tm = t
    return tm, 'seconds'
  elif t >= 60 and t < 3600:
    tm = t / 60
    return tm, 'minutes'
  else:
    tm = t / 3600
    return tm, 'hours'
###############################
# declare below variables:
keyword = 'بورس'
start_date = '2023-01-29'
end_date = '2023-01-30'
lang = 'fa'
chunk = 10000
total_twt = 10000000
###############################
t1 = time.perf_counter()
collect(keyword, start_date, end_date, lang, chunk)
t2 = time.perf_counter() - t1
###############################
tt = time_counter(t2)
clear_output(wait=True)
#os.system('cls')  # clear terminal output. only for windows os
print(f'It took {tt[0]:0.1f} {tt[1]} to collect {sum(file_counter)} tweets and\
 exported into {len(file_counter)} files in "{dir}" directory.')
