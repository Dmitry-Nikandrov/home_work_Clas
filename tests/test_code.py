from classes import *
import pytest
from utils import *

@pytest.fixture
def product_apple():
    return Product('яблоко', 'свежее', 59.99, 120)

def test_init(product_apple):
    assert product_apple.name == 'яблоко'
    assert product_apple.description == 'свежее'
    assert product_apple.price == 59.99
    assert product_apple.amount == 120

@pytest.fixture
def category_phone():
    return Category("Смартфоны",
    "Смартфоны, как средство не только коммуникации",
    [
    Product("Samsung Galaxy C23 Ultra",
    "256GB, Серый цвет, 200MP камера",
     180000.0,
     5)])


def test_cat(category_phone):
    assert category_phone.name == 'Смартфоны'
    assert category_phone.description == "Смартфоны, как средство не только коммуникации"
    assert category_phone.product[0].name == "Samsung Galaxy C23 Ultra"


def test_load_json():
    assert load_json('operations_test.json') == [{"name": "Смартфоны","description": "Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для удобства жизни","products": [{"name": "Samsung Galaxy C23 Ultra","description": "256GB, Серый цвет, 200MP камера","price": 180000.0,"quantity": 5}]}]


def test_create_prod():
    assert create_prod([{"name": "Смартфоны","description": "Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для удобства жизни","products": [{"name": "Samsung Galaxy C23 Ultra","description": "256GB, Серый цвет, 200MP камера","price": 180000.0,"quantity": 5}]}]) == None


def test_count_prod():
    assert count_prod([{'name': 'Смартфоны', 'description': 'Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для удобства жизни', 'products': [{'name': 'Samsung Galaxy C23 Ultra', 'description': '256GB, Серый цвет, 200MP камера', 'price': 180000.0, 'quantity': 5}, {'name': 'Iphone 15', 'description': '512GB, Gray space', 'price': 210000.0, 'quantity': 8}, {'name': 'Xiaomi Redmi Note 11', 'description': '1024GB, Синий', 'price': 31000.0, 'quantity': 14}]}, {'name': 'Телевизоры', 'description': 'Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником', 'products': [{'name': '55 QLED 4K', 'description': 'Фоновая подсветка', 'price': 123000.0, 'quantity': 7}]}]) == 'Количество уникальных продуктов - 4'


def test_create_cat():
    assert create_cat([{'name': 'Смартфоны', 'description': 'Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для удобства жизни', 'products': [{'name': 'Samsung Galaxy C23 Ultra', 'description': '256GB, Серый цвет, 200MP камера', 'price': 180000.0, 'quantity': 5}, {'name': 'Iphone 15', 'description': '512GB, Gray space', 'price': 210000.0, 'quantity': 8}, {'name': 'Xiaomi Redmi Note 11', 'description': '1024GB, Синий', 'price': 31000.0, 'quantity': 14}]}, {'name': 'Телевизоры', 'description': 'Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником', 'products': [{'name': '55 QLED 4K', 'description': 'Фоновая подсветка', 'price': 123000.0, 'quantity': 7}]}])