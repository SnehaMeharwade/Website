# HRMS Lite

Author: Sneha Meharwade

Simple HR app to manage employees and daily attendance.

# Quick start
- Requirements: Python 3.8+, Node.js 14+
- Backend (from project root):

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

# API (examples)
- GET /api/employees/
- POST /api/attendance/

# Notes
- Uses SQLite for development. Use PostgreSQL in production.
- See `QUICK_START.md` for minimal run instructions.

© Sneha Meharwade
