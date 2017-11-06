from sqlalchemy import (
    Column,
    DateTime,
    Integer,
    Unicode,
)

from .meta import Base
from datetime import datetime


class MyModel(Base):
    def __init__(self, *args, **kwargs):
        """Modify the init method to do more things."""
        super(MyModel, self).__init__(*args, **kwargs)
        self.creation_date = datetime.now()

    __tablename__ = 'entries'
    id = Column(Integer, primary_key=True)
    title = Column(Unicode)
    date = Column(DateTime)
    body = Column(Unicode)
