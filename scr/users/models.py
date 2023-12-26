from pydantic import BaseModel
from typing import Optional

class UserClass(BaseModel):
    id_user:int
    login:Optional[str]

class UserPost(BaseModel):
    id_user:int
    login:Optional[str]
    password:Optional[int]
    phone_number: int
    email_address: str
    verified: int
    
class UserPut(BaseModel):
    id_user: int
    phone_number: int