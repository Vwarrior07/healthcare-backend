# Healthcare Backend (Django + DRF)

This project is a backend system for managing patients, doctors, and their relationships using Django REST Framework and PostgreSQL.

---

## Features
- JWT Authentication (Register & Login)
- Patient Management (User-owned)
- Doctor Management
- Patient–Doctor Mapping
- Secure APIs with permissions
- Swagger API Documentation

---

## Tech Stack
- Python
- Django
- Django REST Framework
- PostgreSQL
- JWT (SimpleJWT)

---

## Setup Instructions

1. Clone the repository
```bash
git clone <repo-url>
cd healthcare-backend
```
2. Create and activate virtual environment
```bash
python -m venv venv
venv\Scripts\activate
```
3. Install dependencies
```bash
pip install -r requirements.txt
```
4. Create .env file
```bash
SECRET_KEY=your-secret-key
DEBUG=True
DB_NAME=healthcare_db
DB_USER=postgres
DB_PASSWORD=yourpassword
DB_HOST=localhost
DB_PORT=5432
```
5. Run migrations
```bash
python manage.py migrate
```
6. Start server
```bash
python manage.py runserver
```

---

## API Documentation
### Swagger UI available at:
```bash
/api/docs/
```

---

## Authentication
### Use JWT token in headers:
```bash
Authorization: Bearer <access_token>
```