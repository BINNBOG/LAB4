import json


def task() -> float:
    with open("input.json", 'r') as js_file:
        js_data = json.load(js_file)
    return round(sum([i_dict["score"] * i_dict["weight"] for i_dict in js_data]), 3)


print(task())
