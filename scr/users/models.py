from pydantic import BaseModel
from typing import Optional

class UserClass(BaseModel):
    id_user:int
    login:Optional[int]

class UserPost(BaseModel):
    id_user:int
    login:Optional[int]
    password:Optional[int]
    phone_number: int
    email_address: str
    verified: int