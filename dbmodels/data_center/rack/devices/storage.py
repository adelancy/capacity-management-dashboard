from extensions.sql_alchemy import sqldb


class Storage(sqldb.Model):
    __tablename__ = 'storage'

    id = sqldb.Column(sqldb.Integer, primary_key=True)
    hostname = sqldb.Column(sqldb.String)
    model = sqldb.Column(sqldb.String)
    vendor = sqldb.Column(sqldb.String)
    part_number = sqldb.Column(sqldb.String)
    serial_number = sqldb.Column(sqldb.String)
    description = sqldb.Column(sqldb.String)
    total_capacity = sqldb.Column(sqldb.Integer)
    free_capacity = sqldb.Column(sqldb.Integer)
    env = sqldb.Column(sqldb.String)  # Todo: Convert to relationship

    rack_id = sqldb.Column(sqldb.Integer, sqldb.ForeignKey('rack.id'))
    rack = sqldb.relationship('Rack', backref=sqldb.backref('rus', lazy='dynamic'))

    def __repr__(self):
        return '<{0} {1}'.format(self.__class__.__name__, self.id)

