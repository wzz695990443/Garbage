from sqlalchemy import Column, BigInteger, String, DateTime, CHAR, Integer, Index
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class MemberLinkAddr(Base):
    __tablename__ = "member_link_addr"

    hotel_group_id = Column(BigInteger, nullable=False)
    hotel_id = Column(BigInteger, nullable=False)
    id = Column(BigInteger, primary_key=True, autoincrement=True, comment="地址id")
    member_id = Column(BigInteger, nullable=False, comment="member_base.id")
    addr_type = Column(
        String(10), nullable=False, comment="地址类型 code_base.addr_type.code"
    )
    is_default = Column(
        CHAR(2),
        default="F",
        nullable=False,
        comment="T/F 每个客户必须有且只有一个首选地址",
    )
    country = Column(String(10), nullable=True, comment="code_country.code")
    state = Column(String(10), nullable=True, comment="code.province.code")
    city = Column(String(40), nullable=True)
    division = Column(String(6), nullable=True, comment="code_devision.code")
    street = Column(String(512), nullable=True)
    zipcode = Column(String(12), nullable=True)
    list_order = Column(Integer, default=100, nullable=True)
    remark = Column(String(64), nullable=True)
    create_hotel = Column(String(20), nullable=False)
    create_user = Column(String(20), nullable=False)
    create_datetime = Column(DateTime, nullable=False)
    modify_hotel = Column(String(20), nullable=False)
    modify_user = Column(String(20), nullable=False)
    modify_datetime = Column(DateTime, nullable=False)

    __table_args__ = (
        Index("Index_1", "hotel_group_id", "hotel_id", "member_id"),
        Index("Index_2", "hotel_group_id", "member_id", "is_default"),
    )
