from fastapi import FastAPI, HTTPException
from datetime import datetime
from .models import Post
from .database import create_post

app = FastAPI()

# Route to create a post with user_id passed in the request body
@app.post("/create_post")
async def create_post_route(post: Post):
    # Make sure the user_id is passed in the post body
    user_id = post.userid

    # Create post data
    post_data = {
        "userid": user_id,  # Use the user_id passed in the request
        "content": post.content,
        "timestamp": datetime.now(),
        "likeCounter": 0,
        "commentCounter": 0,
        "liked_users": []
    }

    try:
        # Call create_post function to save the post
        saved_post = create_post(post_data)
        return {"message": "Post created successfully", "postId": saved_post["postId"]}
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
