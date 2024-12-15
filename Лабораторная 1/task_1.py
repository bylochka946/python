import doctest


# TODO Написать 3 класса с документацией и аннотацией типов
class Copybook:
    def __init__(self, total_sheets: int, used_sheets: int):
        """
        Создание и подготовка к работе объекта "Тетрадь"

        :param total_sheets: Количество листов в тетради
        :param used_sheets: Количество использованных листов в тетради

        Примеры:
        >>> copybook = Copybook(48, 12)  # инициализация экземпляра класса
        """
        if not isinstance(total_sheets, int):
            raise TypeError("Количество страниц в тетради должно быть типа 'int'")
        if total_sheets < 0:
            raise ValueError("Количество страниц тетради не может быть равно меньше нуля")
        self.total_sheets = total_sheets

        if not isinstance(used_sheets, int):
            raise TypeError("Количество использованных страниц в тетради должно быть типа 'int'")
        if used_sheets > total_sheets:
            raise ValueError("Количество использованных страниц тетради не может быть больше общего количества страниц")
        self.used_sheets = used_sheets



    def can_use_a_copybook(self) -> bool:
        """
        Функция, которая проверяет можно ли использовать еще тетрадь, т.е. еще есть чистые листы

        return: Можно ли использовать тетрадь

        Примеры:
        >>> copybook = Copybook(48, 24)
        >>> copybook.can_use_a_copybook()
        """
        ...

    def cost_of_copybook_per_year(self, cost_copybook: float) -> None:
        """
        Затраты на тетради в год, при условии, что в год требуется 24 тетради
        number_copybook_per_year = 24

        :param cost_copybook: Стоимость тетради

        Примеры:
        >>> copybook = Copybook(48, 24)
        >>> copybook.cost_of_copybook_per_year(50.8)
        """
        if not isinstance(cost_copybook, float):
            raise TypeError("Стоимость тетради должна быть типа 'float'")
        if cost_copybook < 0:
            raise ValueError("Стоимость тетради не может быть равна меньше нуля")
        ...


class Curtain:
    def __init__(self, desired_curtain_length: float, actual_curtain_length: float):
        """
        Создание и подготовка к работе объекта "Штора"

        :param desired_curtain_length: Нужная длина шторы
        :param actual_curtain_length: Фактическая длина шторы

        Примеры:
        >>> curtain = Curtain(2.2, 2.4)  # инициализация экземпляра класса
        """

        if not isinstance(desired_curtain_length, float):
            raise TypeError("Необходимая длина шторы должна быть типа 'float'")
        if desired_curtain_length < 0:
            raise ValueError("Необходимая длина шторы не может быть равна меньше 0")
        self.desired_curtain_length = desired_curtain_length

        if not isinstance(actual_curtain_length, float):
            raise TypeError("Необходимая длина шторы должна быть типа 'float'")
        if actual_curtain_length < 0:
            raise ValueError("Необходимая длина шторы не может быть равна меньше 0")
        self.actual_curtain_length = actual_curtain_length

    def does_the_curtain_fit_the_length(self) -> bool:
        """
        Функция, которая проверяет подойдет ли фактическая длина шторы для необходимой (не будет ли она короче)

        return: Подойдет ли длина шторы

        Примеры:
        >>> curtain = Curtain(2.7, 2.5)
        >>> curtain.does_the_curtain_fit_the_length()
        """
        ...

    def hem_the_curtain(self) -> None:
        """
        Подшив шторы

        return: Длина, которую надо подшить

        Примеры:
        >>> curtain = Curtain(2.3, 2.9)
        >>> curtain.does_the_curtain_fit_the_length()
        """
        ...


class ClassInElementarySchool:
    def __init__(self, num_children: int, num_copybook_per_child: int, time_to_check_copybook: float):
        """
        Создание и подготовка к работе объекта "Класс в младшей школе"

        :param num_children: Количество детей в классе
        :param num_copybook_per_child: Количество тетрадей у одного ученика
        :param time_to_check_copybook: Время в минутах на проверку одной тетради

        Примеры:
        >>> classInElementarySchool = ClassInElementarySchool(20, 4, 5.5) # инициализация экземпляра класса
        """

        if not isinstance(num_children, int):
            raise TypeError("Количество детей в классе должно быть типа 'int'")
        if num_children < 0:
            raise ValueError("Количество детей не может быть равно меньше нуля")
        self.num_children = num_children

        if not isinstance(num_copybook_per_child, int):
            raise TypeError("Количество тетрадей у ученика должно быть типа 'int'")
        if num_copybook_per_child < 0:
            raise ValueError("Количество тетрадей у ученика не может быть равно меньше нуля")
        self.num_copybook_per_child = num_copybook_per_child

        if not isinstance(time_to_check_copybook, float):
            raise TypeError("Время в минутах на проверку одной тетради должно быть типа 'float'")
        self.time_to_check_copybook = time_to_check_copybook

    def time_to_check_copybooks(self) -> None:
        """
        Нахождение общего времени в часах на проверку всех терадей в классе

        return: Время на проверку

        Примеры:
        >>> classInElementarySchool = ClassInElementarySchool(20, 4, 5.5)
        >>> classInElementarySchool.time_to_check_copybooks()
        """
        ...

    def addition_to_the_class(self, num_of_added_children: int) -> None:
        """
        Пополнение численности детей в классе

        :param num_of_added_children: Количество прибывших детей в класс

        return: Настоящее количество детей в классе

        Примеры:
        >>> classInElementarySchool = ClassInElementarySchool(20, 4, 5.5)
        >>> classInElementarySchool.addition_to_the_class(5)
        """
        if not isinstance(num_of_added_children, int):
            raise TypeError("Количество прибывших детей должно быть типа 'int'")
        if num_of_added_children < 0:
            raise ValueError("Количество прибывших детей не может быть равно меньше нуля")
        ...


if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    doctest.testmod()
