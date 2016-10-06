from marshmallow_jsonapi import Schema, fields
from marshmallow_jsonapi.flask import Relationship
from location import LocationSchema
from rest_api.util import dasherize


class VMSchema(Schema):
    id = fields.Int()
    hostname = fields.String()
    vcpu = fields.Int()
    ram = fields.Int()
    storage = fields.Int()
    role = fields.String()
    environment = fields.String()
    cluster = fields.String()

    location = Relationship(
        schema=LocationSchema,
        include_resource_linkage=True,
        type_='location'
    )

    class Meta:
        type_ = 'vm'
        strict = True
        inflect = dasherize
