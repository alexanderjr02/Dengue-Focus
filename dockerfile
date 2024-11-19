# Use Python 3.9 slim image as base
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy requirements file
COPY app/requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt 

# Install Gunicorn and Eventlet for Socket.IO support
RUN pip install gunicorn eventlet

# Copy all files from the current directory to the working directory    
COPY app/ .

# Expose port 5000
EXPOSE 5000

# Command to run the application with Gunicorn
CMD ["gunicorn", "-w", "4", "-k", "eventlet", "-b", "0.0.0.0:5000", "app:app"]