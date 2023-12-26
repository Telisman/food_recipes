# Django REST API instruction for are project

This Django application provides a RESTful API for user authentication and user management.

## Features

- User registration
- User authentication using JWT tokens
- Retrieving user list
- Fetching user details by ID

## Installation

1. Clone the repository:

   ```bash
   git clone git@github.com:Telisman/food_recipes.git

2. Install dependencies:
   ```bash
   pip install -r requirements.txt

3. Perform migrations:
   ```bash
   python manage.py makemigrations
   python manage.py migrate

##Usage
Register a New User
Endpoint: POST /api/register/

