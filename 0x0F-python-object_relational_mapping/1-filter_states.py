#!/usr/bin/python3
"""
A script that lists all states with a name starting
with N (upper N) from the database hbtn_0e_0_usa
"""

import MySQLdb
import sys

if __name__ == '__main__':
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    # Connect to SQL
    db = MySQLdb.connect(
        host='localhost',
        user=mysql_username,
        passwd=mysql_password,
        db=database_name
    )

    # Create A Cursor
    cur = db.cursor()

    # Execute With the needed Query
    cur.execute("SELECT id, name FROM states WHERE name LIKE 'N%' ORDER BY id ASC")

    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    db.close()
