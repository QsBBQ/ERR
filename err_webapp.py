from flask import Flask, render_template, request, url_for, redirect, json

#Alchemy imports
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
# data model import
from err_model import Base, Location, Team, User

engine = create_engine('sqlite:///err_development.db')
Base.metadata.bind = engine
DBSession = scoped_session(sessionmaker(autocommit=False,
                                        autoflush=False,
                                        bind=engine))

s = DBSession()

app = Flask(__name__)


@app.route("/")
def index():
    return "Index Test"


@app.route("/users", methods=['GET'])
def users():
    locations = s.query(Location).all()
    return render_template('users_display.html',
                           locations=locations
                           )


@app.route("/users/save", methods=['POST'])
def users_save():
    for id, attribute in request.data:
        print(id, attribute)
    return redirect("/users")


@app.route("/events")
def events():
    return "Events test!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=5003)
