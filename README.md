# Django User Authentication System

A clean and secure user authentication system built with Python and Django. This project features user registration, secure login/logout sessions, restricted access pages, password change, and password reset functionalities, all styled using Bootstrap.

## 🚀 Features
* **Sign Up (Registration):** Validates and hashes user passwords natively.
* **Log In / Log Out:** Managed via secure session states with cross-site request forgery (CSRF) protection.
* **Auto-Login:** Automatically logs users in immediately upon successful registration.
* **Route Protection:** Restricts unauthenticated access to sensitive views (like `secret_page`).
* **Account Maintenance:** Fully operational password change and terminal-based local password resets.
* **Responsive UI:** Modern layout and navbar navigation built with Bootstrap.

---

## 🛠️ Tech Stack
* **Backend:** Python, Django
* **Database:** SQLite (Default built-in core)
* **Frontend:** HTML5, Bootstrap (via CDN)

---

## 💻 Installation & Setup

Follow these steps to get your local development server running:

### 1. Clone the repository
```bash
git clone https://github.com/riddhiaryalearn-prog/Django_Authentication_System.git
cd Django_Authentication_System
```

### 2. Set up a Virtual Environment
```powershell
# Create environment
python -m venv venv

# Activate on Windows (PowerShell)
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process
.\venv\Scripts\Activate.ps1

# Activate on Mac/Linux
source venv/bin/activate
```

### 3. Install Django
```bash
pip install django==6.1.2
```

### 4. Run Migrations
Set up your local SQLite database tables (`auth_user`, sessions, etc.):
```bash
python manage.py migrate
```

### 5. Start the Server
```bash
python manage.py runserver
```
Open your browser and navigate to `http://127.0.0`.

---

## ⚙️ Key Configuration Details
To look back at how this app routes internally, ensure your `settings.py` includes these essential fallback definitions:
```python
LOGIN_URL = 'login'
LOGIN_REDIRECT_URL = 'home'
LOGOUT_REDIRECT_URL = 'home'

MAILERS = {
    "default": {
        "BACKEND": "django.core.mail.backends.console.EmailBackend",
    }
}
```

---
