######################################################################
# FILE: NonRecursiveMystery.py
# WRITER: Ori Broda, orib, 308043447
# EXERCISE : intro2cs ex5 2013-2014
# Description : This program produces the same outcome
# as the original function 'mystery_computation(number)' but without
# using recursion.
######################################################################

# Constant for starting the search (cannot divide by zero).
START = 1
# Is divided
DIVIDED = 0
VAR_RESET = 0

def mystery_computation(number):
    """ This function takes a number, finds its dividers and
    summing them.

    Args:
    -number: an integer to sum its dividers.

    Returns the sum of the dividers of the given number -
    an integer."""

    # Variable to sum number's dividers
    sum_dividers = VAR_RESET
    for divider in range(START, number):
        # Found a divider
        if number % divider == DIVIDED:
            sum_dividers += divider
    return sum_dividers
