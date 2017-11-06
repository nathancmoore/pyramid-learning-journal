from sqlalchemy import (
    Column,
    DateTime,
    Integer,
    Unicode,
)

from .meta import Base


class MyModel(Base):
    __tablename__ = 'entries'
    id = Column(Integer, primary_key=True)
    title = Column(Unicode)
    date = Column(DateTime)
    body = Column(Unicode)
