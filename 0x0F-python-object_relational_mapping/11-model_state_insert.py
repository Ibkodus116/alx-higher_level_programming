#!/usr/bin/python3

"""
A script that adds the State object
“Louisiana” to the database hbtn_0e_6_usa
"""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == '__main__':

    # create Engine
    engine = create_engine(
        f'mysql+mysqldb://{argv[1]}:{argv[2]}@localhost:3306/{argv[3]}',
        pool_pre_ping=True
        )

    # Create session and bind
    Session = sessionmaker(bind=engine)
    session = Session()

    # SQL Queries that Adds
    new_state = State(name='Louisiana')
    session.add(new_state)

    session.commit()

    the_state = session.query(State).filter_by(name='Louisiana').first()

    print(the_state.id)
