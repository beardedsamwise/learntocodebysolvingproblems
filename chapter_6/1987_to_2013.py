# https://dmoj.ca/problem/ccc13s1

def is_distinct(year):
    """
    year is an integer; which represents the year to check for a distinct year

    Returns true if the year is distinct (ie. no duplicate digits in the year)
    Otherwise returns False
    """
    year_as_list = list(str(year))
    if len(year_as_list) == len(set(year_as_list)):
        return True
    else:
        return False

# Main Program

# get input year where year is an integer representing the starting year

year = int(input()) + 1

# loop through range of years from Year + 1 to 10000 and check for distinct year 

while True:
    if is_distinct(year):
        print(year)
        break
    else:
        year += 1
    