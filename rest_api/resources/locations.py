import json
from datetime import datetime

from flask import request
from flask_restful import Resource, reqparse
from extensions.sql_alchemy import sqldb
from dbmodels.location import Location
from ..json_schemas.location import LocationSchema
from ..util import output_json


class LocationsCollection(Resource):
    def __init__(self):
        super(LocationsCollection, self).__init__()
        self.db_table = Location
        self.resp_schema = LocationSchema
        self.special_fields = []  # Identify the special fields that need to be handled i.e. arrays, dicts
        self.representations = {
            'application/vnd.api+json': output_json,
        }

    def get(self, db_id=None):
        parser = reqparse.RequestParser()
        parser.add_argument('filter', type=json.loads)
        args = parser.parse_args()
        if db_id is None:
            if args.get('filter', None):
                filters = args.get('filter')
                db_records = self.db_table.query.filter_by(**filters).\
                    filter(self.db_table.deleted.isnot(True)).all()
                return self.resp_schema(many=True).dump(db_records).data, 200
            # Get all locations
            db_records = self.db_table.query.filter(self.db_table.deleted.isnot(True)).all()
            return self.resp_schema(many=True).dump(db_records).data
        db_record = self.get_db_record(db_id)
        print db_record.deleted
        resp = self.resp_schema().dump(db_record).data
        return resp, 200

    def post(self):
        parser = reqparse.RequestParser()
        self.add_post_patch_args(parser)
        data = self.parse_args(parser)
        db_record = self.db_table(**data)  # Todo: Add validation as necessary
        db_record.last_modified_dt = datetime.utcnow()
        sqldb.session.add(db_record)
        self.commit()
        resp = self.resp_schema().dump(db_record).data
        return resp, 201

    def patch(self, db_id):
        parser = reqparse.RequestParser()
        self.add_post_patch_args(parser)
        data = self.parse_args(parser)
        db_record = self.db_table.query.filter_by(id=db_id, deleted=False).first_or_404()
        for k, v in data.items():
            if k in self.special_fields:
                self.handle_special_fields(db_record, k, v)
            try:
                setattr(db_record, k, v)
            except AttributeError:
                pass  # Todo: Log the error
        db_record.last_modified_dt = datetime.utcnow()
        sqldb.session.add(db_record)
        self.commit()
        return '', 204

    def delete(self, db_id):
        db_record = self.get_db_record(db_id)
        db_record.deleted = True
        db_record.last_modified_dt = datetime.utcnow()
        sqldb.session.add(db_record)
        self.commit()
        return '', 204

    def get_db_record(self, db_id):
        db_record = self.db_table.query.filter_by(id=db_id)\
            .filter(self.db_table.deleted.isnot(True)).first_or_404()
        return db_record

    def parse_args(self, parser):
        parser.add_argument('Content-Type', location='headers')
        args = parser.parse_args()
        content_type = args.pop('Content-Type')
        try:
            # Check whether the request is json api format
            if content_type == 'application/vnd.api+json':
                return self.resp_schema().loads(request.data)
            raise TypeError
        except TypeError:
            return args  # Request is just encoded as normal form/json data

    def handle_special_fields(self, db_record, field, value, replace=False):
        """ Use to handle updating special fields such as relationships, labels, tags etc. Use the replace
        flag to determine whether fields should be replaced or incremently updated.
        """
        raise NotImplementedError

    @classmethod
    def commit(cls):
        try:
            sqldb.session.commit()
        except Exception as error:
            sqldb.session.rollback()
            raise error

    @classmethod
    def add_post_patch_args(cls, parser):
        parser.add_argument('name')
        parser.add_argument('city')
        parser.add_argument('country')
        parser.add_argument('region')

