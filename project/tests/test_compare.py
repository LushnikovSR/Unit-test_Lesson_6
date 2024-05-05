from unittest.mock import patch
from project.average import Average
from project.tests.test_find_average import average_f, list_nums_1, list_nums_2, list_nums_3


def test_compare_average_equals(list_nums_2, list_nums_3, capsys):
    with patch.object(
        Average, "find", side_effect=[2.5, 2.5]
    ) as mock_find_average:
        expected_output = "Средние значения равны"
        Average.compare(list_nums_2, list_nums_3)
        captured = capsys.readouterr()
        assert captured.out.strip() == expected_output
        mock_find_average.assert_called_with([4, 3, 2, 1])


def test_compare_average_greater(average_f, list_nums_1, list_nums_2, capsys):
    with patch.object(
        Average, "find", side_effect=[7.0, 2.5]
    ) as mock_find:
        expected_output = "Первый список имеет большее среднее значение"
        Average.compare(list_nums_1, list_nums_2)
        captured = capsys.readouterr()
        assert captured.out.strip() == expected_output
        mock_find.assert_called_with(list_nums_2)


def test_compare_average_less(average_f, list_nums_1, list_nums_2, capsys):
    with patch.object(
        Average, "find", side_effect=[2.5, 7.0]
    ) as mock_find_average:
        expected_output = "Второй список имеет большее среднее значение"
        Average.compare(list_nums_2, list_nums_1)
        captured = capsys.readouterr()
        assert captured.out.strip() == expected_output
        mock_find_average.assert_called_with(list_nums_1)
