# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from column import StrColumn, IntColumn, Value, Schema
from database import Database
from table import Table


def main():
    obj = Database("test")
    # table = Table("students", [IntColumn("id"), StrColumn("name")])
    # obj.add_table(table)
    # table.insert_record([Value(Schema(IntColumn), 1), Value(Schema(StrColumn), "lokesh")])
    # table.print_all_records()

    table = Table("users", [StrColumn("name"), StrColumn("email"), StrColumn("contact")])
    obj.add_table(table)
    table.insert_record([Value(Schema(StrColumn), "lokesh"), Value(Schema(StrColumn),
                                                                   "hi@lokesh.com"),
                         Value(Schema(StrColumn),
                               "abcdef")])
    table.insert_record([Value(Schema(StrColumn), None), Value(Schema(StrColumn),
                                                               "hi@reshmi.com"),
                         Value(Schema(StrColumn),
                               "xyzzz")])
    table.insert_record([Value(Schema(StrColumn), "baljit"), Value(Schema(StrColumn),
                                                                   "hi@balji.com"),
                         Value(Schema(StrColumn), "hello_world")])
    table.insert_record([Value(Schema(StrColumn), "asdfasfasfasfasdfasdfasfadfasdfasdffasd"),
                         Value(Schema(StrColumn),
                                                                   "hi@balji.com"),
                         Value(Schema(StrColumn), "hello_world")])
    table.filter_records("name", "lokesh")
    # table.print_all_records()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
