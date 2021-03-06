import json
import unittest

from flask_restful import url_for
from flask_testing import TestCase

from app import create_app
from extensions.sql_alchemy import sqldb
from dbmodels.team.team import Team
from dbmodels.data_center.location import Location
from dbmodels.team.physical_requirements import PhysicalRequirement
from dbmodels.team.virtual_requirements import VirtualRequirement


class TestSubmitRequirements(TestCase):

    def create_app(self):
        app = create_app(config_options_name='test')
        return app

    def setUp(self):
        sqldb.drop_all()
        sqldb.create_all()
        # Create an initial Team and Location to facilitate the relationship
        team = Team(name='Test Team 1', group='Accenture CIO', description='Temporary Test Team')
        sqldb.session.add(team)
        location = Location(name='Ashburn', city='Ashburn', region='Virginia', country='USA')
        sqldb.session.add(location)
        sqldb.session.commit()

    def tearDown(self):
        sqldb.drop_all()
        sqldb.session.remove()

    def test_create_team(self):
        data = dict(name='Test Team 2', group='Accenture CIO', description='Another Test Team')
        resp = self.client.post(url_for('teams-collection'), data=data)
        self.assertStatus(resp, 201)
        self.assertTrue(resp.json['data']['attributes'])
        self.assertEqual(resp.json['data']['attributes']['name'], 'Test Team 2')

    def test_create_virtual_requirement(self):
        data = {
            'crsf_token': '1480296505##f9cba005afe7b2e4ecc1d6ff8b4ec1d1e95ab274',
            'name': 'Application 1',
            'vm-type': 'Production',
            'os-type': 'windows server 2012',
            'vcpus': '2',
            'ram': '4',
            'team-id': 1
        }

        resp = self.client.post(url_for('vm-reqs-collection'), data=data)
        #print resp.data
        self.assertStatus(resp, 201)
        attributes = resp.json['data']['attributes']
        self.assertTrue(attributes)
        self.assertEqual(attributes['name'], u'Application 1')
        self.assertEqual(attributes['os-type'], u'windows server 2012')
        self.assertEqual(attributes['vm-type'], u'Production')

    def test_create_bare_metal_requirement(self):
        data = {
            'crsf_token': '1480296505##f9cba005afe7b2e4ecc1d6ff8b4ec1d1e95ab274',
            'name': 'App Host 1',
            'model-name': 'Production',
            'vendor': 'Dell',
            'part-number': 'abc12352',
            'ram': '4',
            'procs': '2',
            'hypervisor': 'esxi',
            'storage': '500',
            'power-draw': '50',
            'mgmt-ports': '4',
            'rus': '2',
            'sfp-count': '4',
            'team-id': 1,
            'location-id': Location.query.first()
        }

        resp = self.client.post(url_for('bm-reqs-collection'), data=data)
        self.assertStatus(resp, 201)
        #print resp.data
        resp_data = resp.json['data']
        self.assertEqual(resp_data['attributes']['storage'], 500)
        self.assertEqual(resp_data['attributes']['vendor'], 'Dell')
        self.assertEqual(resp_data['attributes']['part-number'], 'abc12352')
        self.assertEqual(resp_data['attributes']['hypervisor'], 'esxi')
        self.assertTrue(resp_data['relationships']['location'])
        self.assertTrue(resp_data['relationships']['team'])
        self.assertEqual(resp_data['type'], 'bm-req')

