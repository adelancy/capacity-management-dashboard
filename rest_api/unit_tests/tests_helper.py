from extensions.sql_alchemy import sqldb
from dbmodels.location import Location
from dbmodels.vm import VM


def set_up(self):
    sqldb.drop_all()
    sqldb.create_all()
    for x in range(1, 6):
        name = 'Location {0}'.format(x)
        city = 'Location City {0}'.format(x)
        country = 'Location Country {0}'.format(x)
        location = Location(name=name, city=city, country=country)
        sqldb.session.add(location)

        hostname = 'vm {0}'.format(x)
        vm = VM(hostname=hostname)
        vm.location = location
        sqldb.session.add(vm)
    sqldb.session.commit()


def tear_down(self):
    sqldb.drop_all()
    sqldb.session.remove()
