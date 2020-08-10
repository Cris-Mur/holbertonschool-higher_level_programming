#!/usr/bin/python3
''' Script that list Data in a SQLdb '''

def Ls_states(cursor, srch_state):
    SQL_str = 'SELECT * FROM states WHERE name LIKE"{}" ORDER BY id'.format(
        srch_state)
    cursor.execute(SQL_str)
    table = cursor.fetchall()
    for state in table:
        print(state)

if __name__ == '__main__':
    import MySQLdb
    import sys

    datB = MySQLdb.connect(host="localhost", port=3306,
                           user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    mouse = datB.cursor()
    i_str = sys.argv[4]
    Ls_states(mouse, i_str)
    mouse.close()
    datB.close()
