from sqlalchemy import Column, BigInteger, String, DateTime, Index
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class MemberLinkBase(Base):
    __tablename__ = "member_link_base"

    hotel_group_id = Column(BigInteger, nullable=False)
    hotel_id = Column(BigInteger, nullable=False)
    id = Column(BigInteger, primary_key=True, comment="guest_base.id")
    mobile = Column(String(160), nullable=True, comment="可以逗号分隔多个")
    phone = Column(String(160), nullable=True, comment="可以逗号分隔多个")
    fax = Column(String(60), nullable=True, comment="可以逗号分隔多个")
    email = Column(String(160), nullable=True, comment="可以逗号分隔多个")
    website = Column(String(60), nullable=True, comment="可以逗号分隔多个")
    msn = Column(String(60), nullable=True, comment="可以逗号分隔多个")
    qq = Column(String(60), nullable=True, comment="可以逗号分隔多个")
    sns = Column(String(60), nullable=True, comment="可以逗号分隔多个")
    blog = Column(String(60), nullable=True, comment="可以逗号分隔多个")
    linkman1 = Column(String(60), nullable=True)
    linkman2 = Column(String(60), nullable=True)
    create_hotel = Column(String(20), nullable=False)
    create_user = Column(String(20), nullable=False)
    create_datetime = Column(DateTime, nullable=False)
    modify_hotel = Column(String(20), nullable=False)
    modify_user = Column(String(20), nullable=False)
    modify_datetime = Column(DateTime, nullable=False)

    __table_args__ = (
        Index("Index_1", "hotel_group_id", "mobile"),
        Index("Index_2", "hotel_group_id", "email"),
        Index("Index_3", "hotel_group_id", "linkman2"),
        Index("group_phone", "hotel_group_id", "phone"),
    )
