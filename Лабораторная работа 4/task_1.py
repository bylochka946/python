import json

FILENAME = "input.json"


def task() -> float:
    with open(FILENAME) as file:
        writer = json.load(file)

    list_ = [line["score"] * line["weight"] for line in writer]
    return round(sum(list_), 3)


print(task())
