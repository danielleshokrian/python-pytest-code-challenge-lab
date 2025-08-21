import pytest
from palindrome import longest_palindromic_substring


def test_simple_palindrome():
    assert longest_palindromic_substring("babad") in ["bab", "aba"]
    assert longest_palindromic_substring("cbbd") == "bb"

def test_full_string_palindrome():
    assert longest_palindromic_substring("racecar") == "racecar"
    assert longest_palindromic_substring("madam") == "madam"

def test_no_palindrome_longer_than_one():
    assert longest_palindromic_substring("abcd") in ["a", "b", "c", "d"]


def test_empty_string():
    assert longest_palindromic_substring("") == ""

def test_single_character():
    assert longest_palindromic_substring("a") == "a"
    assert longest_palindromic_substring("z") == "z"

def test_repeated_characters():
    assert longest_palindromic_substring("aaaa") == "aaaa"
    assert longest_palindromic_substring("aaab") == "aaa"

def test_long_string():
    s = "forgeeksskeegfor"
    assert longest_palindromic_substring(s) == "geeksskeeg"

def test_multiple_possible_palindromes():
    s = "abaxyzzyxf"
    assert longest_palindromic_substring(s) == "xyzzyx"