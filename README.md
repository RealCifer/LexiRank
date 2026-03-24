```md
# LexiRank – Paragraph Intelligence Engine

A scalable Django-based backend system that processes user-submitted paragraphs, computes word frequencies, and retrieves the most relevant paragraphs using efficient ranking.

---

## Features

- JWT Authentication (Register & Login)
- Multi-paragraph input processing
- Word-based paragraph ranking (Top 10 results)
- Asynchronous processing using Celery
- Redis as message broker
- Dockerized setup (ready)

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
│
├── apps/
│   ├── users/
│   ├── paragraphs/
│
├── config/
│   ├── settings.py
│   ├── celery.py
│
├── docker/
├── scripts/
├── manage.py

```

---

## Setup Instructions

### 1️Clone Repository

```

git clone https://github.com/RealCifer/LexiRank.git
cd LexiRank

```

---

### 2️Create Virtual Environment

```

python -m venv venv
venv\Scripts\activate

```

---

### 3️Install Dependencies

```

pip install -r requirements.txt

```

---

### 4️Run Migrations

```

python manage.py makemigrations
python manage.py migrate

```

---

### 5️Run Server

```

python manage.py runserver

```

---

### 6️Start Redis

```

docker run -d -p 6379:6379 redis

```

---

### 7️Start Celery Worker (Windows)

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

**Headers**
```

Authorization: Bearer <access_token>

````

**Body**
```json
{
  "text": "Hello world\n\nHello again world"
}
````

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

* Implemented custom user model
* Optimized word frequency tracking
* Used asynchronous task queue for scalability
* Designed clean and modular backend architecture

---

## Author

Aditya Khamait

```
```
