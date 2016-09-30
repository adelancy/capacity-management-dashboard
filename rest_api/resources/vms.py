from locations import LocationsCollection
from dbmodels.vm import VM


class VMCollection(LocationsCollection):
    def __init__(self):
        super(VMCollection, self).__init__()
        self.db_table = VM
        # Todo: define jsonapi schema
