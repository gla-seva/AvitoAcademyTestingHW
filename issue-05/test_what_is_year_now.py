from what_is_year_now import what_is_year_now
from unittest.mock import patch
import pytest


def test_check_year_first_format():
    with patch('urllib.request.urlopen'), patch('json.load', return_value={'currentDateTime': '2020-12-01'}):
        year = what_is_year_now()
    exp_year = 2020
    assert year == exp_year


def test_check_year_second_format():
    with patch('urllib.request.urlopen'), patch('json.load', return_value={'currentDateTime': '01.10.2020'}):
        year = what_is_year_now()
    exp_year = 2020
    assert year == exp_year


def test_check_year_wrong_format():
    with patch('urllib.request.urlopen'), patch('json.load', return_value={'currentDateTime': '18/11/20'}):
        with pytest.raises(ValueError):
            what_is_year_now()
