from q1_memory import q1_memory
from q1_time import q1_time 
from q2_memory import q2_memory
from q2_time import q2_time 
from q3_memory import q3_memory
from q3_time import q3_time 
import pytest

"""
Set of functions to test that we have matching outputs for our functions, regardless the approach.
"""

file_path = '/Users/bjuanm/Desktop/Interviews/LATAM/tweets-analysis/data/farmers-protest-tweets-2021-2-4.json'

@pytest.mark.parametrize("input_data", [
    (file_path)
])
def test_q1(input_data):
    result_m = q1_memory(input_data)
    result_t = q1_time(input_data)
    assert result_m == result_t, "Outputs are not the same for excercise 1."

@pytest.mark.parametrize("input_data", [
    (file_path)
])
def test_q2(input_data):
    result_m = q1_memory(input_data)
    result_t = q1_time(input_data)
    assert result_m == result_t, "Outputs are not the same for excercise 2."


@pytest.mark.parametrize("input_data", [
    (file_path)
])
def test_q3(input_data):
    result_m = q3_memory(input_data)
    result_t = q3_time(input_data)
    assert result_m == result_t, "Outputs are not the same for excercise 3."

