import pytest


@pytest.mark.parametrize('letter', ['a', 'b', 'c', 'd', 'e'])
def test_replace(letter, text_for_tests):
    assert letter not in text_for_tests.replace(letter, '')


def test_upper(text_for_tests):
    assert 'THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG' == text_for_tests.upper()


def test_count(text_for_tests):
    assert text_for_tests.count('e') == 3


def test_lower(text_for_tests):
    assert 'the quick brown fox jumps over the lazy dog' == text_for_tests.lower()


def test_swapcase(text_for_tests):
    assert 'tHE QUICK BROWN FOX JUMPS OVER THE LAZY DOG' == text_for_tests.swapcase()
