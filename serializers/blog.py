def decodeblog(data)->dict:
    return {
        "_id":str(data["_id"]),
        "title":data["title"],
        "sub_title":data["sub_title"],
        "content":data["content"],
        "title":data["author"],
        "date":data["date"]
    }

def decodeblogs(docs)->list:
    return [decodeblog(doc) for doc in docs]