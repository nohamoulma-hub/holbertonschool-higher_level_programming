#!/usr/bin/python3
"""Module who list all states via SQLAlchemy"""


import sys
from model_state import Base, State
# importation du model de class à utiliser
from sqlalchemy import create_engine
# créer la connection à la base de donnée
from sqlalchemy.orm import sessionmaker
# permet de créer des sessions pour interroger la base

if __name__ == "__main__":
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    connection_url = (
        f'mysql+mysqldb://{mysql_username}:'
        f'{mysql_password}@localhost:3306/{database_name}'
        )
    engine = create_engine(connection_url, pool_pre_ping=True)

    Session = sessionmaker(bind=engine)  # on retourne une classe
    session = Session()  # on retourne la vraie session (une instance)

    result_query = session.query(State).order_by(State.id).all()
    # on stock le resultat de la requête dans une variable
    for state in result_query:
        print(f'{state.id}: {state.name}')
    # on affiche le résultat
    session.close()
