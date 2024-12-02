# database.py
import random
from pymongo import MongoClient
from bson import ObjectId
from .models import Post, Engagement
import datetime


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
def like_post(post_id: str):
    result = posts_collection.update_one(
        {"postId": post_id},
        {"$inc": {"likeCounter": 1}}  # Increment the like counter
    )
    return result.modified_count > 0

def add_comment_to_post(postId: str, comment: str, userid: str):
    post = posts_collection.find_one({"postId": postId})
    if post:
        # Increment the comment counter
        posts_collection.update_one(
            {"postId": postId},
            {"$inc": {"commentCounter": 1}}
        )
        # Optionally, store the comment in a separate collection (optional)
        comments_collection.insert_one({
            "postId": postId,
            "userid": userid,
            "comment": comment,
            "timestamp": datetime.now()
        })
        return True
    return False
