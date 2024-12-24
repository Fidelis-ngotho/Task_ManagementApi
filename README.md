Project Title: Task Management API
Description: A Django-based API to manage tasks with CRUD functionality.


Setup Instructions:
## Setup Instructions
1. Clone the repository:
   ```bash
   git clone <your-repo-URL>
   cd TaskManagementAPI



# Authentication Setup for the API

## Overview
This API uses JWT-based authentication for secure access.

### Token Authentication
1. Use the `/api/token/` endpoint to obtain an access token.
2. Use the `/api/token/refresh/` endpoint to refresh your token.

### Testing the API
1. Generate an access token by sending your username and password to `/api/token/`.
2. Include the token in the `Authorization` header:
