from extensions.sql_alchemy import sqldb


class VirtualRequirement(sqldb.Model):
    __tablename__ = 'virtual_requirement'
    id = sqldb.Column(sqldb.Integer(), primary_key=True)
    name = sqldb.Column(sqldb.String(50))
    vm_type = sqldb.Column(sqldb.String(50))
    os_type = sqldb.Column(sqldb.String(50))
    cluster = sqldb.Column(sqldb.String(50))
    vcpu = sqldb.Column(sqldb.Integer())
    ram = sqldb.Column(sqldb.Integer())
    vmunits = sqldb.Column(sqldb.Integer())
    description = sqldb.Column(sqldb.Text())

    team_id = sqldb.Column(sqldb.Integer(), sqldb.ForeignKey('team.id'))
    team = sqldb.relationship(
        'Team',
        backref=sqldb.backref('virtual_requirements', lazy='dynamic')
    )

    def __repr__(self):
        return '<{0} {1}'.format(self.__class__.__name__, self.id)
