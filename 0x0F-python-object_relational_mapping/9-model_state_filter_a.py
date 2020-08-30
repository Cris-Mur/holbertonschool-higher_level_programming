#!/usr/bin/python3
'''
Script that list Data in a SQLdb
using SQLAlchemy
'''
import sys
from sqlalchemy import (create_engine)
from model_state import Base, State
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':

    user = sys.argv[1]
    passwd = sys.argv[2]
    db = sys.argv[3]

    datB = create_engine(
        "mysql+mysqldb://{}:{}@localhost:3306/{}".format(user,
                                                         passwd,
                                                         db),
        pool_pre_ping=True)

    Session = sessionmaker(bind=datB)
    session = Session()

    for state in session.query(State).filter(State.name.contains(
            'a')).order_by(State.id).all():
        print("{:d}: {:s}".format(state.id, state.name))

    session.close()
