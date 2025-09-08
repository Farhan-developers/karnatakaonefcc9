# Karnataka One CC9 (Django + SQLite)

A starter template for a Karnataka-One-style citizen service center website for your CC9 franchise.

## Features
- Public pages: Home, Services list, Service detail with request form, Enquiry
- Admin login at `/admin/` to manage categories, services, requests, and enquiries
- SQLite backend, Bootstrap UI
- Media upload for attachments

## Quick Start

```bash
# 1) Create & activate virtual env (Windows PowerShell)
python -m venv venv
venv\Scripts\activate

# 2) Install deps
pip install -r requirements.txt

# 3) Migrate
python manage.py migrate

# 4) Load demo data
python manage.py loaddata core/fixtures/initial_data.json

# 5) Create admin
python manage.py createsuperuser

# 6) Run
python manage.py runserver
```

Open http://127.0.0.1:8000/ for the site and http://127.0.0.1:8000/admin/ for admin login.
