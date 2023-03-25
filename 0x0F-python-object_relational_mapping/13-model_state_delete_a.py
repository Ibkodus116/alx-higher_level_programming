#!/usr/bin/python3
"""
A script that deletes all State objects
with a name containing the letter a from
the database hbtn_0e_6_usa
"""

from sys import argv
from model_state import State, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    # create an engine
    engine = create_engine(
        f'mysql+mysqldb://{argv[1]}:{argv[2]}@localhost:3306/{argv[3]}',
        pool_pre_ping=True
        )

    # Start a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query the SQL with session.query
    a_states = session.query(State).filter(State.name.like("%a%")).all()

    for st in a_states:
        session.delete(st)

    session.commit()
