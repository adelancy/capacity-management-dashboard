from marshmallow_jsonapi import fields, Schema
from marshmallow_jsonapi.flask import Relationship
from rest_api.util import dasherize


class TeamSchema(Schema):
    id = fields.Integer(dump_only=True)
    name = fields.String(allow_none=True)
    group = fields.String(allow_none=True)
    description = fields.String(allow_none=True)

    class Meta:
        strict = True
        type_ = 'team'
        inflect = dasherize


class PhysicalReqSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.String()
    model = fields.String()
    vendor = fields.String()
    part_number = fields.String()
    serial_number = fields.String()
    procs = fields.Int(allow_none=True)
    description = fields.String(allow_none=True)
    sfp_type = fields.String()
    power_draw = fields.String()
    network_ports = fields.Int()
    mgmt_ports = fields.Int()
    group = fields.String(allow_none=True)  # Todo: replace with a team relationship
    ram = fields.Int(allow_none=True)
    storage_capacity = fields.Int(allow_none=True)
    vm_count = fields.Int(allow_none=True)
    os_type = fields.String(allow_none=True)
    env = fields.String(allow_none=True)

    team = Relationship(
        schema=TeamSchema,
        type_='team',
        include_resource_linkage=True
    )

    class Meta:
        strict = True
        type_ = 'bm-req'
        inflect = dasherize


class VMRequirementSchema(Schema):
    id = fields.Int()
    name = fields.String()
    hostname = fields.String()
    vcpus = fields.Int()
    ram = fields.Int()
    storage = fields.Int()
    role = fields.String()
    environment = fields.String()
    cluster = fields.String()
    os_type = fields.String()
    vm_type = fields.String()
    vm_units = fields.String()

    team = Relationship(
        schema=TeamSchema,
        include_resource_linkage=True,
        type_='team'
    )

    class Meta:
        type_ = 'vm-req'
        strict = True
        inflect = dasherize
