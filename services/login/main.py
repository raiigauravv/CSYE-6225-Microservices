from fastapi import FastAPI, HTTPException
from .models import LoginRequest
from .database import get_user_by_email

app = FastAPI()

# Global variable to store the user_id after login
logged_in_user_id = None

@app.post("/login")
async def login(user: LoginRequest):
    # Fetch the user from the database using the provided email
    existing_user = get_user_by_email(user.email)
    
    if not existing_user:
        raise HTTPException(status_code=404, detail="User not found")
    
    # Check if the password matches (NOTE: in a production system, use hashed passwords)
    if existing_user["password"] != user.password:
        raise HTTPException(status_code=400, detail="Incorrect password")
    
    # Store the user_id in the global variable
    global logged_in_user_id
    logged_in_user_id = existing_user["userid"]
    print(f"User {user.email} logged in with user_id {existing_user['userid']}.")

    # Return a success message with the user_id for post creation
    return {"message": "Login successful", "user_id": existing_user["userid"]}
