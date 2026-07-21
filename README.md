# User Service

Service for managing user accounts and registration for the polling system.

## How to Run

```bash
# Start Docker and database
docker compose up -d
python init_db.py

# Run the service
cd user_service
pip install -r requirements.txt
uvicorn main:app --reload --port 8001
```

Access at: http://localhost:8001/docs

## What It Does

- Create and manage user accounts
- Track user registration status
- Store user profile info (name, email, age, address, etc.)
- Delete users and cascade their poll answers

## API Endpoints

**Users:**
- `POST /users/` - Create user
- `GET /users/` - Get all users
- `GET /users/{id}` - Get specific user
- `PUT /users/{id}` - Update user
- `POST /users/{id}/register` - Mark user as registered (allows them to answer polls)
- `DELETE /users/{id}` - Delete user (also deletes their answers from poll service)

## Database

One table: `users` with id, first_name, last_name, email (unique), age, address, joining_date, and is_registered flag

## Configuration

Copy `.env.example` and edit:
- `USER_DB_HOST=localhost`
- `USER_DB_PORT=3307`
- `POLL_SERVICE_URL=http://localhost:8002` (for deleting user answers)
