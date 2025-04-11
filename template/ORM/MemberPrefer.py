from sqlalchemy import Column, BigInteger, String, DateTime, Index
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class MemberPrefer(Base):
    # 针对不同的酒店，可以有不同的喜好
    __tablename__ = "member_prefer"

    hotel_group_id = Column(BigInteger, nullable=False)
    hotel_id = Column(BigInteger, nullable=False)
    id = Column(BigInteger, primary_key=True, autoincrement=True)
    member_id = Column(BigInteger, nullable=False, comment="member_base.id")
    specials = Column(
        String(60), nullable=True, comment="多选代码 code_rsv_special.code"
    )
    amenity = Column(
        String(200), nullable=True, comment="多选代码 code_base.amenities.code"
    )
    feature = Column(String(255), nullable=True)
    room_prefer = Column(String(60), nullable=True, comment="自由输入")
    interest = Column(
        String(60), nullable=True, comment="多选代码 code_base.interest.code"
    )
    prefer_front = Column(String(255), nullable=True)
    prefer_fb = Column(String(255), nullable=True)
    prefer_other = Column(String(255), nullable=True)
    taboo = Column(String(255), nullable=True)
    create_user = Column(String(20), nullable=False)
    create_datetime = Column(DateTime, nullable=False)
    modify_user = Column(String(20), nullable=False)
    modify_datetime = Column(DateTime, nullable=False)

    __table_args__ = (
        Index("Index_1", "hotel_group_id", "hotel_id", "member_id", unique=True),
        Index("idx_gid_mid", "hotel_group_id", "member_id"),
    )
