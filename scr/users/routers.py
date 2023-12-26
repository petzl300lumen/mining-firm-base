from fastapi import APIRouter, Path
from users.models import UserClass, UserPut, UserPost #import models for routers arg
from users import resolvers
from users.resolvers import post_users, get_users, put_user #import resolvers for returning defs

router = APIRouter()

#post
@router.post('/') #/users/
def post_users_r(user: UserPost):
    return resolvers.post_users(user_in=user)

#get
@router.get('/') #/users/
def get_users_r(user: UserClass):
    return resolvers.get_users(user_in=user)


@router.get('/{user_id}/') 
def get_user_id(user_id:int):
    return {
        "user":{
            "id": user_id,
        },
    }
#put
@router.put('/{user_id}/')
def put_user_id(user: UserPut):
    return resolvers.get_users(user_in=user)

#delete
@router.delete('/{user_id}/')
def delete_user_r(user: int):
    return resolvers.delete_user()