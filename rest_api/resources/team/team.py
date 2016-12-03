from rest_api.resources.base import BaseCollection
from dbmodels.team.team import Team
from dbmodels.data_center.location import Location
from dbmodels.team.virtual_requirements import VirtualRequirement
from dbmodels.team.physical_requirements import PhysicalRequirement
from rest_api.json_schemas.team import TeamSchema, PhysicalReqSchema, VMRequirementSchema


class TeamCollection(BaseCollection):
    def __init__(self):
        super(TeamCollection, self).__init__()
        self.db_table = Team
        self.resp_schema = TeamSchema

    def handle_special_fields(self, db_record, field, value, replace=False):
        pass

    @classmethod
    def add_post_patch_args(cls, parser):
        parser.add_argument('name')
        parser.add_argument('group')
        parser.add_argument('description')


class VMRequirementsCollection(BaseCollection):
    def __init__(self):
        super(VMRequirementsCollection, self).__init__()
        self.db_table = VirtualRequirement
        self.resp_schema = VMRequirementSchema
        self.special_fields = ['team', 'team-id', 'location', 'location-id']

    def handle_special_fields(self, db_record, field, value, replace=False):
        if field in ['team', 'team-id']:
            team = Team.query.filter_by(id=value, deleted=False).first()
            db_record.team = team
        if field in ['location', 'location-id']:
            location = Location.query.filter_by(id=value, deleted=False).first()
            db_record.location = location

    @classmethod
    def add_post_patch_args(cls, parser):
        parser.add_argument('name')
        parser.add_argument('hostname')
        parser.add_argument('vcpus')
        parser.add_argument('storage')
        parser.add_argument('vm-type', dest='vm_type')
        parser.add_argument('os-type', dest='os_type')
        parser.add_argument('environment')
        parser.add_argument('cluster')
        parser.add_argument('ram')
        parser.add_argument('group')
        parser.add_argument('location')
        parser.add_argument('team-id', dest='team')


class BMRequirementsCollection(BaseCollection):
    def __init__(self):
        super(BMRequirementsCollection, self).__init__()
        self.db_table = PhysicalRequirement
        self.resp_schema = PhysicalReqSchema
        self.special_fields = ['team', 'location']

    def handle_special_fields(self, db_record, field, value, replace=False):
        if field in ['team', 'team-id']:
            team = Team.query.filter_by(id=value, deleted=False).first()
            print team
            db_record.team = team
        if field in ['location', 'location-id']:
            location = Location.query.filter_by(id=value, deleted=False).first()
            print location
            db_record.location = location

    @classmethod
    def add_post_patch_args(cls, parser):
        parser.add_argument('name')
        parser.add_argument('model')
        parser.add_argument('part-number', dest='part_number')
        parser.add_argument('cpus')
        parser.add_argument('procs')
        parser.add_argument('storage')
        parser.add_argument('environment')
        parser.add_argument('cluster')
        parser.add_argument('ram')
        parser.add_argument('vendor')
        parser.add_argument('os-type', dest='os_type')
        parser.add_argument('hypervisor')
        parser.add_argument('location')
        parser.add_argument('location-id', dest='location')
        parser.add_argument('team-id', dest='team')

