# sklearn_tweets
Capture tweets based on keywords, create targets for those tweets based on sentiment analysis, then process, train and fit the tweets and sentiment scores are training date for Sci-kit learn. 

# Purpose
Often times when experimenting with machine learning on text data in Scikit-Learn you practice by using static datasets like 20News. This can create a misinformed view on the model fitting and f1 score reports of real world, changing data. This demo is designed to capture tweets in real-time, analyze their sentiment in real-time and create a dataset of filtered tweets as the training data (X) with ranked sentiment scores as the target data (y). 


**Results**
You should be able to get report charts like this that change as the new twitter data is captured.
<img src=http://i.imgur.com/Rt85Gcg.png>

# Modules
**Install the requirements with pip**
	pip install -r /path/to/requirements.txt

**Twitter**
Make sure you have a twitter account and enter the O Auth credentials
	OAUTH_TOKEN =  "enter your token in" 
	OAUTH_TOKEN_SECRET = "enter your token secret in"
	CONSUMER_KEY = "enter your consumer key"
	CONSUMER_SECRET = "enter your consumer secret"
