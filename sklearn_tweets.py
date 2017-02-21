from nltk.corpus import stopwords
from sklearn.pipeline import Pipeline
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np
from sklearn.metrics import classification_report

from get_tweets import process_tweets
from get_sentiment import process_sentiment, sent_labels


tweets = process_tweets('Trump','Merkel','Brexit')
scores = process_sentiment(tweets)


def preproc_data():
	SPLIT_PERC = 0.50
	split_size = int(len(tweets)*SPLIT_PERC)
	a = tweets[:split_size]
	b = tweets[split_size:]
	c = scores[:split_size]
	d = scores[split_size:]
	return a,b,c,d

X_train,X_test,y_train,y_test = preproc_data()


stop_words = set(stopwords.words('english'))

from sklearn.cross_validation import cross_val_score, KFold
from scipy.stats import sem

def eval_cross_val(clf_, X, y, K):
	cv = KFold(len(y), K, shuffle=True, random_state=0)
	scores = cross_val_score(clf_, X, y, cv=cv)
	print ("Mean score: {0:.3f} (+/-{1:.3f})") .format (np.mean(scores), sem(scores))

pipeline = Pipeline([
	('vect', TfidfVectorizer(
				stop_words,
				token_pattern=ur"\b[a-z0-9_\-\.]+[a-z][a-z0-9_\-\.]+\b",
				)),
				('clf', MultinomialNB(alpha=0.2)),
			])

eval_cross_val(pipeline, X_train, y_train, 6)

pipeline.fit(X_train, y_train)
y = pipeline.predict(X_test)

def get_report():
	return (classification_report(y, y_test, target_names=sent_labels))





