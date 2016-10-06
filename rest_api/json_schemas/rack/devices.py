from marshmallow_jsonapi import fields, Schema
from marshmallow_jsonapi.flask import Relationship
from rest_api.json_schemas.rack.schemas import RackSchema
from rest_api.util import dasherize


class BMSchema(Schema):
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
    env = fields.String(allow_none=True)

    rack = Relationship(
        schema=RackSchema,
        type_='rack',
        include_resource_linkage=True
    )

    class Meta:
        strict = True
        type_ = 'bm-host'
        inflect = dasherize


class FirewallSchema(Schema):
    id = fields.Integer(dump_only=True)
    vendor = fields.String(allow_none=True)
    hostname = fields.String(allow_none=True)
    model = fields.String(allow_none=True)
    part_number = fields.String(allow_none=True)
    serial_number = fields.String(allow_none=True)
    description = fields.String(allow_none=True)
    env = fields.String(allow_none=True)

    rack = Relationship(
        schema=RackSchema,
        type_='rack',
        include_resource_linkage=True
    )

    class Meta:
        strict = True
        type_ = 'firewall'
        inflect = dasherize


class LoadBalancerSchema(Schema):
    id = fields.Integer(dump_only=True)
    vendor = fields.String(allow_none=True)
    hostname = fields.String(allow_none=True)
    model = fields.String(allow_none=True)
    part_number = fields.String(allow_none=True)
    serial_number = fields.String(allow_none=True)
    description = fields.String(allow_none=True)
    env = fields.String(allow_none=True)

    rack = Relationship(
        schema=RackSchema,
        type_='rack',
        include_resource_linkage=True
    )

    class Meta:
        strict = True
        type_ = 'load-balancer'
        inflect = dasherize


class StorageSchema(Schema):
    id = fields.Integer(dump_only=True)
    vendor = fields.String(allow_none=True)
    hostname = fields.String(allow_none=True)
    model = fields.String(allow_none=True)
    part_number = fields.String(allow_none=True)
    serial_number = fields.String(allow_none=True)
    description = fields.String(allow_none=True)
    storage_capacity = fields.String(allow_none=True)
    free_capacity = fields.String(allow_none=True)
    env = fields.String(allow_none=True)

    rack = Relationship(
        schema=RackSchema,
        type_='rack',
        include_resource_linkage=True
    )

    class Meta:
        strict = True
        type_ = 'storage'
        inflect = dasherize


class SwitchSchema(Schema):
    id = fields.Integer(dump_only=True)
    vendor = fields.String(allow_none=True)
    hostname = fields.String(allow_none=True)
    model = fields.String(allow_none=True)
    part_number = fields.String(allow_none=True)
    serial_number = fields.String(allow_none=True)
    description = fields.String(allow_none=True)
    one_gig_ports_total = fields.Int(allow_none=True)
    ten_gig_ports_total = fields.Int(allow_none=True)
    one_gig_ports_free = fields.Int(allow_none=True)
    ten_gig_ports_free = fields.Int(allow_none=True)
    ten_gig_plus_ports_total = fields.Int(allow_none=True)
    ten_gig_plus_ports_free = fields.Int(allow_none=True)
    env = fields.String(allow_none=True)

    rack = Relationship(
        schema=RackSchema,
        type_='rack',
        include_resource_linkage=True
    )

    class Meta:
        strict = True
        type_ = 'switch'
        inflect = dasherize


class WirelessSchema(Schema):
    id = fields.Integer(dump_only=True)
    vendor = fields.String(allow_none=True)
    hostname = fields.String(allow_none=True)
    model = fields.String(allow_none=True)
    part_number = fields.String(allow_none=True)
    serial_number = fields.String(allow_none=True)
    description = fields.String(allow_none=True)
    device_type = fields.Int(allow_none=True)
    env = fields.String(allow_none=True)

    rack = Relationship(
        schema=RackSchema,
        type_='rack',
        include_resource_linkage=True
    )

    class Meta:
        strict = True
        type_ = 'wireless'
        inflect = dasherize


