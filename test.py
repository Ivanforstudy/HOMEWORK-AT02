import pytest
from main import count_vowels

def test_all_vowels():
    assert count_vowels("aeiouAEIOU") == 10

def test_no_vowels():
    assert count_vowels("bcdfghjklmnpqrstvwxyz") == 0

def test_mixed_string():
    assert count_vowels("Hello World!") == 3

def test_empty_string():
    assert count_vowels("") == 0

def test_numbers_and_symbols():
    assert count_vowels("123!@#") == 0