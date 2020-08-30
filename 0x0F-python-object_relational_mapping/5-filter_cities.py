#!/usr/bin/python3
''' Script that list Data in a SQLdb '''


if __name__ == '__main__':
    import MySQLdb
    import sys

    datB = MySQLdb.connect(host="localhost", port=3306,
                           user=sys.argv[1], passwd=sys.argv[2],
                           db=sys.argv[3])
    mouse = datB.cursor()
    SQL_str = 'SELECT cities.name FROM cities INNER JOIN states ON\
    cities.state_id = states.id WHERE states.name = %s ORDER BY cities.id'
    mouse.execute(SQL_str, (sys.argv[4], ))
    table = mouse.fetchall()
    flag = 0
    for state in table:
        if flag != 0:
            print(", ", end="")
        flag = 1
        print("%s" % state, end="")
    print("")
    mouse.close()
    datB.close()
