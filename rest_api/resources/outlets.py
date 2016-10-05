from racks import RacksCollection, Rack
from dbmodels.rack.outlets import Outlets, OutletType
from rest_api.json_schemas.rack.schemas import OutletTypeSchema, OutletSchema


class OutletCollection(RacksCollection):
    def __init__(self):
        super(OutletCollection, self).__init__()
        self.db_table = Outlets
        self.resp_schema = OutletSchema
        self.special_fields = ['rack']

    def handle_special_fields(self, db_record, field, value, replace=False):
        if field == 'rack':
            rack = Rack.query.filter_by(id=value, deleted=False).first()
            db_record.location = rack

    @classmethod
    def add_post_patch_args(cls, parser):
        parser.add_argument('total_count')
        parser.add_argument('total_free')
        parser.add_argument('rack')


class OutletTypeCollection(OutletCollection):
    def __init__(self):
        super(OutletTypeCollection, self).__init__()
        self.db_table = OutletType
        self.resp_schema = OutletTypeSchema

    @classmethod
    def add_post_patch_args(cls, parser):
        parser.add_argument('name')
        parser.add_argument('voltage')
        parser.add_argument('amperage')

