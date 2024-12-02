# Use a base Python image
FROM python:3.9

# Set the working directory inside the container
WORKDIR /app

# Copy all the files from the current directory into the container's working directory
COPY . /app

# Install the necessary Python dependencies
RUN pip install fastapi uvicorn pymongo pydantic email-validator 

# Command to run the FastAPI app with Uvicorn when the container starts
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
