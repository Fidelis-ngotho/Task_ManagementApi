Project Title

Task Management API
Description:

The Task Management API is a Django-based API designed to manage tasks efficiently. It provides CRUD functionality (Create, Read, Update, Delete), JWT-based authentication for secure access, and task prioritization features.

This API enables users to:

    Create tasks with detailed descriptions, priorities, and deadlines.
    View all tasks or retrieve specific tasks by ID.
    Update task details such as status, priority, and description.
    Delete tasks that are no longer required.
    Authenticate users with secure JWT-based tokens.

Setup Instructions
1. Clone the Repository

First, clone the repository to your local system and navigate into the project directory:

git clone <your-repo-URL>
cd TaskManagementAPI

2. Prerequisites

Ensure the following are installed on your system:

    Python 3.8 or higher
    pip (Python package manager)
    PostgreSQL (if using PostgreSQL as your database)
    Virtualenv (for isolating dependencies)

3. Create a Virtual Environment

To avoid dependency conflicts, create and activate a virtual environment:

python3 -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate

4. Install Dependencies

Install all required dependencies using:

pip install -r requirements.txt

5. Database Setup

    Set Up Environment Variables: Create a .env file in the project directory and add the following variables:

SECRET_KEY=<your-django-secret-key>
DEBUG=True
DATABASE_URL=postgres://<username>:<password>@<host>:<port>/<database-name>

Apply Migrations: Run the following commands to set up the database schema:

    python manage.py makemigrations
    python manage.py migrate

6. Run the Server

Start the Django development server:

python manage.py runserver

Access the API locally at http://127.0.0.1:8000.
Authentication Setup for the API
Overview

The API uses JWT-based authentication to secure user access.
Token Authentication

    Obtain Access Token: Use the /api/token/ endpoint with your username and password.
    Refresh Access Token: Use the /api/token/refresh/ endpoint to refresh your token.

Example: Generate Access Token

Send a POST request with your username and password to /api/token/:

POST /api/token/
{
    "username": "<your-username>",
    "password": "<your-password>"
}

Include the token in the Authorization header of your requests:

Authorization: Bearer <your-access-token>

Testing the API

To test the API, you can use tools like Postman, cURL, or any REST client.
Endpoints
Method	Endpoint	Description
POST	/api/token/	Obtain access token
POST	/api/token/refresh/	Refresh access token
GET	/tasks/	List all tasks
POST	/tasks/	Create a new task
GET	/tasks/<id>/	Retrieve a specific task
PUT	/tasks/<id>/	Update a specific task
DELETE	/tasks/<id>/	Delete a specific task
Common Errors and Troubleshooting

    Database Connection Error:
        Check that the .env file is correctly configured with the database credentials.
        Ensure your database server is running and accessible.

    Token Authentication Fails:
        Confirm you are including the token in the Authorization header.
        If the token has expired, use the /api/token/refresh/ endpoint to generate a new one.

    Static Files Not Loading:
        Run python manage.py collectstatic to gather static files.
        Configure your server to serve static files.