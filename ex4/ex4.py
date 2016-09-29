#############################################################
# FILE: ex4.py
# WRITER: Ori Broda, orib, 308043447
# EXERCISE : intro2cs ex4 2013-2014
# Description : This ex is a continuation of ex3 and as such,
# it uses functions from ex3 to implement more functions
# regarding our pension
#############################################################

# We will use this to copy a list in bubble_sort_2nd_value
from copy import deepcopy

# Constant for the minimum legal value of growth_rates
GROWTH_RATES_MIN = -100
# Constant for the maximum legal value of save
SAVE_MAX = 100

# Same functions from ex3

# This function receives 3 variables: employee's salary-float,
# saving into the retirement fund-float, and a list of
# annual growth percentages in investments-list of floats.
# The function returns list of the fund's value
# at the end of each year.
def variable_pension(salary, save, growth_rates):
    if((salary < 0) or (save < 0) or (save > SAVE_MAX)):
        return None
    # Checking for ilegal input
    
    for i in range(len(growth_rates)):
        if(growth_rates[i] < GROWTH_RATES_MIN): 
            return None    
    fund_list = []
    for i in range(len(growth_rates)):
        if(i == 0):
            fund_list.append(salary * save*0.01)
        else:
            fund_list.append(fund_list[i-1] * (1+growth_rates[i]*0.01)
                             + salary * save*0.01)
    return fund_list

# This function receives 3 variables: initial amount on the account,
# List of annual growth_rates and annual expenses.
# The function returns a list of the fund values in each year,
# after accounting for the expanses and growth rate values.
def post_retirement(savings, growth_rates, expenses):
    if ((savings < 0) or (expenses < 0)):
        return None
    for growth_rate in growth_rates:
        if(growth_rate < GROWTH_RATES_MIN):
            return None
    # Counter for the list of new fund values    
    index = 0 
    remaining_savings = []
    for growth_rate in growth_rates:
        if(index == 0):
            remaining_savings.append(savings * (1+growth_rates[0]*0.01)
                                     -expenses)
            index = index + 1
        else:    
            remaining_savings.append(remaining_savings[index-1] *
                                     (1+growth_rate*0.01)-expenses) 
            index = index + 1          
    return remaining_savings

    
def live_like_a_king(salary, save, pre_retire_growth_rates,
                  post_retire_growth_rates, epsilon):
    """ Find the maximal expenses you may expend during your lifetime  

    A function that calculates what is the maximal annual expenses you may
    expend each year and not enter into debts
    You may Calculate it using binary search or using arithmetics
    Specify in your README in which method you've implemnted the function

    Args:  
    -salary: the amount of money you make each year-a non negative float.
    -save: the percent of your salary to save in the investment account
    each working year -  a non negative float between 0 and 100
    -pre_retire_growth_rates: a list of annual growth percentages in your
    investment account - a list of floats larger than or equal to -100.
    -post_retire_growth_rates: a list of annual growth percentages
    on investments while you are retired. a list of floats larger
    than or equal to -100. In case of empty list return None
    - epsilon: an upper bound on the money must remain in the account
    on the last year of retirement. A float larger than 0

    Returns the maximal expenses value you found (such that the amount of
    money left in your account will be positive but smaller than epsilon)

    In case of bad input: values are out of range returns None

    You can assume that the types of the input arguments are correct."""
    # Checking for ilegal input
    if((salary < 0) or (save < 0) or (save > SAVE_MAX) or
       (epsilon <= 0)):
        return None
    if(post_retire_growth_rates is None or
       len(post_retire_growth_rates) == 0):
        return None
    if(pre_retire_growth_rates is None or
       len(pre_retire_growth_rates) == 0):
        return 0.0
    if salary == 0 or save == 0:
        return 0.0
    
    for i in range(len(pre_retire_growth_rates)):
        if(pre_retire_growth_rates[i] < GROWTH_RATES_MIN):
            return None
    for i in range(len(post_retire_growth_rates)):
        if(post_retire_growth_rates[i] < GROWTH_RATES_MIN):
            return None
  
    
    pre_retire_values = variable_pension(salary, save,
                                 pre_retire_growth_rates)

    # Variable for our initial savings as we entered retirement 
    savings = pre_retire_values[-1]
    # Checking for Special case
    if(len(post_retire_growth_rates) == 1):
        remaining_savings = post_retirement(
            savings, post_retire_growth_rates, 0)[-1]
        return remaining_savings
    # Variables for binary search like we saw in the tirgul
    low = 0
    high = savings
    mid_expenses = (low+high)/2
    # Looking for the maximum expenses between all adequate
    # real numbers
    while(mid_expenses < 0 or mid_expenses > epsilon):
        mid_expenses = (low+high)/2
        # Variable for our remaining savings on the account in
        # the last year of retirement
        remaining_savings = post_retirement(
            savings, post_retire_growth_rates, mid_expenses)[-1]
        if(remaining_savings > epsilon):
            low = mid_expenses
        elif(remaining_savings < 0):
            high = mid_expenses
        else:
            return mid_expenses
    return mid_expenses

