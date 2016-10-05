from extensions.sql_alchemy import sqldb
from dbmodels.location import Location
from dbmodels.vm import VM
from dbmodels.rack.rack import Rack, RackUnit
from dbmodels.rack.pdu import PDU
from dbmodels.rack.outlets import OutletType, Outlets


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