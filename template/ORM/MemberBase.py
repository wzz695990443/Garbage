from sqlalchemy import Column, BigInteger, String, DateTime, Text, CHAR, Index
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class MemberBase(Base):
    __tablename__ = "member_base"

    hotel_group_id = Column(BigInteger, nullable=False)
    hotel_id = Column(BigInteger, nullable=False)
    id = Column(BigInteger, primary_key=True, autoincrement=True, comment="档案id")
    inner_id = Column(BigInteger, nullable=False)
    guest_id = Column(BigInteger, nullable=True)
    name = Column(String(60), nullable=False)
    last_name = Column(String(40), nullable=False)
    first_name = Column(String(40), nullable=False)
    name2 = Column(String(60), nullable=False)
    name3 = Column(String(60), nullable=False)
    name_combine = Column(String(192), nullable=False)
    is_save = Column(
        String(2),
        default="F",
        nullable=False,
        comment="表示该档案是否长久保存，不能删除",
    )
    sex = Column(String(2), nullable=False, comment="code_base.sex.code")
    language = Column(String(10), nullable=False, comment="code_base.language.code")
    title = Column(String(10), nullable=True, comment="code_greeting.code")
    salutation = Column(String(60), nullable=True, comment="自由输入")
    birth = Column(DateTime, nullable=True)
    race = Column(String(10), nullable=True, comment="code_base.race.code")
    religion = Column(String(10), nullable=True, comment="code_base.religion.code")
    occupation = Column(String(30), nullable=True, comment="code_base.occupation.code")
    career = Column(String(60), nullable=True, comment="自由输入")
    nation = Column(String(10), nullable=False, comment="code_country.code")
    id_code = Column(String(10), nullable=False, comment="code_base.idcode")
    id_no = Column(String(20), nullable=False)
    id_end = Column(DateTime, nullable=True)
    salary = Column(String(10), nullable=True, comment="code_base.salary.code")
    education = Column(String(10), nullable=True, comment="code_base.education.code")
    marital = Column(String(10), nullable=True, comment="code_base.marital.code")
    company_id = Column(BigInteger, nullable=True, comment="company_base.id")
    company_name = Column(String(60), nullable=True)
    pic_photo = Column(String(256), nullable=True, comment="相片图片路径")
    pic_sign = Column(String(256), nullable=True, comment="签字图片路径")
    remark = Column(Text, nullable=True)
    is_anonymous = Column(CHAR(2), default="F", nullable=True, comment="是否匿名卡")
    create_hotel = Column(String(20), nullable=False, comment="hotel.code")
    create_user = Column(String(20), nullable=False, comment="user.code")
    create_datetime = Column(DateTime, nullable=False)
    modify_hotel = Column(String(20), nullable=False)
    modify_user = Column(String(20), nullable=False)
    modify_datetime = Column(DateTime, nullable=False)

    __table_args__ = (
        Index("Index_1", "hotel_group_id", "hotel_id", "name_combine"),
        Index("Index_2", "hotel_group_id", "id_no"),
        Index("Index_3", "hotel_group_id", "inner_id"),
        Index("Index_4", "hotel_group_id", "name"),
        Index("index_birth", "hotel_group_id", "birth"),
        Index("index_create_datetime", "hotel_group_id", "create_datetime"),
        Index(
            "index_create_hotel", "hotel_group_id", "create_hotel", "create_datetime"
        ),
        Index("index_name2", "hotel_group_id", "name2"),
    )
