##########################################################
# FILE : ex1.py
# WRITER : Ori Broda , orib , 308043447
# EXERCISE : intro2cs ex1 2013-2014
# DESCRIPTION:
# A program that presents the Einstein puzzle to the user
##########################################################


print("Welcome to the Einstein puzzle")  
input_number = input("Please enter a three digit number:")
input_number = int(input_number)    ## Input from the user
ones = input_number % 10            ## Sifrat ha-achadot
tens = (input_number % 100) - ones  ## (Sifrat ha-asarot) * 10 [for sum] 
hundreds = input_number // 100      ## Sifrat ha-meot
reversed_number = (ones * 100) + tens + hundreds ##Reversing the digits
print("For the number:", input_number, "the reverse number is:",
reversed_number)
difference = abs(input_number - reversed_number)  ## Positive difference
print("The difference between", input_number, "and", reversed_number,
"is", difference)
ones_dif = difference % 10
tens_dif = (difference % 100) - ones_dif
hundreds_dif = difference // 100
reversed_difference = (ones_dif * 100) + tens_dif + hundreds_dif 
print("The reverse difference is:", reversed_difference)
sum_dif = difference + reversed_difference
print("The sum of:", difference, "and", reversed_difference, "is:",
sum_dif)



                







