import pytest


@pytest.mark.parametrize('element', [3, '5', -1, 'a', None])
def test_add(element, set_for_tests):
    set_for_tests.add(element)
    assert element in set_for_tests


def test_discard(set_for_tests):
    set_for_tests.discard('one')
    assert 'one' not in set_for_tests


def test_intersection_update(set_for_tests):
    set_for_tests.intersection_update({'one', 'two', '5'})
    assert set_for_tests == {'one', 'two'}


def test_difference_update(set_for_tests):
    set_for_tests.difference_update({'one', 'two', '5'})
    assert set_for_tests == {5, 4, 3, None}


def test_update(set_for_tests):
    set_for_tests.update({'one', 'two', 'five'})
    assert set_for_tests == {5, 4, 3, 'two', 'one', None, 'five'}
