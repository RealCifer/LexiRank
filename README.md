# LexiRank – Paragraph Intelligence Engine

A scalable Django-based backend system that processes user-submitted paragraphs, computes word frequencies, and retrieves the most relevant paragraphs using efficient ranking.

---

## Features

- JWT Authentication (Register & Login)
- Multi-paragraph input processing
- Word-based paragraph ranking (Top 10 results)
- Asynchronous processing using Celery
- Redis as message broker
- Dockerized setup

---

## Tech Stack

- Django + Django REST Framework
- PostgreSQL / SQLite
- Celery (Task Queue)
- Redis (Message Broker)
- Docker & Docker Compose

---

## Project Structure

```
LexiRank/
├── apps/
│   ├── users/
│   │   ├── models.py
│   │   ├── views.py
│   │   ├── serializers.py
│   │   ├── urls.py
│   │   └── apps.py
│   │
│   ├── paragraphs/
│   │   ├── models.py
│   │   ├── views.py
│   │   ├── tasks.py
│   │   ├── serializers.py
│   │   ├── urls.py
│   │   └── apps.py
│
├── config/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── celery.py
│   └── wsgi.py
│
├── docker/
├── scripts/
├── manage.py
├── requirements.txt
└── README.md
```

---

## Setup Instructions

### 1. Clone Repository

```
git clone https://github.com/RealCifer/LexiRank.git
cd LexiRank
```

### 2. Create Virtual Environment

```
python -m venv venv
venv\Scripts\activate
```

### 3. Install Dependencies

```
pip install -r requirements.txt
```

### 4. Run Migrations

```
python manage.py makemigrations
python manage.py migrate
```

### 5. Run Server

```
python manage.py runserver
```

### 6. Start Redis

```
docker run -d -p 6379:6379 redis
```

### 7. Start Celery Worker (Windows)

```
celery -A config worker -l info --pool=solo
```

---

## Authentication APIs

### Register

```
POST /api/users/register/
```

### Login

```
POST /api/users/login/
```

---

## Paragraph APIs

### Upload Paragraphs

```
POST /api/paragraphs/upload/
```

Headers:
```
Authorization: Bearer <access_token>
```

Body:
```json
{
  "text": "Hello world\n\nHello again world"
}
```

---

### Search Word

```
GET /api/paragraphs/search/?word=hello
```

---

## Architecture

```
Client → Django API → Celery → Redis → Worker → Database
```

---

## Key Highlights

- Custom user model implementation
- Efficient word frequency tracking
- Asynchronous processing using Celery
- Modular and scalable backend design

---

## Author

Aditya Khamait