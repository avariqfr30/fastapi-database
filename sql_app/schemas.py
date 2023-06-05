from typing import Union

from pydantic import BaseModel


class teacherInfoBase(BaseModel):
    name: str
    role: Union[str, None] = None
    phone : Union[int, None] = None
    email : Union[str, None] = None



class teacherInfoCreate(teacherInfoBase):
    pass


class teacherInfo(teacherInfoBase):
    reg_id: int
    owner_id: int

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    is_active: bool
    teacherInfos: list[teacherInfo] = []

    class Config:
        orm_mode = True