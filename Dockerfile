# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir jinja2

# Make port 3000 available to the world outside this container
EXPOSE 3000

# Create a volume for persistent data storage
VOLUME /app/storage

# Run main.py when the container launches
CMD ["python", "main.py"]