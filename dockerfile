# Use Python 3.9 slim image as base
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy requirements file
COPY app/requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy all files from the current directory to the working directory    
COPY app/ .

# Expose port 5000
EXPOSE 5000

# Set environment variables for AWS
ENV AWS_DEFAULT_REGION=us-east-1
ENV FLASK_ENV=production

# Command to run the application
CMD ["python", "app.py"]