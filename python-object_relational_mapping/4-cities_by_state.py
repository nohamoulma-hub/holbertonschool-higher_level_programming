#!/usr/bin/python3
"""Module list Cities by states"""


import sys
import MySQLdb

if __name__ == "__main__":
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=mysql_username,
        passwd=mysql_password,
        db=database_name
    )

    cursor = db.cursor()
    cursor.execute(
        """SELECT cities.id, cities.name, states.name
        FROM cities
        INNER JOIN states ON states.id = cities.state_id
        ORDER BY cities.id ASC
        """
    )
    cities_name = cursor.fetchall()
    for citie in cities_name:
        print(citie)
    cursor.close()
    db.close()
