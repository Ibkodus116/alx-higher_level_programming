#!/usr/bin/python3

"""
A script that changes the name of a State
object from the database hbtn_0e_6_usa
"""

from sys import argv
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model_state import State, Base

if __name__ == '__main__':
    # create an engine
    engine = create_engine(
        f'mysql+mysqldb://{argv[1]}:{argv[2]}@localhost:3306/{argv[3]}',
        pool_pre_ping=True
        )
    # Start a session with sessionmaker

    Session = sessionmaker(bind=engine)
    session = Session()

    # Make Queries
    new_name = session.query(State).filter_by(id=2).first()

    new_name.name = 'New Mexico'
    session.commit()

    session.close()
