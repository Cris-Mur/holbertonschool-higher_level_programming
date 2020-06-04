#!/usr/bin/python3
"""
load, add, save
"""


import sys
import json

save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file

if __name__ == "__main__":

try:
    coso_json = load_from_json_file("add_item.json")
except:
    coso_json = []

argc = len(sys.argv)
for ant in range(1, argc):
    coso_json.append(sys.argv[i])

save_to_json_file(coso_json, "add_item.json")
