#!/usr/bin/python3
"""Module who list all State that contain the letter 'a'"""


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

    result_query = (session.query(State)
                    .order_by(State.id)
                    .filter(State.name.like('%a%'))
                    .all())

    for state in result_query:
        print(f'{state.id}: {state.name}')
    session.close()
