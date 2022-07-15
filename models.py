from sqlalchemy import Column, MetaData, Integer
from sqlalchemy.sql.sqltypes import NullType
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = MetaData()

class UserTBL(Base):
    __tablename__ = 'user_tbl'
    iduser_id = Column(Integer, primary_key=True, index=True)
    first_name = Column('first_name', NullType)
    last_name = Column('last_name', NullType)
    dob = Column('dob', NullType)