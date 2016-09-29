##################################################################
# FILE : ex2_square.py
# WRITER : Ori Broda , orib , 308043447
# EXERCISE : intro2cs ex2 2013-2014
# DESCRIPTION :
# Task 1: A program that draws a rhombus within a square,
# depend on an input number from the user.
##################################################################


#!/usr/bin/env python3
def square_printing(n):
    
    size = 2*n + 1
    print('#' * size)   # Prints the top of the square
    # Prints '*' as the upper edge of the rhombus
    print('#' + ' '*(n-1) + '*' + ' '*(n-1) + '#')  
    i = 0
    # Prints the upper section of the rhombus including middle line
    while i in range(0,n-1): 
        print('#' + ' '*((n-i)-2) + '*' + ' '*((2*i)+1)
              + '*' + ' '*((n-i)-2) + '#')
        i = i + 1
    i = 0
    # Prints the lower section of the rhombus 
    while i in range(0,n-2):  
        print('#' + ' '*(i+1) + '*' + ' '*((2*n)-(2*i+5))
              + '*' + ' '*(i+1) + '#')
        i = i + 1
    # Prints '*' as the lower edge of the rhombus
    # (n=1 prints '*' inside a square)    
    if(n != 1):    
        print('#' + ' '*(n-1) + '*' + ' '*(n-1) + '#') 
    print('#' * size)   # Prints the bottom of the square

if __name__=="__main__":  #If we are the main script, and not imported
    from sys import argv
    try:
        n = int(argv[1])
    except:
        n = int(input("Please enter a positive integer: "))
    square_printing(n)
