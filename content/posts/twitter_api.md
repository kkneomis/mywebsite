title: Using the Twitter API to retweet content
date: 2017-05-06
image: twitter.png

The first hackathon I attended was a Startup Weekend hackathon in Washigton D.C. It occurred as a series with various hackathons occuring at the same time in various cities. There was a hashtag was going on between all the various cities. Surprisingly, DC was actually in second place even though we only had about 100 people competiting, 20 of whom were actually tweeting. The reason was that someone at the hackathon https://twitter.com/kevinohashi?lang=en has a bot running that would retweet all tweets with the hashtag of our city. We would had won too, except there was another meddling city that has a bot running longer than we did.

In this guide, I will show you how to create a twitter bot that will retweet all of a user's tweets, and a bot that will retweet all tweets with a certain hastag.

### What you will need
1. A twitter developer account
2. A python editor
3. Your thinking hat

### Getting Started

The first thing you want to do is create an application. Go to https://dev.twitter.com/ and log in. You probably have to confirm a phone number for your twitter account before creating an app.

Click My apps > Create New App > Fill in all the required fields to create your Twitter app.

Once your application has been created, you want to navigate to the "Keys and Acess Tokens" tabs and generate your acess tokens. You will need all the keys from this page in order to use twitter's api.

### Introducing Tweepy

Tweepy is a python library that can use used to access twitter's api. http://tweepy.readthedocs.io/
If you do not already have it installed, run the following command in your terminal.

    pip install tweepy

Create a file called tweet.py using a code editor (like pycharm) and insert the following. Now replace al the keys with your own keys that you just got.

    #!/usr/bin/env python
    # -*- coding: utf-8 -*-

    import tweepy, time, sys

    argfile = str(sys.argv[1])

    #enter the corresponding information from your Twitter application:
    CONSUMER_KEY = '1234abcd...'#keep the quotes, replace this with your consumer key
    CONSUMER_SECRET = '1234abcd...'#keep the quotes, replace this with your consumer secret key
    ACCESS_KEY = '1234abcd...'#keep the quotes, replace this with your access token
    ACCESS_SECRET = '1234abcd...'#keep the quotes, replace this with your access token secret
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
    api = tweepy.API(auth)


### Retweeting content from one user

The first thing we need to do is actually get our user. We can do this using the user's Twitter handle. Add the following line to your file within the code editor:

    user = api.get_user('realSimDawg')
    print user.screen_name

If you run the file, it should now print the user's name. Now we actually want the get the user's tweets and retweet them. In the following lines, we will get all the users tweets, loop through them, and retween each of them.

    tweets = api.user_timeline(screen_name = user.screen_name,count=200)
    for tweet in tweets:
      try:
        api.retweet(tweet.id)
      except:
        # if we get an error
        print "I probably retweeted this already"


Your file should now look like this

    #!/usr/bin/env python
    # -*- coding: utf-8 -*-

    import tweepy, time, sys

    argfile = str(sys.argv[1])

    #enter the corresponding information from your Twitter application:
    CONSUMER_KEY = '1234abcd...'#keep the quotes, replace this with your consumer key
    CONSUMER_SECRET = '1234abcd...'#keep the quotes, replace this with your consumer secret key
    ACCESS_KEY = '1234abcd...'#keep the quotes, replace this with your access token
    ACCESS_SECRET = '1234abcd...'#keep the quotes, replace this with your access token secret
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
    api = tweepy.API(auth)

    user = api.get_user('realSimDawg')

    tweets = api.user_timeline(screen_name = user.screen_name,count=200)
    for tweet in tweets:
      try:
        api.retweet(tweet.id)
      except:
        # if we get an error
        print "I probably retweeted this already"


### Retweeting content from a hashtag

This is for the most part the same. First we will set some variables.

    searchQuery = '#GradSZN'  # this is what we're searching for
    tweetsPerQry = 100  # this is the max the API permits

Now we will use a one-liner to actually get the tweets and then retweet them.

    new_tweets = api.search(q=searchQuery, count=tweetsPerQry,
                                            since_id=None)

    for tweet in new_tweets:
      print tweet.text
      try:
        api.retweet(tweet.id)
      except:
        print "I already retweeted this"

Your final file should look something like this.

    #!/usr/bin/env python
    # -*- coding: utf-8 -*-

    import tweepy, time, sys

    argfile = str(sys.argv[1])

    #enter the corresponding information from your Twitter application:
    CONSUMER_KEY = '1234abcd...'#keep the quotes, replace this with your consumer key
    CONSUMER_SECRET = '1234abcd...'#keep the quotes, replace this with your consumer secret key
    ACCESS_KEY = '1234abcd...'#keep the quotes, replace this with your access token
    ACCESS_SECRET = '1234abcd...'#keep the quotes, replace this with your access token secret
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
    api = tweepy.API(auth)

    user = api.get_user('realSimDawg')

    tweets = api.user_timeline(screen_name = user.screen_name,count=200)
    for tweet in tweets:
      try:
        api.retweet(tweet.id)
      except:
        # if we get an error
        print "I probably retweeted this already"

    searchQuery = '#GradSZN'  # this is what we're searching for
    tweetsPerQry = 100  # this is the max the API permits

    new_tweets = api.search(q=searchQuery, count=tweetsPerQry,
                                            since_id=None)

    for tweet in new_tweets:
      print tweet.text
      try:
        api.retweet(tweet.id)
      except:
        print "I already retweeted this"


You can learn more [by reading the Tweepy docs](http://tweepy.readthedocs.io/en/v3.5.0/streaming_how_to.html), [or using the guide I followed](https://dototot.com/how-to-write-a-twitter-bot-with-python-and-tweepy/), [or the other guide I followed.](https://www.karambelkar.info/2015/01/how-to-use-twitters-search-rest-api-most-effectively./)