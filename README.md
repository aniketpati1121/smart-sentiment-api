# Smart Sentiment API

## Project Overview

Smart Sentiment API is a FastAPI-based microservice that provides sentiment analysis. This project demonstrates:

* Python FastAPI backend
* Docker containerization
* Kubernetes deployment
* Horizontal Pod Autoscaler (HPA)
* Port-forwarding for local access

---

## Project Structure

```
smart-sentiment-api/
│
├── app/
│   ├── main.py                  
│   └── main.py                   
│
├── Dockerfile          
├── requirements.txt             
├── k8s/
│   ├── deployment.yaml        
│   ├── service.yaml            
│   ├── hpa.yaml                 
│   └── ingress.yaml             
└── README.md
```

---

## Local Setup

1. **Clone the repository**:

```bash
git clone <repo-url>
cd smart-sentiment-api
```

2. **Setup Python virtual environment**:

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

3. **Run FastAPI locally**:

```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

* Test: `curl http://localhost:8000`
* Response: `{"message":"Smart Sentiment API is running"}`

---

## Docker Setup

1. **Build Docker Image**:

```bash
docker build -t smart-sentiment-api:latest .
```

2. **Tag Docker Image for Docker Hub**:

```bash
docker tag smart-sentiment-api:latest aniketpatil01/smart-sentiment-api:1.0
```

3. **Push Docker Image to Docker Hub**:

```bash
docker push aniketpatil01/smart-sentiment-api:1.0
```

4. **Check Docker Images**:

```bash
docker images
```

---

## Kubernetes Setup (Kind Cluster)

1. **Create Kind Cluster** (if not already):

```bash
kind create cluster --name sentiment-cluster
```

2. **Apply Kubernetes manifests**:

```bash
kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml
kubectl apply -f k8s/hpa.yaml
# Optional
kubectl apply -f k8s/ingress.yaml
```

3. **Verify resources**:

```bash
kubectl get pods
kubectl get svc
kubectl get hpa
kubectl get ingress
```

---

## Access API via Port-forwarding

```bash
kubectl port-forward service/sentiment-service 8000:80
```

* API accessible at: `http://localhost:8000`

## Deploy Using Helm Chart 

---

## Notes

* Ingress is optional for local dev; port-forwarding is sufficient.
* Make sure Docker image is pushed to Docker Hub if using `imagePullPolicy: Always`.
* Resource limits, liveness/readiness probes are configured in `deployment.yaml`.

---

## References

* [FastAPI Docs](https://fastapi.tiangolo.com/)
* [Kubernetes Docs](https://kubernetes.io/docs/home/)
* [Docker Hub](https://hub.docker.com/)

