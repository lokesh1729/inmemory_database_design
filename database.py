import uuid

from table import Table


class Database:
    """
    name
unique_id (uuid | random)
tables - dictionary which is a mapping of table unique id to table object
create_table(table_obj) # TODO
delete_table(table_id) # TODO
Get_name -> name of the database
Get_id -> id of the database
    """
    def __init__(self, name):
        self.name = name
        self.tables = {}
        self.id = uuid.uuid4()

    def add_table(self, table_obj: Table):
        self.tables[table_obj.id] = table_obj

    def delete_table(self, table_id):
        del self.tables[table_id]

    def get_name(self):
        return self.name

    def get_id(self):
        return self.id

    def get_all_tables(self):
        return list(map(lambda item: item.name, self.tables))
