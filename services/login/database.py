from pymongo import MongoClient
from .models import LoginRequest

client = MongoClient("mongodb://localhost:27017/")
db = client["social_media_platform"]
users_collection = db["users"]

def get_user_by_email(email: str):
    return users_collection.find_one({"email": email})
