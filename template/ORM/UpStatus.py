from sqlalchemy import Column, String, BigInteger, DateTime, Integer, Index
from sqlalchemy.ext.declarative import declarative_base
import pandas as pd

Base = declarative_base()

class UpStatus(Base):
    __tablename__ = 'up_status'

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    hotel_id = Column(BigInteger, nullable=False)
    up_step = Column(String(32), nullable=False)
    time_begin = Column(DateTime, nullable=True)
    time_end = Column(DateTime, nullable=True)
    time_long = Column(Integer, default=0, nullable=False)
    remark = Column(String(64), nullable=True)

    __table_args__ = (
        Index('Index_1', 'hotel_id', 'up_step', unique=True),
    )
    
    def __repr__(self):
        data = {
            "Field": ["id", "hotel_id", "up_step", "time_begin", "time_end", "time_long", "remark"],
            "Value": [self.id, self.hotel_id, self.up_step, self.time_begin, self.time_end, self.time_long, self.remark]
        }
        df = pd.DataFrame(data)
        return df.to_string(index=False)