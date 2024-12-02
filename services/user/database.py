from pymongo import MongoClient
from .models import User
import uuid  # For generating unique user IDs

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["social_media_platform"]  # Updated database name
users_collection = db["users"]  # Collection name

# Function to check if a user exists by email
def get_user_by_email(email: str):
    return users_collection.find_one({"email": email})

# Function to create a new user
def create_user(user: User):
    user_data = user.dict()
    user_data["userid"] = str(uuid.uuid4())  # Generate a unique userid
    users_collection.insert_one(user_data)


