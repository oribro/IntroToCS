######################################################################
# FILE: nation_mood.py
# WRITER: Ori Broda, orib, 308043447
# EXERCISE : intro2cs ex7 2013-2014
# Description : This program uses functions to calculate data
# about tweets in their states in the U.S.
######################################################################

from data import load_tweets
from tweet import Tweet 
from geo_tweet_tools import group_tweets_by_state

RESET_VALUE = 0
HOURS_A_DAY = 24

def most_talkative_state(tweets,find_state):
    """Return the state that has the largest number of tweets containing term.
    >>> state_centers = {n: find_center(s) for n, s in us_states.items()}
    >>> tweets = load_tweets('texas')
    >>> find_state = find_closest_state(state_centers);
    >>> most_talkative_state(tweets,find_state)
    'TX'
    >>> tweets = load_tweets('sandwich')
    >>> most_talkative_state(tweets,find_state)
    'NJ'
    """
    # A dictionary with the names of the states and their lists of tweets.
    tweets_per_state = group_tweets_by_state(tweets, find_state)
    # The highest number of tweets for a state.
    max_tweets = RESET_VALUE
    for state in tweets_per_state.keys():
        # Found a state with more tweets.
        if max_tweets < len(tweets_per_state[state]):
            # This is the state with the most tweets now.
            max_tweets = len(tweets_per_state[state])
            # The code of the most talkative state.
            state_code = state
    # No states are 'talking'.
    if max_tweets == RESET_VALUE:
        return None
    else:
        return state_code
    


def average_sentiments(tweets_by_state,word_sentiments):
    """Calculate the average sentiment of the states by averaging over all
    the tweets from each state. Return the result as a dictionary from state
    names to average sentiment values (numbers).

    If a state has no tweets with sentiment values, leave it out of the
    dictionary entirely.  Do NOT include states with no tweets, or with tweets
    that have no sentiment, as 0.  0 represents neutral sentiment, not unknown
    sentiment.

    tweets_by_state -- A dictionary from state names to lists of tweets
    """
    # A dictionary for each state and it's average sentiment.
    mood_of_the_nation = {}
    for state in tweets_by_state.keys():
        # Create a new list of tweet sentiments for each state.
        mood_of_the_nation[state] = []
        for tweet in tweets_by_state[state]:
            # The current tweet has a sentiment value
            if tweet.get_sentiment(word_sentiments) is not None:
                # Add the sentiment to the list of sentiments.
                mood_of_the_nation[state].append(tweet.get_sentiment\
                                                 (word_sentiments))
        # There are sentiment values for the tweets of the state
        if len(mood_of_the_nation[state]) != 0:
            # Calculate the average sentiment of the state.
            mood_of_the_nation[state] = sum(\
                mood_of_the_nation[state])/len(mood_of_the_nation[state])
        # No sentiments for that state.
        elif mood_of_the_nation[state] == []:
            # We do not include that kind of states, so we delete
            # the key from the dictionary (along with the value).
            del mood_of_the_nation[state] 

   
    return mood_of_the_nation
            
        

def group_tweets_by_hour(tweets):
    """Return a list of lists of tweets that are gouped by the hour 
    they were posted.

    The indexes of the returned list represent the hour when they were posted
    - the integers 0 through 23.

    tweets_by_hour[i] is the list of all
    tweets that were posted between hour i and hour i + 1. Hour 0 refers to
    midnight, while hour 23 refers to 11:00PM.

    To get started, read the Python Library documentation for datetime 
    objects:
    http://docs.python.org/py3k/library/datetime.html#datetime.datetime

    tweets -- A list of tweets to be grouped
    """
    # Dictionary for sorting tweets by their posting hour.
    hours_dict = {}
    for hour in range(HOURS_A_DAY):
        # Create a list for every hour.
        hours_dict[hour] = []
    for tweet in tweets:
        # Add the tweet to the list in it's matched posting hour.
        hours_dict[tweet.get_time().hour].append(tweet)
    # Return a list of lists of tweets
    return [hours_dict[keys] for keys in hours_dict]
    
        
    
        
    


