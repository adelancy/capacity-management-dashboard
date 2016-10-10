from dbmodels.data_center.rack.rack import Rack, RackUnit

from dbmodels.data_center.rack.pdu import PDU
from rest_api.resources.data_center.locations import LocationsCollection, Location
from rest_api.json_schemas.rack.schemas import RackSchema, RackUnitSchema


class RacksCollection(LocationsCollection):
    def __init__(self):
        super(RacksCollection, self).__init__()
        self.db_table = Rack
        self.resp_schema = RackSchema
        self.special_fields = ['location', 'pdus']

    def handle_special_fields(self, db_record, field, value, replace=False):
        if field == 'location':
            location = Location.query.filter_by(id=value, deleted=False).first()
            db_record.location = location
        if field == 'pdus':
            pdus = PDU.query.filter_by(id=value, deleted=False).all()
            db_record.pdus.extend(pdus)

    @classmethod
    def add_post_patch_args(cls, parser):
        parser.add_argument('vendor')
        parser.add_argument('model')
        parser.add_argument('serial-number', dest='serial_number')
        parser.add_argument('pdus')
        parser.add_argument('locations')


class RackUnitCollection(RacksCollection):
    def __init__(self):
        super(RackUnitCollection, self).__init__()
        self.db_table = RackUnit
        self.resp_schema = RackUnitSchema
        self.special_fields = ['rack']

    def handle_special_fields(self, db_record, field, value, replace=False):
        if field == 'rack':
            rack = Rack.query.filter_by(id=value, deleted=False).first()
            db_record.rack = rack

    @classmethod
    def add_post_patch_args(cls, parser):
        parser.add_argument('ru-start', dest='ru_start')
        parser.add_argument('ru-end', dest='ru_end')
