#!/usr/bin/python3
"""Module getting all states"""


import sys
import MySQLdb

if __name__ == "__main__":
    mysql_username = sys.argv[1]  # root
    mysql_password = sys.argv[2]  # password
    database_name = sys.argv[3]  # name database

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=mysql_username,
        passwd=mysql_password,
        db=database_name)
    cur = db.cursor()  # je créer le stylo
    cur.execute(
        "SELECT * FROM states ORDER BY name ASC"
        )  # j'écris ma requête avec le stylo
    rows = cur.fetchall()  # récupère les résultats stockés
    for row in rows:  # Lit chaque résultat un à un 
        print(row)  # affiche les tupples
    cur.close()
    db.close()
