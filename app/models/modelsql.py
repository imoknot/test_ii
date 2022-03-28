from sqlalchemy import Column, Integer, String, Date, Boolean, DateTime, BigInteger, MetaData
from sqlalchemy.sql import func
from sqlalchemy.schema import ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects.postgresql import JSONB, ARRAY

metadata: MetaData = MetaData()
Base = declarative_base(metadata=metadata)


class User(Base):
    __tablename__ = "user"
    user_id = Column(BigInteger, primary_key=True, index=True, autoincrement=True)
    username = Column(String, default='')
    first_name = Column(String, default='')
    last_name = Column(String, default='')
    sex = Column(Integer[1], default=0)
    email = Column(String, index=True, default='')
    password = Column(String, default='')
    birthday = Column(Date)
    balans = Column(Integer, default=0)
    image = Column(String, default='')
    phone = Column(BigInteger, default=0)
    rang = Column(Integer, default=0)
    date_created = Column(DateTime(timezone=False), server_default=func.now())
    date_updated = Column(DateTime(timezone=False), server_default=func.now(), onupdate=func.now())