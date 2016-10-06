from extensions.sql_alchemy import sqldb


class BMHost(sqldb.Model):
    __tablename__ = 'bm_host'

    id = sqldb.Column(sqldb.Integer, primary_key=True)
    name = sqldb.Column(sqldb.String)
    model = sqldb.Column(sqldb.String)
    vendor = sqldb.Column(sqldb.String)
    part_number = sqldb.Column(sqldb.String)
    serial_number = sqldb.Column(sqldb.String)
    procs = sqldb.Column(sqldb.Integer)
    description = sqldb.Column(sqldb.String)
    sfp_type = sqldb.Column(sqldb.String)
    power_draw = sqldb.Column(sqldb.String)
    network_ports = sqldb.Column(sqldb.String)
    mgmt_ports = sqldb.Column(sqldb.String)
    group = sqldb.Column(sqldb.String)  # Todo: replace with a team relationship
    ram = sqldb.Column(sqldb.Integer)
    storage_capacity = sqldb.Column(sqldb.Integer)
    vm_count = sqldb.Column(sqldb.Integer)
    env = sqldb.Column(sqldb.String)  # Todo: Convert to relationship

    rack_id = sqldb.Column(sqldb.Integer, sqldb.ForeignKey('rack.id'))
    rack = sqldb.relationship('Rack', backref=sqldb.backref('rus', lazy='dynamic'))

    def __repr__(self):
        return '<{0} {1}'.format(self.__class__.__name__, self.id)

