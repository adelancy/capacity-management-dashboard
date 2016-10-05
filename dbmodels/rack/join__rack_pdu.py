from extensions.sql_alchemy import sqldb

join__rack_pdu = sqldb.Table('join__rack_pdu', sqldb.metadata,
    sqldb.Column('rack_id', sqldb.Integer, sqldb.ForeignKey('rack.id')),
    sqldb.Column('pdu_id', sqldb.Integer, sqldb.ForeignKey('pdu.id'))
)
