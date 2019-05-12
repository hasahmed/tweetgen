Ever wanted your computer to generate more tweets based on a users existing tweets?
Not really? Oh... Well now you can anyway!

You will need to create an application via twitter to get the credentials to run this.
You can find more information here https://developer.twitter.com/apps

After you have gotten your credentials from twitter you will need to put them in
your home directory in a file named `.twitter_auth`.
On Unix-like systems this is ~/.twitter_auth. The format of the file should be as
follows:
```
consumer_key : "your assigned consumer_key"
consumer_secret : "your assigned consumer_secrete"
access_token : "your assigned access_token"
access_token_secret : "your assigned access_token_secret"
```
After you have completed your twitter application registration and put your
auth stuff in ~/.twitter_auth you will need to:
- clone repo, run `pip install tweepy`.
- Run `./make_tweets` to run the program with the defaults (Trumps twitter)
- Run `./make_tweets --help` for usage info
NOTE* This project runs on Python 3
