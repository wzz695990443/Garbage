import tool
from tool import convert_dict_valuestype
from DBConnect import DBConnect

company_datatype = {'no': 'varchar', 'accnt': 'varchar', 'name': 'varchar', 'valid_begin': 'varchar',
                    'valid_end': 'varchar', 'sys_cat': 'varchar', 'linkman1': 'varchar', 'ratecode': 'varchar',
                    'mobile': 'varchar', 'phone': 'varchar', 'fax': 'varchar', 'saleman': 'varchar',
                    'street': 'varchar', }


def companydata_process(companydata, conn: DBConnect, hotel_code):
    n = 0
    data: list = companydata
    conn.connect()
    hotel_group_id = conn.query(f'select hotel_group_id from hotel where code = {hotel_code}')
    hotel_id = conn.query(f'select hotel_id from hotel where code = {hotel_code}')
    sales_man = conn.query(f'select code,name from sales_man where hotel_group_id = {hotel_group_id[0][0]} and hotel_id = {hotel_id[0][0]}')
    conn.close()

    for item in data:
        convert_dict_valuestype(item, company_datatype, True)
        for key, value in item.items():
            match key:
                case 'sys_cat':
                    match item['sys_cat']:
                        case '协议单位':
                            item['sys_cat'] = 'C'
                        case '订房中心':
                            item['sys_cat'] = 'S'
                        case '旅行社':
                            item['sys_cat'] = 'A'
                case 'name':
                    item['name'] = item['name'].strip()
                case 'mobile':
                    item['mobile'] = item['mobile'].strip()
                case 'phone':
                    item['phone'] = item['phone'].strip()
                case 'saleman':
                    item['saleman'] = item['saleman'].strip()
                    for code, saleman in sales_man:
                        if item['saleman'] == saleman:
                            item['saleman'] = code
                            break
                case 'no':
                    item['no'] = item['no'].strip()
                case _:
                    pass
        item['accnt'] = n
        n = n + 1

    return data

def companydata_import(company_data, conn: DBConnect,hotel_code):
    conn.connect()
    hotel_group_id = conn.query(f'select hotel_group_id from hotel where code = {hotel_code}')
    hotel_id = conn.query(f'select hotel_id from hotel where code = {hotel_code}')
    conn.execute(f'INSERT INTO up_status(hotel_id,up_step,time_begin,time_end,time_long,remark) VALUES({hotel_group_id[0][0]},\'COMPANY\',NOW(),NULL,0,\'\')')

    conn.close()

