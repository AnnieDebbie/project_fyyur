from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy_utils import PhoneNumberType
from datetime import datetime


db = SQLAlchemy()
now = datetime.now()


def create_db(app):
    db.app = app
    db.init_app(app)
    migrate = Migrate(app, db, compare_type=True)

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
    shows = db.relationship('Show', backref='VenueShows', lazy='dynamic')

    def past_shows(self):
        return self.shows.filter(Show.start_time < now)

    def upcoming_shows(self):
        return self.shows.filter(Show.start_time > now)

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
    shows = db.relationship('Show', backref='ArtistShows',
                            lazy='dynamic', cascade='delete-orphan')

    def past_shows(self):
        return self.shows.filter(Show.start_time < now)

    def upcoming_shows(self):
        return self.shows.filter(Show.start_time > now)

    # TODO: implement any missing fields, as a database migration using Flask-Migrate

# TODO: Implement Show and Artist models, and complete all model relationships and properties, as a database migration.


class Show(db.Model):
    __tablename__ = 'shows'
    id = db.Column(db.Integer, primary_key=True)
    start_time = db.Column(db.DateTime())
    artist_id = db.Column(db.Integer, db.ForeignKey('artists.id'))
    venue_id = db.Column(db.Integer, db.ForeignKey('venues.id'))
    artist = db.relationship('Artist', backref='ShowArtist', )
    venue = db.relationship('Venue', backref='ShowVenue', )
    artist_name = association_proxy('artist', 'name')
    venue_name = association_proxy('venue', 'name')