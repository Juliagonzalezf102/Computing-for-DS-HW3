# %%
# Try to use map and reduce in the next 3 exercises
# 1)
# Create a function called "count_simba" that counts
# the number of times that Simba appears in a list of
# strings. Example:
# ["Simba and Nala are lions.", "I laugh in the face of danger.",
#  "Hakuna matata", "Timon, Pumba and Simba are friends, but Simba could eat the other two."]
import datetime as dt
hk = ["Simba and Nala are lions.", "I laugh in the face of danger.", "Hakuna matata",
      "Timon, Pumba and Simba are friends, but Simba could eat the other two."]

# we create the function by using the count method on each string in the list in a lambda function within the map function


def count_simba(list):
    return sum(
        map(
            lambda x: x.count("Simba"),
            list
        )
    )


# count_simba(hk)
count_simba(hk)

# %%
# 2)
# Create a function called "get_day_month_year" that takes
# a list of datetimes.date and returns a pandas dataframe
# with 3 columns (day, month, year) in which each of the rows
# is an element of the input list and has as value its
# day, month, and year.
#
# create a list of dates to test the function created below and print it to check
dates = [
    dt.date(2022, 1, 1),
    dt.date(2022, 1, 2),
    dt.date(2022, 1, 3)
]
# print(dates[0])
# print(dates[1])
# print(dates[2])

# create the function


#def get_day_month_year(list_of_dates):
    # import necesary packages
    import pandas as pd
    import datetime as dt

    # create a dataframe with the dates and the columns day, month, year
    # using the methods from the datetime package in a map function
    df = pd.DataFrame(
        map(
            lambda x: [x.day, x.month, x.year],
            list_of_dates
        ),

        # set the index of the dataframe to be different than [0, 1, 2]
        index=[
            'date1',
            'date2',
            'date3'
        ],

        # set the column names to be 'day', 'month', 'year'
        columns=[
            'day',
            'month',
            'year'
        ]
    )

    return df


# test the function
print(get_day_month_year(dates))
# %%
# 3)
# Create a function called "compute_distance" that takes
# a list of tuple pairs with latitude and longitude coordinates and
# returns a list with the distance between the two pairs
example_input = [((41.23, 23.5), (41.5, 23.4)), ((52.38, 20.1), (52.3, 17.8))]
# HINT: You can use geopy.distance in order to compute the distance
#

# we create the function by importing the geopy package and using the distance method
# on each pair of tuples using the map function with a lambda inside it that iterates
# over the list of tuples.


def compute_distance(list_of_tuples):
    import geopy.distance as gp

    distances = list(
        map(
            lambda x: gp.distance(
                x[0],
                x[1]
            ).km,
            (pair for pair in list_of_tuples)
        )
    )

    # We return the distances formatted a little bit and rounded to 2 decimals
    return f'The distances are {round(distances[0], 2)} and {round(distances[1], 2)} km'


print(compute_distance(example_input))


# %%
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


list_1 = [[2], 4, 5, [1, [2], [3, 5, [7, 8]], 10], 1]
result = sum_general_int_list(list_1)
print(result)
