from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from err_model import Base, User, Team, Location

engine = create_engine('sqlite:///err_development.db')

Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)

s=DBSession()

#tests checking the model
#clean ip develment db
for users in s.query(User).all():
    s.delete(users)
for teams in s.query(Team).all():
    s.delete(teams)
for locations in s.query(Location).all():
    s.delete(locations)
# for addresses in s.query(Address).all():
#     s.delete(addresses)
# for cities in s.query(City).all():
#     s.delete(cities)
# for races in s.query(Race).all():
#     s.delete(races)
s.commit()

print("Clean db test")
print(s.query(User).count() == 0)
print(s.query(Team).count() == 0)
print(s.query(Location).count() == 0)

# print(s.query(Address).count() == 0)
# print(s.query(City).count() == 0)
# print(s.query(Race).count() == 0)

#Location test
mylocation = Location(name = "Chicago",
                      comments = "chicago pizza"
                      )
s.add(mylocation)
s.commit()

print("Location add record")
print(s.query(Location).count() == 1)
print(s.query(Location).filter(Location.name == "Chicago").first().name == "Chicago")

#Team Test
myteam = Team(name = "Team1",
              description = "Team1 rocks!"
             )
s.add(myteam)
s.commit()

print("Team add record")
print(s.query(Team).count() == 1)
print(s.query(Team).filter(Team.name == "Team1").first().name == "Team1")

#User Test
myuser = User(name = "Chuck Norris",
              email = "chuck@norris.com",
              age = 50,
              status = "Confirmed",
              comments = "Chuck Norris is awesome"
             )
s.add(myuser)
s.commit()
print("User add record")
print(s.query(User).count() == 1)
print(s.query(User).filter(User.name == "Chuck Norris").first().name == "Chuck Norris")

#relationships
myuser.team_id = myteam.id
s.commit()
#
print(myuser.teams.name == "Team1")

myteam.location_id = mylocation.id
s.commit()
print(myteam.locations.name == "Chicago")

for locations in s.query(Location).all():
    print(locations.name == "Chicago")
    for teams in s.query(Team).all():
        print(teams.name == "Team1")
        for users in s.query(User).all():
            print(users.name == "Chuck Norris")
