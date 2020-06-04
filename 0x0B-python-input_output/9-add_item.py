#!/usr/bin/python3
''' load, add, save '''

import sys

save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file


try:
    coso_json = load_from_json_file("add_item.json") + sys.argv[1:]
except:
    coso_json = sys.argv[1:]
save_to_json_file(coso_json, "add_item.json")
