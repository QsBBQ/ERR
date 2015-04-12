

# Think about abstracting this stuff
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from err_model import Base, User, Team, Location

engine = create_engine('sqlite:///err_development.db')

Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)

s = DBSession()

import random
from faker import Factory
faker = Factory.create()

# clean ip develment db
for users in s.query(User).all():
    s.delete(users)
for teams in s.query(Team).all():
    s.delete(teams)
for locations in s.query(Location).all():
    s.delete(locations)
s.commit()


location_list = ["Chicago", "New York", "Los Angeles", "Atlanta", "Seattle"]

for locations in location_list:
    location = Location(name=locations,
                        comments=faker.bs())
    s.add(location)
    s.commit()
    for n in range(0, 10):
        team = Team(name=faker.company(),
                    description=faker.bs(),
                    locations=location)
        s.add(team)
        s.commit()
        for n in range(0, 100):
            user = User(name=faker.name(),
                        email=faker.email(),
                        age=random.randint(18, 65),
                        status="Confirmed",
                        comments=faker.bs(),
                        teams=team)

            s.add(user)
            s.commit()


# print(s.query(Location).count() == 5)
