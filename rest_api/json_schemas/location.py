from marshmallow_jsonapi import Schema, fields
from marshmallow_jsonapi.flask import Relationship


class LocationSchema(Schema):
    id = fields.Integer()
    name = fields.String()
    city = fields.String()
    region = fields.String()
    country = fields.String()
