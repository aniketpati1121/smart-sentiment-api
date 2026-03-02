# Smart Sentiment API

A production-ready, containerized Machine Learning REST API built using **FastAPI** and **Scikit-learn** for real-time sentiment analysis.

---

# Project Overview

Smart Sentiment API is a simple ML-powered web service that:

- Accepts user text input
- Analyzes sentiment using a trained ML model
- Returns prediction as **Positive** or **Negative**

This project demonstrates:

- Machine Learning inference
- REST API development
- Clean Python project structure
- Docker containerization
- Production-style deployment

---

# Architecture

User → FastAPI → ML Model → Prediction → JSON Response

---

#  Tech Stack

- Python 3.12
- FastAPI
- Uvicorn
- Scikit-learn
- NumPy
- Docker

---

# Complete Project Structure

```
smart-sentiment-api/
│
├── app/
│   ├── main.py          
│   ├── model.py       
│   └── __init__.py     
│
├── requirements.txt     
├── Dockerfile           
├── README.md            
└── venv/               
```

---

# Local Development Setup

## Clone Repository

```
git clone <your-repository-url>
cd smart-sentiment-api
```

---

##  Create Virtual Environment

### Mac/Linux

```
python -m venv venv
source venv/bin/activate
```

### Windows

```
python -m venv venv
venv\Scripts\activate
```

If activated successfully, you will see:

```
(venv)
```

---

## Install Dependencies

```
pip install -r requirements.txt
```

To upgrade pip (if needed):

```
python -m pip install --upgrade pip
```

---

##  Run Application (Local)

```
uvicorn app.main:app --reload
```

Open in browser:

```
http://127.0.0.1:8000/docs
```

Swagger UI will appear.

---

# API Endpoints

##  Health Check

### GET /

Response:

```json
{
  "message": "Smart Sentiment API is running"
}
```

---

## Sentiment Prediction

### GET /predict?text=your_text

Example:

```
/predict?text=I love this product
```

Response:

```json
{
  "prediction": "positive"
}
```

---

# 🐳 Docker Setup

## Build Docker Image

```
docker build -t smart-sentiment-api .
```

---

## Run Docker Container

```
docker run -d -p 8000:8000 smart-sentiment-api
```

Explanation:
- `-d` → Run in background
- `-p 8000:8000` → Port mapping

---

## Check Running Containers

```
docker ps
```

You should see:

```
0.0.0.0:8000->8000/tcp
```

---

##  Access API from Docker

```
http://localhost:8000/docs
```

---

## Stop Container

```
docker stop <container_id>
```

---

# 📦 requirements.txt

```
fastapi
uvicorn
scikit-learn
numpy
```


# 👨‍💻 Author

Aniket Patil

