from functools import partial


def custom_sort(iterable, key=None):
    # If the key is a string
    if isinstance(key, str):
        key_func = lambda item: item[key]
    # If the key is not a string
    else:
        key_func = key
    return sorted(iterable, key=key_func)

custom_sort = partial(custom_sort)


students = [
    {"name": "Alice",   "age": 25, "score": 85},
    {"name": "Bob",     "age": 22, "score": 90},
    {"name": "Charlie", "age": 23, "score": 88},
]

# 根据年龄排序
sorted_by_age = custom_sort(students, key="age")
print(sorted_by_age)

# 根据成绩排序
sorted_by_score = custom_sort(students, key="score")
print(sorted_by_score)
