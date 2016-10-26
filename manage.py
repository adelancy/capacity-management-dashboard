from flask_script import Manager, Server
from app import create_app
from extensions.sql_alchemy import sqldb

import dbmodels.data_center.location as loc

manager = Manager(lambda config_filename, config_options: create_app(config_filename, config_options))
manager.add_option('-cf', '--configuration-file', dest='config_filename', default=None)
manager.add_option('-co', '--configuration-options', dest='config_options', default=None)

server = Server(port=5000, use_debugger=True, use_reloader=True)
manager.add_command("runserver", server)


@manager.command
def create_db():
    sqldb.create_all()


@manager.command
def clear_db():
    sqldb.drop_all()


@manager.command
def add_location():
    location = loc.Location(city='Chicago', name='Chicago')
    sqldb.session.add(location)
    sqldb.session.commit()

if __name__ == "__main__":
    manager.run()

