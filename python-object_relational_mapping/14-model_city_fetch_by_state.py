#!/usr/bin/python3
""" list all State objects from the database
"""

if __name__ == "__main__":
    import sys
    from model_state import Base, State
    from model_city import City
    from sqlalchemy.orm import sessionmaker

    from sqlalchemy import (create_engine)

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    res = session.query(State, City).filter(
        State.id == City.state_id).order_by(City.id).all()

    for s, c in res:
        print(f'{s.name}: ({c.id}) {c.name}')

    session.commit()
