from extensions.sql_alchemy import sqldb
from location import Location  # Needed for relationship


class VM(sqldb.Model):

    __tablename__ = 'vm'

    id = sqldb.Column(sqldb.Integer, primary_key=True)
    hostname = sqldb.Column(sqldb.String)  # Data Center name or label
    vcpu = sqldb.Column(sqldb.Integer)
    ram = sqldb.Column(sqldb.Integer)
    group = sqldb.Column(sqldb.String)
    storage = sqldb.Column(sqldb.Integer)
    vmunit = sqldb.Column(sqldb.Integer)
    role = sqldb.Column(sqldb.String)
    environment = sqldb.Column(sqldb.String)
    cluster = sqldb.Column(sqldb.String)
    deleted = sqldb.Column(sqldb.Boolean)
    last_modified_dt = sqldb.Column(sqldb.DateTime)
    # Many to One Relationship with Location Table
    location_id = sqldb.Column(sqldb.Integer, sqldb.ForeignKey('location.id'))
    location = sqldb.relationship('Location', backref=sqldb.backref('vms', lazy='dynamic'))

    def __repr__(self):
        return '<{0} name: {1}'.format(self.__class__.__name__, self.name)
