"""MODELS FOR FYYUR APP."""

from sqlalchemy import Column, String, Integer, Boolean, DateTime, ARRAY, ForeignKey
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
db = SQLAlchemy()


def db_setup(app):
    """Set up DB."""
    app.config.from_object('config')
    db.app = app
    db.init_app(app)
    migrate = Migrate(app, db)
    return db

# ---------------------------------------------------------------------------#
# Models.
# ---------------------------------------------------------------------------#


class Venue(db.Model):
    """Parent Class for Venues."""

    __tablename__ = 'Venue'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True)
    city = db.Column(db.String(120))
    state = db.Column(db.String(120))
    address = db.Column(db.String(120))
    phone = db.Column(db.String(120))
    genres = db.Column(ARRAY(db.String))
    seeking_description = db.Column(db.String(500), default='')
    seeking_talent = db.Column(db.Boolean, default=False)
    facebook_link = db.Column(db.String(120))
    image_link = db.Column(db.String(500))
    website = db.Column(String(120))
    shows = db.relationship('Show', backref='Venue', lazy='dynamic')

    def __init__(self, name, genres, address, city, state, phone, website,
                 facebook_link, image_link, seeking_talent=False,
                 seeking_description=" "):
        """Initialize Venues."""
        self.name = name
        self.genres = genres
        self.city = city
        self.state = state
        self.address = address
        self.phone = phone
        self.seeking_description = seeking_description
        self.image_link = image_link
        self.facebook_link = facebook_link
        self.website = website

    def insert(self):
        """Create new Venue entry in database."""
        db.session.add(self)
        db.session.commit()

    def update(self):
        """Update Venue entry in database."""
        db.session.commit()

    def short(self):
        """Return abridged details."""
        return{
            'id': self.id,
            'name': self.name,
        }

    def long(self):
        """Return details."""
        print(self)
        return{
            'id': self.id,
            'name': self.name,
            'city': self.city,
            'state': self.state,
        }

    def details(self):
        """Return all venue information."""
        return{
            'id': self.id,
            'name': self.name,
            'genres': self.genres,
            'address': self.address,
            'city': self.city,
            'state': self.state,
            'phone': self.phone,
            'website': self.website,
            'facebook_link': self.facebook_link,
            'seeking_talent': self.seeking_talent,
            'seeking_description': self.seeking_description,
            'image_link': self.image_link
        }


class Artist(db.Model):
    """Parent Class for Artists."""

    __tablename__ = 'Artist'
    id = Column(Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True)
    city = db.Column(db.String(120))
    state = db.Column(db.String(120))
    phone = db.Column(db.String(120))
    genres = db.Column(ARRAY(db.String))
    seeking_venue = db.Column(db.Boolean, default=False)
    seeking_description = db.Column(db.String(120), default=' ')
    facebook_link = db.Column(db.String(120))
    image_link = db.Column(db.String(500))
    website = db.Column(db.String(120))
    shows = db.relationship('Show', backref='Artist', lazy=True)

    def __init__(self, name, genres, city, state, phone, image_link,
                 website, facebook_link, seeking_venue=False,
                 seeking_description=""):
        """Initialize Artists."""
        self.name = name
        self.genres = genres
        self.city = city
        self.state = state
        self.phone = phone
        self.seeking_description = seeking_description
        self.facebook_link = facebook_link
        self.image_link = image_link
        self.website = website

    def insert(self):
        """Create new artist entry."""
        db.session.add(self)
        db.session.commit()

    def update(self):
        """Update artist entry."""
        db.session.commit()

    def short(self):
        """Return abridged artist details."""
        return{
            'id': self.id,
            'name': self.name,
        }

    def details(self):
        """Return all artist info."""
        return{
            'id': self.id,
            'name': self.name,
            'genres': self.genres,
            'city': self.city,
            'state': self.state,
            'phone': self.phone,
            'website': self.website,
            'facebook_link': self.facebook_link,
            'seeking_venue': self.seeking_venue,
            'seeking_description': self.seeking_description,
            'image_link': self.image_link,

        }


class Show(db.Model):
    """Parent Class for Shows."""

    __tablename__ = 'Show'
    id = db.Column(Integer, primary_key=True)
    venue_id = db.Column(Integer, ForeignKey(Venue.id), nullable=False)
    artist_id = db.Column(Integer, ForeignKey(Artist.id), nullable=False)
    start_time = db.Column(String(), nullable=False)

    def __init__(self, venue_id, artist_id, start_time):
        """Initialize Show."""
        self.venue_id = venue_id
        self.artist_id = artist_id
        self.start_time = start_time

    def insert(self):
        """Create new show entry."""
        db.session.add(self)
        db.session.commit()

    def detail(self):
        """Return Show info."""
        return{
            'venue_id': self.venue_id,
            'venue_name': self.Venue.name,
            'artist_id': self.artist_id,
            'artist_name': self.Artist.name,
            'artist_image_link': self.Artist.image_link,
            'start_time': self.start_time
        }

    def artist_details(self):
        """Return artist details."""
        return{
            'artist_id': self.artist_id,
            'artist_name': self.Artist.name,
            'artist_image_link': self.Artist.image_link,
            'start_time': self.start_time

        }

    def venue_details(self):
        """Return venue details."""
        return{
            'venue_id': self.venue_id,
            'venue_name': self.Venue.name,
            'venue_image_link': self.Venue.image_link,
            'start_time': self.start_time

        }
