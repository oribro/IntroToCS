######################################################################
# FILE: AlignDNA.py
# WRITER: Ori Broda, orib, 308043447
# EXERCISE : intro2cs ex5 2013-2014
# Description : This program checks the similarity between
# two given DNA strands.
######################################################################

# Score value for 2 similar characters.
MATCH_VALUE = 1
# Addition for strand index variable.
INCREMENT = 1
# Constant for slicing the strand's first character.
REST = 1
# The returned straned number one in the returned tuple.
STRAND_ONE = 1
# Score value for 2 different characters.
MISMATCH_VALUE = -1
# Score value for a gap in the strand.
GAP_VALUE = -2
# Dash for length aligning.
GAP_SIGN = "-"
VAR_RESET = 0
# Constant for base case of the recursion.
EMPTY_STRING = 0
# The returned score in the returned tuple.
SCORE_INDEX = 0
# Constant for adding the sliced strand's first character.
FIRST_CHAR = 0
# The returned straned number two in the returned tuple.
STRAND_TWO = 2

def get_alignment_score(strand_one, strand_two, match=MATCH_VALUE,
                        mismatch=MISMATCH_VALUE, gap=GAP_VALUE):
    """ A function that takes 2 aligned DNA strands (they have the same
    length), and calculates the score of the alignment which is
    determined by the similarity between every 2 aligned characters,
    one in each strand, and given score values. Dash ("-") represents a
    character that is missing but we cannot determine it (gap) and
    is used to align the strands.

    Args:
    -strand_one: Aligned DNA strand number one - a string of the
    characters 'A','C','G','T' and a gap "-".
    -strand_two: Aligned DNA strand number two - a string of
    the characters: 'A','C','G','T' and a gap "-".
    -match: optional score value for 2 similar characters - an integer
    with default value of 1.
    -mismatch: optional score value for 2 different characters -
    an integer with default value of -1.
    -gap: optional score value for a gap in the strand - an integer
    with default value of -2.

    The function returns the score of the alignment - an integer."""
    
    # Variable for computing the alignment's score.
    score = VAR_RESET
    # Variable for the index of strand number two.
    strand_two_index = VAR_RESET
    for strand_one_index in range(len(strand_one)):
        if strand_one[strand_one_index] == strand_two[strand_two_index]:
            score += match
        elif strand_one[strand_one_index] == GAP_SIGN or strand_two[
            strand_two_index] == GAP_SIGN:
            score += gap
        else:
            score += mismatch
        strand_two_index += INCREMENT
    return score

def get_best_alignment_score(strand_one, strand_two, match=MATCH_VALUE,
                             mismatch=MISMATCH_VALUE, gap=GAP_VALUE):
    """ A function that takes 2 unaligned DNA strands.
    The function calculates the maximal score of ALL
    possible strand alignments and aligns the strands accordingly.
    The implementation of this function is recursive as follows:
    We take the first character of each strand - two chars,
    and slice them, calling the function over and over again with
    the remaining strands. It has 3 cases:
    1) The length of the strands is identical.
    2) Strand number one is longer than the other.
    3) Strand number two is longer than the other.
    When there is no strand left to slice,
    we will add gaps as a function of the other strand's length
    in order to start the computations.
    (If the length is identical there will be no added gaps).
    The recursion will then begin "climbing" the tree structure,
    looking for the best alignment- one that will result in a
    maximum score value by comparing every 2 characters of the strands.
    The function will compensate for the slicing of the strands by
    adding the first 2 char's (or gap) score and the first 2 chars or
    gap to the strands in the adequate places.
    By the time the recursion has reached the top of the tree again,
    it would have the best alignment that would produce the highest
    possible score for the 2 given strands, accounting for the given
    scoring values.

    Args:
    -strand_one: Unaligned DNA strand number one - a string of the
    characters 'A','C','G','T'.
    -strand_two: Unaligned DNA strand number two - a string of
    the characters: 'A','C','G','T'.
    -match: optional score value for 2 similar characters - an integer
    with default value of 1.
    -mismatch: optional score value for 2 different characters -
    an integer with default value of -1.
    -gap: optional score value for a gap in the strand - an integer
    with default value of -2.

    The function returns a tuple of the highest score of alignment
    between the strands and the two aligned strands:
    tuple = (highest_score, strand_number_one, strand_number_two). """
    
    
    # Base case: strand one is empty. return gaps in strand one until
    # identical length acheived and return their score value.
    if len(strand_one) == EMPTY_STRING:
        return (gap*len(strand_two), GAP_SIGN*len(strand_two),
                strand_two)
    # Base case: strand two is empty. return gaps in strand two until
    # identical length acheived and return their score value.
    if len(strand_two) == EMPTY_STRING:
        return (gap*len(strand_one), strand_one,
                GAP_SIGN*len(strand_one))

    # The current two letters are identical.
    if strand_one[FIRST_CHAR] == strand_two[FIRST_CHAR]:
        first_score = match
    # There is a gap in one of the strands (cannot be in both).   
    elif strand_one[FIRST_CHAR] == GAP_SIGN or strand_two[
        FIRST_CHAR] == GAP_SIGN:
        first_score = gap
    # The current two letters are different.  
    elif strand_one[FIRST_CHAR] != strand_two[FIRST_CHAR]:
        first_score = mismatch

    # Case 1: identical length. No gaps needed.      
    no_gap = get_best_alignment_score(
        strand_one[REST:], strand_two[REST:], match, mismatch, gap)
    # Case 2: strand one is longer. Add gaps to strand two.
    strand_one_longer = get_best_alignment_score(
        strand_one[REST:], strand_two, match, mismatch, gap)
    # Case 3: strand two is longer. Add gaps to strand one.
    strand_two_longer = get_best_alignment_score(
        strand_one, strand_two[REST:], match, mismatch, gap)
    # Add the score of the first 2 chars to the accumulated score.
    no_gap_score = first_score + no_gap[SCORE_INDEX]
    # Add gap score value to the accumulated score.
    strand_two_longer_score = gap + strand_two_longer[SCORE_INDEX] 
    strand_one_longer_score = gap + strand_one_longer[SCORE_INDEX]
    # Finding the highest score of all 3 cases.
    max_score = max(no_gap_score, strand_one_longer_score,
                    strand_two_longer_score)
    # Case 1 is the best alignment. Add the sliced characters for a
    # complete alignment.
    if max_score == no_gap_score:
        return (no_gap_score, strand_one[FIRST_CHAR]+no_gap[STRAND_ONE],
                strand_two[FIRST_CHAR]+no_gap[STRAND_TWO])
    # Case 2 is the best alignment. Add the sliced characters and
    # needed gaps for a complete alignment.
    elif max_score == strand_one_longer_score:
               return (strand_one_longer_score, strand_one[FIRST_CHAR]+
                strand_one_longer[STRAND_ONE],
                GAP_SIGN+strand_one_longer[STRAND_TWO])
    # Case 3 is the best alignment. Add the sliced characters and
    # needed gaps for a complete alignment.
    elif max_score == strand_two_longer_score:
        return (strand_two_longer_score, GAP_SIGN+
                strand_two_longer[STRAND_ONE],
                strand_two[FIRST_CHAR]+strand_two_longer[STRAND_TWO])
        
    
