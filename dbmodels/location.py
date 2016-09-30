from extensions.sql_alchemy import sqldb


class Location(sqldb.Model):
    id = sqldb.Column(sqldb.INTEGER, primary_key=True)
    name = sqldb.Column(sqldb.String)  # Data Center name or label
    city = sqldb.Column(sqldb.String)
    region = sqldb.Column(sqldb.String)
    country = sqldb.Column(sqldb.String)
    deleted = sqldb.Column(sqldb.Boolean)
    last_modified_dt = sqldb.Column(sqldb.DateTime)

    def __repr__(self):
        return '<{0} name: {1}'.format(self.__class__.__name__, self.name)
