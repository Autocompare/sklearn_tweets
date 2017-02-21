from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from get_tweets import process_tweets # expects two strings as tweet subjects

def process_sentiment(some_array):

	def sent_analyze(element):
			vader_A  = SentimentIntensityAnalyzer()
			vs = vader_A.polarity_scores(element)

			if vs['neg'] >= vs['pos']:
				return vs['compound']

			elif vs['pos'] >['neg']:
				return vs['pos']

			else:
				return vs['neu']

	def enumerate_score(some_float):
		"""
		# enumerate scores based on sentiment float value
		"""
		nf = round(some_float,3)
		if nf < -.899 and nf > -.999:
			return 0
		elif nf < -.799 and nf > -.900:
			return 1
		elif nf < -.699 and nf > -.800:
			return 2
		elif nf < -.599 and nf > -.700:
			return 3
		elif nf < -.499 and nf > -.600:
			return 4
		elif nf < -.399 and nf > -.500:
			return 5
		elif nf < -.299 and nf > -.400:
			return 6
		elif nf < -.199 and nf > -.300:
			return 7
		elif nf < -.099 and nf > -.200:
			return 8
		elif nf < 0.0 and nf > -.099:
			return 9
		elif nf >= 0.0 and nf < .100:
			return 10
		elif nf > .100 and nf < .199:
			return 11
		elif nf > .200 and nf < .299:
			return 12
		elif nf > .300 and nf < .399:
			return 13
		elif nf > .400 and nf < .499:
			return 14
		elif nf > .500 and nf < .599:
			return 15
		elif nf > .600 and nf < .699:
			return 16
		elif nf > .700 and nf < .799:
			return 17
		elif nf > .800 and nf < .899:
			return 18
		elif nf > .900 and nf < .999:
			return 19
		elif nf > .999:
			return 20

		else:
			return 10



		#elif nf 

	def process_scores():
		raw_scores = [sent_analyze(tweet) for tweet in some_array]
		enumarated_scores = [enumerate_score(score) for score in raw_scores]
		return enumarated_scores



	return process_scores()

sent_labels = ['lowest','1','2','3','4','5','6','7','8','9',
				'neutral','11','12','13','14','15','16','17','18','19'
				'highest']

#print get_sentiment(process_tweets('Trump','Merkel'))



