class Book:
    """ Базовый класс книги. """

    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author

    def __str__(self):
        return f"Книга {self.name}. Автор {self._author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self._author!r})"

    """Свойство, которое не позволят изменить атрибут name"""
    @property
    def name(self):
        return self._name

    """Свойство, которое не позволят изменить атрибут author"""
    @property
    def author(self):
        return self._author


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)  # вызов конструктора родительского класса с помощью функции super()
        self.pages = pages

    @property
    def pages(self) -> int:
        return self.pages

    @pages.setter
    def pages(self, pages) -> None:
        if not isinstance(pages, int):
            raise TypeError
        if not 0 < pages:
            raise ValueError
        self.pages = pages


class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)  # вызов конструктора родительского класса с помощью функции super()
        self.duration = duration

    @property
    def duration(self) -> float:
        return self.duration

    @duration.setter
    def pages(self, duration) -> None:
        if not isinstance(duration, float):
            raise TypeError
        if not 0 < duration:
            raise ValueError
        self.duration = duration
