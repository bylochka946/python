# TODO Напишите функцию find_common_participants
def find_common_participants(first_string, second_string, separator=","):
    first_string = first_string.split(separator)
    second_string = second_string.split(separator)
    list_ = list(set(first_string).intersection(second_string))
    list_.sort()
    return list_

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Проверьте работу функции с разделителем отличным от запятой

participants = find_common_participants(participants_first_group, participants_second_group, separator="|")
print(f"Общие участники: {participants}")
