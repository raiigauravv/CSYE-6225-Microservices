# database.py
import random
from pymongo import MongoClient
from bson import ObjectId
from .models import Post, Engagement
import datetime
from fastapi import HTTPException


# MongoDB client setup
client = MongoClient('mongodb://localhost:27017/')
db = client['social_media_platform']
posts_collection = db['posts']
comments_collection = db["comments"]

def get_all_posts():
    # Fetch all posts from the collection
    posts = list(posts_collection.find())
    # Optionally, you can convert them to Post model objects if needed
    # for example:
    # posts = [Post(**post) for post in posts]
    return posts

# Function to get a random postId from the posts collection
def get_random_post_id():
    # Get all posts
    posts = list(posts_collection.find())
    if not posts:
        return None  # Return None if there are no posts
    # Pick a random post
    random_post = random.choice(posts)
    return random_post.get("postId")  # Return the postId of the randomly selected post

# Function to like a post by postId
def like_post(post_id: str, user_id:str):
    post = posts_collection.find_one({"postId": post_id})
    
    if not post:
        raise HTTPException(status_code=404, detail=f"Post with postId {post_id} not found.")

    # Check if user has already liked the post
    if user_id in post.get('liked_users', []):
        # User has already liked the post, so remove like and decrement counter
        posts_collection.update_one(
            {"postId": post_id},
            {
                "$pull": {"liked_users": user_id},  # Remove the user from liked_users
                "$inc": {"likeCounter": -1}  # Decrement the like counter
            }
        )
        print(f"Like removed: User {user_id} has removed their like from post {post_id}.")
        return False  # Return False to indicate a like was removed
    else:
        # User has not liked the post, so add like and increment counter
        posts_collection.update_one(
            {"postId": post_id},
            {
                "$push": {"liked_users": user_id},  # Add the user to liked_users
                "$inc": {"likeCounter": 1}  # Increment the like counter
            }
        )
        return True  # Return True to indicate a like was added

def add_comment_to_post(postId: str, comment: str, userid: str):
    # Fetch the post from the database (post is a dictionary, not a Post model)
    post = posts_collection.find_one({"postId": postId})
    
    if post:
        # Increment the comment counter for this post (no need to manipulate the content)
        posts_collection.update_one(
            {"postId": postId},
            {"$inc": {"commentCounter": 1}}  # Increment commentCounter by 1
        )
          # Debugging statement
        # Optionally, store the comment in a separate collection (comments are stored separately)
        comments_collection.insert_one({
            "postId": postId,
            "userId": userid,
            "comment": comment,
            "timestamp": datetime.datetime.now()  # Store the current timestamp
        })
        
        return True
    return False
