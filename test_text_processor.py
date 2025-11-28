# import module
# from file import class 
# 
# python -m pytest .\test_text_processor.py -v
import pytest
from text_processor import TextProcessor

def test_capitalize_text_equal():
    """1. Assert equal - egyenlőség ellenőrzés"""
    processor = TextProcessor()
    result = processor.capitalize_text('hello')
    assert processor.capitalize_text('hello') == 'HELLO'


def test_capitalize_text_not_equal():
    """2. Assert not equal - nem egyenlő"""
    processor = TextProcessor()
    result = processor.capitalize_text('world')
    assert processor.capitalize_text('world') != 'WORLD!'


def test_reverse_text_in():
    """3. Assert in - benne van"""
    processor = TextProcessor()
    result = processor.reverse_text('abcd')
    assert 'dcba' in result 



def test_reverse_text_not_in():
    """4. Assert not in - nincs benne"""
    processor = TextProcessor()
    result = processor.reverse_text('abcd')
    assert 'abcd' not in result


def test_count_words_isinstance():
    """5. Assert isinstance - típus ellenőrzés"""
    processor = TextProcessor()
    result = processor.count_words('Hello world')
    assert isinstance(result, int)


def test_count_words_greater_less():
    """6. Assert >, <, >=, <= - összehasonlítás"""
    processor = TextProcessor()
    result = processor.count_words('Hello world from pytest')
    assert result > 2
    assert result >= 3
    assert result < 5
    assert result <= 4


def test_count_words_empty_string():
    """7. Üres sztring bemenet ellenőrzése"""
    processor = TextProcessor()
    result = processor.count_words('')
    assert result == 0


def test_is_palindrome_true_false():
    """8. Assert True/False - boolean ellenőrzés"""
    processor = TextProcessor()
    assert processor.is_palindrome('anna') is True
    assert processor.is_palindrome('hello') is False


def test_remove_spaces_multiple_asserts():
    """9. Több assert egy tesztben"""
    processor = TextProcessor()
    result = processor.remove_spaces('a b c d e')
    assert result == 'abcde'
    assert ' ' not in result
    assert len(result) == 5