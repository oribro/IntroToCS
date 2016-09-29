######################################################################
# FILE: oneliners.py
# WRITER: Ori Broda, orib, 308043447
# EXERCISE : intro2cs ex6 2013-2014
# Description : This program implements the usage of one line
# functions (or at least shortest as possible).
######################################################################

# See README's special comments for details regarding imports
from random import choice
from string import ascii_lowercase
from re import split

# Constant for odd string length
ODD = 1
# Constant for even string length
EVEN = 0
# Constant included in reversing the string using slice
REVERSE = -1
REGEX_WORD = '\W+'
# Whitespaces
EMPTY_STRING = ""
UNDERSCORE = '_'


def is_two_palindrome(string):
    """ This function checks if a given string is comprised of 2
    palindromes (= reversing them does not change them) of the
    same length. The palindromes don't have to be related.
    If the string is of even length, each palindrome comprise
    half of the string. If of odd length, we check if a
    middle character seperates between 2 palindromes.

    Args:
    -string: String of any length. May include punctuation,
    spaces, and other symbols.

    Returns True if found 2 palindromes and False if not."""

    # Checks if the string is of even length and its sub-strings
    # remain the same when reversed
    return (len(string)%2 == EVEN and string[:len(string)//2] == \
            string[:len(string)//2][::REVERSE] and \
            string[len(string)//2:] == string[len(string)//2:][::REVERSE]) \
            or (len(string)%2 == ODD and string[:len(string)//2] == \
            string[:len(string)//2][::REVERSE] and \
            string[(len(string)//2 + ODD):] == \
            string[(len(string)//2 + ODD):][::REVERSE])
            # Checks if the string is of odd length and its sub-strings,
            # seperated by a character, remain the same when reversed.

def uni_sort(list_a, list_b):
    """ The function combines two unsorted lists of integers
    into one sorted list. The output list is sorted in ascending order
    (from smaller to larger). The function handles duplicates:
    If a certain number appears more than once, it will appear only
    once in the output list.

    Args:
    -list_a: First unsorted list of integers.
    -list_b: Second unsorted list of integers.

    Returns A sorted list of integers without duplicates."""

    # Combining the two lists into one sorted list.
    merged_list = sorted(list_a + list_b)
    # Checks if the current number is found again in the remaining
    # part of the list and adding it if no duplicate is found.
    return [merged_list[index] for index,duplicate in \
            enumerate(merged_list) if duplicate not in \
            merged_list[index+1:]]

def dot_product(vector_a, vector_b):
    """ The function returns the dot product of two vectors,
    represented as lists.

    Args:
    -vector_a: First list (representing vector) of integers.
    -vector_b: Second list (representing vector) of integers.

    Returns an integer – the dot product of the two input vectors."""

    # Going over the lists simultaneously, multiplying every 2
    # values with the same index and summing the list of
    # multiplications, resulting in the dot product.
    return sum([index_a*index_b for index_a, index_b \
                in zip(vector_a, vector_b)])

def list_intersection(list_a, list_b):
    """ The function gets as input two lists of integers and returns
    a new list sorted in ascending order containing the common integers
    between the lists.

    Args:
    -list_a: First unsorted list of integers.
    -list_b: Second unsorted list of integers.

    Returns A list of integers sorted in ascending order containing
    those integers that appear in both input lists."""

    # Using set's special operator '&' we can find the common
    # values to the lists, then create a list and sort it.
    return sorted(list(set(list_a) & set(list_b)))

def list_difference(list_a, list_b):
    """ The function is similar to list_intersection.
    Given two input lists of integers, the function returns a list
    sorted in ascending order. The output list contains exactly
    those integers that appear in just one of the input lists.

    Args:
    -list_a: First unsorted list of integers.
    -list_b: Second unsorted list of integers.

    Returns A list of integers sorted in ascending order containing
    those integers that appear in exactly one of the input lists."""

    # Using set's special operator '^' we can find the integers that
    # appear only in one list, then create a list and sort it.
    return sorted(list(set(list_a) ^ set(list_b)))

def random_string(number):
    """ The function generates a random string of a given length.
    The string contains lower-case letters only.

    Args:
    -number: An integer denoting the length of the output random string.

    Returns A random string of the length: number."""

    # Random a lower-case letter and build a string from it.
    # Repeat -number- times.
    return EMPTY_STRING.join(choice(ascii_lowercase) \
                             for index in range(number))

def word_mapper(string_input):
    """ The function takes a string and returns a dictionary mapping
    from the words comprising the string. Each entry in the dictionary
    appears once and is followed by the number of times the entry
    appears in the string. We consider punctuation marks as whitespaces,
    as they are not considered words.

     Args:
    -string_input: A string of words separated by whitespace and/or
    punctuation marks.
    
    Returns a dictionary containing a mapping between words and the
    number of times they appear in the original input string."""

    # Creates a list of lower-cased words from the string, using regex.
    # We discern between words and whitespaces by using 'REGEX_WORD'.
    word_list = split(REGEX_WORD,string_input.lower())
    # Returns a dictionary mapping by counting each word's appearances
    # using the built-in 'count' function of a list, no whitespaces.
    return {entry:word_list.count(entry) for entry in set(word_list) \
            if entry != EMPTY_STRING and entry != UNDERSCORE}

def gimme_a_value(f_function, x0):
    """ This function creates a generator that computes a sequence
    of values by applying an input function. The generator runs
    endlessly.

     Args:
    -f_function: Some input function.
    -x0: An initial value.

    Returns The next element in the sequence generated by applying to
    the previous element. The first returned value is x0."""
    
    while True:
        yield x0
        x0 = f_function(x0)





        
    
