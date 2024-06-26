from sqlmodel import SQLModel, Field, Column, VARCHAR
from pydantic import EmailStr
from pydantic_extra_types.phone_numbers import PhoneNumber
from typing import Optional
import datetime

class UserCreate(SQLModel):
    name: str = Field(min_length=3, max_length=50, description="Name of the User", schema_extra={'example': "A very nice Item"}, title="Name")  # noqa
    email: EmailStr = Field(sa_column=Column("email", VARCHAR, unique=True, index=True), description="Email of the passenger",)
    phone: PhoneNumber = Field(description="Phone number of the passenger", title="Phone Number", schema_extra={})  # noqa
    password: str = Field(min_length=8, max_length=100, description="Password of the passenger",title="Password")  # noqa        

class User(UserCreate, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    is_active: bool = Field(default=False, description="Is the user active", title="Is Active")
    
class UserLogin(SQLModel):
    email: EmailStr = Field(description="Email of the passenger",)
    password: str = Field(min_length=8, max_length=100, description="Password of the passenger",title="Password")  # noqa

class Token(SQLModel):
    access_token: str
    token_type: str = "bearer"

class TokenData(SQLModel):
    sub: int | None = None

class UserOutput(SQLModel):
    id: int
    name: str
    email: EmailStr
    phone: PhoneNumber

class Message(SQLModel):
    message: str


class NewPassword(SQLModel):
    token: str
    new_password: str
