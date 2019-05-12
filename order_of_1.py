from bidict import bidict
import numpy as np
import re
from tweet_gather_util import TweetGatherer # our stuff
import general_util as gutil




trumps_username = "realDonaldTrump" # the username that we want all the tweets for
tweet_gatherer = TweetGatherer() # instance of our tweet gatherer class which verifies twitter app credentials on instanciation
# trumps_tweets a list where every tweet is a string entry
trumps_tweets = tweet_gatherer.get_tweets_from_disk(trumps_username)


charnumberings = {
    "a": 0,
    "b": 0,
    "c": 0,
    "d": 0,
    "e": 0,
    "f": 0,
    "g": 0,
    "h": 0,
    "i": 0,
    "j": 0,
    "k": 0,
    "l": 0,
    "m": 0,
    "n": 0,
    "o": 0,
    "p": 0,
    "q": 0,
    "r": 0,
    "s": 0,
    "t": 0,
    "u": 0,
    "v": 0,
    "w": 0,
    "x": 0,
    "y": 0,
    "z": 0,
    " ": 0,
    ".": 0,
    "!": 0,
}
for i, char in enumerate(charnumberings):
    charnumberings[char] = i





# This is counts how many times a particular character follows another character
charnumberings = bidict(charnumberings)

# 2d 27x27 array of zeros
M = np.zeros((len(charnumberings), len(charnumberings)))

#fill it in with the counts
for i in range(0, len(trumps_tweets)):
    for j in range(0, len(trumps_tweets[i]) -1):
        x = trumps_tweets[i][j].lower()
        y = trumps_tweets[i][j + 1].lower()
        regex = "^[A-Za-z.! ]$" # match only letters A-Z or a-z and '!', ' ', '.'
        if re.match(regex, x) and re.match(regex, y):
            try:
                M[charnumberings.get(x)][charnumberings.get(y)] += 1
            except:
                print("len(trumps_tweets[i])", len(trumps_tweets[i]))
                print("current j:", j)
                print("current j + 1:", j + 1)
                print("x, y:", x, y)
                print("charnumberings.gets", charnumberings.get(x), charnumberings.get(y))
                print("--------------------")


sums = np.zeros(len(charnumberings)) #every entry will contain a sum of its corrisponding row in the M matrix
for i, row in enumerate(M):
    sums[i] = np.sum(row)

# take our matrix and convert it to probabilities
probs = np.zeros((len(charnumberings), len(charnumberings))) #every entry will contain a sum of its corrisponding row in the M matrix

for i in range(0, len(M)):
    for j in range(0, len(M)):
        probs[i][j] = M[i][j] / sums[i]

for i in range(0, len(M)):
    for j in range(0, len(M)):
        print(probs[i][j],end=', ')
    print()

#end probabilities


def make_sentance(probability_matrix, starting_letter, sentence_length=140):
    next_letter = [starting_letter]
    output = starting_letter

    for i in range(0, sentence_length): # we will pick the most likely character 140 times
        sl_index = charnumberings.get(next_letter[0])
        starting_letter_row = probability_matrix[sl_index] #list row that represents starting_letter
        # next_letter_index = np.where(starting_letter_row == max(starting_letter_row))[0][0] # pick the max index of the probabliities
        next_letter_index = gutil.index_by_prob(starting_letter_row)
        # but we want to pick the max only maxs percentage of the time
        next_letter[0] = charnumberings.inv.get(next_letter_index)
        output += next_letter[0]
    return output


for char in charnumberings.inv:
    print(make_sentance(probs, charnumberings.inv.get(char)))


