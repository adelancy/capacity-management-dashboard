import json
import unittest

from flask_restful import url_for
from flask_testing import TestCase

import base_config as cfg
from app import create_app

from dbmodels.data_center.location import Location
from dbmodels.data_center.rack.outlets import OutletType, Outlets
from dbmodels.data_center.rack.rack import Rack
from dbmodels.data_center.rack.pdu import PDU
from dbmodels.data_center.vm import VM
from extensions.sql_alchemy import sqldb


def set_up(self):
    sqldb.drop_all()
    sqldb.create_all()
    for x in range(1, 6):
        name = 'Location {0}'.format(x)
        city = 'Location City {0}'.format(x)
        country = 'Location Country {0}'.format(x)
        location = Location(name=name, city=city, country=country)
        sqldb.session.add(location)

        # Create Vm Records
        hostname = 'vm {0}'.format(x)
        vm = VM(hostname=hostname)
        vm.location = location
        sqldb.session.add(vm)

        outlet_type = create_outlet_type(self, x)
        pdu = create_pdu_records(self, x, outlet_type)
        rack = create_rack_records(self, x, location, pdu=pdu)
        create_power_outlet_records(self, x, rack, outlet_type)
    sqldb.session.commit()


def tear_down(self):
    sqldb.drop_all()
    sqldb.session.remove()


# Middleware methods
def create_rack_records(self, index, location, pdu=None, outlets=None):
    rack = Rack(model='test-model', vendor='vendor-{0}'.format(index))
    rack.location = location
    if not pdu:
        rack.pdus.append(pdu)
    sqldb.session.add(rack)
    return rack


def create_pdu_records(self, index, outlet_type):
    pdu = PDU(total_count=10, name='pdu{0}'.format(index), vendor='test-vendor', total_free=5)
    pdu.type = outlet_type
    sqldb.session.add(pdu)
    return pdu


def create_power_outlet_records(self, index, rack, outlet_type):
    outlet = Outlets(total_count=48 + 6*index, total_free=12 + index, rack=rack, type=outlet_type)
    sqldb.session.add(outlet)
    return outlet


def create_outlet_type(self, index):
    outlet_type = OutletType(name='NemaL{0}'.format(index), voltage=5000, amperage=10)
    sqldb.session.add(outlet_type)
    return outlet_type

#######Start Testing ##################


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
            'Content-Type': 'application/vnd.api+json;charset=utf8'
        }

        resp = self.client.post(url_for('vms-collection'), data=json.dumps(data), headers=headers)
        # print resp.data
        self.assertStatus(resp, 201)

if __name__ == '__main__':
    unittest.main()
