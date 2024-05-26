# Use the official lightweight Python image
# https://hub.docker.com/_/python
FROM python:3.11-alpine
# Set the working directory in the container
WORKDIR /app
# Copy the requirements file into the container at /app
COPY requirements.txt /app/
# Install the dependencies specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
# Copy the rest of the application code into the container at /app
COPY . /app/
# Expose the port the app runs on
EXPOSE 5000
# Run the application when the container starts
CMD ["python", "app.py"]