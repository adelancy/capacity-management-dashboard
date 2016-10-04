import json
import unittest

from app import create_app
import config as cfg
from flask_testing import TestCase
from flask_restful import url_for
from dbmodels.location import Location
from dbmodels.vm import VM
from tests_helper import set_up, tear_down


class TestLocationCollection(TestCase):

    def create_app(self):

        app = create_app(cfg.TestingConfig)
        return app

    def setUp(self):
        set_up(self)

    def tearDown(self):
        tear_down(self)

    def test_get_request(self):
        p = Location.query.first()
        resp = self.client.get(url_for('locations-collection', db_id=p.id))
        self.assert200(resp)

    def test_get_vms_request(self):
        p = VM.query.first()
        resp = self.client.get(url_for('vms-collection', db_id=p.id))
        self.assert200(resp)

    def test_create_vms(self):
        location_id = Location.query.all()[2].id
        data = {
            'hostname': 'adrian-test-vm',
            'vcpu': 4,
            'vmunit': 2,
            'location': location_id
        }

        resp = self.client.post(url_for('vms-collection'), data=data)
        self.assertStatus(resp, 201)

    def test_create_vms_json_api(self):
        location_id = Location.query.all()[2].id
        data = {
            'data': {
                'type': 'vm',
                'attributes': {
                    'hostname': 'adrian-test-vm',
                    'vcpu': 4,
                    'vmunit': 2,
                },
                'relationships': {
                    'location': {
                        'data': {
                            'id': location_id,
                            'type': 'location'
                        }
                    }
                }
            }
        }

        headers = {
            'Content-Type': 'application/vnd.api+json'
        }

        resp = self.client.post(url_for('vms-collection'), data=json.dumps(data), headers=headers)
        print resp.data
        self.assertStatus(resp, 201)

if __name__ == '__main__':
    unittest.main()
