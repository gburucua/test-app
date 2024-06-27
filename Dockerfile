# Use the official Python image from the Docker Hub
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
#RUN pip install --no-cache-dir --verbose -r requirements.txt
RUN pip install --no-cache-dir --upgrade pip setuptools
RUN pip install --no-cache-dir -r requirements.txt


# Install MySQL client
RUN apt-get update && apt-get install -y default-mysql-client

# Expose the Flask port
EXPOSE 5000

# Run the application
CMD ["python", "app.py"]
