
# Random Password Generator

This is a simple Flask web application that serves a static webpage with an SVG image. The app can be run either directly using Python or by building a Docker image.

---

## Prerequisites

- Python 3.8.10
- Docker (optional, if running via Docker)

---

## Installation

### **Running with Python Flask**

1. Clone the repository (if not already done):
   ```bash
   pip install -r requirements.txt
   python3 app.py
   ```

### **Running with Docker**

1. Build the Docker image:
   ```bash
   docker build -t flask-app .
   ```
1. Run the Docker container:
   ```bash
   docker run -p 8000:8000 flask-app
   ```

### **Access the app**:
   Open your browser and navigate to http://127.0.0.1:8000/


## Demo

BLOB

## Authors

- [@sagarpandav](https://www.github.com/sagarpandav)