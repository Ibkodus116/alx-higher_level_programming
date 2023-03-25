#!/usr/bin/python3
"""
a script that takes in an argument and displays all
values in the states table of hbtn_0e_0_usa where
name matches the argument.
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    mysql_username = argv[1]
    mysql_password = argv[2]
    database_name = argv[3]
    state_name = argv[4]

    # Connect to SQL
    db = MySQLdb.connect(
        db=database_name,
        port=3306,
        user=mysql_username,
        passwd=mysql_password,
        )

    # Create a cursor for your connection
    cur = db.cursor()

    # Excecute MySQL Queries

    query = "SELECT * FROM states WHERE CONVERT name=%s;"
    cur.execute(query, (state_name,))


# Printing each row
    for row in cur.fetchall():
        print(row)
