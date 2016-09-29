######################################################################
# FILE: hzlib.py
# WRITER: Ori Broda, orib, 308043447
# EXERCISE : intro2cs ex9 2013-2014
# Description : This module contains several function for compress and
# decompress data, using the Huffman code algorithm.
######################################################################

from collections import Counter
from bisect import bisect

MAGIC = b"i2cshcfv1"
# The Character induce in the tree.
CHARACTER = 0
# The code induce in the codebook.
BIN_CODE = 1
# The number of the times the character appeared (induce).
APPEARANCES = 1
# The first tuple of the tree which contains all its characters.
FIRST = 0
BINARY_ZERO = '0'
BINARY_ONE = '1'
BINARY_CONVERSION = 2
# The fixed length of bit sequence.
LENGTH_OF_SEQUENCE = 8
MAXIMUM_BYTES = 256
# Induce for the values of the codebook dictionary.
DICT_VALUE = 1
# Induce for the length of the binary code.
LENGTH = 0
# Induce for the right parts in the tree.
RIGHT = 1
# Induce for the left parts in the tree.
LEFT = 0

def symbol_count(data):
    """ This function counts how many times a character appears in a
    a string.

    Args:
    -data: a string of characters.

    Returns a dictionary in which the key is a character in the string
    and the value is the number of it's appearances."""
    
    return Counter(data)

def make_huffman_tree(counter):
    """ This function builds a special version of the huffman tree,
    such that the tree is made of tuples instead of binTree nodes.

    Args: 
    -counter: The dictionary from the previous function.
    
    Returns a tuple of tuples of characters represnting the huffman tree."""
    
    # Data container (list) for the tuples of the tree.
    tuples = []
    # Checking for legal input.
    if counter == {}:
        return None
    # Create a tuple for each character.
    for character in counter:
        tuples.append((character, counter[character]))
    # Sort the tuples by the characters.
    tuples.sort(key=lambda n: n[CHARACTER])
    # Reverse the list to match the requirement of numbers in "natural
    # order".
    tuples.reverse()
    # Sort the tuples by the character's number of appearances.
    tuples.sort(key=lambda n: n[APPEARANCES])
    # Build the tree
    while len(tuples) > 1:
        # Extract the two nodes with most counts
        first_tuple = tuples.pop(FIRST) # Most frequent char
        second_tuple = tuples.pop(FIRST) # Second-most frequent char
        # New tuple
        characters = (second_tuple[CHARACTER], first_tuple[CHARACTER])
        # Its count
        appearances = first_tuple[APPEARANCES] + second_tuple[APPEARANCES] 
        # Create a parent of the two extracted nodes
        parent = (characters, appearances)
        # Find the index where to insert the new node
        appearances_list = [n[APPEARANCES] for n in tuples]
        insert_place = bisect(appearances_list, appearances)
        tuples.insert(insert_place, parent)
    return tuples[FIRST][CHARACTER]

def build_codebook(huff_tree):
    """ This functions builds a codebook for the tree, with binary
    numbers representing each character.

    Args:
    -huff_tree: The tree returned from the previous function.

    Returns: A dictionary with mapping from character to a tuple
    containing its code and the length of the code."""

    # A new dictionary.
    codebook = {}
    # Checking for legal tree.
    if huff_tree is None:
        return codebook
    def recursive_codebook(huff_tree, code):
        """ This functions implements a recursion to go over the tree.

        Args:
        -huff_tree: The tree returned from the previous function.
        -code: The binary code for the characters of the tree.

        Returns: None, as it goes over the branches of the tree."""
        # We start with no binary code, and as we advance in the tree,
        # '0' will be added to the code for left branches, and '1'
        # for right branches.
        
        # The tree has one leaf.
        if type(huff_tree) is not tuple and code is "":
            # Assign tuple to that dictionary key.
            codebook[huff_tree] = (1,0)
            return None
        # Base case:
        # We reached a leaf.
        if type(huff_tree) is not tuple :
            # By that time we have the full code for that leaf.
            # Convert to decimal and consider the length of the binary code.
            codebook[huff_tree] = (len(code), int(code, BINARY_CONVERSION))
            return None
        # Go over the left branches of the tree.
        recursive_codebook(huff_tree[LEFT], code + BINARY_ZERO)
        # Go over the right branches of the tree.
        recursive_codebook(huff_tree[RIGHT], code + BINARY_ONE)
    # Call for the recursion.
    recursive_codebook(huff_tree, "")
    return codebook 

