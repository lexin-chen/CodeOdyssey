# mytwitterbot.py
# IAE 101, Fall 2020
# Project 04 - Building a Twitterbot
# Name: Lexin Chen    
# netid: lexchen
# Student ID: 111763005

import sys
import time
import simple_twit

def main():
    # This call to simple_twit.create_api will create the api object that
    # Tweepy needs in order to make authenticated requests to Twitter's API.
    # Do not remove or change this function call.
    # Pass the variable "api" holding this Tweepy API object as the first
    # argument to simple_twit functions.
    api = simple_twit.create_api()
    simple_twit.version()
    
##    # Project 04 Exercises
#### Exercise 1 - Get and print 10 tweets from your home timeline
##    my_tweets = simple_twit.get_home_timeline(api,10)
##    for tweet in my_tweets:
##        print(tweet.id)
##        print(type(tweet.user))
##        print(tweet.author.name)
##        print(tweet.full_text)
##        print()
####    # Exercise 2 - Get and print 10 tweets from another user's timeline
##    their_tweets = simple_twit.get_user_timeline(api, 'ScienceMagazine', 10)
##    for tweet in their_tweets:
##        print(tweet.id)
##        print(type(tweet.user))
##        print(tweet.author.name)
##        print(tweet.full_text)
##        print()
##    # Exercise 3 - Post 1 tweet to your timeline.
##    my_tweet = simple_twit.send_tweet(api, "If you can be any animal, what would you be?")
##    print(type(my_tweet))
##    # Exercise 4 - Post 1 media tweet to your timeline.
##    simple_twit.send_media_tweet(api, text= "aesthetics is strategic. ", filename= "runaway.jpg")





# YOUR BOT CODE BEGINS HERE

import tweepy
auth = tweepy.OAuthHandler("CONSUMER_KEY", "CONSUMER_SECRET")
auth.set_access_token("ACCESS_TOKEN", "ACCESS_TOKEN_SECRET")
api = simple_twit.create_api()


#bot 1

mentions = api.mentions_timeline()

for mention in mentions:
    print(str(mention.id) + '-' + mention.text)
    if 'goodday' in mention.text.lower():
        print('found and responding...')
        api.update_status('@' + mention.user.screen_name + '#goodday to you too, bless you', mention.id)


#bot 2

import datetime
new_years = datetime.date(2021, 1, 1) - datetime.date.today()
new_year = str(new_years)
api.update_status("2021 New Years is in " + new_year.strip("0:") + "happy holidays! :)")

   




    
# end def main()

if __name__ == "__main__":
       main()
