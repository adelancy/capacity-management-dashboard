from rest_api.resources.base import BaseCollection
from dbmodels.team.team import Team
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
        self.special_fields = ['team']

    def handle_special_fields(self, db_record, field, value, replace=False):
        if field == 'team':
            team = Team.query.filter_by(id=value, deleted=False).first()
            db_record.team = team

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
        self.special_fields = ['team']

    def handle_special_fields(self, db_record, field, value, replace=False):
        if field == 'team':
            team = Team.query.filter_by(id=value, deleted=False).first()
            db_record.team = team

    @classmethod
    def add_post_patch_args(cls, parser):
        parser.add_argument('name')
        parser.add_argument('model')
        parser.add_argument('vcpu')
        parser.add_argument('storage-capacity', dest='storage_capacity')
        parser.add_argument('procs')
        parser.add_argument('environment')
        parser.add_argument('cluster')
        parser.add_argument('ram')
        parser.add_argument('os-type', dest='os_type')
        parser.add_argument('serial-number', dest='serial_number')

