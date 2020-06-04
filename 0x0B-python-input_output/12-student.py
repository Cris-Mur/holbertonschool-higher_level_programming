#!/usr/bin/python3
''' class to json '''


class Student:
    ''' class student '''
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    ''' return dict '''
    def to_json(self, attrs=None):
        if type(attrs) != list:
            return self.__dict__
        else:
            return dict(filter(lambda i: i[0] in attrs, self.__dict__.items()))
