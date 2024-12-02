from pymongo import MongoClient
import uuid

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["social_media_platform"]
posts_collection = db["posts"]
users_collection = db["users"]

def create_post(post_data):
    # Check if user_id exists in the users collection
    user = users_collection.find_one({"userid": post_data["userid"]})
    
    if not user:
        raise ValueError("User not found")  # Handle error if user does not exist
    
    # Generate a unique post ID
    post_data["postId"] = str(uuid.uuid4())  # This is a string ID for the post
    
    # Insert the post into the database
    result = posts_collection.insert_one(post_data)  
    
    # Ensure the MongoDB ObjectId is converted to a string for JSON serialization
    post_data["postId"] = str(result.inserted_id)  # Convert Mongo ObjectId to string
    
    # Update the user's document with the new post ID and content
    users_collection.update_one(
        {"userid": post_data["userid"]},  # Find the user by user_id
        {"$push": {
            "posts": {
                "postId": post_data["postId"],
                "content": post_data["content"]
            }
        }}
    )
    
    return post_data
