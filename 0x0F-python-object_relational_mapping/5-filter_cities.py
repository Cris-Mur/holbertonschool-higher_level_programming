#!/usr/bin/python3
''' Script that list Data in a SQLdb '''


if __name__ == '__main__':
    import MySQLdb
    import sys

    datB = MySQLdb.connect(host="localhost", port=3306,
                           user=sys.argv[1], passwd=sys.argv[2],
                           db=sys.argv[3])
    mouse = datB.cursor()
    SQL_str = 'SELECT cities.name FROM cities, states WHERE states.name = %s\
    AND states.id = cities.state_id ORDER BY id'
    mouse.execute(SQL_str, (sys.argv[4], ))
    table = mouse.fetchall()
    for state in table:
        print(state)
    mouse.close()
    datB.close()
