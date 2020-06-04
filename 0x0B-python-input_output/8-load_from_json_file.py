#!/usr/bin/python3
'''
its is 8
'''


def load_from_json_file(filename):
    '''
    read json file
    '''
    import json
    with open(filename, mode='r', encoding='utf-8') as coso:
        coso_json = coso.read()
    return json.loads(coso_json)
