#!/usr/bin/python3
''' Script that list Data in a SQLdb '''
import sys
from sqlalchemy import create_engine
from model_state import State
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    user = sys.argv[1]
    passwd = sys.argv[2]
    db = sys.argv[3]

    datB = create_engine(
        "mysql+mysqldb://{}:{}@localhost:3306/{}".format(user, passwd, db))

    Session = sessionmaker(bind=datB)
    session = Session()

    for point in session.query(State).order_by(State.id):
        print("{}: {}".format(point.id, point.name))

    session.close()
