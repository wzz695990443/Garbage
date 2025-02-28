from sqlalchemy import Column, String, BigInteger, Index
from sqlalchemy.ext.declarative import declarative_base
import pandas as pd

Base = declarative_base()

class UpMapAccnt(Base):
    __tablename__ = 'up_map_accnt'

    hotel_group_id = Column(BigInteger, nullable=False)
    hotel_id = Column(BigInteger, nullable=False)
    id = Column(BigInteger, primary_key=True, autoincrement=True)
    accnt_type = Column(String(16), nullable=False, comment='比如:登记单=master')
    accnt_class = Column(String(8), default='', nullable=False, comment='比如档案的 F G C A S')
    accnt_old = Column(String(16), nullable=False)
    accnt_new = Column(BigInteger, default=-1, nullable=False)

    __table_args__ = (
        Index('Index_1', 'hotel_group_id', 'hotel_id', 'accnt_type', 'accnt_old', unique=True),
        Index('Index_2', 'hotel_group_id', 'hotel_id', 'accnt_type', 'accnt_new'),
    )
    
    def __repr__(self):
        data = {
            "Field": ["hotel_group_id", "hotel_id", "id", "accnt_type", "accnt_class", "accnt_old", "accnt_new"],
            "Value": [self.hotel_group_id, self.hotel_id, self.id, self.accnt_type, self.accnt_class, self.accnt_old, self.accnt_new]
        }
        df = pd.DataFrame(data)
        return df.to_string(index=False)