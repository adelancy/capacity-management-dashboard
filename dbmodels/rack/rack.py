from extensions import sqldb
from dbmodels.location import Location  # Needed for relationship
from join__rack_pdu import join__rack_pdu, PDU


class Rack(sqldb.Model):

    __tablename__ = 'rack'

    id = sqldb.Column(sqldb.Integer, primary_key=True)
    hostname = sqldb.Column(sqldb.String)
    vendor = sqldb.Column(sqldb.String)
    model = sqldb.Column(sqldb.String)
    serial_number = sqldb.Column(sqldb.String)
    deleted = sqldb.Column(sqldb.Boolean)
    last_modified_dt = sqldb.Column(sqldb.DateTime)
    # Many to One Relationship with Location Table
    location_id = sqldb.Column(sqldb.Integer, sqldb.ForeignKey('location.id'))
    location = sqldb.relationship('Location', backref=sqldb.backref('racks', lazy='dynamic'))
    # Many to Many with Rack Table --> PDU may power more than one rack
    pdus = sqldb.relationship(
        'PDU',
        secondary=join__rack_pdu,
        backref=sqldb.backref('racks', lazy='dynamic')
    )

    def __repr__(self):
        return '<{0} name: {1}'.format(self.__class__.__name__, self.name)


class RackUnit(sqldb.Model):
    __tablename__ = 'rack_unit'
    id = sqldb.Column(sqldb.Integer, primary_key=True)
    ru_start = sqldb.Column(sqldb.Integer)
    ru_end = sqldb.Column(sqldb.Integer)
    rack_id = sqldb.Column(sqldb.Integer, sqldb.ForeignKey('rack.id'))
    rack = sqldb.relationship('Rack', backref=sqldb.backref('rus', lazy='dynamic'))
    deleted = sqldb.Column(sqldb.Boolean)
    last_modified_dt = sqldb.Column(sqldb.DateTime)

    def __repr__(self):
        return '<{0} name: {1}'.format(self.__class__.__name__, self.name)
