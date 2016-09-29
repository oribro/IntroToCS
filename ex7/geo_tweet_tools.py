######################################################################
# FILE: geo_tweet_tools.py
# WRITER: Ori Broda, orib, 308043447
# EXERCISE : intro2cs ex7 2013-2014
# Description : This program implements functions that help us
# calculate geographical data regarding states in the U.S and tweets
# incoming from them.
######################################################################

from geo import us_states, Position, geo_distance
from tweet import Tweet

# Constant for resetting a variable for summing.
SUM_RESET = 0
# Indice of the Position of a centroid's polygon.
CENTROID_POSITION = 0
# Indice of the area of a polygon.
AREA = 1

    
def find_centroid(polygon):
    """Finds the centroid of a polygon according to a formula:

    http://en.wikipedia.org/wiki/Centroid #Centroid_of_polygon

    polygon -- A list of positions, in which the first and last are the same

    Returns: 3 numbers; centroid latitude, centroid longitude, and polygon area
    Returns A tuple containing the position of the centroid and the polygon's
    area. If a polygon has 0 area, returns its first position as its centroid.

    >>> p1, p2, p3 = Position(1, 2), Position(3, 4), Position(5, 0)
    >>> triangle = [p1, p2, p3, p1]  # First vertex is also the last vertex
    >>> find_centroid(triangle)
    (Position(3.0, 2.0), 6.0)
    >>> find_centroid([p1, p3, p2, p1])
    (Position(3.0, 2.0), 6.0)
    >>> find_centroid([p1, p2, p1])
    (Position(1.0, 2.0), 0)
    """

    # Variable for summing the X-coordinates, resembling the centroid's
    # latitude 6 times the area of the polygon (see formula). 
    centroid_lat = SUM_RESET
    # Variable for summing the Y-coordinates, resembling the centroid's
    # longitude 6 times the area of the polygon (see formula). 
    centroid_lon = SUM_RESET
    # Variable for computing the area of the polygon. May have
    # a negative sign if the points are numbered in clockwise order.
    area = SUM_RESET
    # Going over the vertices of the polygon.
    for vertex in range(len(polygon)-1):
        # Computing the value of the sigma of the centroid's latitude
        # according to the formula.
        centroid_lat += (Position.latitude(polygon[vertex]) + \
                         Position.latitude(polygon[vertex+1])) * \
                         (Position.latitude(polygon[vertex]) * \
                           Position.longitude(polygon[vertex+1]) - \
                            Position.latitude(polygon[vertex+1]) * \
                            Position.longitude(polygon[vertex]))
        # Computing the value of the sigma of the centroid's latitude
        # according to the formula.
        centroid_lon += (Position.longitude(polygon[vertex]) + \
                         Position.longitude(polygon[vertex+1])) * \
                         (Position.latitude(polygon[vertex]) * \
                          Position.longitude(polygon[vertex+1]) - \
                          Position.latitude(polygon[vertex+1]) * \
                          Position.longitude(polygon[vertex]))
        # Computing the value of the sigma of the polygon's area.
        area += (Position.latitude(polygon[vertex]) * \
                 Position.longitude(polygon[vertex+1]) - \
                 Position.latitude(polygon[vertex+1]) * \
                 Position.longitude(polygon[vertex]))
    # Dividing to get the area of the polygon according to the formula.
    area = area/2
    # Special case: polygon has 0 area (one vertex: a dot). 
    if (area == 0):
        return (polygon[FIRST_POSITION], area)
    else:
        return (Position(centroid_lat/(area*6), centroid_lon/(area*6))\
                , abs(area))
    


