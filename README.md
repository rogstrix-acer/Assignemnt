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
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

2. **Install dependencies:**
   ```
   pip install -r requirements.txt
   ```

3. **Configure the database:**
   Set the `DATABASE_URL` environment variable in your `.env` file or directly in your environment. Example for PostgreSQL:
   ```
   DATABASE_URL=postgresql://username:password@localhost/dbname
   ```

4. **Create tables and apply the trigger:**
   Run the SQL commands in `triggers.sql` to set up the database schema and trigger:
   ```
   psql -U username -d dbname -f triggers.sql
   ```

5. **Start the application:**
   ```
   uvicorn app.main:app --reload
   ```

## API Endpoints

### Members
- **POST /members**: Create a new member.
- **GET /members**: List all members (optional query parameter: status).

### Plans
- **POST /plans**: Create a new plan.
- **GET /plans**: List all plans.

### Subscriptions
- **POST /subscriptions**: Create a subscription for a member.
- **GET /members/{member_id}/current-subscription**: Retrieve the current active subscription for a member.

### Attendance
- **POST /attendance/check-in**: Check in a member.
- **GET /members/{member_id}/attendance**: Retrieve attendance records for a member.

## Example Requests

### Create a Member
```
POST /members
{
  "name": "John Doe",
  "phone": "1234567890"
}
```

### List Members
```
GET /members?status=active
```

### Create a Plan
```
POST /plans
{
  "name": "Monthly",
  "price": 29.99,
  "duration_days": 30
}
```

### Check In a Member
```
POST /attendance/check-in
{
  "member_id": 1
}
```

## Notes
- Ensure that PostgreSQL is running and accessible.
- Modify the `requirements.txt` file as needed to include any additional dependencies.
- The project is structured for clarity and maintainability, following best practices for FastAPI applications.