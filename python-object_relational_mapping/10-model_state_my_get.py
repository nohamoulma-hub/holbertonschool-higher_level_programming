#!/usr/bin/python3
"""Module who print the State object"""


import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    state_name_to_search = sys.argv[4]

    connection_url = (
        f'mysql+mysqldb://{mysql_username}:'
        f'{mysql_password}@localhost:3306/{database_name}'
    )

    engine = create_engine(connection_url, pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    result_query = (session.query(State)
                    .order_by(State.id)
                    .filter(State.name == state_name_to_search)
                    .first())
    if result_query:
        print(f'{result_query.id}')
    else:
        print('Not found')
    session.close()
