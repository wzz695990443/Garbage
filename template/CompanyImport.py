import datetime
from template.tool import convert_dict_valuestype
from template.DBConnect import DBConnect

from template.ORM.Connect import Connect
from template.ORM.CompanyBase import CompanyBase, Base
from template.ORM.CompanyType import CompanyType, Base
from template.ORM.UpStatus import UpStatus, Base
from template.ORM.UpMapAccnt import UpMapAccnt, Base

import pandas as pd

company_datatype = {'no': 'varchar', 'accnt': 'varchar', 'name': 'varchar', 'valid_begin': 'varchar',
                    'valid_end': 'varchar', 'sys_cat': 'varchar', 'linkman1': 'varchar', 'ratecode': 'varchar',
                    'mobile': 'varchar', 'phone': 'varchar', 'fax': 'varchar', 'saleman': 'varchar',
                    'street': 'varchar', }

class CompanyImport:
    def __init__(self, companydata: pd.DataFrame, conn: DBConnect, hotel_code):
        self.hotel_code = hotel_code
        self.hotel_group_id = None
        self.hotel_id = None
        self.sales_man = None
        self.conn = conn
        self.conn.connect()
        self.companydata = convert_dict_valuestype(companydata.to_dict(), company_datatype, False)
        self.hotel_group_id = conn.query(f"""
                                         select hotel_group_id from hotel 
                                         where code = {hotel_code}
                                         """)
        self.hotel_id = conn.query(f"""
                                   select hotel_id from hotel 
                                   where code = {hotel_code}
                                   """)
        self.sales_man = conn.query(f"""
                                    select code,name from sales_man 
                                    where hotel_group_id = {self.hotel_group_id[0][0]} and hotel_id = {self.hotel_id[0][0]}
                                    """)
        self.conn.close()
        
        
        
    def data_preprocess(self,companydata: pd.DataFrame,sales_man) -> pd.DataFrame:
        n = 0
        data: pd.DataFrame = companydata
        data['valid_begin'] = data['valid_begin'].apply(lambda x: datetime.datetime.strptime(x, '%Y-%m-%d').strftime('%Y%m%d'))
        data['valid_end'] = data['valid_end'].apply(lambda x: datetime.datetime.strptime(x, '%Y-%m-%d').strftime('%Y%m%d'))
        data.astype(str)
        for index, row in data.iterrows():
            match row['sys_cat']:
                case '协议单位':
                    row['sys_cat'] = 'C'
                case '订房中心':
                    row['sys_cat'] = 'S'
                case '旅行社':
                    row['sys_cat'] = 'A'
            row['name'] = row['name'].strip()
            row['mobile'] = row['mobile'].strip()
            row['phone'] = row['phone'].strip()
            row['saleman'] = row['saleman'].strip()
            row['no'] = row['no'].strip()
            row['street'] = row['street'].strip()
            row['comments'] = row['comments'].strip()
            row['linkman1'] = row['linkman1'].strip()
            for code, saleman in sales_man:
                if row['saleman'] == saleman:
                    row['saleman'] = code
                    break
            row['accnt'] = n
            n = n + 1
        
        self.companydata = data
        return data

    def companydata_import(self,companydata: pd.DataFrame):
        insert_up_status_query = f"""
            INSERT INTO up_status(hotel_id, up_step, time_begin, time_end, time_long, remark) 
            VALUES ({self.hotel_id}, 'COMPANY', NOW(), NOW(), 0, '')
            """
        try:
            for index, row in self.companydata.iterrows():
                insert_company_query = f"""
                    INSERT INTO company(no, accnt, name, valid_begin, valid_end, sys_cat, linkman1, ratecode, mobile, phone, fax, saleman, street, comments, hotel_group_id, hotel_id) 
                    VALUES ('{row['no']}', '{row['accnt']}', '{row['name']}', '{row['valid_begin']}', '{row['valid_end']}', '{row['sys_cat']}', '{row['linkman1']}', '{row['ratecode']}', '{row['mobile']}', '{row['phone']}', '{row['fax']}', '{row['saleman']}', '{row['street']}', '{row['comments']}', '{self.hotel_group_id}', '{self.hotel_id}')
                    """
                self.conn.connect()
                self.conn.conn.begin()
                self.conn.execute(insert_up_status_query)
                self.conn.execute(insert_company_query)
                self.conn.conn.commit()
                
        except Exception as e:
            print(e)
            self.conn.conn.rollback()
            return False
        finally:
            self.conn.close()

        self.conn.close()


