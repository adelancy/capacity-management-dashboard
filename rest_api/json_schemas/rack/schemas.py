from marshmallow_jsonapi import Schema, fields
from marshmallow_jsonapi.flask import Relationship
from rest_api.json_schemas.location import LocationSchema


class OutletTypeSchema(Schema):
    id = fields.Integer(dump_only=True)
    name = fields.String(allow_none=True)
    voltage = fields.Int()
    amperage = fields.Int()
    last_modified_dt = fields.DateTime()

    class Meta:
        type_ = 'outlet-type',
        strict = 'true'


class PDUSchema(Schema):
    id = fields.Integer(dump_only=True)
    name = fields.String()
    total_count = fields.Integer(allow_none=True)
    total_free = fields.Integer(allow_none=True)
    last_modified_dt = fields.DateTime()
    outlet_type = Relationship(
        schema=OutletTypeSchema,
        include_resource_linkage=True,
        type_='outlet-type',
        attribute='type'
    )

    class Meta:
        type_ = 'pdu'
        strict = True


class RackSchema(Schema):
    id = fields.Int(dump_only=True)
    vendor = fields.String()
    model = fields.String()
    serial_number = fields.String()
    last_modified_dt = fields.DateTime()

    location = Relationship(
        schema=LocationSchema,
        include_resource_linkage=True,
        type_='location'
    )

    pdus = Relationship(
        schema=PDUSchema,
        include_resource_linkage=True,
        type_='pdu',
        many=True
    )

    class Meta:
        type_ = 'rack'
        strict = True


class RackUnitSchema(Schema):
    id = fields.Integer(dump_only=True)
    ru_start = fields.Int()
    ru_end = fields.Int()
    last_modified_dt = fields.DateTime()

    rack = Relationship(
        schema=RackSchema,
        include_resource_linkage=True,
        type_='rack'
    )

    class Meta:
        type_ = 'rack-unit'
        strict = True


class OutletSchema(Schema):
    id = fields.Integer(dump_only=True)
    total_count = fields.Integer()
    total_free = fields.Int()
    last_modified_dt = fields.DateTime()

    rack = Relationship(
        schema=RackSchema,
        include_resource_linkage=True,
        type_='rack'
    )

    outlet_type = Relationship(
        schema=OutletTypeSchema,
        include_resource_linkage=True,
        type_='outlet-type',
        attribute='type'
    )

    class Meta:
        type_ = 'outlet'
        strict = True


class CircuitSchema(Schema):
    id = fields.Int(dump_only=True)
    voltage = fields.Int(allow_none=True)
    amperage = fields.Int(allow_none=True)
    power_rating = fields.Int(allow_none=True)
    last_modified_dt = fields.DateTime()

    rack = Relationship(
        schema=RackSchema,
        include_resource_linkage=True,
        type_='rack'
    )

    class Meta:
        type_ = 'circuit'
        strict = True