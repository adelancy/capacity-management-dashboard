from flask_script import Manager, Server
from app import create_app
from extensions.sql_alchemy import sqldb

manager = Manager(create_app)
server = Server(port=5000, use_debugger=True)
manager.add_command("runserver", server)


@manager.command
def create_db():
    sqldb.create_all()


@manager.command
def clear_db():
    sqldb.drop_all()


if __name__ == "__main__":
    manager.run()

