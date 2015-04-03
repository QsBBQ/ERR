from sqlalchemy import Table, Column, ForeignKey, DateTime, Integer, String
from sqlalchemy import Sequence
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref

from sqlalchemy import create_engine
import datetime

Base = declarative_base()

#The tables

#Seemed like the thing to do for many to many. ie. many users have many races
#association_table = Table('association', Base.metadata,
#    Column('users_id', Integer, ForeignKey('users.id')),
#    Column('races_id', Integer, ForeignKey('races.id'))
#)


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    name = Column(String(50), nullable=True)
    email = Column(String(50), nullable=True)
    age = Column(Integer, nullable=True)
    #address = Column(String(50), nullable=True)
    status = Column(String(50))
    comments = Column(String(250))
    create_date = Column(DateTime, default=datetime.datetime.now())
    last_modified = Column(DateTime, onupdate=datetime.datetime.now)
    #Relationships
    #A user has a address(worry about multiple address later)
    #address_id = Column(Integer, ForeignKey("addresses.id"))
    #A race has many users. Worry about this later
    #race = relationship("Race",
    #                    secondary=association_table,
    #                    backref="users")
    #Many users have a team
    team_id = Column(Integer, ForeignKey('teams.id'))

class Team(Base):
    __tablename__ = "teams"
    id = Column(Integer, Sequence('team_id_seq'), primary_key=True)
    name = Column(String(50), nullable=True)
    description = Column(String(250))
    create_date = Column(DateTime, default=datetime.datetime.now())
    last_modified = Column(DateTime, onupdate=datetime.datetime.now)
    #Relationships
    #A team has a location
    location_id = Column(Integer, ForeignKey('locations.id'))
    #A team has many users
    users = relationship("User", backref=backref('teams', order_by=id))

class Location(Base):
    __tablename__ = "locations"
    id = Column(Integer, Sequence('location_id_seq'), primary_key=True)
    name = Column(String(50), nullable=True)
    comments = Column(String(250))
    create_date = Column(DateTime, default=datetime.datetime.now())
    last_modified = Column(DateTime, onupdate=datetime.datetime.now)
    #Relationships
    teams = relationship("Team", backref=backref('locations', order_by=id))

#Simplied the example above but hope to explore more options.
#
# class Address(Base):
#     __tablename__ = "addresses"
#     id = Column(Integer, Sequence('address_id_seq'), primary_key=True)
#     street = Column(String(50))
#     #city = Column(String(50))
#     state = Column(String(50))
#     country = Column(String(50))
#     #Relationships
#     #A user has an address
#     users = relationship("User", backref=backref('addresses', order_by=id))
#     #An address has a city
#     city_id = Column(Integer, ForeignKey("cities.id"))
#
# class City(Base):
#     __tablename__ = "cities"
#     id = Column(Integer, Sequence('city_id_seq'), primary_key=True)
#     name = Column(String(50), nullable=True)
#     #This will probably expand
#     #Relationships
#     #An address has a city.
#     address = relationship("Address", backref=backref('cities', order_by=id))
#
# class State(Base):
#     #Not using currently
#     __tablename__ = "states"
#     id = Column(Integer, Sequence('state_id_seq'), primary_key=True)
#     name = Column(String(50), nullable=True)
#
# class Country(Base):
#     #Not using currently
#     __tablename__ = "countries"
#     id = Column(Integer, Sequence('country_id_seq'), primary_key=True)
#     name = Column(String(50), nullable=True)
#
# class Race(Base):
#     #Not using currently
#     __tablename__ = "races"
#     id = Column(Integer, Sequence('race_id_seq'), primary_key=True)
#     name = Column(String(50), nullable=True)
#     #Relationships
#     #A user has many races
#     #users = relationship("User", backref=backref('races', order_by=id))
#
# class RaceLeg(Base):
#     #Not using
#     __tablename__ = "race_legs"
#     id = Column(Integer, Sequence('raceleg_id_seq'), primary_key=True)
#     name = Column(String(50), nullable=True)
#
# class Expense(Base):
#     #Not using
#     __tablename__ = "expenses"
#     id = Column(Integer, Sequence('bank_id_seq'), primary_key=True)
#     name = Column(String(50), nullable=True)


engine = create_engine('sqlite:///err_development.db')

Base.metadata.create_all(engine)
