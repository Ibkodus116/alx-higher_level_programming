#!/usr/bin/python3
"""
A script that prints the first
State object from the database hbtn_0e_6_usa
"""


from model_state import Base, State
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    # create Engine
    engine = create_engine(
        f"mysql+mysqldb://{argv[1]}:{argv[2]}@localhost:3306/{argv[3]}",
        pool_pre_ping=True
        )

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query for MySQL
    state = session.query(State).order_by(State.id).first()

    if state:
        print(f"{state.id}: {state.name}")
    else:
        print('Nothing')
