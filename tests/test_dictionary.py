import pytest


@pytest.mark.parametrize('element', [{'list': []}, {'none': None}, {'dict': {}}])
def test_update(dict_for_tests, element):
    """
    Проверка, что метод update добавляет в словарь ключи и значения из словаря в аргументе.
    """
    dict_for_tests.update(element)
    assert all(item in dict_for_tests.items() for item in element.items())


def test_get(dict_for_tests):
    """
    Проверка, что метод get возвращает значение по ключу.
    """
    assert dict_for_tests.get('integer') == 1


def test_values(dict_for_tests):
    """
    Проверка, что метод values возвращает все значения словаря.
    """
    assert list(dict_for_tests.values()) == [1, 0.1984, 'The quick brown fox jumps over the lazy dog', True]


def test_keys(dict_for_tests):
    """
    Проверка, что метод keys возвращает все ключи словаря.
    """
    assert list(dict_for_tests.keys()) == ['integer', 'float', 'string', 'boolean']


def test_popitem(dict_for_tests):
    """
    Проверка, что пара ключ-значение, возвращённая методом popitem, не встречается в исходном словаре.
    """
    popped = dict_for_tests.popitem()
    assert popped not in dict_for_tests.items()