def bubble_sort_2nd_value(tuple_list):
    """sort a list of tuples using bubble sort algorithm

    Args:
    tuples_list - a list of tuples, where each tuple is composed of a
    string value and a float value - ('house_1',103.4)

    Return: a NEW list that is sorted by the 2nd value of the tuple,
    the numerical one. The sorting direction should be from the lowest
    to the largest. sort should be stable (if values are equal,
    use original order)

    You can assume that the input is correct."""


    if tuple_list is None or len(tuple_list) == 0:
        return []
    list_for_sorting = deepcopy(tuple_list)
    for i in range(len(list_for_sorting)):
        for j in range(0, len(list_for_sorting)-i-1):
            if(list_for_sorting[j][1] > list_for_sorting[j+1][1]):
                list_for_sorting[j+1], list_for_sorting[j] =\
                list_for_sorting[j], list_for_sorting[j+1]
    return list_for_sorting
                




def choosing_retirement_home(savings,growth_rates,retirement_houses):
    """Find the most expensive retirement house one can afford.

    Find the most expensive, but affordable, retiremnt house.
    Implemnt the function using binary search

    Args:
    -savings: the initial amount of money in your savings account.
    -growth_rates: a list of annual growth percentages in your
    investment account - a list of floats larger than or equal to -100.
    -retirement_houses: a list of tuples of retirement_houses, where
    the first value is a string - the name of the house and the
    second is the annual rent of it - nonnegative float.

    Return: a string - the name of the chosen retirement house
    Return None if can't afford any house.

    You need to test the legality of savings and growth_rates
    but you can assume legal retirement_house list 
    You can assume that the types of the input are correct"""
    if(savings <= 0):
        return None
    # Checking for ilegal input
    if growth_rates is None or len(growth_rates) == 0:
        return None

    for growth in growth_rates:
        if(growth < GROWTH_RATES_MIN): 
            return None
        
    if retirement_houses is None or len(retirement_houses) == 0:
        return None
    
    sorted_retirement_houses = bubble_sort_2nd_value(retirement_houses)
    low = 0
    high = len(sorted_retirement_houses)

    # Looking for the most expensive yet affordable house using
    # binary search
    while(low < high):
        mid = (low+high)//2
        mid_rent = sorted_retirement_houses[mid][1]
        # Variable for the fund's value in the last year
        remaining_savings = post_retirement(savings, growth_rates,
                            mid_rent)[-1]
        if(remaining_savings > 0):
            low = mid + 1
            # Checking if the current house is the best we can afford
            if (low <= (len(sorted_retirement_houses)-1)):
                # Variable to look for negative fund
                # value result for the next house in the list
                remaining_savings_plus_one =\
                post_retirement(savings,
                                growth_rates,
                                sorted_retirement_houses[mid+1][1])[-1]
                if (remaining_savings_plus_one < 0):
                    return sorted_retirement_houses[mid][0]
                
        elif(remaining_savings < 0):
            high = mid
        else:
            return sorted_retirement_houses[mid][0]
    if(remaining_savings > 0):
        return sorted_retirement_houses[mid][0]

    


    
def get_value_key(value=0):
    """returns a function that calculates the new value of a house


    #Args:
    -value: the value added per opponent - a float - the default
    value is 0

    This function returns a function that accepts triple containing
    (house ,anntual rent,number of opponents) and returns the new
    value of this house - annual_rent+value*opponents

    You can assume that the input is correct."""
    # Checking for ilegal input
    if value < 0:
        return None
    def key_function(house_triple):
        return house_triple[1] + value*house_triple[2]
    return key_function

    



def choose_retirement_home_opponents(budget,key ,
                                     retirement_houses):
    """ Find the best retiremnt house that is affordable and fun

    A function that returns the best retiremnt house to live in
    such that: the house is affordable and
    his value (annual_rent+value*opponents) is the highest

    Args:
    -annual_budget: positive float. The amount of money you can
    expand per year.
    -key: a function of the type returned by get_value_key
    -retirement_houses: a list of houses (tuples) where  the first value
    is a string - the name of the house,
    the second is the annual rent on it - a non negative float, and the
    third is the number of battleship opponents the home hosts -
    non negative int
    
    Returns the name of the retirement home which provides the best
    value and which is affordable.

    You need to test the legality of annual_budget,
    but you can assume legal retirement_house list 
    You can assume that the types of the input are correct"""
    # Checking for ilegal input
    if retirement_houses is None or len(retirement_houses) == 0:
        return None
    if budget < 0:
        return None
    # Variable for the name of the best house
    best_house_name = None
    # Variable for best house value
    highest_key = 0
    # Looking for the best house
    for house in retirement_houses:
        if house[2] < 0:
            return None
        key_function = key(house)
        if budget >= house[1]:
            if highest_key < key_function:
                best_house_name = house[0]
                highest_key = key_function
    return best_house_name


   
