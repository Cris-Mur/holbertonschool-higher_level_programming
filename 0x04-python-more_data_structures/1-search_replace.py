#!/usr/bin/python3
def search_replace(my_list, search, replace):
    if my_list != []:
        return [replace if step == search else step for step in my_list]
    return my_list
