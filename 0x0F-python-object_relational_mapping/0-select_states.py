#!/usr/bin/python3
''' Script that list Data in a SQLdb '''

if name == '__main__':
    import MySQLdb
    import sys
# argv[1] user
# argv[2] passwd
# argv[3] DataBase

    datB = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])

    mouse = datB.cursor()

    Ls_states(mouse)

    mouse.close()