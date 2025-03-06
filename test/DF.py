import time
import pandas as pd
from template.ORM.Connect import Connect
from template.ORM.CompanyBase import CompanyBase, Base
from template.CompanyImport import insert_company_base, insert_company_type


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
    dict1 = {
        "hotel_group_id": 2,
        "hotel_id": 9,
        "name": "test001",
        "phone": "13912345678",
        "mobile": "13912345678",
        "fax": "13912345678",
        "email": "",
        "website": "",
        "blog": "",
        "linkman1": "ZS02",
        "occupation": "",
        "linkman2": "",
        "country": "CN",
        "state": "",
        "city": "",
        "division": "",
        "street": " test001",
        "zipcode": "",
        "representative": "",
        "register_no": "",
        "bank_name": "",
        "bank_account": "",
        "tax_no": "",
        "remark": "",
        "sys_cat": "C",
        "ratecode":"",
        "saleman": "",
    }
    dict2 = {
        "hotel_group_id": 2,
        "hotel_id": 9,
        "name": "test002",
        "phone": "13912345678",
        "mobile": "13912345678",
        "fax": "13912345678",
        "email": "",
        "website": "",
        "blog": "",
        "linkman1": "ZS02",
        "occupation": "",
        "linkman2": "",
        "country": "CN",
        "state": "",
        "city": "",
        "division": "",
        "street": " test002",
        "zipcode": "",
        "representative": "",
        "register_no": "",
        "bank_name": "",
        "bank_account": "",
        "tax_no": "",
        "remark": "",
        "sys_cat": "C",
        "ratecode": "",
        "saleman": "",
    }

    test = pd.DataFrame([dict1, dict2])
    for round in test.index:
        print(test["name"].values[round])
    # try:
    #     conn = Connect(db_host = db_host, db_port = db_port, db_user = db_user, db_pwd = db_pwd, db_name = db_name, is_ssh = is_ssh, db_ssh_host = db_ssh_host, db_ssh_port = db_ssh_port, db_ssh_user = db_ssh_user, db_ssh_pwd = db_ssh_pwd)
    #     for round in test.index:
    #         company_id = insert_company_base(test, conn, 0, 2, 9)
    #         print(company_id)
    #         print(insert_company_type(test, conn, round, 2, 9, company_id))
    #         print(insert_company_type(test, conn, round, 2, 0, company_id))
    # except Exception as e:
    #     print(e)
