import uuid
from typing import List
from column import Value, Column


class Table:
    """
    Name
Unique_id
Columns (schema) - dictionary which is a mapping of column id to column object, should be received in the constructor
Data - List[List[Value]]
insert_record(List[Value]) -> inserts into data, based on the schema the value will be validated and inserted
print_all_records() -> traverses through data and prints
Filter_records() ->
    """

    def __init__(self, name: str, columns: List[Column]):
        self.name = name
        self.columns = columns
        self.records = []
        self.id = uuid.uuid4()

    def insert_record(self, value: List[Value]):
        if len(value) != len(self.columns):
            raise ValueError("value %s should have same columns as per schema" % value)
        for schema_val, record_val in zip(self.columns, value):
            if not record_val.schema.schema_class.type != schema_val.type:
                raise ValueError("Invalid data received for value %s" % value)
            if schema_val.required and record_val.value is None:
                raise ValueError("value %s is required, but not given" % record_val.value)
            for each_validation in schema_val.constraints:
                if not each_validation(record_val.value):
                    raise ValueError("invalid value received for %s" % record_val.value)

        self.records.append(value)

    def print_all_records(self):
        for each_record in self.records:
            curr_row = []
            for each_column in each_record:
                curr_row.append(str(each_column))
            print(curr_row)

    def filter_records(self, column_name: str, column_value: any):
        filtered_records = []
        for each_record in self.records:
            for col_idx, each_column in enumerate(each_record):
                if self.columns[col_idx].name == column_name and each_column.value == column_value:
                    filtered_records.append(each_record)
        for each_record in filtered_records:
            curr_row = []
            for each_column in each_record:
                curr_row.append(str(each_column))
            print(curr_row)
