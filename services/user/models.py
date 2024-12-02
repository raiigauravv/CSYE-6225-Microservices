from pydantic import BaseModel, EmailStr
from typing import Optional

# Define the User model
class User(BaseModel):
   
    firstName: str
    lastName: str
    email: EmailStr
    password: str
   

