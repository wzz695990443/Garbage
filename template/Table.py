import datetime
from abc import ABC, abstractmethod

import pandas as pd
import numpy as np

from template.DBConnect import DBConnect

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
    "date": 'datetime64[ns]',
    "datetime": 'datetime64[ns]',
    "datestamp": 'datetime64[ns]',
    "time": 'datetime64[ns]',
    "year": str,
    "blob": bytes,
    "longblob": bytes
}

class Table(ABC):
    def __init__(self):
        self.table_name = None
        self.table_columns = None
        self.table_types = None
        self.table_data = None
        self.hotel_group_id = None
        self.hotel_id = None

    @abstractmethod
    def append(self, data):
        pass

    @abstractmethod
    def get(self):
        pass

    @abstractmethod
    def set(self,data):
        pass

    @abstractmethod
    def init_type(self):
        pass

class CompanyBase(Table):

    def __init__(self):
        super().__init__()
        self.table_name = 'company_base'
        self.table_columns = (
            'hotel_group_id', 'hotel_id', 'id', 'name', 'name2', 'name3', 'name_combine', 'is_save',
            'language', 'nation', 'phone', 'mobile', 'mobile2', 'fax', 'email', 'email2', 'website', 'blog',
            'linkman1', 'occupation', 'birth', 'birth2', 'linkman2', 'occupation2', 'country', 'state', 'city',
            'division', 'street', 'zipcode', 'representative', 'representative_id_no', 'is_host',
            'register_no', 'bank_name', 'bank_account', 'tax_no', 'remark', 'is_visible', 'create_hotel',
            'create_user', 'create_datetime', 'modify_hotel', 'modify_user', 'modify_datetime', 'strict'
        )
        self.table_types = (
            'bigint', 'bigint', 'bigint', 'varchar', 'varchar', 'varchar', 'varchar', 'varchar', 'varchar',
            'varchar', 'varchar',
            'varchar', 'varchar', 'varchar', 'varchar', 'varchar', 'varchar', 'varchar', 'varchar', 'varchar',
            'date', 'date', 'varchar',
            'varchar', 'varchar', 'varchar', 'varchar', 'varchar', 'varchar', 'varchar', 'varchar', 'varchar',
            'varchar', 'varchar', 'varchar',
            'varchar', 'varchar', 'text', 'varchar', 'varchar', 'varchar', 'datetime', 'varchar', 'varchar',
            'datetime', 'varchar'
        )
        self.table_data: pd.DataFrame = pd.DataFrame(
            columns = self.table_columns
        )

    def append(self, data = None):
        length = len(self.table_data)
        if isinstance(data, list):
            data_ls = dict(zip(self.table_columns, data))
            self.table_data.loc[length] = data_ls

    def get(self):
        return self.table_data

    def set(self, data):
        self.table_data = data

    def init_type(self):
        self.table_data = self.table_data.astype(
            dict(zip(self.table_columns, [mysql_to_python_type[col_type] for col_type in self.table_types])))

    def insertintodb(self, conn: DBConnect,is_auto:bool = True):
        try:
            conn.connect()
            if is_auto:
                for index, row in self.table_data.iterrows():
                    sql = f'INSERT INTO {self.table_name}({", ".join(item for item in self.table_columns)}) VALUES ({self.hotel_group_id},{self.hotel_id},NULL,{", ".join(item for item in row[3:].astype(str))})'
                    conn.execute(sql)
            else:
                for index, row in self.table_data.iterrows():
                    sql = f'INSERT INTO {self.table_name}({", ".join(item for item in self.table_columns)}) VALUES ({", ".join(item for item in row.astype(str))})'
                    conn.execute(sql)
        except Exception as e:
            print(e)
        finally:
            conn.close()


class CompanyType:
    def __init__(self):
        super().__init__()
        self.table_name = 'company_type'
        self.table_columns = (
            'hotel_group_id', 'hotel_id', 'id', 'company_id', 'sta', 'manual_no', 'sys_cat', 'flag_cat', 'grade',
            'latency', 'class1', 'class2', 'class3', 'class4', 'src', 'channel', 'market', 'vip',
            'belong_app_code', 'membership_type', 'membership_no', 'membership_level', 'over_rsvsrc',
            'valid_begin', 'valid_end', 'code1', 'code2', 'code3', 'code4', 'code5', 'flag', 'saleman', 'ar_no1',
            'ar_no2', 'extra_flag', 'extra_info', 'comments', 'create_user', 'create_datetime',
            'modify_user', 'modify_datetime', 'is_verified'
        )
        self.table_types = (
            'bigint', 'bigint', 'bigint', 'bigint', 'varchar', 'varchar', 'varchar', 'varchar', 'varchar', 'varchar',
            'varchar', 'varchar', 'varchar', 'varchar', 'varchar', 'varchar', 'varchar', 'varchar', 'varchar',
            'varchar', 'varchar', 'varchar', 'varchar', 'datetime', 'datetime', 'varchar', 'varchar', 'varchar',
            'varchar', 'varchar', 'varchar', 'varchar', 'bigint', 'bigint', 'varchar', 'varchar', 'varchar', 'varchar',
            'datetime', 'varchar', 'datetime', 'varchar'
        )
        self.table_data: pd.DataFrame = pd.DataFrame()

    def append(self, data):
        length = len(self.table_data)
        if isinstance(data, list):
            data_ls = dict(zip(self.table_columns, data))
            self.table_data.loc[length] = data_ls

    def get(self):
        return self.table_data

    def set(self, data):
        self.table_data = data

    def init_type(self):
        self.table_data = self.table_data.astype(
            dict(zip(self.table_columns, [mysql_to_python_type[col_type] for col_type in self.table_types])))

    def insertintodb(self, conn: DBConnect):
        pass
