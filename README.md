# User Service

A FastAPI microservice for managing users and user registration in the University Poll System.

## Overview

The User Service is responsible for:
- Managing user accounts and registration
- Storing user profile information
- Tracking user registration status
- Coordinating with the Poll Service for cascade deletion

## Features

- **Full CRUD for Users**: Create, read, update, and delete user accounts
- **User Registration**: Mark users as registered (required to answer polls)
- **Profile Management**: Update user information
- **Cascade Deletion**: Automatically delete user's poll answers when user is deleted
- **Inter-Service Communication**: Notifies Poll Service of deletions

## Technology Stack

- **Framework**: FastAPI 0.115.0
- **Database**: MySQL 8.0
- **Async Driver**: aiomysql 0.2.0
- **HTTP Client**: httpx 0.27.0
- **Validation**: Pydantic 2.9.2

## Project Structure

```
user_service/
├── main.py                          # FastAPI app entry point
├── requirements.txt                 # Dependencies
├── .env.example                     # Configuration template
├── init.sql                         # Database schema
└── app/
    ├── config.py                    # Configuration settings
    ├── model/
    │   └── user.py                  # Pydantic models
    ├── controller/
    │   └── user_controller.py       # REST endpoints
    ├── service/
    │   └── user_service.py          # Business logic
    └── repository/
        ├── database.py              # Database connection
        └── user_repository.py       # SQL queries
```

## Setup

### Prerequisites
- Docker and Docker Compose
- Python 3.11+ (for local development)

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd poll_system
   ```

2. **Set up environment variables**
   ```bash
   cp user_service/.env.example .env
   ```

3. **Start MySQL with Docker Compose**
   ```bash
   docker compose up -d
   python init_db.py
   ```

4. **Install dependencies**
   ```bash
   cd user_service
   pip install -r requirements.txt
   ```

5. **Run the service**
   ```bash
   uvicorn main:app --reload --port 8001
   ```

The service will be available at `http://localhost:8001`

## API Endpoints

### User Management

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/users/` | Create a new user |
| GET | `/users/` | Get all users |
| GET | `/users/{user_id}` | Get a specific user |
| PUT | `/users/{user_id}` | Update user information |
| POST | `/users/{user_id}/register` | Mark user as registered |
| DELETE | `/users/{user_id}` | Delete a user |

## Request/Response Examples

### Create a User

**Request:**
```bash
POST /users/
Content-Type: application/json

{
  "first_name": "John",
  "last_name": "Doe",
  "email": "john@example.com",
  "age": 20,
  "address": "123 Main Street",
  "joining_date": "2024-07-17",
  "is_registered": false
}
```

**Response:**
```json
{
  "id": 1,
  "first_name": "John",
  "last_name": "Doe",
  "email": "john@example.com",
  "age": 20,
  "address": "123 Main Street",
  "joining_date": "2024-07-17",
  "is_registered": false
}
```

### Register a User

**Request:**
```bash
POST /users/1/register
```

**Response:**
```json
{
  "id": 1,
  "first_name": "John",
  "last_name": "Doe",
  "email": "john@example.com",
  "age": 20,
  "address": "123 Main Street",
  "joining_date": "2024-07-17",
  "is_registered": true
}
```

### Update User Information

**Request:**
```bash
PUT /users/1
Content-Type: application/json

{
  "age": 21,
  "address": "456 Oak Avenue"
}
```

**Response:**
```json
{
  "id": 1,
  "first_name": "John",
  "last_name": "Doe",
  "email": "john@example.com",
  "age": 21,
  "address": "456 Oak Avenue",
  "joining_date": "2024-07-17",
  "is_registered": true
}
```

### Get User Details

**Request:**
```bash
GET /users/1
```

**Response:**
```json
{
  "id": 1,
  "first_name": "John",
  "last_name": "Doe",
  "email": "john@example.com",
  "age": 21,
  "address": "456 Oak Avenue",
  "joining_date": "2024-07-17",
  "is_registered": true
}
```

## Database Schema

### users
- `id`: Auto-increment primary key
- `first_name`: User's first name (VARCHAR 100)
- `last_name`: User's last name (VARCHAR 100)
- `email`: User's email address (VARCHAR 100, UNIQUE)
- `age`: User's age (INT)
- `address`: User's address (VARCHAR 255)
- `joining_date`: Date user joined (DATE)
- `is_registered`: Registration status (BOOLEAN, default: FALSE)

## Architecture

### MVC Pattern
The service follows the Model-View-Controller architecture:

- **Model** (`user.py`): Pydantic models for request/response validation
- **Controller** (`user_controller.py`): HTTP endpoint definitions and routing
- **Service** (`user_service.py`): Business logic and validation
- **Repository** (`user_repository.py`): Database query execution

### Inter-Service Communication
The User Service communicates with the Poll Service to:
- Delete user's poll answers when a user is deleted
- Cascading deletion ensures data consistency across services

## User Registration Flow

1. User is created with `is_registered: false`
2. User calls `POST /users/{user_id}/register` to become registered
3. Only registered users can answer poll questions
4. Poll Service validates registration before accepting answers

## Running Tests

```bash
# Using Postman or curl
curl http://localhost:8001/users/

# Or use the interactive API docs
http://localhost:8001/docs
```

## Configuration

Edit `.env.example` to customize:

```env
USER_DB_HOST=localhost
USER_DB_PORT=3307
USER_DB_USER=root
USER_DB_PASSWORD=root_password
USER_DB_NAME=user_db
POLL_SERVICE_URL=http://localhost:8002
```

## Error Handling

- **400**: Bad request (invalid input)
- **404**: User not found
- **409**: Conflict (email already exists)

## Author

Orian Ben Old

## License

This project is part of the University Poll System backend assignment.
