from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy_utils import PhoneNumberType
from datetime import datetime


db = SQLAlchemy()
now = datetime.now()


class Venue(db.Model):
    __tablename__ = 'venues'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    city = db.Column(db.String(120))
    state = db.Column(db.String(120))
    address = db.Column(db.String(120))
    phone = db.Column(PhoneNumberType())
    website = db.Column(db.String(120))
    image_link = db.Column(db.String(500))
    facebook_link = db.Column(db.String(120))
    seeking_talent = db.Column(db.Boolean)
    seeking_description = db.Column(db.String(150))
    genres = db.Column(db.ARRAY(db.String(120)))
    shows = db.relationship('Show', backref='venue', lazy=True)


# TODO: implement any missing fields, as a database migration using Flask-Migrate


class Artist(db.Model):
    __tablename__ = 'artists'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    city = db.Column(db.String(120))
    state = db.Column(db.String(120))
    phone = db.Column(PhoneNumberType())
    genres = db.Column(db.ARRAY(db.String(120)))
    website = db.Column(db.String(120))
    image_link = db.Column(db.String(500))
    facebook_link = db.Column(db.String(120))
    seeking_venue = db.Column(db.Boolean(True))
    seeking_description = db.Column(db.String(250))
    shows = db.relationship('Show', backref='artist',
                            lazy=True, cascade='delete-orphan')

    # TODO: implement any missing fields, as a database migration using Flask-Migrate

# TODO: Implement Show and Artist models, and complete all model relationships and properties, as a database migration.


class Show(db.Model):
    __tablename__ = 'shows'
    id = db.Column(db.Integer, primary_key=True)
    start_time = db.Column(db.DateTime())
    artist_id = db.Column(db.Integer, db.ForeignKey('artists.id'))
    venue_id = db.Column(db.Integer, db.ForeignKey('venues.id'))


def get_artists_shows(db, artist_id, flag=True):
    if flag:
        shows_query = db.session.query(Show).join(Artist).filter(
            Show.artist_id == artist_id).filter(Show.start_time < now).all()

    else:
        shows_query = db.session.query(Show).join(Artist).filter(
            Show.artist_id == artist_id).filter(Show.start_time > now).all()

    shows = []

    for show in shows_query:
        shows.append({"artist_id": show.artist.id,
                      "artist_name": show.artist.name, "artist_image_link": show.artist.image_link, "start_time": show.start_time, })
    return shows


def get_venues_shows(db, venue_id, flag=True):
    if flag:
        shows_query = db.session.query(Show).join(Venue).filter(
            Show.venue_id == venue_id).filter(Show.start_time < now).all()

    else:
        shows_query = db.session.query(Show).join(Venue).filter(
            Show.venue_id == venue_id).filter(Show.start_time > now).all()
    shows = []
    for show in shows_query:
        shows.append({"artist_id": show.artist.id,
                      "artist_name": show.artist.name, "artist_image_link": show.artist.image_link, "start_time": show.start_time, })
    return shows
