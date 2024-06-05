from fastapi import APIRouter
from models.blog import BlogModel,UpdateBlogModel
from config.config import client
from serializers import blog
import datetime
from bson import ObjectId


blog_root=APIRouter()

@blog_root.post('/new/blog')
def new_blog(data:BlogModel):
    data=dict(data)
    current_date=datetime.date.today()
    data["date"]=str(current_date)

    res=client.local.one.insert_one(data)
    data_id=str(res.inserted_id)
    return {
        "status":"ok",
        "_id":data_id
    }

@blog_root.get('/all/blog')
def findall():
    data=blog.decodeblogs(client.local.one.find())
    return data

@blog_root.get('/one/{id}')
def getone(_id:str):
    data=client.local.one.find_one({"_id":ObjectId(_id)})
    decodeddata=blog.decodeblog(data)
    return decodeddata

@blog_root.patch('/update/{id}')
def updateblog(id:str,data:UpdateBlogModel):
    req=data.model_dump(exclude_unset=True)
    client.local.one.find_one_and_update({"_id":ObjectId(id)},{"$set":req})
    return {
        "Message":"Succesful"
    }