#!/usr/bin/python3
"""Module who print first State"""


import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    connection_url = (
        f'mysql+mysqldb://{mysql_username}:'
        f'{mysql_password}@localhost:3306/{database_name}'
        )
    engine = create_engine(connection_url, pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    result_query = session.query(State).order_by(State.id).first()
    if result_query:  # vérifie si le résultat de la table est vide ou non
        print(f'{result_query.id}: {result_query.name}')
    else:
        print("Nothing")
    session.close()
