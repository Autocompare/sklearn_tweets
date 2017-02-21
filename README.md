# sklearn_tweets
Run sci-kit learn based machine learning trained on datasets of keyword searched tweets and their sentiment
analysis scores in real time. 

# Purpose
Often times when experimenting with machine learning on text data in Scikit-Learn you practice by using static datasets like 20Newsgroup. This can create a misinformed view on model fitting and f1 score reports of real world, constantly changing data. This demo is designed to capture tweets in real-time, analyze their sentiment in real-time and create a dataset of filtered tweets as the training data (X) with ranked sentiment scores as the target data (y). The demo also makes and measures predictions on the fit model of X,y.


**Results**

You should be able to get report charts like this that change as the new twitter data is captured.


<img src=http://i.imgur.com/Rt85Gcg.png>

# Modules
**Install the requirements with pip**

	pip install -r /path/to/requirements.txt

**Twitter**

Make sure you have a twitter account and enter your O Auth credentials in get_tweets.py

	OAUTH_TOKEN =  "enter your token" 
	OAUTH_TOKEN_SECRET = "enter your token secret"
	CONSUMER_KEY = "enter your consumer key"
	CONSUMER_SECRET = "enter your consumer secret"

Expand your search criteria and subject to exceed the 100 tweets per search cap of the API.

	tweets = process_tweets('Trump','Merkel','Brexit')


**Scikit-Learn**

Obviously sklearn fit models do dramatically better the more data you have but this is a real world,
real-time demo to show what happens when you don't. This demo creates pipelines and vectorizes the 
tokenized tweet text with the TfidfVectorizer and uses Multinomial Naive Bayes as the classifier.
Those experienced in sklearn can easily add more pipelines to check other vector / classifier pairings.

	pipeline = Pipeline([
	('vect', TfidfVectorizer(
				stop_words,
				token_pattern=ur"\b[a-z0-9_\-\.]+[a-z][a-z0-9_\-\.]+\b",
				)),
				('clf', MultinomialNB(alpha=0.2)),
			])


As you can see from this sample report the precision and f1-score can yield interesting
results with shallow data. The target data has 20 labels ranging from extremely low sentiment
to extremely high sentiment. It's unlikely without several thousand tweets to see support at every label.
Because of this the classification report will throw label warnings.


		         precision    recall  f1-score   support

     lowest       0.00      0.00      0.00         0
          1       0.00      0.00      0.00         0
          2       0.25      1.00      0.40         1
          3       0.00      0.00      0.00         0
          4       0.00      0.00      0.00         0
          5       0.00      0.00      0.00         0
          6       0.00      0.00      0.00         0
          7       0.00      0.00      0.00         0
          8       1.00      0.47      0.64        88
          9       0.00      0.00      0.00         0
    neutral       0.00      0.00      0.00         0
         11       0.00      0.00      0.00         0
         12       0.00      0.00      0.00         1
         13       0.00      0.00      0.00         0

	avg / total       0.98      0.47      0.63        90

	[Finished in 8.1s]


**Vader Sentiment**

For sentiment analysis we are using the interesting Valence Aware Dictionary and sEntiment Reasoner
module for python created by [@cjhutto](https://github.com/cjhutto/vaderSentiment). Each tweet is
iterated through sentiment analysis and enumerated to create the labeled target data.

		def process_scores():
		raw_scores = [sent_analyze(tweet) for tweet in some_array]
		enumarated_scores = [enumerate_score(score) for score in raw_scores]
		return enumarated_scores





