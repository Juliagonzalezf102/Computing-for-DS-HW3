# %%

from hw3_updated import get_day_month_year

# %%


def test_count_simba(input_list):
    output = count_simba(input_list)
    assert output == expected_output
