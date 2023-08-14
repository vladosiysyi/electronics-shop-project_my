"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item

@pytest.fixture
def item1():
    return Item("Смартфон", 10000, 20)
@pytest.fixture
def item2():
    return Item("Ноутбук", 20000, 5)

def test_item_calculate_total_price(item1):
    assert item1.calculate_total_price() == 200000


def test_apply_discount(item1):
    assert item1.apply_discount() == None


def test_apply_discount(item1):
    pay = 2
    assert item1.apply_discount() == 100000

