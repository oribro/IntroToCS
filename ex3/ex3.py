
#############################################################
# FILE: ex3.py
# WRITER: Ori Broda , orib , 308043447
# EXERCISE : intro2cs ex3 2013-2014
# DESCRIPTION :
# This file includes 6 functions which calculate data
# regarding our pension.
#############################################################

# This function receives 4 variables: employee's salary-float,
# saving into the retirement fund-float, the annual growth
# rate of the fund-float, and number of work years-int.
# The function returns list of the fund's value
# at the end of each year.
def constant_pension(salary, save, growth_rate, years):
    # Checking for ilegal input
    if((salary < 0) or (save < 0) or (save > 100) or
       (growth_rate < -100) or (years < 0)):
        return None    
    fund_list = []
    # Calculate the fund's value according to a formula
    for i in range(years):
        if(i == 0):
            fund_list.append(salary * save*0.01)
        else:
            fund_list.append(fund_list[i-1] * (1+growth_rate*0.01)
                             + salary * save*0.01)
    return fund_list

# This function receives 3 variables: employee's salary-float,
# saving into the retirement fund-float, and a list of
# annual growth percentages in investments-list of floats.
# The function returns list of the fund's value
# at the end of each year.
def variable_pension(salary, save, growth_rates):
    if((salary < 0) or (save < 0) or (save > 100)):
        return None
    # Checking for ilegal input
    for i in range(len(growth_rates)):
        if(growth_rates[i] < -100): 
            return None    
    fund_list = []
    for i in range(len(growth_rates)):
        if(i == 0):
            fund_list.append(salary * save*0.01)
        else:
            fund_list.append(fund_list[i-1] * (1+growth_rates[i]*0.01)
                             + salary * save*0.01)
    return fund_list

# This function receives 3 variables: employee's salary,
# saving into the retirement fund, and a file that 
# contains annual growth rate percentages of different funds.
# The function returns tuple including the name of the 
# most profittable fund (highest value) and it's value.
def choose_best_fund(salary, save, funds_file):
    if((salary < 0) or (save < 0) or (save > 100)):
        return None
    # Open the file for reading.
    file = open(funds_file, 'r')
    # Copy the file's content.
    lines = file.readlines()  
    file.close()
    # Highest value of all funds
    max_value = 0
    # Scan the current fund
    for line in lines:
        fund_list = []
        # Make a list from the current line
        string_to_list = line.split(',')
        # Save the fund's name
        fund_name = string_to_list[0]
        # Create a new list of numbers only
        growth_rates = string_to_list[1:]
        # Convert to float for using
        for i in range(len(growth_rates)):
            growth_rates[i] = float(growth_rates[i])
        for i in range(len(growth_rates)):
            if(i == 0):
                fund_list.append(salary * save*0.01)
            else:
                fund_list.append(fund_list[i-1] *
                                 (1+growth_rates[i]*0.01)
                                 + salary * save*0.01)
        # Keep last year's fund value for the current fund       
        last_year_value = fund_list[-1]
        # Look for the highest fund value
        if(max_value < last_year_value):
            max_value = last_year_value
            fund_name = fund_name.replace("#","")
            max_name = fund_name
    return (max_name, max_value)

# This function receives 2 variables: List of annual growth_rates
# and a specific working year.
# The function returns the value of growth_rates in the given year.
def growth_in_year(growth_rates, year):
    if (year >= len(growth_rates)) or (year < 0):
        return None
    for growth_rate in growth_rates:
        if growth_rate < -100:
            return None
    return growth_rates[year]  
    
# This function receives 2 variables: List of annual growth_rates
# and list of inflation factors(floats) for different years.
# The function returns a new list containing the growth rates
# after they were affected by the inflation.
def inflation_growth_rates(growth_rates, inflation_factors):
    for growth_rate in growth_rates:
        if(growth_rate < -100):
            return None
    # Checking for ilegal input
    for inflation_factor in inflation_factors:
        if(inflation_factor <= -100):
            return None
    # Counter for inflation factors    
    index = 0
    new_growth_rates = []
    for growth_rate in growth_rates:
        # Check for inflation factors
        if index != len(inflation_factors):
            inflation_factor = inflation_factors[index]
            # Formula for calculating inflation effect on growth rates.
            new_growth_rates.append(100*((100+growth_rate)
                                            /(100+inflation_factor)-1))
            index = index + 1
        # No factors so there was no inflation this year
        else:
            new_growth_rates.append(growth_rate)
    return new_growth_rates

# This function receives 3 variables: initial amount on the account,
# List of annual growth_rates and annual expenses.
# The function returns a list of the fund values in each year,
# after accounting for the expanses and growth rate values.
def post_retirement(savings, growth_rates, expenses):
    if ((savings < 0) or (expenses < 0)):
        return None
    for growth_rate in growth_rates:
        if(growth_rate < -100):
            return None
    # Counter for the list of new fund values    
    index = 0 
    remaining_savings = []
    # Calculating the fund values using a formula like we did in
    # the previous functions but in a different fashion (without range,
    # and using a different formula)  
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




