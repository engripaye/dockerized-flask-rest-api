# 🐳 Dockerized Flask REST API

A lightweight **Flask-based REST API** packaged and deployed inside a **Docker container**.
This project demonstrates **modern backend development practices**, including **environment reproducibility**, **dependency management**, and **containerized deployment**.

---

## 🚀 Features

* **Flask REST API** – Simple and clean endpoints for managing users or tasks.
* **Dockerized Environment** – Fully containerized using Docker for consistent setup across machines.
* **Dependency Isolation** – Uses `requirements.txt` and Docker layers for clean dependency management.
* **Scalable Design** – Easily extendable for production use with Docker Compose or Kubernetes.

---

## 📁 Project Structure

```
dockerized-flask-api/
│
├── app/
│   ├── __init__.py
│   ├── routes.py          # API endpoints
│   └── models.py          # Simple data structure / logic
│
├── requirements.txt       # Python dependencies
├── Dockerfile             # Docker build configuration
├── .dockerignore          # Files ignored during Docker build
├── README.md              # Project documentation
└── run.py                 # Entry point for the Flask app
```

---

## ⚙️ Setup & Usage

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/dockerized-flask-api.git
cd dockerized-flask-api
```

### 2. Build the Docker image

```bash
docker build -t flask-api .
```

### 3. Run the container

```bash
docker run -d -p 5000:5000 flask-api
```

### 4. Test the API

Visit: [http://localhost:5000](http://localhost:5000)

Example endpoint:

```bash
curl http://localhost:5000/api/todos
```

---

## 🧩 Example Endpoint

**GET /api/todos**
Returns all todos in JSON format.

**POST /api/todos**
Creates a new todo item.

Example JSON payload:

```json
{
  "task": "Learn Docker",
  "completed": false
}
```

---

## 🧠 Key Learnings

* How to **containerize Python/Flask apps** using Docker.
* Managing **dependencies and environments** for reproducibility.
* Building **RESTful APIs** with Flask.
* Preparing apps for **scalable deployment pipelines**.

---

## 🧰 Tech Stack

| Tool             | Purpose            |
| ---------------- | ------------------ |
| **Python 3.10+** | Backend logic      |
| **Flask**        | REST API framework |
| **Docker**       | Containerization   |
| **JSON**         | API data format    |

---

## 📸 Architecture Diagram

```
+---------------------+
|     Client App      |
| (Postman / Browser) |
+----------+----------+
           |
           v
+---------------------+
|     Flask API       |
|   (Python / Flask)  |
+----------+----------+
           |
           v
+---------------------+
|     Docker Engine   |
| (Isolated Container)|
+---------------------+
```

---

## 🧪 Example Dockerfile

```dockerfile
# Use official lightweight Python image
FROM python:3.10-slim

# Set work directory
WORKDIR /app

# Copy dependencies
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Expose the app port
EXPOSE 5000

# Run the application
CMD ["python", "run.py"]
```

---

## 👨‍💻 Author

**Olabowale Babatunde Ipaye**
💼 Backend Developer | Cloud & DevOps Enthusiast
🌐 [LinkedIn](https://linkedin.com/in/engripayebabatunde) • [GitHub](https://github.com/engripaye)

---

## 🏁 Future Improvements

* Add database integration (SQLite or PostgreSQL).
* Implement user authentication.
* Deploy using Docker Compose or Kubernetes.

---

Would you like me to also **generate the code files** (`app/routes.py`, `run.py`, and `Dockerfile`) so you can instantly run and push this to GitHub?
I can make it **simple, clean, and production-ready**.
