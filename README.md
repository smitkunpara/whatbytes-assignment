# Healthcare Management System

A secure backend for a healthcare application using Django, Django REST Framework (DRF), and PostgreSQL. The app supports user registration/login and allows authenticated users to manage patients, doctors, and their assignments.

## Features

- User Authentication (Registration/Login) using JWT
- Patient Management
- Doctor Management
- Patient-Doctor Assignment Management
- RESTful API for all operations
- Simple Frontend Interface for interaction

## Tech Stack

- **Backend Framework**: Django + Django REST Framework
- **Database**: PostgreSQL (configurable with SQLite for development)
- **Authentication**: JWT using djangorestframework-simplejwt
- **Frontend**: Simple HTML/CSS/JavaScript interface

## API Endpoints

### Authentication APIs

- `POST /api/auth/register/` - Register a new user
- `POST /api/auth/login/` - Log in and receive JWT token
- `POST /api/auth/token/refresh/` - Refresh JWT token
- `GET /api/auth/user/` - Get current user details

### Patient Management APIs

- `POST /api/patients/` - Create a new patient
- `GET /api/patients/` - Get all patients
- `GET /api/patients/<id>/` - Get a specific patient's details
- `PUT /api/patients/<id>/` - Update patient info
- `DELETE /api/patients/<id>/` - Delete patient record
- `GET /api/patients/<id>/doctors/` - Get all doctors assigned to a specific patient

### Doctor Management APIs

- `POST /api/doctors/` - Create a new doctor
- `GET /api/doctors/` - Get all doctors
- `GET /api/doctors/<id>/` - Get a specific doctor's details
- `PUT /api/doctors/<id>/` - Update doctor info
- `DELETE /api/doctors/<id>/` - Delete doctor record
- `GET /api/doctors/<id>/patients/` - Get all patients assigned to a specific doctor

### Patient-Doctor Mapping APIs

- `POST /api/mappings/` - Assign a doctor to a patient
- `GET /api/mappings/` - Get all mappings
- `GET /api/mappings/<id>/` - Get specific mapping details
- `DELETE /api/mappings/<id>/` - Remove doctor from patient

## Setup Instructions

1. Clone the repository
2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Set up environment variables (edit `.env` file):
   ```
   # Database connection
   DATABASE_URL=postgres://username:password@localhost:5432/healthcare
   
   # JWT Configuration
   JWT_SECRET=your_secret_key
   JWT_ALGORITHM=HS256
   JWT_EXP_MINUTES=180
   ```
4. Run migrations:
   ```
   python manage.py migrate
   ```
5. Create a superuser:
   ```
   python manage.py createsuperuser
   ```
6. Run the development server:
   ```
   python manage.py runserver
   ```
7. Access the admin interface at:
   ```
   http://127.0.0.1:8000/admin/
   ```
8. Access the frontend interface at:
   ```
   http://127.0.0.1:8000/
   ```

## Security Features

- JWT Authentication for API protection
- Password validation and hashing
- Permission-based access control
- Environment variables for sensitive data

## Frontend Interface

The application includes a simple frontend interface built with HTML, CSS, and JavaScript that allows users to:

- Register and login
- Manage patients and doctors
- Create and manage doctor-patient assignments

## License

This project is licensed under the MIT License - see the LICENSE file for details.
