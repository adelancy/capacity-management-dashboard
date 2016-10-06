from extensions.sql_alchemy import sqldb


class Wireless(sqldb.Model):
    __tablename__ = 'wireless'

    id = sqldb.Column(sqldb.Integer, primary_key=True)
    hostname = sqldb.Column(sqldb.String(70))
    model = sqldb.Column(sqldb.String(70))
    vendor = sqldb.Column(sqldb.String(70))
    part_number = sqldb.Column(sqldb.String(50))
    serial_number = sqldb.Column(sqldb.String(70))
    description = sqldb.Column(sqldb.Text())
    env = sqldb.Column(sqldb.String(70))  # Todo: Convert to relationship
    device_type = sqldb.Column(sqldb.String(70))

    rack_id = sqldb.Column(sqldb.Integer, sqldb.ForeignKey('rack.id'))
    rack = sqldb.relationship('Rack', backref=sqldb.backref('rus', lazy='dynamic'))

    def __repr__(self):
        return '<{0} {1}'.format(self.__class__.__name__, self.id)

