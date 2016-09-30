from flask_restful import Resource, reqparse
from dbmodels.location import Location


class LocationsCollection(Resource):
    def __init__(self):
        super(LocationsCollection, self).__init__()

    def get(self, location_id=None):
        parser = reqparse.RequestParser()
        parser.add_argument('query')
        parser.add_argument('filter')
        args = parser.parse_args()
        if location_id is None:
            pass
        location = Location.query.filter_by(id=location_id).first_or_404()
        return location.name
