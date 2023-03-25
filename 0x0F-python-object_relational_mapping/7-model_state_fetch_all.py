#!/usr/bin/python3

from sys import argv
from model_state import State, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    user = argv[1]
    passwd = argv[2]
    db_name = argv[3]

    # create an Engine
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'
        .format(user, passwd, db_name),
        pool_pre_ping=True
        )

    # Create a Session
    Session = sessionmaker(bind=engine)
    session = Session()

    # query database for all state object
    states = session.query(State).order_by(State.id)

    for state in states:
        # print(f"{}: {}".format(state.id, state.name))
        print(f"{state.id}: {state.name}")
