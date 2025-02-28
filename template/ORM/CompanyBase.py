from sqlalchemy import Column, String, BigInteger, Date, Text, DateTime, Index
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class CompanyBase(Base):
    __tablename__ = 'company_base'

    hotel_group_id = Column(BigInteger, nullable=False)
    hotel_id = Column(BigInteger, nullable=False)
    id = Column(BigInteger, primary_key=True, autoincrement=True, comment='档案id')
    name = Column(String(256), nullable=False)
    name2 = Column(String(256), nullable=False)
    name3 = Column(String(256), nullable=False)
    name_combine = Column(String(256), nullable=False)
    is_save = Column(String(2), default='F', nullable=False, comment='表示该档案是否长久保存，不能删除')
    language = Column(String(10), nullable=False, comment='code_base.language.code')
    nation = Column(String(10), nullable=False, comment='code_country.code')
    phone = Column(String(160), nullable=True, comment='可以逗号分隔多个')
    mobile = Column(String(160), nullable=True)
    mobile2 = Column(String(160), default='', nullable=False)
    fax = Column(String(60), nullable=True, comment='可以逗号分隔多个')
    email = Column(String(160), nullable=True, comment='可以逗号分隔多个')
    email2 = Column(String(160), default='', nullable=False)
    website = Column(String(60), nullable=True, comment='可以逗号分隔多个')
    blog = Column(String(60), nullable=True, comment='可以逗号分隔多个')
    linkman1 = Column(String(60), nullable=True)
    occupation = Column(String(60), nullable=False)
    birth = Column(Date, nullable=True)
    birth2 = Column(Date, nullable=True)
    linkman2 = Column(String(60), nullable=True)
    occupation2 = Column(String(60), default='', nullable=False)
    country = Column(String(10), nullable=False, comment='code_country.code')
    state = Column(String(10), nullable=True, comment='code_province.code')
    city = Column(String(40), nullable=False)
    division = Column(String(6), nullable=True, comment='code_division.code')
    street = Column(String(512), nullable=True)
    zipcode = Column(String(12), nullable=True)
    representative = Column(String(60), nullable=True)
    representative_id_no = Column(String(20), default='', nullable=True)
    is_host = Column(String(2), default='', nullable=True)
    register_no = Column(String(30), nullable=True)
    bank_name = Column(String(60), nullable=True)
    bank_account = Column(String(30), nullable=True)
    tax_no = Column(String(30), nullable=True)
    remark = Column(Text, nullable=True)
    is_visible = Column(String(2), default='T', nullable=True, comment='F商务版不可见/默认(NULL or T)商务版可见')
    create_hotel = Column(String(20), nullable=False)
    create_user = Column(String(20), nullable=False)
    create_datetime = Column(DateTime, nullable=False)
    modify_hotel = Column(String(20), nullable=False)
    modify_user = Column(String(20), nullable=False)
    modify_datetime = Column(DateTime, nullable=False)
    strict = Column(String(128), default='*', nullable=True)

    __table_args__ = (
        Index('Index_1', 'hotel_group_id', 'hotel_id', 'name_combine'),
        Index('group_hotel_mobile', 'hotel_group_id', 'hotel_id', 'mobile'),
        Index('group_hotel_phone', 'hotel_group_id', 'hotel_id', 'phone'),
        Index('group_name_index', 'hotel_group_id', 'name'),
        Index('name', 'hotel_group_id', 'hotel_id', 'name'),
    )