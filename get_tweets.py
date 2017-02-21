from string import punctuation
from string import maketrans
import re, string
import unicodedata
import twitter

# Cached static lists
cachedPunctuation = string.punctuation

OAUTH_TOKEN =  "enter your token" 
OAUTH_TOKEN_SECRET = "enter your token secret"
CONSUMER_KEY = "enter your consumer key"
CONSUMER_SECRET = "enter your consumer secret"

auth = twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET, CONSUMER_KEY, CONSUMER_SECRET)
twitter_api = twitter.Twitter(auth=auth)


def process_tweets(subject_1,subject_2,subject_3):
	""" 
	takes tweet subjects as a strings and returns array of tweets
	add more subject variables and statuses variables for larger arrays
	"""

	q = subject_1
	u = subject_2
	t = subject_3

	results_1 = twitter_api.search.tweets(q=q, count=100) 
	results_2 = twitter_api.search.tweets(q=u, count=100) 
	results_3 = twitter_api.search.tweets(q=t, count=100) 

	statuses_1 = results_1['statuses']
	statuses_2 = results_2['statuses']
	statuses_3 = results_2['statuses']

	extracted_tweets_1 = [status['text']
					for status in statuses_1 ]


	extracted_tweets_2 = [status['text']
					for status in statuses_2 ]

	extracted_tweets_3 = [status['text']
				for status in statuses_3 ]
	
	
	def format_tweet(string_):
		""" removes emoji,links and non-ascii """
		tweets = unicodedata.normalize('NFKD', string_).encode('ascii','ignore') 

		table = string.maketrans("","")
		remove_punct = lambda s: s.translate(table, cachedPunctuation)
		tweet_text = remove_punct(tweets)

		tweet_text_list = tweet_text.split()
		no_links = 'http'
		regex_ = re.compile(".*(%s).*" % no_links)
		search_ = [m.group(0) for l in tweet_text_list for m in [regex_.search(l)] if m]
		clean_tweet = [word for word in tweet_text_list if word not in search_]
		
		return ' '.join(clean_tweet)


	group_0 = [format_tweet(tweet) for tweet in extracted_tweets_1]
	group_1 = [format_tweet(tweet) for tweet in extracted_tweets_2]
	group_2 = [format_tweet(tweet) for tweet in extracted_tweets_3]

	# remove any redundant tweets between groups
	output_list = list(set(group_0 + group_1 + group_2))
	
	
	return output_list

#print len(process_tweets('trump','merkel','brexit'))

