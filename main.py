from fastapi import FastAPI
from routes.entry import user
from routes.blog import blog_root

app=FastAPI()

app.include_router(user)
app.include_router(blog_root)
