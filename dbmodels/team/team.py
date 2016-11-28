from extensions.sql_alchemy import sqldb


class Team(sqldb.Model):
    __tablename__ = 'team'
    id = sqldb.Column(sqldb.Integer(), primary_key=True)
    name = sqldb.Column(sqldb.String(50), unique=True)
    group = sqldb.Column(sqldb.String(50))
    description = sqldb.Column(sqldb.Text())

    def __repr__(self):
        return '<{0} {1}>'.format(self.__class__.__name__, self.id)
