#!/usr/bin/python3
"""Module who list all cities by state"""


import sys
import MySQLdb

if __name__ == "__main__":
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    state_name = sys.argv[4]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=mysql_username,
        passwd=mysql_password,
        db=database_name
    )

    cursor = db.cursor()
    cursor.execute(
        """SELECT states.name, cities.name
        FROM cities
        INNER JOIN states ON states.id = cities.state_id
        WHERE states.name = %s
        ORDER BY cities.id ASC""", (state_name,)
    )
    cities_name = cursor.fetchall()

    cities = [row[1] for row in cities_name]
    print(",".join(cities))

    cursor.close()
    db.close()
