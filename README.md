# Library Management API (DRF + JWT)

This is a RESTful API for managing a book library, built with **Django REST Framework**. The project implements a robust system for handling books and authors, secured by **JWT (JSON Web Token)** authentication.

## Features
*   **Book & Author Management**: Full CRUD capabilities with relational database structure.
*   **JWT Authentication**: Secure access to endpoints using `djangorestframework-simplejwt`.
*   **User Registration**: Custom endpoint for new user creation.
*   **Data Validation**: Strict validation for unique ISBNs and required fields.
*   **Enhanced Output**: Optimized serializers that return author names instead of just IDs for better readability.

## Tech Stack
*   **Language**: Python 3.x
*   **Framework**: Django 5.x
*   **API Toolkit**: Django REST Framework
*   **Authentication**: SimpleJWT
*   **Database**: SQLite

## Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone <your-repository-link>
   cd library_jwt
2. **Create and activate a virtual environment:**
  ```bash
  python -m venv venv
  # For Windows:
  venv\Scripts\activate
  ```
3. **Install dependencies:**
  ```bash
  pip install -r requirements.txt
  ```
4. **Apply migrations:**
  ```bash
  python manage.py migrate
  ```

5. **Run the development server:**
  ```bash
  python manage.py runserver
  ```

## API Endpoints
**Authentication & Users:**
- POST /api/register/ - Register a new user.
- POST /api/token/ - Obtain Access and Refresh tokens (Login).
- POST /api/token/refresh/ - Refresh the Access token.

**Books:**
- GET /api/books/ - Retrieve a list of all books.
- POST /api/books/ - Create a new book entry (requires Bearer Token).

## Testing with Postman
1. Use the /api/register/ endpoint to create an account.
2. Login via /api/token/ to receive your access token.
3. In your request to /api/books/, go to the Authorization tab, select Bearer Token, and paste your access token.


