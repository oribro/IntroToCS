######################################################################
# FILE: tweet.py
# WRITER: Ori Broda, orib, 308043447
# EXERCISE : intro2cs ex7 2013-2014
# Description : This program implements the class "Tweet".
######################################################################

from doctest import run_docstring_examples
# We use this in get_location.
from geo import Position
from datetime import datetime
# We use these in get_words.
from re import sub, findall

# Alphabetical letters only, adjusted for regex usage.
ASCII_LETTERS = "[^a-zA-Z]"
# Constant to discern between words.
SEPERATION = " "

class Tweet:
    def __init__(self, text, time, lat, lon):
        """ Initializes an instance of the type Tweet.

        Args (parameters to initialize):
        -text: a string, the text of the tweet. 
        -time: a datetime object, when the tweet was posted. 
        -lat: a floating-point number, the latitude of the tweet's
        location. 
        -lon: a floating-point number, the longitude of the tweet's
        location."""

        self.__text = text
        self.__time = time
        self.__lat = lat
        self.__lon = lon
        
    def get_words(self):
        """Return the words in a tweet, not including punctuation.
        Returns an ordered list of all words in the tweet.
        """
        # Retreive a substring of the tweet's text using regex's 'sub'.
        # The substring contains ascii letters only - words, converted
        # to lower-case. Create a list of words from the substring
        # using regex's 'findall'.
        return findall(r'\w+', sub(ASCII_LETTERS , SEPERATION, \
                                   self.__text.lower())) 

    def get_text(self):
        """Return the text of the tweet."""
        return self.__text

    def get_time(self):
        """Return the datetime that represents when the tweet was
        posted."""
        return self.__time

    def get_location(self):
        """Return a position (a class, see geo.py) that represents
        the tweet's location."""
        return Position(self.__lat, self.__lon)

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return (self.get_text() == other.get_text() and
                    self.get_location() == other.get_location() and
                    self.get_time() == other.get_time())
        else:
            return False

    def __str__(self):
        """Return a string representing the tweet."""
        return '"{0}" @ {1} : {2}'.format(self.get_text(), 
                                          self.get_location(), 
                                          self.get_time())

    def __repr__(self):
        """Return a string representing the tweet."""
        return 'Tweet({0}, {1}, {2}, {3})'\
               .format(*map(repr,(self.get_text(),
                                  self.get_time(),
                                  self.get_location().latitude(),
                                  self.get_location().longitude())))

    def get_sentiment(self,word_sentiments):
        """ Return a sentiment representing the degree of positive or
        negative sentiment in the given tweet, averaging over all the
        words in the tweet that have a sentiment value.

        Args:
        -word_sentiments: A dictionary that maps words to values
        (between -1 and 1), which represent negative and positive
        feelings.

        Returns the average sentiment or None if none of the words
        have a sentiment.
        """
        # List for saving the sentiment value of words in the tweet.
        sentiment_values = []
        # Go over the words in the tweet
        for word in self.get_words():
            # The word has a sentiment value.
            if word in word_sentiments:
                sentiment_values.append(word_sentiments[word])
        # Some words have sentiment value. Return the average value.
        if len(sentiment_values) > 0:
            return sum(sentiment_values)/len(sentiment_values)
        # None of the words have a sentiment.
        else:
            return None
    
