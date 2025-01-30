# Use an official Python image as the base
FROM python:3.10-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the application code and requirements file into the container
COPY ./app /app

# Navigate to the correct directory where requirements.txt is located
WORKDIR /app

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Set PYTHONPATH so Python knows where to look for modules
ENV PYTHONPATH=/app

# Run the application
CMD ["python", "api.py"]

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    libpq-dev \
    && apt-get clean
