import time
import pandas as pd
from template.ORM.Connect import Connect
from template.ORM.CompanyBase import CompanyBase, Base
from template.CompanyImport import insert_company_base


db_host = "192.168.63.240"
db_port = 3306
db_user = "gc_spt"
db_pwd = "gc_spt20220509"
db_name = "portal_pms"
is_ssh = True
db_ssh_host = "122.224.119.138"
db_ssh_port = 13305
db_ssh_user = "root"
db_ssh_pwd = "240.deviskaifa"


if __name__ == "__main__":
    dict = {
        "hotel_group_id": 2,
        "hotel_id": 9,
        "name": "test",
        "name2": "test",
        "name3": "test",
        "name_combine": "test",
        "is_save": "F",
        "language": "C",
        "nation": "CN",
        "phone": "13912345678",
        "mobile": "13912345678",
        "fax": "13912345678",
        "email": "",
        "website": "",
        "blog": "",
        "linkman1": "ZS",
        "occupation": "",
        "linkman2": "",
        "country": "CN",
        "state": "",
        "city": "",
        "division": "",
        "street": "test",
        "zipcode": "",
        "representative": "",
        "register_no": "",
        "bank_name": "",
        "bank_account": "",
        "tax_no": "",
        "remark": "",
        "create_hotel": 9,
        "create_user": "SYSTEM",
        "create_datetime": time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),
        "modify_hotel": 9,
        "modify_user": "SYSTEM",
        "modify_datetime": time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),
    }

    test = pd.DataFrame(dict, index=[0])
    print(test)
    try:
        conn = Connect(db_host = db_host, db_port = db_port, db_user = db_user, db_pwd = db_pwd, db_name = db_name, is_ssh = is_ssh, db_ssh_host = db_ssh_host, db_ssh_port = db_ssh_port, db_ssh_user = db_ssh_user, db_ssh_pwd = db_ssh_pwd)
        a = insert_company_base(test, conn, 0, 2, 9)
        print(a)
    except Exception as e:
        print(e)
