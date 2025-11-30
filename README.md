# Service Membership System API

This project is a backend API for a Service Membership System, designed to manage members, plans, subscriptions, and attendance for services like gyms, coaching centers, or salons. It is built using FastAPI and SQLAlchemy, with PostgreSQL as the preferred database.

## Project Structure

```
service-membership-system
├── app
│   ├── routers
│   │   ├── attendance.py
│   │   ├── members.py
│   │   ├── plans.py
│   │   └── subscriptions.py
│   ├── database.py
│   ├── main.py
│   ├── models.py
│   └── schemas.py
├── triggers.sql
├── requirements.txt
└── README.md
```

## Setup Instructions

1. **Create and activate a virtual environment:**
   ```bash
   python -m venv venv
   # Windows
   venv\Scripts\activate
   # Linux/Mac
   source venv/bin/activate
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure the database:**
   Set the `DATABASE_URL` environment variable in your `.env` file.
   ```env
   DATABASE_URL="postgresql://username:password@localhost:5432/dbname"
   ```

4. **Create tables and apply the trigger:**
   Run the SQL commands in `triggers.sql` to set up the database schema and trigger:
   ```bash
   psql -U username -d dbname -f triggers.sql
   ```

5. **Start the application:**
   ```bash
   uvicorn app.main:app --reload
   ```

## API Documentation

### Members

#### Create Member
**Endpoint:** `POST /members`

**Request Body:**
```json
{
  "name": "John Doe",
  "phone": "1234567890"
}
```

**Response:**
```json
{
  "id": 1,
  "name": "John Doe",
  "phone": "1234567890",
  "join_date": "2023-10-27T10:00:00",
  "status": "active",
  "total_check_ins": 0
}
```

#### List Members
**Endpoint:** `GET /members`
**Query Parameters:** `status` (optional, e.g., `active`)

**Response:**
```json
[
  {
    "id": 1,
    "name": "John Doe",
    "phone": "1234567890",
    "join_date": "2023-10-27T10:00:00",
    "status": "active",
    "total_check_ins": 0
  }
]
```

### Plans

#### Create Plan
**Endpoint:** `POST /plans/`

**Request Body:**
```json
{
  "name": "Gold Plan",
  "price": 100.0,
  "duration_days": 30
}
```

**Response:**
```json
{
  "id": 1,
  "name": "Gold Plan",
  "price": 100.0,
  "duration_days": 30
}
```

#### List Plans
**Endpoint:** `GET /plans/`

**Response:**
```json
[
  {
    "id": 1,
    "name": "Gold Plan",
    "price": 100.0,
    "duration_days": 30
  }
]
```

### Subscriptions

#### Create Subscription
**Endpoint:** `POST /subscriptions/`

**Request Body:**
```json
{
  "member_id": 1,
  "plan_id": 1,
  "start_date": "2023-10-27T10:00:00"
}
```

**Response:**
```json
{
  "id": 1,
  "member_id": 1,
  "plan_id": 1,
  "start_date": "2023-10-27T10:00:00",
  "end_date": "2023-11-26T10:00:00"
}
```

#### Get Current Subscription
**Endpoint:** `GET /subscriptions/members/{member_id}/current`

**Response:**
```json
{
  "id": 1,
  "member_id": 1,
  "plan_id": 1,
  "start_date": "2023-10-27T10:00:00",
  "end_date": "2023-11-26T10:00:00"
}
```

### Attendance

#### Check In
**Endpoint:** `POST /attendance/check-in`

**Request Body:**
```json
{
  "member_id": 1
}
```

**Response:**
```json
{
  "id": 1,
  "member_id": 1,
  "check_in_time": "2023-10-28T09:00:00"
}
```
