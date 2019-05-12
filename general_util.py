import random



def index_by_prob(choices):
    r = random.random()
    upto = 0
    for i in range(0, len(choices)):
        if upto + choices[i] >= r:
            return i
        upto += choices[i]
    raise ValueError("This should never be reached")

def weighted_choice(choices):
    r = random.random()
    upto = 0
    for ele in choices:
        if upto + choices[ele] >= r:
            return ele
        upto += choices[ele]
    raise ValueError("This should never be reached")


def get_context(sub_str, string):
    index = string.index(sub_str)
    if index == -1:
        return False
    start_index = index - 10
    if start_index < 0:
        start_index = 0
    end_index = index + 10
    if end_index >= len(string) -1:
        end_index = index
    return string[start_index : end_index]


def print_context(sub_str, tweet_array):
    context_count = 0
    for tweet in tweet_array:
        if sub_str in tweet:
            context_count += 1
            print(get_context(sub_str, tweet))
    if context_count > 0:
        return True


def clean_tweets(tweet_array):
    bad_stuff = {"'", '"'}
    cleaned_tweets = []
    for tweet in tweet_array:
        tmp = ''.join(char for char in tweet if char not in bad_stuff) #remove bad
        tmp = ''.join((lambda word: word + ' ' if word != "&amp;" else "& ")(word) for word in tmp.split())
        tmp = ''.join((lambda word: word + ' ' if word != "\n" else " ")(word) for word in tmp.split())
        tmp = ''.join(word + " " for word in tmp.split() if "http" not in word)
        # print(bad_removed)
        cleaned_tweets.append(tmp)
    return cleaned_tweets


def get_rand_starting_letters(tweet_array, order=5):
    tweet_index = random.randrange(0, len(tweet_array))
    return tweet_array[tweet_index][0:order]

def polish_tail(finished_tweet, trumps_words):
    acceptable_finish = {".", "!"}

    # trim words off the end util hitting a real one
    # note... add a check to see if the word is a stop_word as well
    words = finished_tweet.split()
    for i, word in reversed(list(enumerate(words))):
        if word in trumps_words:
            tmp_tweet = ''
            for j in range(0, i + 1):
                tmp_tweet += words[j] + " "
            finished_tweet = tmp_tweet
            break

    finished_tweet = finished_tweet.strip()
    #need to check to see if -1 is out of range of string
    if len(finished_tweet) > 1:
        last_char = finished_tweet[-1]
        if last_char not in acceptable_finish:
            finished_tweet += "!"
    return finished_tweet

def get_percentage_of_one_char(string):
    chars_to_percent = 100.0 / len(string) # the number of characters that equal a percentage of the tweet
    return chars_to_percent

def get_percentage_of_one_word(string):
    if(len(string.split())) == 0:
        return 100
    words_to_percent = 100.0 / len(string.split()) # the number of characters that equal a percentage of the tweet
    return words_to_percent

def longer_first(str1, str2):
    if len(str1) > len(str2):
        return str1, str2
    return str2, str1

def index_of_first_occuring_word(gend_tweet, tweet):
    tweet_arr = tweet.split()
    for word in gend_tweet.split():
        try:
            return tweet_arr.index(word)
        except:
            pass
    return -1


def test_sentence_too_much_overlap(gend_words, all_tweets, max_overlap_percentage=70):
    gend_words_percentage = get_percentage_of_one_word(gend_words)
    for tweet in all_tweets:
        percent_of_consecutive_overlap = 0.0
        starting_index = index_of_first_occuring_word(gend_words, tweet)
        if starting_index != -1:
            sorted_by_length = longer_first(gend_words, tweet)
            longer = sorted_by_length[0]
            shorter = sorted_by_length[1]
            for i in range(starting_index, len(shorter.split())): #loop through the longer of the two
                if longer[i] == shorter[i]:
                    percent_of_consecutive_overlap += gend_words_percentage
                else:
                    percent_of_consecutive_overlap = 0.0
                if percent_of_consecutive_overlap >= max_overlap_percentage:
                    return "generated tweet: %s" % gend_words, "original: %s" % tweet
    return False

