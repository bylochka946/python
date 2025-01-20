BOOKS_DATABASE = [
    {
        "id": 1,
        "name": "test_name_1",
        "pages": 200,
    },
    {
        "id": 2,
        "name": "test_name_2",
        "pages": 400,
    }
]


class Book:
    def __init__(self, id_, name, pages):
        """
        Создание и подготовка к работе экземпляра класса "Книга"

        :id_: Идентификатор книги
        :name: Название книги
        :pages: Количество страниц в книге
        """
        self.id = id_
        self.name = name
        self.pages = pages

    def __str__(self) -> str:
        """
        Магический метод __str__

        return: Строковое представление объекта
        """
        return f'Книга "{self.name}"'

    def __repr__(self) -> str:
        """
        Магический метод __repr__

        return: Строка, показывающая, как может быть инициализирован экземпляр
        """
        return f"{self.__class__.__name__}(id_={self.id}, name='{self.name}', pages={self.pages})"


if __name__ == '__main__':
    # инициализируем список книг
    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    for book in list_books:
        print(book)  # проверяем метод __str__

    print(list_books)  # проверяем метод __repr__
