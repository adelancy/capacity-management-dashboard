from marshmallow_jsonapi import Schema, fields
from marshmallow_jsonapi.flask import Relationship
from location import LocationSchema


class LicenseSchema(Schema):
    id = fields.Int()
    vendor = fields.String()
    model = fields.Int()
    name = fields.Int()
    type = fields.Int()
    quantity = fields.String()
    in_use = fields.String()
    expiration_dt = fields.String()
    last_modified_dt = fields.String()

    location = Relationship(
        schema=LocationSchema,
        include_resource_linkage=True,
        type_='location'
    )

    class Meta:
        type_ = 'license'
        strict = True
