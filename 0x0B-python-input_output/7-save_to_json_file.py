#!/usr/bin/python3
'''
saves a json file
'''


def save_to_json_file(my_obj, filename):
    '''
    function that save json file
    '''
    import json
    with open(filename, mode='w', encoding="utf-8") as coso:
        json.dump(my_obj, coso)
