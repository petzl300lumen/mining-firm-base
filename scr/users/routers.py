from fastapi import APIRouter, Path
from users.models import UserClass
from users.models import UserPost
from users import resolvers
from users.resolvers import post_users

router = APIRouter() #router prefix

@router.post('/') #/users/
def post_users_r(user: UserPost):
    # return resolvers.post_users(user_in=user)
    return {"message": "success"}

@router.get('/') #/users/
def get_users_r(user: UserClass):
    return resolvers.get_users(user_in=user)

@router.get('/{user_id}/') #/users/
def get_user_id(user_id:int):
    return {
        "user":{
            "id": user_id,
        },
    }
