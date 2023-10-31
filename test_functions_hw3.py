# %%
import datetime as dt
from hw3_updated import sum_general_int_list
from hw3_updated import get_day_month_year
from hw3_updated import compute_distance
from hw3_updated import count_simba
import unittest
import sys
from pandas.testing import assert_series_equal
import pandas as pd


class countsimba(unittest.TestCase):

    def test_count_simba_no_values(self):
        input_list = ["Hello World", "Good Morning", "Good Night"]
        output = count_simba(input_list)
        expected_output = 0
        self.assertEqual(output, expected_output)

    def test_count_simba_many_values(self):
        input_list = ["Hello Simba",
                      "Good Morning, Simba", "Good Night, Simba"]
        output = count_simba(input_list)
        expected_output = 3
        self.assertEqual(output, expected_output)

    def test_count_simba_empty_list(self):
        input_list = []
        output = count_simba(input_list)
        expected_output = 0
        self.assertEqual(output, expected_output)

    def test_count_simba_one_value(self):
        input_list = ["Hello Simba",
                      "Good Morning", "Good Night"]
        output = count_simba(input_list)
        expected_output = 1
        self.assertEqual(output, expected_output)


# TEST FUNCTION 2

class Getdaymonthyear(unittest.TestCase):

    def test_get_day_month_year(self):

        input_list = [
            dt.date(2022, 1, 1),
            dt.date(2022, 1, 2),
            dt.date(2022, 1, 3),
            dt.date(2022, 8, 13)
        ]
        output = get_day_month_year(input_list)
        expected_output = pd.DataFrame({'day': [1, 2, 3, 13], 'month': [1, 1, 1, 8], 'year': [
                                       2022, 2022, 2022, 2022]}, index=['date', 'date', 'date', 'date'])
        self.assertTrue(expected_output.equals(output))


# TEST FUNCTION 3
class Computedistance(unittest.TestCase):
    def test_compute_distance(self):
        input_list = [((41.23, 23.5), (41.5, 23.4)),
                      ((52.38, 20.1), (52.3, 17.8))]
        output = compute_distance(input_list)
        expected_output = "The distances are 31.13 and 157.01 km"
        self.assertEqual(output, expected_output)

    def test_compute_distance_0(self):
        input_list = [((0, 0), (0, 0)), ((0, 0), (0, 0))]
        output = compute_distance(input_list)
        expected_output = "The distances are 0.0 and 0.0 km"
        self.assertEqual(output, expected_output)

    def test_compute_distance_missing(self):
        input_list = [((0, 0)), ((0, 0), (0, 0))]
        self.assertRaises(ValueError)


# TEST FUNCTION 4
class Sumgeneralintlist(unittest.TestCase):
    def test_general_int_list(self):
        input_list = [[1, 2, 3], 4, [5, [6, 7], 8, 9]]
        output = sum_general_int_list(input_list)
        expected_output = 45
        self.assertEqual(output, expected_output)

    def test_general_int_list_no_values(self):
        input_list = []
        output = sum_general_int_list(input_list)
        expected_output = 0
        self.assertEqual(output, expected_output)
