import pytest


@pytest.mark.parametrize('element', [{'list': []}, {'none': None}, {'dict': {}}])
def test_update(dict_for_tests, element):
    dict_for_tests.update(element)
    assert all(item in dict_for_tests.items() for item in element.items())


def test_get(dict_for_tests):
    assert dict_for_tests.get('integer') == 1


def test_values(dict_for_tests):
    assert list(dict_for_tests.values()) == [1, 0.1984, 'The quick brown fox jumps over the lazy dog', True]


def test_keys(dict_for_tests):
    assert list(dict_for_tests.keys()) == ['integer', 'float', 'string', 'boolean']


def test_popitem(dict_for_tests):
    popped = dict_for_tests.popitem()
    assert popped not in dict_for_tests.items()
