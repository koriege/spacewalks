# automatically identified by python -m pytest if test_* or *_test is part of basename or file lives in tests directory
import pytest
from eva_data_analysis import text_to_duration
from eva_data_analysis import calculate_crew_size

def test_text_to_duration_integer():
    """
    test expected return values from text_to_duration_integer using zero minutes
    """
    #input_value = "10:00"
    #test_result = text_to_duration(input_value) == 10
    #print(f'text_to_duration({input_value}) == 10 ? {test_result}')
    assert text_to_duration("10:00") == 10

def test_text_to_duration_float():
    """
    test expected return values from text_to_duration_integer using non-zero minutes
    """
    assert text_to_duration("10:15") == 10.25
    assert text_to_duration("10:20") == 10+1/3
    # proper way is to allow tolerance in testing floats
    assert text_to_duration("10:20") - 10.3333333 < 1e-5
    assert text_to_duration("10:20") == pytest.approx(10.33333333)

# no need to explicitly call when using pytest
# test_text_to_duration_integer()
# test_text_to_duration_float()
