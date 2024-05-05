from pytest import raises
from project.tests.test_find_average import average_f, list_nums_1, list_nums_2, list_nums_3


def test_compare_average_equals(average_f, list_nums_2, list_nums_3, capsys):
    """
    Проверка результата работы метода на равенство результатов
    """
    expected_output = "Средние значения равны"
    average_f.compare(list_nums_2, list_nums_3)
    captured = capsys.readouterr()
    assert captured.out.strip() == expected_output


def test_compare_average_greater(average_f, list_nums_1, list_nums_2, capsys):
    """
    Проверка результата работы метода на верность сравнения результатов вычисления,
    первое > второго
    """
    expected_output = "Первый список имеет большее среднее значение"
    average_f.compare(list_nums_1, list_nums_2)
    captured = capsys.readouterr()
    assert captured.out.strip() == expected_output


def test_compare_average_less(average_f, list_nums_1, list_nums_2, capsys):
    """
    Проверка результата работы метода на верность сравнения результатов вычисления,
    первое < второго
    """
    expected_output = "Второй список имеет большее среднее значение"
    average_f.compare(list_nums_2, list_nums_1)
    captured = capsys.readouterr()
    assert captured.out.strip() == expected_output


def test_compare_average_raises_on_not_list(average_f, list_nums_1):
    """
    Проверка результата работы метода на вызов сообщения об ошибке
    при передаче данных неверного типа
    """
    with raises(TypeError):
        average_f.compare("type not list", list_nums_1)


def test_compare_average_raises_data_type_not_int_float(average_f, list_nums_1):
    """
    Проверка результата работы метода на вызов сообщения об ошибке
    при передаче списка с данными неверного типа
    """
    with raises(TypeError):
        average_f.compare(["abc", "abc"], list_nums_1)
