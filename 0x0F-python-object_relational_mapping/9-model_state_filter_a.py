#!/usr/bin/python3

"""
print first state
"""

import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv
from model_state import Base, State


if __name__ == "__main__":
    eng = create_engine("mysql+mysqldb://{}:{}@localhost/{}".format(argv[1],
                                                                    argv[2],
                                                                    argv[3]))
    Base.metadata.create_all(eng)
    Session = sessionmaker(bind=eng)
    session = Session()
    s = '%a%'
    st = session.query(State).filter(State.name.like(s)).order_by(State.id).first()
    for states in st:
        print("{}: {}".format(st.id, st.name))
    session.close()
