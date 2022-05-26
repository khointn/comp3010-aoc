## day12
import json

file = r'C:\Users\nguye\comp3010-aoc\day-12\data.json'
with open(file) as json_data:
    data = json.load(json_data)


def sum_recurse(d, skip_value=None):
    if isinstance(d, list):
            return sum(sum_recurse(e, skip_value) for e in d)
    if isinstance(d, dict):
        if skip_value and skip_value in d.values():
            return 0
        return sum(sum_recurse(e, skip_value) for e in d.values())
    if isinstance(d, (int, float)):
        return d
    return 0


print(sum_recurse(data))
print(sum_recurse(data, 'red'))