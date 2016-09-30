from extensions import sqldb
from rack import Rack


class OutletType(sqldb.Model):
    __tablename__ = 'outlet_type'
    id = sqldb.Column(sqldb.Integer, primary_key=True)
    name = sqldb.Column(sqldb.String)
    voltage = sqldb.Column(sqldb.Integer)
    amperage = sqldb.Column(sqldb.Integer)
    deleted = sqldb.Column(sqldb.Boolean)
    last_modified_dt = sqldb.Column(sqldb.DateTime)

    def __repr__(self):
        return '<{0} name: {1}'.format(self.__class__.__name__, self.name)


class Outlet(sqldb.Model):
    __tablename__ = 'outlet'
    id = sqldb.Column(sqldb.Integer, primary_key=True)
    total_count = sqldb.Column(sqldb.Integer)
    total_free = sqldb.Column(sqldb.Integer)
    deleted = sqldb.Column(sqldb.Boolean)
    last_modified_dt = sqldb.Column(sqldb.DateTime)

    rack_id = sqldb.Column(sqldb.Integer, sqldb.ForeignKey('rack.id'))
    rack = sqldb.relationship('Rack', backref=sqldb.backref('rus', lazy='dynamic'))

    type_id = sqldb.Column(sqldb.Integer, sqldb.ForeignKey('outlet_type.id'))
    type = sqldb.relationship('Outlet', backref=sqldb.backref('outlet', lazy='dynamic'))

    def __repr__(self):
        return '<{0} name: {1}'.format(self.__class__.__name__, self.name)
