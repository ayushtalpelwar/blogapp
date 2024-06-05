from fastapi import APIRouter

user=APIRouter()

@user.get('/')
def apirunning():
    res={
        "status":"ok",
        "message":"Api is running"
    }
    return res