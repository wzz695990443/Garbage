from sqlalchemy import Column, String, BigInteger, DateTime, Text, LargeBinary, Index, Integer
from sqlalchemy.ext.declarative import declarative_base
import pandas as pd

Base = declarative_base()

class Hotel(Base):
    __tablename__ = 'hotel'

    hotel_group_id = Column(BigInteger, nullable=False)
    id = Column(BigInteger, primary_key=True, autoincrement=True)
    code = Column(String(20), nullable=False, unique=True)
    sta = Column(String(2), default='0', nullable=False, comment='R=初始 H=停用 I=在用')
    audit = Column(String(2), default='0', nullable=False, comment='0=正常 1=不正常')
    descript = Column(String(60), nullable=False, unique=True)
    descript_en = Column(String(60), default='', nullable=False)
    descript_short = Column(String(20), nullable=True)
    country = Column(String(3), nullable=False, comment='code_country.code')
    city = Column(String(60), default='', nullable=False, comment='自由输入')
    address1 = Column(String(256), default='', nullable=False)
    address2 = Column(String(256), default='', nullable=False)
    phone = Column(String(30), default='', nullable=False)
    fax = Column(String(30), default='', nullable=False)
    phone_rsv = Column(String(30), nullable=True)
    website = Column(String(128), nullable=True)
    email = Column(String(64), default='', nullable=False)
    dns = Column(String(64), nullable=True)
    remark = Column(Text, nullable=True)
    logo = Column(LargeBinary, nullable=True)
    photo = Column(String(256), nullable=True)
    html_info = Column(String(256), nullable=True)
    list_order = Column(Integer, default=0, nullable=False)
    create_user = Column(String(20), nullable=False)
    create_datetime = Column(DateTime, nullable=False)
    modify_user = Column(String(20), nullable=False)
    modify_datetime = Column(DateTime, nullable=False)
    province_code = Column(String(32), nullable=True)
    city_code = Column(String(32), nullable=True)
    district_code = Column(String(32), nullable=True)
    town_code = Column(String(32), nullable=True)
    shopping_district_code = Column(String(32), nullable=True)
    scenic_spot_code = Column(String(32), nullable=True)
    book_list_order = Column(String(32), nullable=True)
    start_level_code = Column(String(32), nullable=True)
    brand_code = Column(String(32), nullable=True)
    score = Column(String(5), default='5.0', nullable=True)
    category_code = Column(String(10), nullable=True)
    manage_type = Column(String(10), default='', nullable=True)
    map_html = Column(Text, nullable=True)
    pair_pic = Column(String(350), nullable=True)
    app_type = Column(String(20), default='', nullable=True)
    client_type = Column(String(10), default='', nullable=True)
    client_version = Column(String(10), nullable=True)
    area1 = Column(String(20), nullable=True)
    area2 = Column(String(20), nullable=True)
    online_check = Column(String(2), default='T', nullable=True)
    server_name = Column(String(128), nullable=True)
    decoration_date = Column(DateTime, nullable=True)
    open_date = Column(DateTime, nullable=True)
    hotel_policy = Column(String(2000), nullable=True)

    __table_args__ = (
        Index('Index_3', 'hotel_group_id', 'server_name'),
    )

    def __repr__(self):
        data = {
            "Field": [
                "hotel_group_id", "id", "code", "sta", "audit", "descript", "descript_en", "descript_short", "country",
                "city", "address1", "address2", "phone", "fax", "phone_rsv", "website", "email", "dns", "remark", "logo",
                "photo", "html_info", "list_order", "create_user", "create_datetime", "modify_user", "modify_datetime",
                "province_code", "city_code", "district_code", "town_code", "shopping_district_code", "scenic_spot_code",
                "book_list_order", "start_level_code", "brand_code", "score", "category_code", "manage_type", "map_html",
                "pair_pic", "app_type", "client_type", "client_version", "area1", "area2", "online_check", "server_name",
                "decoration_date", "open_date", "hotel_policy"
            ],
            "Value": [
                self.hotel_group_id, self.id, self.code, self.sta, self.audit, self.descript, self.descript_en, self.descript_short,
                self.country, self.city, self.address1, self.address2, self.phone, self.fax, self.phone_rsv, self.website,
                self.email, self.dns, self.remark, self.logo, self.photo, self.html_info, self.list_order, self.create_user,
                self.create_datetime, self.modify_user, self.modify_datetime, self.province_code, self.city_code, self.district_code,
                self.town_code, self.shopping_district_code, self.scenic_spot_code, self.book_list_order, self.start_level_code,
                self.brand_code, self.score, self.category_code, self.manage_type, self.map_html, self.pair_pic, self.app_type,
                self.client_type, self.client_version, self.area1, self.area2, self.online_check, self.server_name, self.decoration_date,
                self.open_date, self.hotel_policy
            ]
        }
        df = pd.DataFrame(data)
        return df.to_string(index=False)