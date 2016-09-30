from extensions import sqldb
from location import Location  # Needed for relationship


class VM(sqldb.Model):

    __tablename__ = 'vm'

    id = sqldb.Column(sqldb.Integer, primary_key=True)
    hostname = sqldb.Column(sqldb.String)  # Data Center name or label
    vcpu = sqldb.Column(sqldb.String)
    ram = sqldb.Column(sqldb.String)
    group = sqldb.Column(sqldb.String)
    storage = sqldb.Column(sqldb.String)
    vmunit = sqldb.Column(sqldb.String)
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
