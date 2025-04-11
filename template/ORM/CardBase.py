from sqlalchemy import (
    Column,
    BigInteger,
    String,
    DateTime,
    CHAR,
    DECIMAL,
    Integer,
    Index,
)
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class CardBase(Base):
    __tablename__ = "card_base"

    hotel_group_id = Column(BigInteger, nullable=False)
    hotel_id = Column(BigInteger, nullable=False)
    id = Column(BigInteger, primary_key=True, autoincrement=True)
    member_id = Column(BigInteger, nullable=False, comment="member_base.id")
    card_no = Column(String(20), nullable=False)
    card_no2 = Column(String(20), default="", nullable=False)
    inner_card_no = Column(
        BigInteger, nullable=True, comment="插入记录是生成,升级换卡号等操作不能更改"
    )
    card_master = Column(String(30), default="", nullable=False)
    sta = Column(
        CHAR(2),
        default="R",
        nullable=False,
        comment="状态=R=初始 I-有效,X-销卡,L-挂失,M-损坏,O-停用 S=休眠",
    )
    card_type = Column(String(30), nullable=False, comment="card_type.code")
    card_level = Column(String(30), nullable=True, comment="card_level.code")
    card_src = Column(String(30), nullable=False, comment="code_base.card_src.code")
    card_name = Column(String(50), default="", nullable=False)
    ratecode = Column(String(128), default="", nullable=False)
    posmode = Column(String(128), default="", nullable=False, comment="暂时不用")
    code3 = Column(String(10), default="", nullable=True)
    code4 = Column(String(10), default="", nullable=True)
    code5 = Column(String(10), default="", nullable=True)
    code6 = Column(String(10), default="", nullable=True)
    date_begin = Column(DateTime, nullable=False)
    date_end = Column(DateTime, nullable=False)
    password = Column(String(64), default="", nullable=False, comment="消费密码")
    salesman = Column(String(10), nullable=False, comment="sales_man.code")
    extra_flag = Column(String(30), default="", nullable=True, comment="占位信息")
    card_flag = Column(
        String(64), nullable=False, comment="多选代码 code_base.card_flag.code"
    )
    crc = Column(String(20), nullable=True, comment="写卡效验码")
    remark = Column(String(512), nullable=True)
    point_pay = Column(DECIMAL(10, 2), default=0.00, nullable=False)
    point_charge = Column(DECIMAL(10, 2), default=0.00, nullable=False)
    point_last_num = Column(Integer, default=0, nullable=False)
    point_last_num_link = Column(Integer, default=0, nullable=False)
    charge = Column(DECIMAL(10, 2), default=0.00, nullable=False)
    pay = Column(DECIMAL(10, 2), default=0.00, nullable=False)
    virtual_child_cards = Column(String(2000), nullable=True)
    freeze = Column(DECIMAL(12, 2), default=0.00, nullable=False)
    credit = Column(DECIMAL(12, 2), default=0.00, nullable=False)
    receipt = Column(DECIMAL(12, 2), default=0.00, nullable=False)
    real_pay = Column(DECIMAL(12, 2), default=0.00, nullable=False)
    last_num = Column(Integer, default=0, nullable=False)
    last_num_link = Column(Integer, default=0, nullable=False)
    sta_trans_date = Column(DateTime, nullable=True)
    create_user = Column(String(20), nullable=False)
    create_datetime = Column(DateTime, nullable=False)
    iss_hotel = Column(String(20), nullable=False, comment="hotel.code")
    create_user2 = Column(String(20), nullable=False)
    create_datetime2 = Column(DateTime, nullable=False)
    modify_user2 = Column(String(20), nullable=False)
    modify_datetime2 = Column(DateTime, nullable=False)
    modify_user = Column(String(20), nullable=False)
    modify_datetime = Column(DateTime, nullable=False)

    __table_args__ = (
        Index("Index_1", "hotel_group_id", "card_no", unique=True),
        Index("Index_2", "hotel_group_id", "inner_card_no"),
        Index("Index_3", "hotel_group_id", "member_id"),
        Index("Index_4", "hotel_group_id", "create_datetime"),
        Index("Index_6", "hotel_group_id", "card_name"),
        Index("Index_cardNo2", "hotel_group_id", "card_no2"),
        Index("Index_cardSrc", "hotel_group_id", "card_src"),
        Index("index_7", "hotel_group_id", "hotel_id", "card_level", "create_datetime"),
        Index("index_8", "hotel_group_id", "hotel_id", "create_datetime"),
        Index("index_9", "hotel_group_id", "hotel_id", "credit"),
        Index("index_card_master", "hotel_group_id", "card_master"),
        Index("index_iss_hotel", "hotel_group_id", "iss_hotel"),
        Index("mi_gid_card_level", "hotel_group_id", "card_level"),
    )
