import tool
from tool import convert_dict_valuestype

company_datatype = {'no': 'varchar','accnt': 'varchar','name': 'varchar','valid_begin': 'varchar','valid_end': 'varchar','sys_cat': 'varchar','linkman1': 'varchar','ratecode': 'varchar','mobile': 'varchar','phone': 'varchar','fax': 'varchar','saleman': 'varchar','street': 'varchar',}

def companydata_process(data):
    for item in data:
        convert_dict_valuestype(item,company_datatype,True)
        for key,value in item.items():
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
                case 'no':
                    item['no'] = item['no'].strip()
