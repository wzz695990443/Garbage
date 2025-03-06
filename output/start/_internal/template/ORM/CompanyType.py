from sqlalchemy import Column, String, BigInteger, DateTime, Index
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class CompanyType(Base):
    __tablename__ = 'company_type'

    hotel_group_id = Column(BigInteger, nullable=False)
    hotel_id = Column(BigInteger, nullable=False)
    id = Column(BigInteger, primary_key=True, autoincrement=True, comment='档案id')
    company_id = Column(BigInteger, nullable=False, comment='company_base.id')
    sta = Column(String(2), default='I', nullable=False, comment='code_base.profile_sta.code')
    manual_no = Column(String(60), nullable=False)
    sys_cat = Column(String(10), nullable=False, comment='C=公司 S=预订中心 A=旅行社')
    flag_cat = Column(String(10), nullable=False, comment='code_base.guest_type.code')
    grade = Column(String(10), nullable=False, comment='code_base.guest_grade.code')
    latency = Column(String(10), nullable=False, comment='code_base.latency.code')
    class1 = Column(String(10), nullable=False, comment='code_base.profile_class1.code')
    class2 = Column(String(10), nullable=False, comment='code_base.profile_class2.code')
    class3 = Column(String(10), nullable=False, comment='code_base.profile_class3.code')
    class4 = Column(String(10), nullable=False, comment='code_base.profile_class4.code')
    src = Column(String(20), nullable=False, comment='code_base.src_code.code')
    channel = Column(String(20), default='', nullable=True)
    market = Column(String(20), nullable=False, comment='code_base.market_code.code')
    vip = Column(String(10), nullable=False, comment='code_base.vip.code')
    belong_app_code = Column(String(3), nullable=False, comment='code_base.guest_belong.code')
    membership_type = Column(String(30), nullable=True, comment='code_profile_card_type.code')
    membership_no = Column(String(20), nullable=False)
    membership_level = Column(String(30), nullable=True, comment='code_profile_card_level.code')
    over_rsvsrc = Column(String(2), default='F', nullable=False, comment='T/F')
    valid_begin = Column(DateTime, nullable=True)
    valid_end = Column(DateTime, nullable=True)
    code1 = Column(String(80), nullable=True)
    code2 = Column(String(20), nullable=True, comment='预留')
    code3 = Column(String(20), nullable=True, comment='佣金码 ')
    code4 = Column(String(20), nullable=True)
    code5 = Column(String(20), nullable=True)
    flag = Column(String(60), nullable=False, comment='多选代码 code_base.guest_flag.code')
    saleman = Column(String(20), nullable=False, comment='sales_man.code')
    ar_no1 = Column(BigInteger, nullable=True)
    ar_no2 = Column(BigInteger, nullable=True)
    extra_flag = Column(String(30), nullable=False, comment='位置状态列')
    extra_info = Column(String(30), nullable=False, comment='预留')
    comments = Column(String(2048), nullable=True)
    create_user = Column(String(20), nullable=False)
    create_datetime = Column(DateTime, nullable=False)
    modify_user = Column(String(20), nullable=False)
    modify_datetime = Column(DateTime, nullable=False)
    is_verified = Column(String(2), default='F', nullable=True)

    __table_args__ = (
        Index('Index_1', 'hotel_group_id', 'hotel_id', 'company_id', unique=True),
        Index('Index_2', 'hotel_group_id', 'hotel_id', 'saleman'),
        Index('Index_3', 'hotel_group_id', 'hotel_id', 'valid_begin', 'valid_end'),
        Index('Index_4', 'hotel_group_id', 'hotel_id', 'membership_type', 'membership_no'),
        Index('Index_5', 'hotel_group_id', 'hotel_id', 'manual_no'),
        Index('pt_cmpid_idx_0', 'hotel_group_id', 'company_id'),
    )