def build_canonical_codebook(codebook):
    """ The function constructs a canonical codebook based on
    the length of the codes of the characters.

    Args:
    -codebook: The codebook returned from the previous function.

    Returns a dictionary, the canonical codebook."""


    # Empty dictionary.
    canonical_codebook = {}
    # Checking for legal input.
    if codebook is None:
        return canonical_codebook
    # List for the values and keys of the dictionary.
    codebook_list = list(codebook.items())
    # Sort by character.
    codebook_list.sort(key=lambda n: n[CHARACTER])
    # Sort by length.
    codebook_list.sort(key=lambda n: n[DICT_VALUE][LENGTH])
    for character in codebook_list:
        if (canonical_codebook == {}):
            code_int_value = 0
        else:
            # The decimal value of the code.
            code_int_value = save_last[BIN_CODE] + 1
            # The lengths of the current code and the previous one are
            # different. We will add 0 to match the length.
            if character[DICT_VALUE][LENGTH] != save_last[LENGTH]:
                code_int_value = int(str(bin(save_last[BIN_CODE]+1)[2:])+ \
                                     BINARY_ZERO,BINARY_CONVERSION)
                
        canonical_codebook[character[LENGTH]] = \
                        (character[DICT_VALUE][LENGTH], code_int_value)
        # Save the previous length to compare with the current.
        save_last = canonical_codebook[character[LENGTH]]
    return canonical_codebook
        
        
        
    

def build_decodebook(codebook):
    """ The function switches between keys and values.

    Args: codebook: The codebook from the previous function.

    Returns the switched dictionary."""
    
    return dict([[value,key] for key, value in codebook.items()])

def compress(corpus, codebook):
    """ The function returns an iterator which goes over the coded values
    of the corpus. Corpus is a sequence of characters.
    Convert chars to bits."""
    
    for character in corpus:
        # The coded character is found in the corpus.
        if character in codebook.keys():
            # Convert the binary code to a usuable bit sequence.
            temp_bits = bin(codebook[character][1])[2:]
            # Variable for the length of the code.
            code_length = codebook[character][0]
            bits = BINARY_ZERO * (code_length-len(temp_bits)) + temp_bits
            for bit in bits:
                yield int(bit)
                
def decompress(bits, decodebook):
    """ The function converts bits to chars using decodebook.

    Args:
    -bits: A sequence of bits from the previous function.
    -decodebook: The dictionary from the 'build_decodebook' function.
    
    Returns an iterator which goes over all original chars
    which were coded to binary values. """
    
    # A variable to help in converting to chars.
    temp_bits = ''
    for bit in bits:
        temp_bits += str(bit)
    key = ''
    for bit in temp_bits:
        key += str(bit)
        temp_bits[0:1]
        if (len(key),int(key, BINARY_CONVERSION)) in decodebook.keys():
            yield decodebook[(len(key),int(key, BINARY_CONVERSION))]
            key = ''
    

def pad(bits):
    """ The function converts bit values to byte values and returns
    an iterator which goes over them. We add zeros to match length
    and perform the conversion."""

    # A variable to help in the conversion.
    temp_bits = ''
    for bit in bits:
        temp_bits += str(bit)
    remaining_length = (LENGTH_OF_SEQUENCE - len(temp_bits) %\
                        LENGTH_OF_SEQUENCE)
    temp_bits += BINARY_ONE
    for i in range(remaining_length -1):
        temp_bits += BINARY_ZERO
    counter = 0
    # String of bits.
    byte = ''
    # Convert bits to byte.
    for bit in temp_bits:
        counter += 1
        byte += str(bit)
        if counter == LENGTH_OF_SEQUENCE:
            yield int(byte, BINARY_CONVERSION)
            byte = ''
            counter = 0

def unpad(byteseq):
    """ The function takes a sequence of numbers which were converted to bytes
    using pad. The function returns the original sequences before they were
    converted to bytes (removes the zeros and one)"""
    byteseq = list(byteseq)
    original_code = ""
    # Do the opposite process of that performed in pad in order
    # to acheive bytes to bits.
    for value in byteseq:
        current_value = (LENGTH_OF_SEQUENCE-len(bin(value)[2:]))*BINARY_ZERO\
                        + str(bin(value))[2:]
        original_code += current_value
    # We stop when we reach '1'.
    while original_code[-1] != BINARY_ONE:
        original_code = original_code[:-1]

    original_code = original_code[:-1]

    for value in original_code:
        yield int(value)
        
def join(data, codebook):
    """ This function returns an iterator that goes over the byte values
    in the dictionary codebook"""
    
    for value in range(MAXIMUM_BYTES):
        # The value is in codebook
        if value in codebook:
            yield codebook[value][LENGTH]
        else:
            yield 0    
    for byte in data:
        yield byte

def split(byteseq):
    """ The function works as the opposite of 'join'. It returns
    a tuple in which the first value is a canonical table and the
    second value of the tuple is an iterator which goes over the rest
    of byteseq values (as bytes)."""

    byteseq_list = list(byteseq)
    # Create an empty list for data.
    bytes_data = []
    # An empty dictionary for data.
    data_dictionary = {}
    for value in range(MAXIMUM_BYTES):
        if (byteseq_list[value] != 0):
            # Add the value to the dictionary
            data_dictionary[value] = (byteseq_list[value],0)
    # Use the function we implemented earlier to build a canonical
    # codebook from data dictionary        
    codebook = build_canonical_codebook(data_dictionary)
    for value in range(MAXIMUM_BYTES, len(byteseq_list)):
        # Add value from byteseq to bytes data list
        bytes_data.append(byteseq_list[value])
    # Make iterator for bytes data
    bytes_data = (value for value in bytes_data)
    return (bytes_data, codebook)
