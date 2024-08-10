# Use an official Python runtime as a parent image
FROM python:3.9

# Set the working directory in the container
WORKDIR /WEAVR.IO

# Copy the current directory contents into the container at /app
COPY . /WEAVR.IO/

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Run the application
CMD ["python", "transformation.py"]
