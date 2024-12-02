# main.py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from .models import Post, Engagement, CommentRequest
from .database import get_random_post_id, like_post, get_all_posts, add_comment_to_post

app = FastAPI()

# Define the Engagement model to receive the userId
class EngagementRequest(BaseModel):
    userId: str  # Only userId is required for liking a post

# Endpoint to get all posts
@app.get("/post_feed")
async def get_post_feed():
    posts = get_all_posts()  # Fetch all posts
    # Extract only the 'content' field from each post
    posts_content = [{"content": post["content"]} for post in posts]
    return {"posts": posts_content}

# Endpoint to like a random post
@app.post("/like_post")
async def like_a_post(engagement: EngagementRequest):
    # Fetch a random postId from the posts collection
    #random_post_id = get_random_post_id()
    random_post_id="e0b5c2fc-9748-4cf8-b45a-664fa7cd8f54"
    if not random_post_id:
        raise HTTPException(status_code=404, detail="No posts available to like.")
    
    # Like the post (increment the like counter)
    success = like_post(random_post_id, engagement.userId)  # Correctly use engagement.userId
    if not success:
        return {"message": f"Like removed from post {random_post_id}."}
    
    return {"message": f"Post {random_post_id} liked successfully!"}

@app.post("/comment_post")
async def comment_on_post(comment_request: CommentRequest):
    # Fetch a random postId from the posts collection
    random_post_id = get_random_post_id()
    if not random_post_id:
        raise HTTPException(status_code=404, detail="No posts available to comment on.")
    
    # Add the comment to the post (this will increment the comment counter and store the comment)
    success = add_comment_to_post(random_post_id, comment_request.comment, comment_request.userId)
    if not success:
        raise HTTPException(status_code=404, detail="Post not found or unable to add comment.")
    
    return {"message": f"Post {random_post_id} commented successfully!"}

