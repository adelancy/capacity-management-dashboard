import json
from datetime import datetime

from flask import request, current_app
from flask_restful import Resource, reqparse

# from dbmodels.data_center.location import Location
from extensions.sql_alchemy import sqldb
# from ..json_schemas.location import LocationSchema
from ..util import output_json, handle_rest_error_response


class BaseCollection(Resource):
    """
    Abstract class to be overridden
    """
    def __init__(self):
        super(BaseCollection, self).__init__()
        self.db_table = None
        self.resp_schema = None
        self.special_fields = []  # Identify the special fields that need to be handled i.e. arrays, dicts
        self.representations = {
            'application/vnd.api+json': output_json,
        }

    def get(self, db_id=None):
        parser = reqparse.RequestParser()
        parser.add_argument('filter', type=json.loads)
        args = parser.parse_args()
        try:
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
            resp = self.resp_schema().dump(db_record).data
            return resp, 200
        except Exception as error:
            return handle_rest_error_response(error, 'Location Collection')

    def post(self):
        parser = reqparse.RequestParser()
        try:
            self.add_post_patch_args(parser)
            data = self.parse_args(parser)
            print data
            current_app.logger.debug(data)
            db_record = self.create_update_db_reccord(data, self.db_table())
            resp = self.resp_schema().dump(db_record).data
            return resp, 201
        except Exception as error:
            return handle_rest_error_response(error, 'Locations Collection')

    def patch(self, db_id):
        parser = reqparse.RequestParser()
        try:
            self.add_post_patch_args(parser)
            data = self.parse_args(parser)
            db_record = self.db_table.query.filter_by(id=db_id, deleted=False).first_or_404()
            self.create_update_db_reccord(data, db_record)
            return '', 204
        except Exception as error:
            return handle_rest_error_response(error, 'Locations Collection')

    def delete(self, db_id):
        try:
            db_record = self.get_db_record(db_id)
            db_record.deleted = True
            db_record.last_modified_dt = datetime.utcnow()
            sqldb.session.add(db_record)
            self.commit()
            return '', 204
        except Exception as error:
            return handle_rest_error_response(error, 'Locations Collection')

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
                return self.resp_schema().loads(request.data).data
            raise TypeError
        except TypeError:
            return args  # Request is just encoded as normal form/json data

    def handle_special_fields(self, db_record, field, value, replace=False):
        """ Use to handle updating special fields such as relationships, labels, tags etc. Use the replace
        flag to determine whether fields should be replaced or incremently updated.
        """
        raise NotImplementedError

    def create_update_db_reccord(self, data, db_record):
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
        return db_record

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

