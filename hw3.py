#%%
##### Try to use map and reduce in the next 3 exercises
# 1)
# Create a function called "count_simba" that counts
# the number of times that Simba appears in a list of
# strings. Example: 
# ["Simba and Nala are lions.", "I laugh in the face of danger.",
#  "Hakuna matata", "Timon, Pumba and Simba are friends, but Simba could eat the other two."]
def count_simba(lst:list):
    '''Return the amount of times Simba (case sensitive) appears on the given list'''
    count = sum(item.count('Simba') for item in lst)
    return count

x = count_simba(["Simba and Nala are lions.", "I laugh in the face of danger.",
    "Hakuna matata", "Timon, Pumba and Simba are friends, but Simba could eat the other two simba."])
print(x)

#%%
# 2)
# Create a function called "get_day_month_year" that takes 
# a list of datetimes.date and returns a pandas dataframe
# with 3 columns (day, month, year) in which each of the rows
# is an element of the input list and has as value its 
# day, month, and year.
# 
import pandas as pd
from datetime import date

def get_day_month_year(dates):
    '''Return a DataFrame with the day, month and year from the dates list'''
    data = [[d.day, d.month, d.year] for d in dates]
    df = pd.DataFrame(data, columns=['day', 'month', 'year'])
    return df

dates = [date(2022, 11, 1), date(2018, 2, 1), date(2022, 3, 12)]
df = get_day_month_year(dates)
df.head()
#%%
# 3) 
# Create a function called "compute_distance" that takes
# a list of tuple pairs with latitude and longitude coordinates and 
# returns a list with the distance between the two pairs
# example input: [((41.23,23.5), (41.5, 23.4)), ((52.38, 20.1),(52.3, 17.8))]
# HINT: You can use geopy.distance in order to compute the distance
#
from geopy.distance import geodesic

def compute_distance(coordinates):
    '''Returns a list with the distances from the list of tuples with coordinates given'''
    distances = [geodesic(coordinate[0], coordinate[1]).miles for coordinate in coordinates]
    return distances

coordinates = [((41.23,23.5), (41.5, 23.4)), ((52.38, 20.1),(52.3, 17.8))]
distances = compute_distance(coordinates)
print(distances)


#%%
# 4)
# Consider a list that each element can be an integer or
# a list that contains integers or more lists with integers
# example: [[2], 4, 5, [1, [2], [3, 5, [7,8]], 10], 1]. 
# create a recursive function called "sum_general_int_list"
# that takes as input this type of list 
# and returns the sum of all the integers within the lists
# for instance for list_1=[[2], 3, [[1,2],5]] 
# the result should be 13
#
def sum_general_int_list(lst):
    total = 0
    for i in lst:
        if type(i) == list:
            total += sum_general_int_list(i)
        else:
            total += i
    return total

list_1 = [[2], 4, 5, [1, [2], [3, 5, [7,8]], 10], 1]
result = sum_general_int_list(list_1)