def find_center(polygons):
    """Compute the geographic center of a state, averaged over its polygons.

    The center is the average position of centroids of the polygons in
    polygons,    weighted by the area of those polygons.

    Arguments:
    polygons -- a list of polygons

    Returns a position of the center of the state.
    
    >>> ca = find_center(us_states['CA'])  # California
    >>> round(ca.latitude(), 5)
    37.25389
    >>> round(ca.longitude(), 5)
    -119.61439

    >>> hi = find_center(us_states['HI'])  # Hawaii
    >>> round(hi.latitude(), 5)
    20.1489
    >>> round(hi.longitude(), 5)
    -156.21763
    """

    # Variable for computing the sum of the latitude of the centroids
    centroids_lat = 0
    # Variable for computing the sum of the longitude of the centroids
    centroids_lon = 0 
    # Variable for computing the sum of the areas of the polygons
    areas = 0 
    
    for polygon in polygons:
        # Sum the areas of the polygons.
        areas += find_centroid(polygon)[1]
        # Sum the latitude of the centroids.
        centroids_lat += Position.latitude(find_centroid(polygon)\
                                           [CENTROID_POSITION]) * \
                                           find_centroid(polygon)[AREA]
        # Sum the longitude of the centroids.
        centroids_lon += Position.longitude(find_centroid(polygon)\
                                            [CENTROID_POSITION]) * \
                                            find_centroid(polygon)[AREA]

    # Calculate the latitude of the state's center.    
    state_center_lat = centroids_lat / areas
    #  Calculate the longitude of the state's center. 
    state_center_lon = centroids_lon / areas

    return Position(state_center_lat, state_center_lon) 
    

def find_closest_state(state_centers):
    """Returns a function that takes a tweet and returns the name of the state 
    closest to the given tweet's location.

    Use the geo_distance function (already provided) to calculate distance
    in miles between two latitude-longitude positions.

    Arguments:
    tweet -- a tweet abstract data type
    state_centers -- a dictionary from state names to positions.

    >>> state_centers = {n: find_center(s) for n, s in us_states.items()}
    >>> sf = Tweet("Welcome to San Francisco", None, 38, -122)
    >>> nj = Tweet("Welcome to New Jersey", None, 41.1, -74)
    >>> find_state = find_closest_state(state_centers)
    >>> find_state(sf)
    'CA'
    >>> find_state(nj)
    'NJ'
    """
    def find_state(tweet):
        """ Takes a tweet and returns the name of the state 
        closest to the given tweet's location.

        Arguments:
        tweet -- a tweet abstract data type.
        """

        # The position of the tweet
        tweet_location = tweet.get_location()
        # The distance between the tweet and the center of a state.
        distance = None
        # Go over the states in the dictionary
        for state in state_centers.keys():
            # Accounting for a special case for when the distance has
            # no numerical value (we give it a value here).
            if distance is None:
                # Assign state code for closest state.
                state_code = state
                # This is the shortest distance now.
                distance = geo_distance(tweet_location, \
                                        state_centers[state])
            # A closer state is found.
            elif distance > geo_distance(tweet_location, \
                                         state_centers[state]):
                state_code = state
                distance = geo_distance(tweet_location, \
                                        state_centers[state])
        return state_code
    return find_state

def find_containing_state(states):
    """Returns a function that takes a tweet and returns the name of the state 
    containing the given tweet's location.

    Use the geo_distance function (already provided) to calculate distance
    in miles between two latitude-longitude positions.

    Arguments:
    tweet -- a tweet abstract data type
    us_states -- a dictionary from state names to positions.

    >>> sf = Tweet("Welcome to San Francisco", None, 38, -122)
    >>> ny = Tweet("Welcome to New York", None, 41.1, -74)
    >>> find_state = find_containing_state(us_states)
    >>> find_state(sf)
    'CA'
    >>> find_state(ny)
    'NY'
    """
    "*** YOUR CODE HERE ***"
    
def group_tweets_by_state(tweets,find_state):
    """Return a dictionary that aggregates tweets by their nearest state center.

    The keys of the returned dictionary are state names, and the values are
    lists of tweets that appear closer to that state center than any other.

    tweets -- a sequence of tweet abstract data types

    >>> state_centers = {n: find_center(s) for n, s in us_states.items()}
    >>> find_state = find_closest_state(state_centers);
    >>> sf = Tweet("Welcome to San Francisco", None, 38, -122)
    >>> ny = Tweet("Welcome to New York", None, 41, -74)
    >>> ca_tweets = group_tweets_by_state([sf, ny],find_state)['CA']
    >>> ca_tweets
    [Tweet('Welcome to San Francisco', None, 38, -122)]
    """
    # A dictionary of state names and lists of closest tweets.
    tweets_per_state = {}
    for tweet in tweets:
        # The state name is not in the dictionary.
        if find_state(tweet) not in tweets_per_state:
            # Assign a new key - state name to the dictionary with
            # a value- a new list with that tweet inside.
            tweets_per_state[find_state(tweet)] = [tweet]
        # There is a key with that state name in the dictionary
        else:
            # Add that tweet to the existing list of tweets.
            tweets_per_state[find_state(tweet)].append(tweet)
    return tweets_per_state

