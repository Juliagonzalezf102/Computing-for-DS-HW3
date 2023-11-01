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

    def test_no_values(self):
        input_list = ["Hello World", "Good Morning", "Good Night"]
        output = count_simba(input_list)
        expected_output = 0
        self.assertEqual(output, expected_output)

    def test_many_values(self):
        input_list = ["Hello Simba",
                    "Good Morning, Simba", "Good Night, Simba"]
        output = count_simba(input_list)
        expected_output = 3
        self.assertEqual(output, expected_output)

    def test_empty_list(self):
        input_list = []
        output = count_simba(input_list)
        expected_output = 0
        self.assertEqual(output, expected_output)

    def test_one_value(self):
        input_list = ["Hello Simba",
                    "Good Morning", "Good Night"]
        output = count_simba(input_list)
        expected_output = 1
        self.assertEqual(output, expected_output)
    
    def test_multiple_simbas_same_string(self):
        input_list = ["Simba, Simba, Simba, my name's Simba", "do you know Simba?", "Simba is such a nice version of Simba",
                    "i know, i know him", "", "Simba is the best Simba"]
        output = count_simba(input_list)
        expected_output = 9
        self.assertEqual(output, expected_output)
    
    def test_simba_not_alone(self):
        input_list = ["Simbaland", "vamos a hacer un Simbagar"]
        output = count_simba(input_list)
        expected_output = 2
        self.assertEqual(output, expected_output)
    
    def test_simba_lowercase(self):
        input_list = ["simba", "simba", "simba"]
        output = count_simba(input_list)
        expected_output = 0
        self.assertEqual(output, expected_output)
    
    def test_Simba_siamese(self):
        input_list = ["SimbaSimbaSimba", "I SimbaSimba"]
        output = count_simba(input_list)
        expected_output = 5
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

    def test_get_day_month_year_empyt_list(self):

        input_list = []
        output = get_day_month_year(input_list)
        expected_output = pd.DataFrame(
            columns=['day', 'month', 'year'], index=[])
        self.assertTrue(expected_output.equals(output))


# TEST FUNCTION 3
class Computedistance(unittest.TestCase):
    def test_compute_distance(self):
        input_list = [((39.51, 21.3), (25.3, 55.67)),
                    ((32.31, 2.12), (52.38, 19.23))]
        output = compute_distance(input_list)
        expected_output = "The distances are 3567.42 and 2622.91 km"
        self.assertEqual(output, expected_output)

    def test_compute_distance_0(self):
        input_list = [((0, 0), (0, 0)), ((0, 0), (0, 0))]
        output = compute_distance(input_list)
        expected_output = "The distances are 0.0 and 0.0 km"
        self.assertEqual(output, expected_output)

    def test_compute_distance_missing(self):
        input_list = [((39.51, 21.3), (25.3, 55.67)),
                    ((32.31, 2.12))]
        self.assertRaises(ValueError)


# TEST FUNCTION 4
class Sumgeneralintlist(unittest.TestCase):
    def test_normal(self):
        input_list = [[1, 2, 3], 4, [5, [6, 7], 8, 9]]
        output = sum_general_int_list(input_list)
        expected_output = 45
        self.assertEqual(output, expected_output)

    def test_no_values(self):
        input_list = []
        output = sum_general_int_list(input_list)
        expected_output = 0
        self.assertEqual(output, expected_output)
    
    def test_roger_example(self):
        input_list = [[2], 3, [[1,2],5]]
        output = sum_general_int_list(input_list)
        expected_output = 13
        self.assertEqual(output, expected_output)
    
    def test_combined_list(self):
        input_list = [[1], 6, [[[3, 0], 2], []], [[[[[]]]], 10], 5, 0, [[0], [[[[[0]]], [[4]]]]]]
        output = sum_general_int_list(input_list)
        expected_output = 31
        self.assertEqual(output, expected_output)