from extensions.sql_alchemy import sqldb


class PDU(sqldb.Model):
    __tablename__ = 'pdu'
    id = sqldb.Column(sqldb.Integer, primary_key=True)
    name = sqldb.Column(sqldb.String, nullable=False)
    vendor = sqldb.Column(sqldb.String)
    total_count = sqldb.Column(sqldb.Integer)
    total_free = sqldb.Column(sqldb.Integer)
    deleted = sqldb.Column(sqldb.Boolean)
    last_modified_dt = sqldb.Column(sqldb.DateTime)

    type_id = sqldb.Column(sqldb.Integer, sqldb.ForeignKey('outlet_type.id'))
    type = sqldb.relationship('OutletType', backref=sqldb.backref('outlet_type', lazy='dynamic'))

    def __repr__(self):
        return '<{0} name: {1}'.format(self.__class__.__name__, self.name)
