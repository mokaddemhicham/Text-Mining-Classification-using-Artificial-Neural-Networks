# Data Mining Techniques for Text-Mining Classification with Artificial Neural Networks

This project provides a web application that utilizes an Artificial Neural Network (ANN) for sentiment classification of movie reviews. The application is built with Flask and containerized using Docker.

## Features

- Sentiment classification using an ANN model
- Web interface for submitting movie reviews
- REST API for programmatically accessing the classification service

## Prerequisites

- Docker installed on your system

## Getting Started

### Setup and Installation 

- #### Method 1 - Build the Docker Image from the Dockerfile

  1. **Clone the repository:**
     ```bash
     git clone https://github.com/mokaddemhicham/Text-Mining-Classification-using-Artificial-Neural-Networks.git
     cd Text-Mining-Classification-using-Artificial-Neural-Networks
     ```

  2. **Build the Docker image:**

     ```bash
     docker build -t ann-web-app 
      ```
  3. **Run the Docker container:**

     ```bash
     docker run -p 5000:1000 ann-web-app
     ```
- #### Method 2 - Pull the Docker Image from Docker Hub
    
  1. **Pull the Docker image:**
    
        ```bash
        docker pull mokaddemhicham/flask-ann-app:latest
        ```
    
  2. **Run the Docker container:**
        ```
     docker run -d -p 5000:1000 --name flask-ann-app-container mokaddemhicham/flask-ann-app:latest

## Usage

1. Access the web application:

    Open your web browser and navigate to `http://localhost:5000`.

2. Submit a movie review:

   Enter your movie review in the text box.
      Click the `Predict` button to see the sentiment classification result.

## API Endpoints

The application provides a REST API for sentiment classification as well.

- ### POST /predict

    - Request (JSON):
        ```
        { "review": "This is a sample movie review." }

    - Response (JSON):
        ```
        { "sentiment": "positive" }

## Project Structure

    Text-Mining-Classification-using-Artificial-Neural-Networks/
    ├── mo.tf/  # The ANN model
    ├── static/
    |       ├── autotyping/ # JavaScript files for auto-typing effect
    │       ├── bootstrap/ # Bootstrap CSS and JS files
    ├── templates/
    │       ├── index.html  # The web interface template
    ├── app.py  # The Flask application
    ├── Dockerfile # Docker image configuration
    ├── requirements.txt  # Required Python packages
    └── README.md

## Dockerfile

This file defines how the Docker image is built.

## Requirements

The `requirements.txt` file lists the necessary Python libraries:
```
Flask==2.3.2
numpy==1.26.2
tensorflow==2.15.0
tensorflow-datasets==4.9.4
waitress
```

## Contributing
We welcome contributions! Feel free to open an issue or submit a pull request.

## Contact

For any inquiries or support, please contact [Hicham Mokaddem](https://www.linkedin.com/in/mokaddemhicham) or [Mohamed Louak](https://www.linkedin.com/in/louakmohamed).