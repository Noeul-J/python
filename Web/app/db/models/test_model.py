from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from app.db.session import Base


class Test(Base):
    __tablename__ = "process_name"

    process_id = Column(Integer, primary_key=True, index=True)
    process_name = Column(String)