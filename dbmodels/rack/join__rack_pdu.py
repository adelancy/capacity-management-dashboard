from extensions import sqldb
from rack import Rack
from pdu import PDU


join__rack_pdu = sqldb.table('join__rack_pdu', sqldb.Model.metadata,
    sqldb.Column('rack_id', sqldb.Integer, sqldb.ForeignKey('rack.id')),
    sqldb.Column('pdu_id', sqldb.Integer, sqldb.ForeignKey('pdu.id'))
)
