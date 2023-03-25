#!/usr/bin/python3

"""
a script that prints all City objects
from the database hbtn_0e_14_usa
"""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City


if __name__ == '__main__':
    # Create an engine here
    engine = create_engine(
        f'mysql+mysqldb://{argv[1]}:{argv[2]}@localhost:3306/{argv[3]}',
        pool_pre_ping=True
        )

    # Create a Session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query SQL with session.query
    cities = session.query(City, State).filter(City.state_id == State.id)

    for city, state in cities:
        print(f"{state.name}: ({city.id}) {city.name}")
