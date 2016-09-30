from marshmallow_jsonapi import Schema, fields


class LocationSchema(Schema):
    id = fields.Integer()
    name = fields.String()
    city = fields.String()
    region = fields.String()
    country = fields.String()

    class Meta:
        type_ = 'location'
        strict = True
