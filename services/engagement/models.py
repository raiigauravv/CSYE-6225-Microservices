from pydantic import BaseModel
from typing import Optional
from datetime import datetime
import uuid

# Post Model
class Post(BaseModel):
    postId: Optional[str] = None  # Optional, will be auto-generated if not provided
    content: str
    timestamp: Optional[str] = None  # Optional, will be auto-generated if not provided
    likeCounter: int = 0  # Default value set to 0
    commentCounter: int = 0  # Default value set to 0

    # Root validator to automatically generate postId and timestamp
   

# Engagement Model (for liking posts)
class Engagement(BaseModel):
    postId: str  # Post ID to be liked
    userId: str  # User who is liking the post

class CommentRequest(BaseModel):
    userId: str  # User who is commenting on the post
    content: str  # Content of the comment
