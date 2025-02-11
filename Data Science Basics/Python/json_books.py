""" Module to import json. """
import json

with open('books.json', 'r', encoding='utf-8') as j:
    json_data = json.load(j)
    print(json_data)
