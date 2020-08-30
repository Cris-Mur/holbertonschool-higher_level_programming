#!/usr/bin/python3
''' Script that list Data in a SQLdb '''
import sys
from sqlalchemy import (create_engine)
from model_state import Base, State
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':

    user=sys.argv[1]
    passwd=sys.argv[2]
    db=sys.argv[3]

    datB = create_engine(
        "mysql+mysqldb://{}:{}@localhost:3306/{}".format(user,
                                                         passwd,
                                                         db),
        pool_pre_ping=True)

    Session = sessionmaker(bind=datB)
    session = Session()

    query = session.query(State).filter(State.id)
    table = query.first()
    if not table:
        print("{}".format("Nothing"))
    else:
        print("{:d}: {:s}".format(table.id, table.name))

    session.close()
