import csv
import json

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    json_array = []
    with open(INPUT_FILENAME) as file_csv:
        reader = csv.DictReader(file_csv)

        for row in reader:
            json_array.append(row)

    with open(OUTPUT_FILENAME, "w") as file_json:
        json_string = json.dumps(json_array, indent=4)
        file_json.write(json_string)


if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
