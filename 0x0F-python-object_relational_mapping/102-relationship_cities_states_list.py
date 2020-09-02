#!/usr/bin/python3
''' Script that list Data in a SQLdb '''
import sys
from sqlalchemy import (create_engine)
from relationship_state import Base, State
from sqlalchemy.orm import sessionmaker
from relationship_city import City

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

    cosos = session.query(City).order_by(City.id).all()
    for city in cosos:
            print("{}: {} -> {}".format(city.id, city.name, city.state.name))

    session.close()
