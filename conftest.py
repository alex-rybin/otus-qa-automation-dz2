import pytest


@pytest.fixture(scope='module')
def text_for_tests():
    return 'The quick brown fox jumps over the lazy dog'


@pytest.fixture
def list_for_tests():
    return [5, 4, 3, 'two', 'one', None]


@pytest.fixture
def set_for_tests():
    return {5, 4, 3, 'two', 'one', None}


@pytest.fixture
def dict_for_tests():
    return {
        'integer': 1,
        'float': 0.1984,
        'string': 'The quick brown fox jumps over the lazy dog',
        'boolean': True
    }
