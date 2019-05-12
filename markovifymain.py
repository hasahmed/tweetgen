import markovify
from tweet_gather_util import TweetGatherer # our stuff

trumps_username = "realDonaldTrump" # the username that we want all the tweets for
tweet_gatherer = TweetGatherer() # instance of our tweet gatherer class which verifies twitter app credentials on instanciation
# trumps_tweets a list where every tweet is a string entry
trumps_tweets = tweet_gatherer.get_tweets_from_disk(trumps_username)


tweets_togeter = ""
# make trumps_tweets into a single string
for tweet in trumps_tweets:
    tweets_togeter += tweet
    tweets_togeter += "\n" #space between every tweet

text_model = markovify.NewlineText(tweets_togeter)

for i in range(0, 100):
    gend = text_model.make_short_sentence(140)
    lastchar = gend[len(gend) -1]
    if lastchar == '.':
        gend = gend[0:len(gend) -1] + "!"
    else: gend += "!"
    print(gend)
