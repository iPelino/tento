# Tento Backend

This is the backend for the Tento housing platform, built with Django and Django REST Framework.

## Getting Started

### Prerequisites

- Python 3.8+
- PostgreSQL
- Redis (for Celery)

### Installation

1. Navigate to the backend directory:
```bash
cd backend
```

2. Create and activate a virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up the database:
```bash
python manage.py migrate
```

5. Create a superuser (optional):
```bash
python manage.py createsuperuser
```

### Running the Server

To run the development server, make sure you're in the backend directory and run:

```bash
python manage.py runserver
```

The server will be available at http://localhost:8000.

**Important**: Always run the server from the backend directory, not from the project root.

### API Documentation

API documentation is available at:
- Swagger UI: http://localhost:8000/swagger/
- ReDoc: http://localhost:8000/redoc/

## Project Structure

The backend follows a modular structure with separate Django apps for different features:

- `apps/core`: Core functionality and utilities
- `apps/users`: User management
- `apps/properties`: Property listings and management
- `apps/leases`: Lease agreements and management
- `apps/payments`: Rent payments and financial transactions
- `apps/maintenance`: Maintenance requests and tracking
- `apps/communications`: Messaging and notifications

## Environment Variables

The backend uses environment variables for configuration. These are loaded from a `.env` file in the backend directory. See the `.env` file for available configuration options.