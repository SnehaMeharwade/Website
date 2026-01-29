# HRMS Lite - Quick Start

Author: Sneha Meharwade

Minimal steps to run locally:

- Backend (project root):

```bash
python -m venv myenv
myenv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

- Frontend:

```bash
cd frontend
npm install
npm start
```

API examples:
- GET /api/employees/
- POST /api/attendance/

Use SQLite for development. For production use PostgreSQL and set environment variables.
