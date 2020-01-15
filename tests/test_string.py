import pytest


@pytest.mark.parametrize('letter', ['a', 'b', 'c', 'd', 'e'])
def test_replace(letter, text_for_tests):
    """
    Проверка, что после удаления символа из строки методом replace, символ в строке больше не встречается.
    """
    assert letter not in text_for_tests.replace(letter, '')


def test_upper(text_for_tests):
    """
    Проверка, что метод upper приводит строку в верхний регистр.
    """
    assert 'THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG' == text_for_tests.upper()


def test_count(text_for_tests):
    """
    Проверка, что метод count правильно считает количество символов в строке.
    """
    assert text_for_tests.count('e') == 3


def test_lower(text_for_tests):
    """
    Проверка, что метод lower приводит строку в нижний регистр.
    """
    assert 'the quick brown fox jumps over the lazy dog' == text_for_tests.lower()


def test_swapcase(text_for_tests):
    """
    Проверка, что метод swapcase заменяет в строке символы нижнего регистра на верхний и наоборот.
    """
    assert 'tHE QUICK BROWN FOX JUMPS OVER THE LAZY DOG' == text_for_tests.swapcase()
