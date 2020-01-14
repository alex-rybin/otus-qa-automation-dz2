import pytest


@pytest.fixture
def text_for_tests():
    return 'The quick brown fox jumps over the lazy dog'


@pytest.fixture
def list_for_tests():
    return [5, 4, 3, 'two', 'one', None]
