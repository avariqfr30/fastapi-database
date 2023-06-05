from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)

    teacherInfos = relationship("teacherInfo", back_populates="owner")


class teacherInfo(Base):
    __tablename__ = "teacherInfos"

    reg_id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    role = Column(String, index=True)
    owner_id = Column(Integer, ForeignKey("users.id"))
    phone = Column(Integer, index=True)
    email = Column(String, index=True)
    is_active = Column(Boolean, default=True)
  

    owner = relationship("User", back_populates="teacherInfos")