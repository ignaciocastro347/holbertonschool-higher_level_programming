#!/usr/bin/python3
""" list all State objects from the database
"""

if __name__ == "__main__":
	import sys
	from model_state import Base, State
	from sqlalchemy.orm import sessionmaker

	from sqlalchemy import (create_engine)

	engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
		sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
	Base.metadata.create_all(engine)

	Session = sessionmaker(bind=engine)
	session = Session()

	state = State(id=2, name="New Mexico")
	session.add(state)
	session.commit()
