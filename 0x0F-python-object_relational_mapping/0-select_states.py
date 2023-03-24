#!/usr/bin/python3
"""
This is a Script that query My SQL
"""
import MySQLdb
import sys
if __name__ == '__main__':
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    # connect to MySQL server
    db = MySQLdb.connect(
            host='localhost', user=mysql_username,
            passwd=mysql_password, db=database_name
            )

    # Create a cursor object
    cursor = db.cursor()

    # Execute SQL query
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    # Fecth all rows
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    cursor.close()
    db.close()
