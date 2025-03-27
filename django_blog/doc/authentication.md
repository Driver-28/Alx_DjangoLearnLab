## Features
- User Login
- User Logout
- User Registration with Email
- Profile Management (View/Edit)
- Secure Authentication with CSRF Protection

## Setup Instructions
1. Run migrations: `python manage.py migrate`
2. Create a superuser: `python manage.py createsuperuser`
3. Start the server: `python manage.py runserver`
4. Test authentication features by visiting `/login`, `/register`, `/profile`

## Security Measures
- CSRF protection enabled.
- Passwords are hashed using Django’s authentication system.
- Profile management is restricted to logged-in users.
