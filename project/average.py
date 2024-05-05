class Average:
    """
    Класс для расчёта и сравнения среднего значения чисел.
    """

    @staticmethod
    def find(numbers: list[int, float]) -> float:
        """
        Метод для расчёта среднего значения из списка чисел.

        Args:
            numbers: список чисел
        Returns: число - среднее значение либо исключение TypeError.
        """
        if not isinstance(numbers, list):
            raise TypeError(f"expected list but got {type(numbers)}")
        if not numbers:
            return 0
        try:
            return sum(numbers) / len(numbers)
        except TypeError as e:
            raise TypeError("Given list should contain only numbers") from e

    @staticmethod
    def compare(
        first: list[int, float], second: list[int, float]
    ) -> None:
        """
        Метод для сравнения средних значений двух списков чисел.

        Args:
            first: Список с числами.
            second: Список с числами.

        Может вызывать исключение TypeError.
        """
        first_average = Average.find(first)
        second_average = Average.find(second)
        if first_average > second_average:
            print("Первый список имеет большее среднее значение")
        elif first_average < second_average:
            print("Второй список имеет большее среднее значение")
        else:
            print("Средние значения равны")


if __name__ == "__main__":
    avg = Average()
    nums_1 = [10, 9, 8, 7, 6, 5, 4]
    nums_2 = [1, 2, 3, 4]
    print(avg.find(nums_1))
    print(avg.find(nums_2))
    avg.compare(nums_1, nums_2)
