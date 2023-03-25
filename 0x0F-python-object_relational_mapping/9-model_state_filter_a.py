#!/usr/bin/python3

"""
A script that lists all State objects that
contain the letter a from the database hbtn_0e_6_usa
"""

from model_state import State, Base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sys import argv

if __name__ == "__main__":
    # Create an engine
    engine = create_engine(
        f'mysql+mysqldb://{argv[1]}:{argv[2]}@localhost:3306/{argv[3]}',
        pool_pre_ping=True
        )

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Create the Query session.query()

    states = session.query(State).order_by(State.id)
    # print(states)

    for state in states:
        if 'a' in state.name:
            print(f'{state.id}: {state.name}')
