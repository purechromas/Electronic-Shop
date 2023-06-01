import os
from csv import DictReader


def read_csv_file(path):
    list_of_items = []
    with open(path, encoding='utf-8') as f:
        file = DictReader(f)
        for item in file:
            if len(item) < 3:
                raise Exception
            list_of_items.append(item)
    return list_of_items


print(read_csv_file('items.csv'))
"""
        Reading a csv-file and storing the data in list.
        """