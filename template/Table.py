from datetime import datetime
from abc import ABC, abstractmethod

import pandas as pd
import numpy as np

from template.DBConnect import DBConnect
from pydantic import BaseModel, Field, validator
from typing import List, Optional

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
    "date": datetime,
    "datetime": datetime,
    "datestamp": datetime,
    "time": datetime,
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
    def set(self, data):
        pass

    @abstractmethod
    def init_type(self):
        pass

    @abstractmethod
    def insertintodb(self, conn: DBConnect, is_auto: bool = True):
        pass

    def validate_data(self, data):
        if not isinstance(data, list) or len(data) != len(self.table_columns):
            raise ValueError(f"Data must be a list with {len(self.table_columns)} elements.")
        for value, col_type in zip(data, self.table_types):
            if not isinstance(value, mysql_to_python_type[col_type]):
                raise TypeError(f"Value {value} for column {self.table_columns[data.index(value)]} must be of type {mysql_to_python_type[col_type]}.")

class CompanyBaseModel(BaseModel):
    hotel_group_id: int
    hotel_id: int
    id: int
    name: str
    name2: Optional[str] = None
    name3: Optional[str] = None
    name_combine: Optional[str] = None
    is_save: Optional[str] = None
    language: Optional[str] = None
    nation: Optional[str] = None
    phone: Optional[str] = None
    mobile: Optional[str] = None
    mobile2: Optional[str] = None
    fax: Optional[str] = None
    email: Optional[str] = None
    email2: Optional[str] = None
    website: Optional[str] = None
    blog: Optional[str] = None
    linkman1: Optional[str] = None
    occupation: Optional[str] = None
    birth: Optional[datetime] = None
    birth2: Optional[datetime] = None
    linkman2: Optional[str] = None
    occupation2: Optional[str] = None
    country: Optional[str] = None
    state: Optional[str] = None
    city: Optional[str] = None
    division: Optional[str] = None
    street: Optional[str] = None
    zipcode: Optional[str] = None
    representative: Optional[str] = None
    representative_id_no: Optional[str] = None
    is_host: Optional[str] = None
    register_no: Optional[str] = None
    bank_name: Optional[str] = None
    bank_account: Optional[str] = None
    tax_no: Optional[str] = None
    remark: Optional[str] = None
    is_visible: Optional[str] = None
    create_hotel: Optional[str] = None
    create_user: Optional[str] = None
    create_datetime: Optional[datetime] = None
    modify_hotel: Optional[str] = None
    modify_user: Optional[str] = None
    modify_datetime: Optional[datetime] = None
    strict: Optional[str] = None

class CompanyBase(Table):
    def __init__(self):
        super().__init__()
        self.table_name = 'company_base'
        self.table_columns = tuple(CompanyBaseModel.model_fields.keys())
        self.table_types = tuple(
            [field.type_.__name__ for field in CompanyBaseModel.model_fields.values()]
        )
        self.table_data: pd.DataFrame = pd.DataFrame(columns=self.table_columns)

    def append(self, data=None):
        validated_data = CompanyBaseModel(**dict(zip(self.table_columns, data)))
        length = len(self.table_data)
        self.table_data.loc[length] = validated_data.dict()

    def get(self):
        return self.table_data

    def set(self, data):
        if isinstance(data, list):
            validated_data = [CompanyBaseModel(**dict(zip(self.table_columns, row))) for row in data]
            self.table_data = pd.DataFrame([item.dict() for item in validated_data], columns=self.table_columns)
        elif isinstance(data, pd.DataFrame):
            for index, row in data.iterrows():
                CompanyBaseModel(**row.to_dict())
            self.table_data = data
        else:
            raise ValueError("Data must be a list of rows or a pandas DataFrame.")

    def init_type(self):
        self.table_data = self.table_data.astype(
            dict(zip(self.table_columns, [mysql_to_python_type[col_type] for col_type in self.table_types])))

    def insertintodb(self, conn: DBConnect, is_auto: bool = True):
        try:
            conn.connect()
            for index, row in self.table_data.iterrows():
                values = [self.hotel_group_id, self.hotel_id] if is_auto else []
                values.extend(row[2:].astype(str))
                sql = f'INSERT INTO {self.table_name}({", ".join(self.table_columns)}) VALUES ({", ".join(["%s"] * len(values))})'
                conn.execute(sql, tuple(values))
        except Exception as e:
            print(e)
        finally:
            conn.close()

class CompanyTypeModel(BaseModel):
    hotel_group_id: int
    hotel_id: int
    id: int
    company_id: int
    sta: Optional[str] = None
    manual_no: Optional[str] = None
    sys_cat: Optional[str] = None
    flag_cat: Optional[str] = None
    grade: Optional[str] = None
    latency: Optional[str] = None
    class1: Optional[str] = None
    class2: Optional[str] = None
    class3: Optional[str] = None
    class4: Optional[str] = None
    src: Optional[str] = None
    channel: Optional[str] = None
    market: Optional[str] = None
    vip: Optional[str] = None
    belong_app_code: Optional[str] = None
    membership_type: Optional[str] = None
    membership_no: Optional[str] = None
    membership_level: Optional[str] = None
    over_rsvsrc: Optional[str] = None
    valid_begin: Optional[datetime] = None
    valid_end: Optional[datetime] = None
    code1: Optional[str] = None
    code2: Optional[str] = None
    code3: Optional[str] = None
    code4: Optional[str] = None
    code5: Optional[str] = None
    flag: Optional[int] = None
    saleman: Optional[str] = None
    ar_no1: Optional[int] = None
    ar_no2: Optional[int] = None
    extra_flag: Optional[str] = None
    extra_info: Optional[str] = None
    comments: Optional[str] = None
    create_user: Optional[str] = None
    create_datetime: Optional[datetime] = None
    modify_user: Optional[str] = None
    modify_datetime: Optional[datetime] = None
    is_verified: Optional[str] = None

class CompanyType(Table):
    def __init__(self):
        super().__init__()
        self.table_name = 'company_type'
        self.table_columns = tuple(CompanyTypeModel.__fields__.keys())
        self.table_types = tuple([field.type_.__name__ for field in CompanyTypeModel.__fields__.values()])
        self.table_data: pd.DataFrame = pd.DataFrame(columns=self.table_columns)

    def append(self, data):
        validated_data = CompanyTypeModel(**dict(zip(self.table_columns, data)))
        length = len(self.table_data)
        self.table_data.loc[length] = validated_data.dict()

    def get(self):
        return self.table_data

    def set(self, data):
        if isinstance(data, list):
            validated_data = [CompanyTypeModel(**dict(zip(self.table_columns, row))) for row in data]
            self.table_data = pd.DataFrame([item.dict() for item in validated_data], columns=self.table_columns)
        elif isinstance(data, pd.DataFrame):
            for index, row in data.iterrows():
                CompanyTypeModel(**row.to_dict())
            self.table_data = data
        else:
            raise ValueError("Data must be a list of rows or a pandas DataFrame.")

    def init_type(self):
        self.table_data = self.table_data.astype(
            dict(zip(self.table_columns, [mysql_to_python_type[col_type] for col_type in self.table_types])))

    def insertintodb(self, conn: DBConnect):
        try:
            conn.connect()
            for index, row in self.table_data.iterrows():
                values = row.astype(str)
                sql = f'INSERT INTO {self.table_name}({", ".join(self.table_columns)}) VALUES ({", ".join(["%s"] * len(values))})'
                conn.execute(sql, tuple(values))
        except Exception as e:
            print(e)
        finally:
            conn.close()
