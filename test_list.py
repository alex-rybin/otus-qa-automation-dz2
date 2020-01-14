import pytest


@pytest.mark.parametrize('last_element', [-1, 0, 'some text', 5.34, True])
def test_append(list_for_tests, last_element):
    list_for_tests.append(last_element)
    assert list_for_tests[-1] == last_element


def test_copy(list_for_tests):
    list_copy = list_for_tests.copy()
    assert not (list_copy is list_for_tests)


def test_clear(list_for_tests):
    list_for_tests.clear()
    assert list_for_tests == []


def test_insert(list_for_tests):
    list_for_tests.insert(3, 'X')
    assert list_for_tests[3] == 'X'


def test_pop(list_for_tests):
    popped = list_for_tests.pop(1)
    assert popped not in list_for_tests
