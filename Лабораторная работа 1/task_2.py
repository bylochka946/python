# TODO Найдите количество книг, которое можно разместить на дискете
memory_for_one_character = 4  # байта
characters_per_line = 25
line_per_page = 50
pages_in_book = 100
information_value_mb = 1.44
information_value_byte = information_value_mb * 1024 * 1024  # ... * Кб * байт

information_value_one_book = memory_for_one_character * characters_per_line \
                             * line_per_page * pages_in_book
number_of_book = information_value_byte / information_value_one_book

print("Количество книг, помещающихся на дискету:", int(number_of_book))
