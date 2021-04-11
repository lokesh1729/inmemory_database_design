"""
Class Column:
Name
Id
Required - bool

Class Value:
Schema -> Column object
Value -> actual value


Class IntColumn(Column):
Min_va_allowed - -1024
Max_val_allowed - 1024
__init__
Add the constraints related checks


Class StrColumn(Column):
	- max_len = 20
__init__
Add the constraints related checks

Class DateTimeColumn(Column):
Value should be a datetime object
__init__
Add the constraints related checks

Class BoolColumn(Column):
	- allowed_values - True/False
__init__
Add the constraints related checks
"""
from abc import ABC
from datetime import datetime


class Column(ABC):
    type = None

    def __init__(self, name, _type, constraints, required=False):
        self.name = name
        self.type = _type
        self.required = required
        self.constraints = constraints

    def __str__(self):
        return self.name


class IntColumn(Column):
    def __init__(self, name, _type=None, constraints=None, required=False):
        super(IntColumn, self).__init__(name, "int", [
            lambda val: (val >= -1024 & val<= 1024)
        ], required=required)


class DateTimeColumn(Column):
    def __init__(self, name, _type=None, constraints=None, required=False):
        super(DateTimeColumn, self).__init__(name, "datetime", [
            lambda val: isinstance(val, datetime)
        ], required=required)


class StrColumn(Column):
    def __init__(self, name, _type=None, constraints=None, required=False):
        super(StrColumn, self).__init__(name, "str", [
            lambda val: val is None or isinstance(val, str) and len(val) <= 20
        ], required=required)


class BoolColumn(Column):
    def __init__(self, name, _type=None, constraints=None, required=False):
        super(BoolColumn, self).__init__(name,"bool", [
            lambda val: isinstance(val, bool)
        ], required=required)


class Schema:
    def __init__(self, schema_class):
        self.schema_class = schema_class


class Value:
    def __init__(self, schema: Schema, value: any):
        self.schema = schema
        self.value = value

    def __str__(self):
        return "%s" % self.value
