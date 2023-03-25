#!/usr/bin/python3
"""
A script that takes in the name of a state
as an argument and lists all cities of that
state, using the database hbtn_0e_4_usa
"""
import MySQLdb
from sys import argv

if __name__ == '__main__':
    # Create a connection
    db = MySQLdb.connect(port=3306, user=argv[1], passwd=argv[2], db=argv[3])

    # create a cursor
    cur = db.cursor()

    # use the cursor to execute

    cur.execute("""
                SELECT cities.name FROM cities
                WHERE cities.state_id = (
                SELECT id FROM states WHERE name = %s);
                """, (argv[4],)
                )

    # fetch the row and print
    rows = cur.fetchall()
    output = ", ".join(row[0] for row in rows[:-1])
    if output:
        output += ", "
    output += rows[-1][0]
    print(output)
