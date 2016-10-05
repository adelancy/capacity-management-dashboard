from extensions.sql_alchemy import sqldb


class Circuit(sqldb.Model):
    __tablename__ = 'circuit'
    id = sqldb.Column(sqldb.Integer, primary_key=True)
    amperage = sqldb.Column(sqldb.Integer)
    voltage = sqldb.Column(sqldb.Integer)
    power_rating = sqldb.Column(sqldb.Integer)
    deleted = sqldb.Column(sqldb.Boolean)
    last_modified_dt = sqldb.Column(sqldb.DateTime)

    rack_id = sqldb.Column(sqldb.Integer, sqldb.ForeignKey('rack.id'))
    rack = sqldb.relationship('Rack', backref=sqldb.backref('rus', lazy='dynamic'))

    def __repr__(self):
        return '<{0} name: {1}>'.format(self.__class__.__name__, self.name)
