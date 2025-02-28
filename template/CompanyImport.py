import time
from template.tool import convert_dict_valuestype
from template.DBConnect import DBConnect

from template.ORM.Connect import Connect
from template.ORM.CompanyBase import CompanyBase, Base
from template.ORM.CompanyType import CompanyType, Base
from template.ORM.UpStatus import UpStatus, Base
from template.ORM.UpMapAccnt import UpMapAccnt, Base

# from DataPipeline import DataPipeline

import pandas as pd
required_columns = [
    "no",
    "name",
    "valid_begin",
    "valid_end",
    "sys_cat",
    "linkman1",
    "ratecode",
    "mobile",
    "phone",
    "fax",
    "saleman",
    "street",
]
def insert_company_base(data :pd.DataFrame, conn, round, hotel_group_id, hotel_id) -> int:
    try:
        session = conn.connect()
        Base.metadata.create_all(conn.engine)
        if session is not None:
            print("Connect success")
            new_companybase = CompanyBase(
                hotel_group_id=hotel_group_id,
                hotel_id=hotel_id,
                name=data["name"].values[round],
                name2=data["name"].values[round],
                name3=data["name"].values[round],
                name_combine=data["name"].values[round],
                is_save="F",
                language="C",
                nation="CN",
                phone=data["phone"].values[round],
                mobile=data["mobile"].values[round],
                fax=data["fax"].values[round],
                email="",
                website="",
                blog="",
                linkman1=data["linkman1"].values[round],
                occupation="",
                linkman2="",
                country="CN",
                state="",
                city="",
                division="",
                street=data["street"].values[round],
                zipcode="",
                representative="",
                register_no="",
                bank_name="",
                bank_account="",
                tax_no="",
                remark="",
                create_hotel=hotel_id,
                create_user="SYSTEM",
                create_datetime=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),
                modify_hotel=hotel_id,
                modify_user="SYSTEM",
                modify_datetime=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),
            )

            session.add(new_companybase)
            company_id = session.flush()
            session.refresh(new_companybase)
            session.commit()
            return new_companybase.id
    except Exception as e:
        print(e)
        return None
    finally:
        print('Connect Closing')
        session.close()
        conn.close()

def insert_company_type(data :pd.DataFrame, conn, round, hotel_group_id, hotel_id, company_id) -> int:
    try:
        session = conn.connect()
        Base.metadata.create_all(conn.engine)
        if session is not None:
            print("Connect success")
            new_companytype = CompanyType(
                hotel_group_id=hotel_group_id,
                hotel_id=hotel_id,
                sta="I",
                manual_no=data["no"].values[round],
                sys_cat=data["sys_cat"].values[round],
                flag_cat="",
                grade="",
                latency="",
                class1="",
                class2="",
                class3="",
                class4="",
                src="",
                market="",
                vip="",
                belong_app_code="",
                membership_type="",
                membership_no="",
                membership_level="",
                over_rsvsrc="",
                valid_begin="",
                valid_end="",
                code1="",
                code2="",
                code3="",
                code4="",
                code5="",
                flag="",
                saleman="",
                ar_no1="",
                ar_no2="",
                extra_flag="",
                extra_info="",
                comments="",
                create_user="SYSTEM",
                create_datetime=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),
                modify_user="SYSTEM",
                modify_datetime=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),
            )

    except Exception as e:
        print(e)
        return None
    finally:
        print('Connect Closing')
        session.close()
        conn.close()        
