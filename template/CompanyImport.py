import datetime
from template.tool import convert_dict_valuestype
from template.DBConnect import DBConnect
import pandas as pd

company_datatype = {'no': 'varchar', 'accnt': 'varchar', 'name': 'varchar', 'valid_begin': 'varchar',
                    'valid_end': 'varchar', 'sys_cat': 'varchar', 'linkman1': 'varchar', 'ratecode': 'varchar',
                    'mobile': 'varchar', 'phone': 'varchar', 'fax': 'varchar', 'saleman': 'varchar',
                    'street': 'varchar', }



def companydata_process(companydata: pd.DataFrame, conn: DBConnect, hotel_code) -> pd.DataFrame:
    n = 0
    data: pd.DataFrame = companydata
    conn.connect()
    hotel_group_id = conn.query(f'select hotel_group_id from hotel where code = {hotel_code}')
    hotel_id = conn.query(f'select hotel_id from hotel where code = {hotel_code}')
    sales_man = conn.query(f'select code,name from sales_man where hotel_group_id = {hotel_group_id[0][0]} and hotel_id = {hotel_id[0][0]}')
    conn.close()

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
        for code, saleman in sales_man:
            if row['saleman'] == saleman:
                row['saleman'] = code
                break
        row['accnt'] = n
        n = n + 1

    return data

def companydata_import(company_data, conn: DBConnect,hotel_code):
    conn.connect()
    hotel_group_id = conn.query(f'select hotel_group_id from hotel where code = {hotel_code}')
    hotel_id = conn.query(f'select hotel_id from hotel where code = {hotel_code}')
    conn.execute(f'INSERT INTO up_status(hotel_id,up_step,time_begin,time_end,time_long,remark) VALUES({hotel_group_id[0][0]},\'COMPANY\',NOW(),NULL,0,\'\')')

    conn.close()

class CompanyImport:
    def __init__(self):
        pass




