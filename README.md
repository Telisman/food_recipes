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

## Usage
Register a New User
Endpoint:
 ```bash
POST http://127.0.0.1:8000/api/register/
```
Sample request:
 ```bash
Content-Type: application/json
{
    "email": "user@example.com",
    "password": "password123",
    "first_name": "John",
    "last_name": "Doe",
    "username": "Doe1"
}
```
Obtain JWT Tokens (Login):
Endpoint:
 ```bash
POST http://127.0.0.1:8000/api/token/
```
Sample request:
 ```bash
Content-Type: application/json
{
    "email": "user@example.com",
    "password": "password123"
}
```
Get User Login:
Endpoint:
 ```bash
POST http://127.0.0.1:8000/api/login/
```
Sample request:
 ```bash
Authorization: Bearer <your_access_token>
```
Get User List:
Endpoint:
 ```bash
POST http://127.0.0.1:8000/api/users-list/
```
Sample request:
 ```bash
Authorization: Bearer <your_access_token>
```
Get User Detail by ID:
Endpoint:
 ```bash
POST http://127.0.0.1:8000/api/user-id/<int:id>
```
Sample request:
 ```bash
Authorization: Bearer <your_access_token>
```
# Django web app
## Features
- User Registration 
- User email authentication using hunter.io API endpoint 
- User login page
- Recipes list with filter search form
- Own recipes page
- Detail recipes page, where User can rate recipes from 1 to 5, user can not rate his own recipe.
- Create a recipe page
- List of top 5 ingredients 
