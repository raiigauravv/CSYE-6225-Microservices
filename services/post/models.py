# post/models.py
from pydantic import BaseModel
from datetime import datetime
import uuid
from typing import List, Optional

# Post model
class Post(BaseModel):
    userid: str
    content: str
    postId: str = uuid.uuid4().hex  # Generate a unique post ID dynamically
    timestamp: str = datetime.now().isoformat()  # Dynamically generate timestamp
    likeCounter: int = 0  # Default value set to 0
    commentCounter: int = 0  # Default value set to 0
    liked_users: List[str] = [] 


   


    