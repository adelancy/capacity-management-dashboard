from dbmodels.data_center.license import License
from locations import LocationsCollection, Location
from rest_api.json_schemas.vm import VMSchema


class LicenseCollection(LocationsCollection):
    def __init__(self):
        super(LicenseCollection, self).__init__()
        self.db_table = License
        self.resp_schema = VMSchema
        self.special_fields = ['location']

    def handle_special_fields(self, db_record, field, value, replace=False):
        if field == 'location':
            location = Location.query.filter_by(id=value, deleted=False).first()
            db_record.location = location

    @classmethod
    def add_post_patch_args(cls, parser):
        parser.add_argument('hostname')
        parser.add_argument('vcpu')
        parser.add_argument('storage')
        parser.add_argument('role')
        parser.add_argument('environment')
        parser.add_argument('cluster')
        parser.add_argument('ram')
        parser.add_argument('group')
        parser.add_argument('location')
