from sqlalchemy import Column, BigInteger, String, DateTime, Integer, Index
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class MemberWeb(Base):
    __tablename__ = "member_web"

    hotel_group_id = Column(BigInteger, nullable=False)
    hotel_id = Column(BigInteger, nullable=False)
    id = Column(BigInteger, primary_key=True, autoincrement=True)
    member_Id = Column(BigInteger, nullable=False)
    nick_name = Column(String(16), nullable=True)
    login_accnt = Column(String(16), nullable=True)
    login_pw = Column(String(32), nullable=True)
    pw_question = Column(String(2), nullable=True, comment="code_base.card_pwdask.code")
    pw_answer = Column(String(16), nullable=True)
    longin_type = Column(String(2), nullable=True, comment="code_base.login_type.code")
    login_time = Column(DateTime, nullable=True)
    login_error_time = Column(DateTime, nullable=True)
    login_addr = Column(String(16), nullable=True)
    login_card = Column(BigInteger, nullable=True)
    login_error_count = Column(
        BigInteger, default=0, nullable=True, comment="登录错误次数"
    )
    head_no = Column(Integer, nullable=True)
    head1 = Column(BigInteger, nullable=True)
    head2 = Column(BigInteger, nullable=True)
    head3 = Column(BigInteger, nullable=True)
    head4 = Column(BigInteger, nullable=True)
    head_img_url = Column(String(512), nullable=True, comment="接口注册传入的用户头像")
    open_id_type = Column(String(20), nullable=True)
    open_id_user_id = Column(String(50), nullable=True)
    mobile_send = Column(String(160), nullable=True)
    mobile_bind = Column(String(2), default="F", nullable=True)
    mobile_verify = Column(String(10), nullable=True)
    mobile_valid = Column(DateTime, nullable=True)
    email_send = Column(String(160), nullable=True)
    email_bind = Column(String(2), default="F", nullable=True)
    email_verify = Column(String(10), nullable=True)
    email_valid = Column(DateTime, nullable=True)
    create_hotel = Column(String(20), nullable=False, comment="hotel.code")
    create_user = Column(String(20), nullable=False, comment="user.code")
    create_datetime = Column(DateTime, nullable=False)
    modify_hotel = Column(String(20), nullable=False)
    modify_user = Column(String(20), nullable=False)
    modify_datetime = Column(DateTime, nullable=False)

    __table_args__ = (
        Index("Index_1", "hotel_group_id", "hotel_id", "member_Id"),
        Index("Index_2", "hotel_group_id", "member_Id"),
        Index("Index_3", "hotel_group_id", "open_id_type", "open_id_user_id"),
    )
