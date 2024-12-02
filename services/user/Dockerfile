FROM python:3.9

# Set the working directory
WORKDIR /app

# Copy the source code into the container
COPY . /app

# Install Python dependencies
RUN pip install fastapi uvicorn pymongo pydantic email-validator

# Expose the application port
EXPOSE 8002

# Run the application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8002"]
