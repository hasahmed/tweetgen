import sys
from tweet_gather_util import TweetGatherer
import general_util as gutil
tweet_gatherer = TweetGatherer()
usernames_tweets = tweet_gatherer.get_tweets_from_disk("realdonaldtrump")

gutil.print_context(sys.argv[1], usernames_tweets)
