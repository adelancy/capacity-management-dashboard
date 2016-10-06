from extensions.sql_alchemy import sqldb


class License(sqldb.Model):
    id = sqldb.Column(sqldb.Integer, primary_key=True)
    vendor = sqldb.Column(sqldb.String)  # Data Center name or label
    model = sqldb.Column(sqldb.String)
    name = sqldb.Column(sqldb.String)
    type = sqldb.Column(sqldb.String)
    quantity = sqldb.Column(sqldb.String)
    in_use = sqldb.Column(sqldb.String)
    expiration_dt = sqldb.Column(sqldb.DateTime)
    deleted = sqldb.Column(sqldb.Boolean)
    last_modified_dt = sqldb.Column(sqldb.DateTime)
    # Many to One Relationship with Location Table
    location_id = sqldb.Column(sqldb.Integer, sqldb.ForeignKey('location.id'))
    location = sqldb.relationship('Location', backref=sqldb.backref('licenses', lazy='dynamic'))

    def __repr__(self):
        return '<{0} name: {1}>'.format(self.__class__.__name__, self.name)
