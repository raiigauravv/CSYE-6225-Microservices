
from fastapi import FastAPI, HTTPException
from .models import User
from uuid import uuid4
from .database import get_user_by_email, create_user

# Initialize FastAPI app
app = FastAPI()

# Route for the root path
@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

# Route for user registration
@app.post("/register")
async def register_user(user: User):
    # Check if user already exists
    existing_user = get_user_by_email(user.email)
    if existing_user:
        raise HTTPException(status_code=400, detail="User already exists")
    
    user_data = user.dict()  # Convert Pydantic model to dictionary
    user_data["userid"] = str(uuid4())  # Add a unique user_id field
    # Create new user
    create_user(user)
    return {"message": "User registered successfully"}
