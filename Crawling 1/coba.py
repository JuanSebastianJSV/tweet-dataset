import tweepy
import json

CONSUMER_KEY = 'KmWxn5o75SCllWL0Gw3uuLtpC'
CONSUMER_SECRET = '4AJcAPIO71NBjPSQtv3vWfMni2pIobqYNQGZjzyPXZQeE02rJU'
ACCESS_KEY = '1353996404310515718-ZNXC8qhwQ9denaTsTSy9UsOkzel9kD'
ACCESS_SECRET = '7f1TXnT76Q8PUWEdlEoQqZq9hZ4cYoTunpK4IvBdsnZAP'

auth = tweepy.auth.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

tweetsPerQry = 100
maxTweets = 100000
maxId = -1
tweetCount = 0
no = 1
keyword = '"coral bleaching" OR "ocean warming" OR "coral restoration" OR "coral monitoring" -filter:retweets'

tweet_list = list()

while tweetCount < maxTweets:
	if(maxId <= 0):
		newTweets = api.search(q=keyword, count=tweetsPerQry, result_type='recent', tweet_mode='extended')
	else:
		newTweets = api.search(q=keyword, count=tweetsPerQry, max_id=str(maxId - 1), result_type='recent', tweet_mode='extended')

	if not newTweets:
		print("Tweet Habis")
		break
	
	for tweet in newTweets:

		tweet_list.append(tweet._json)

		print('tweet -',no, 'written by', tweet.user.screen_name)
		print(tweet.created_at)
		no +=1
		print(tweet.full_text)
		print("\n")
		
	tweetCount += len(newTweets)	
	maxId = newTweets[-1].id


with open('crawl_30_01_2021.json', 'w') as out:
    json.dump(tweet_list,out,indent=4)