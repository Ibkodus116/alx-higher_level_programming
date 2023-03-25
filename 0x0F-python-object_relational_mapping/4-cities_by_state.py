#!/usr/bin/python3

import MySQLdb
from sys import argv

if __name__ == '__main__':
    # Create a Connection
    db = MySQLdb.connect(
        host='localhost',
        passwd=argv[2],
        user=argv[1],
        db=argv[3]
        )

    # Create a cursor
    cur = db.cursor()

    # execute the cursor
    cur.execute("""SELECT cities.id, cities.name, states.name
                FROM cities, states
                WHERE cities.state_id = states.id ORDER BY cities.id;
                """
                )

    # fecth all info and print
    for row in cur.fetchall():
        print(row)
