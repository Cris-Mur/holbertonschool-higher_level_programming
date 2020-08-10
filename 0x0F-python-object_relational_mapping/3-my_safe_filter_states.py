#!/usr/bin/python3
''' Script that list Data in a SQLdb '''


if __name__ == '__main__':
    import MySQLdb
    import sys

    datB = MySQLdb.connect(host="localhost", port=3306,
                           user=sys.argv[1], passwd=sys.argv[2],
                           db=sys.argv[3])
    mouse = datB.cursor()
    #i_str = sys.argv[4]
    SQL_str = 'SELECT * FROM states WHERE name = %s\
    COLLATE latin1_general_cs ORDER BY id'
    mouse.execute(SQL_str, (sys.argv[4], ))
    table = mouse.fetchall()
    for state in table:
        print(state)
    mouse.close()
    datB.close()
