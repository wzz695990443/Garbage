from sqlalchemy import Column, BigInteger, String, DateTime, CHAR, Index
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class MemberType(Base):
    __tablename__ = "member_type"

    hotel_group_id = Column(BigInteger, nullable=False)
    hotel_id = Column(BigInteger, nullable=False)
    id = Column(BigInteger, primary_key=True, autoincrement=True)
    member_id = Column(BigInteger, nullable=False, comment="member_base.id")
    sta = Column(
        String(2), default="I", nullable=False, comment="code_base.profile_sta.code"
    )
    manual_no = Column(String(20), nullable=True, comment="自由输入")
    sys_cat = Column(String(10), nullable=True, comment="F=客人 G=团队")
    flag_cat = Column(String(10), nullable=True, comment="code_base.guest_type.code")
    grade = Column(String(10), nullable=True, comment="code_base.guest_grade.code")
    latency = Column(String(10), nullable=True, comment="code_base.latency.code")
    class1 = Column(String(10), nullable=True, comment="code_base.profile_class1.code")
    class2 = Column(String(10), nullable=True, comment="code_base.profile_class2.code")
    class3 = Column(String(10), nullable=True, comment="code_base.profile_class3.code")
    class4 = Column(String(10), nullable=True, comment="code_base.profile_class4.code")
    src = Column(String(20), nullable=True, comment="code_base.src_code.code")
    market = Column(String(20), nullable=True, comment="code_base.market_code..code")
    vip = Column(String(10), nullable=True, comment="code_base.vip.code")
    belong_app_code = Column(String(20), nullable=True)
    membership_type = Column(String(30), nullable=True)
    membership_no = Column(String(20), nullable=True)
    membership_level = Column(String(30), nullable=True)
    over_rsvsrc = Column(CHAR(2), default="F", nullable=True, comment="T/F")
    valid_begin = Column(DateTime, nullable=True)
    valid_end = Column(DateTime, nullable=True)
    code1 = Column(String(20), nullable=True, comment="code_ratecode.code")
    code2 = Column(String(20), nullable=True, comment="预留")
    flag = Column(String(60), nullable=True, comment="code_base.guest_flag.code")
    saleman = Column(String(20), nullable=True, comment="sales_man.code")
    ar_no1 = Column(BigInteger, nullable=True, comment="应收账户id")
    ar_no2 = Column(BigInteger, nullable=True, comment="应收账户id")
    extra_flag = Column(String(30), nullable=True, comment="位置状态列")
    extra_info = Column(String(30), nullable=True, comment="预留字段")
    comments = Column(String(255), nullable=True)
    create_user = Column(String(20), nullable=False)
    create_datetime = Column(DateTime, nullable=False)
    modify_user = Column(String(20), nullable=False)
    modify_datetime = Column(DateTime, nullable=False)

    __table_args__ = (
        Index("Index_1", "hotel_group_id", "hotel_id", "member_id", unique=True),
        Index("Index_2", "hotel_group_id", "hotel_id", "manual_no"),
        Index(
            "Index_3", "hotel_group_id", "hotel_id", "membership_type", "membership_no"
        ),
        Index("Index_4", "hotel_group_id", "hotel_id", "saleman"),
        Index("Index_5", "hotel_group_id", "member_id"),
    )
