from extensions.sql_alchemy import sqldb


class PhysicalRequirement(sqldb.Model):
    __tablename__ = 'physical_requirement'
    id = sqldb.Column(sqldb.Integer(), primary_key=True)
    name = sqldb.Column(sqldb.String(50))
    model = sqldb.Column(sqldb.String(50))
    vendor = sqldb.Column(sqldb.String(50))
    part_number = sqldb.Column(sqldb.String(50))
    procs = sqldb.Column(sqldb.Integer())
    ram = sqldb.Column(sqldb.Integer())
    storage_capacity = sqldb.Column(sqldb.Integer())  # GB
    storage_type = sqldb.Column(sqldb.String(50))
    rack_units = sqldb.Column(sqldb.Integer())
    description = sqldb.Column(sqldb.Text())
    os_type = sqldb.Column(sqldb.String(50))
    env = sqldb.Column(sqldb.String(50))

    team_id = sqldb.Column(sqldb.Integer(), sqldb.ForeignKey('team.id'))
    team = sqldb.relationship(
        'Team',
        backref=sqldb.backref('virtual_requirements', lazy='dynamic')
    )

    # Many to One Relationship with Location Table
    location_id = sqldb.Column(sqldb.Integer, sqldb.ForeignKey('location.id'))
    location = sqldb.relationship('Location', backref=sqldb.backref('bm_reqs', lazy='dynamic'))

    def __repr__(self):
        return '<{0} {1}'.format(self.__class__.__name__, self.id)
