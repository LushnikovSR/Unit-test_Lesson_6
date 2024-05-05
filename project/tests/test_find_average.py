import pytest

from pytest import raises
from project.average import Average


@pytest.fixture
def average_f():
    """
    Создаём экземпляр класса для работы с методами класса в тестах
    """
    return Average()


@pytest.fixture
def list_nums_1():
    """
    Создаём список с числовыми значениями для работы с тестами
    """
    return [10, 9, 8, 7, 6, 5, 4]


@pytest.fixture
def list_nums_2():
    """
    Создаём список с числовыми значениями для работы с тестами
    """
    return [1, 2, 3, 4]


@pytest.fixture
def list_nums_3():
    """
    Создаём список с числовыми значениями для работы с тестами
    """
    return [4, 3, 2, 1]


def test_find_average(average_f, list_nums_1, list_nums_2):
    """
    Проверка результата работы метода на равенство значению
    """
    assert average_f.find(list_nums_1) == 7.0
    assert average_f.find(list_nums_2) == 2.5


def test_find_average_empty_list(average_f):
    """
    Проверка результата работы метода на равенство значению при передаче пустого списка
    """
    assert average_f.find([]) == 0


def test_find_average_raises_type_not_list(average_f):
    """
    Проверка результата работы метода на вызов сообщения об ошибке
    при передаче данных неверного типа
    """
    with raises(TypeError):
        average_f.find("type not list")


def test_find_average_raises_data_type_not_int_float(average_f):
    """
    Проверка результата работы метода на вызов сообщения об ошибке
    при передаче списка с данными неверного типа
    """
    with raises(TypeError):
        average_f.find(["a", "b"])
