import datetime
import pandas as pd
import numpy as np

mysql_to_python_type = {
    "varchar": str,
    "char": str,
    "text": str,
    "mediumtext": str,
    "longtext": str,
    "int": int,
    "tinyint": int,
    "smallint": int,
    "mediumint": int,
    "bigint": int,
    "float": float,
    "double": float,
    "decimal": float,
    "date": datetime.date,
    "datetime": datetime.datetime,
    "datestamp": datetime.datetime,
    "time": datetime.time,
    "year": str,
    "blob": bytes,
    "longblob": bytes
}

class CompanyBase:

    def __init__(self):
        self._columns = (
            'hotel_group_id', 'hotel_id', 'id', 'name', 'name2', 'name3', 'name_combine', 'is_save',
            'language', 'nation', 'phone', 'mobile', 'mobile2', 'fax', 'email', 'email2', 'website', 'blog',
            'linkman1', 'occupation', 'birth', 'birth2', 'linkman2', 'occupation2', 'country', 'state', 'city',
            'division', 'street', 'zipcode', 'representative', 'representative_id_no', 'is_host',
            'register_no', 'bank_name', 'bank_account', 'tax_no', 'remark', 'is_visible', 'create_hotel',
            'create_user', 'create_datetime', 'modify_hotel', 'modify_user', 'modify_datetime', 'strict'
        )
        self._types = (
            'bigint', 'bigint', 'bigint', 'varchar', 'varchar', 'varchar', 'varchar', 'varchar', 'varchar',
            'varchar', 'varchar',
            'varchar', 'varchar', 'varchar', 'varchar', 'varchar', 'varchar', 'varchar', 'varchar', 'varchar',
            'date', 'date', 'varchar',
            'varchar', 'varchar', 'varchar', 'varchar', 'varchar', 'varchar', 'varchar', 'varchar', 'varchar',
            'varchar', 'varchar', 'varchar',
            'varchar', 'varchar', 'text', 'varchar', 'varchar', 'varchar', 'datetime', 'varchar', 'varchar',
            'datetime', 'varchar'
        )
        self.company_base: pd.DataFrame = pd.DataFrame(
            columns = self._columns
        )

    def insert(self, data):
        length = len(self.company_base)
        if isinstance(data, list):
            data1 = dict(zip(self._columns, data))
        self.company_base.loc[length] = data1

    def get(self):
        return self.company_base

class CompanyType:
    def __init__(self):
        pass
