#!/usr/bin/python3
''' create State with City '''


from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City


if __name__ == '__main__':
    datB = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
            argv[1], argv[2], argv[3]))
    Base.metadata.create_all(datB)
    InstanceSession = sessionmaker(bind=datB)
    session = InstanceSession()

    First = State(name='California')
    Second = City(name='San Francisco', state=First)
    session.add(Second)
    session.commit()

    session.close()
