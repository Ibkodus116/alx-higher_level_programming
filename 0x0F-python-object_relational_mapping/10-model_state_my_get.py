#!/usr/bin/python3

"""
A script that prints the State object
with the name passed as argument from
the database hbtn_0e_6_usa
"""

from model_state import State, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv

if __name__ == '__main__':
    # Create the engine
    engine = create_engine(
        f'mysql+mysqldb://{argv[1]}:{argv[2]}@localhost:3306/{argv[3]}',
        pool_pre_ping=True
        )

    # Start a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query SQL
    states = session.query(State)
    found = ''
    for state in states:
        if state.name == argv[4]:
            found = state.id
            print(f'{state.id}')

    if not found:
        print('Not found')
