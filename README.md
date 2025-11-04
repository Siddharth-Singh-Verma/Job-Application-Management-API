# Job Application Management API

A simple Django REST Framework API for managing job applications, applicants, and jobs.
[Demo Video](https://drive.google.com/file/d/1bCj4mVHoV7_BcYu62KSJQhOz-yz0YTAu/view?usp=sharing)
## Setup Instructions

1. **Clone the repository**
2. **Create and activate a virtual environment**
   ```bash
   python -m venv env
   source env/bin/activate  # On Windows: env\Scripts\activate
   ```
3. **Install dependencies**
   ```bash
   pip install django djangorestframework
   ```
4. **Apply migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```
5. **Create a superuser (optional, for admin access)**
   ```bash
   python manage.py createsuperuser
   ```
6. **Run the development server**
   ```bash
   python manage.py runserver
   ```

## API Endpoints

| Endpoint                   | Method         | Description                              |
|---------------------------|----------------|------------------------------------------|
| /api/applicants/          | GET, POST      | List or create applicants                |
| /api/applicants/{id}/     | GET, PUT, DELETE | Retrieve, update or delete applicant   |
| /api/jobs/                | GET, POST      | List or create jobs                      |
| /api/jobs/{id}/           | GET, PUT, DELETE | Retrieve, update or delete job         |
| /api/apply/               | POST           | Apply for a job                          |
| /api/applications/        | GET            | List all applications                    |
| /api/applications/{id}/   | PATCH          | Update application status                |

## Features
- Prevents duplicate applications for the same job by the same applicant
- Search filter on applicants by name or email
- Uses ModelSerializer with validation
- Returns proper HTTP status codes

## Testing
- Use Django admin or tools like Postman/curl to test endpoints
- Ensure migrations are applied before testing

## How It Works
- Applicants and jobs can be created, listed, updated, or deleted
- Applications are created via /api/apply/ and validated for duplicates
- Application status can be updated via PATCH
- Search applicants by name/email using ?search= query param
