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

def validate(data: pd.DataFrame, column: str, round: int, default="") -> str:
    if column in data.columns:
        if data[column].values[round] is not None:
            return data[column].values[round]
    return default


def insert_company_base(
    data: pd.DataFrame, session, round, hotel_group_id, hotel_id, id=None
) -> int:
    try:
        # session = conn.connect()
        # Base.metadata.create_all(session.engine)
        if session is not None:
            print("CompanyBase Importing: "+str(round))
            new_companybase = CompanyBase(
                hotel_group_id=hotel_group_id,
                hotel_id=hotel_id,
                id=id,
                name=validate(data, "name", round),
                name2=validate(data, "name", round),
                name3=validate(data, "name", round),
                name_combine=validate(data, "name", round),
                is_save=validate(data, "is_save", round, default="F"),
                language=validate(data, "language", round, default="C"),
                nation=validate(data, "nation", round, default="CN"),
                phone=validate(data, "phone", round),
                mobile=validate(data, "mobile", round),
                fax=validate(data, "fax", round),
                email=validate(data, "email", round),
                website=validate(data, "website", round),
                blog=validate(data, "blog", round),
                linkman1=validate(data, "linkman1", round),
                occupation=validate(data, "occupation", round),
                linkman2=validate(data, "linkman2", round),
                country=validate(data, "nation", round, default="CN"),
                state=validate(data, "state", round),
                city=validate(data, "city", round),
                division=validate(data, "division", round),
                street=validate(data, "street", round),
                zipcode=validate(data, "zipcode", round),
                representative=validate(data, "representative", round),
                register_no=validate(data, "register_no", round),
                bank_name=validate(data, "bank_name", round),
                bank_account=validate(data, "bank_account", round),
                tax_no=validate(data, "tax_no", round),
                remark=validate(data, "remark", round),
                create_hotel=hotel_id,
                create_user="SYSTEM",
                create_datetime=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),
                modify_hotel=hotel_id,
                modify_user="SYSTEM",
                modify_datetime=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),
            )

            session.add(new_companybase)
            session.flush()
            session.refresh(new_companybase)
            session.commit()
            return new_companybase.id
    except Exception as e:
        print(e)
        session.rollback()
        return -1
    finally:
        print("CompanyBase Imported: " + str(round))
        # session.close()
        # conn.close()


def insert_company_type(
    data: pd.DataFrame,
    session,
    round,
    hotel_group_id,
    hotel_id,
    company_id,
    id=None,
) -> int:
    try:
        # session = conn.connect()
        # Base.metadata.create_all(conn.engine)
        if session is not None:
            print("CompanyType Importing: " + str(round))
            new_companytype = CompanyType(
                hotel_group_id=hotel_group_id,
                hotel_id=hotel_id,
                id = id,
                company_id=company_id,
                sta=validate(data, "sta", round, default="I"),
                manual_no=validate(data, "manual_no", round),
                sys_cat=validate(data, "sys_cat", round),
                flag_cat=validate(data, "flag_cat", round),
                grade=validate(data, "grade", round),
                latency=validate(data, "latency", round),
                class1=validate(data, "class1", round),
                class2=validate(data, "class2", round),
                class3=validate(data, "class3", round),
                class4=validate(data, "class4", round),
                src=validate(data, "src", round),
                market=validate(data, "market", round),
                vip=validate(data, "vip", round),
                belong_app_code=validate(data, "belong_app_code", round, default="1"),
                membership_type=validate(data, "membership_type", round),
                membership_no=validate(data, "membership_no", round),
                membership_level=validate(data, "membership_level", round),
                over_rsvsrc=validate(data, "over_rsvsrc", round, default="F"),
                valid_begin=validate(
                    data,
                    "valid_begin",
                    round,
                    default=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),
                ),
                valid_end=validate(
                    data, "valid_end", round, default="2050-01-01 00:00:00"
                ),
                code1=validate(data, "ratecode", round),
                code2=validate(data, "code2", round),
                code3=validate(data, "code3", round),
                code4=validate(data, "code4", round),
                code5=validate(data, "code5", round),
                flag=validate(data, "flag", round),
                saleman=validate(data, "saleman", round),
                ar_no1=validate(data, "ar_no1", round),
                ar_no2=validate(data, "ar_no2", round),
                extra_flag=validate(
                    data, "extra_flag", round, default="000000000000000000000000000000"
                ),
                extra_info=round,
                comments=str(hotel_group_id) + str(hotel_id) + str(round),
                create_user="SYSTEM",
                create_datetime=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),
                modify_user="SYSTEM",
                modify_datetime=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),
            )
            session.add(new_companytype)
            session.flush()
            session.refresh(new_companytype)
            session.commit()
            return new_companytype.id

    except Exception as e:
        print(e)
        session.rollback()
        return -1
    finally:
        print("CompanyType Imported: " + str(round))
        # session.close()
        # conn.close()
