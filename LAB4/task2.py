import json
import csv


INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    with open("input.csv", 'r') as csv_file:
        reader_csv = csv.DictReader(csv_file)
        with open(OUTPUT_FILENAME, 'w') as js_file:
            dict_list = [elem for elem in reader_csv]
            json.dump(dict_list, js_file, indent=4)


if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
