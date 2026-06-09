#!/usr/bin/python3
"""Module add the State object 'Louisiana"""


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

    new_state = State(name="Louisiana")  # Créer un nouvel objet State
    session.add(new_state)  # ajout à la session
    session.commit()  # save dans la base de donnée
    print(f'{new_state.id}')
    session.close()
