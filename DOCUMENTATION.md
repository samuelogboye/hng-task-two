# My Flask API Documentation

This documentation outlines the usage, formats, and setup instructions for the My Flask API.

## UML Diagram

https://imgur.com/a/d1ECDQm
![UML DIAGRAM](UML-Diagram.png)

## Standard Request and Response Formats

### Create User (POST /api/)

**Request Format:**

```json
{
  "name": "John Doe"
}
```

Response Format (Success - HTTP 201):

```json
{
  "id": 9,
  "message": "User created successfully",
  "name": "John Doe"
}
```

Response Format (Error - HTTP 400 - Validation Error):

```json
{
  "error": "Please provide a name"
}
```

Response Format (Error - HTTP 400 - Validation Error):

```json
{
  "error": "Name must be a string"
}
```

### Get User by ID (GET /api/int:user_id)

Response Format (Success - HTTP 200):

```json
{
  "id": 1,
  "name": "John Doe"
}
```

Response Format (Error - HTTP 404 - User Not Found):

```json
{
  "error": "User not found/id not in Database"
}
```

### Update User by ID (PUT /api/int:user_id or PATCH /api/int:user_id)

Request Format:

```json
{
  "name": "New Name"
}
```

Response Format (Success - HTTP 200):

```json
{
  "id": 15,
  "message": "User updated successfully",
  "name": "New Name"
}
```

Response Format (Error - HTTP 404 - User Not Found):

```json
{
  "error": "User not found/id not in Database"
}
```

### Delete User by ID (DELETE /api/int:user_id)

Response Format (Success - HTTP 200):

```json
{
  "id": 30,
  "message": "User deleted successfully",
  "name": "Temitope"
}
```

Response Format (Error - HTTP 404 - User Not Found):

```json
{
  "error": "User not found/id not in Database"
}
```

### List All Users (GET /api/users)

Response Format (Success - HTTP 200):

```json
[
  {
    "id": 1,
    "name": "John Doe"
  },
  {
    "id": 2,
    "name": "Jane Smith"
  }
]
```

## Sample Usage

### Creating a User

Request:

```http
POST /api/
Content-Type: application/json

{
  "name": "Alice"
}
```

Response (HTTP 201):

```json
{
  "id": 9,
  "message": "User created successfully",
  "name": "John Doe"
}
```

### Getting User by ID

Request:

```http
GET /api/1
```

Response (HTTP 200):

```json
{
  "id": 1,
  "name": "Alice"
}
```

### Updating User by ID

Request:

````http
PUT /api/1
Content-Type: application/json
```http
{
  "name": "Updated Name"
}
````

Response (HTTP 200):

```json
{
  "id": 15,
  "message": "User updated successfully",
  "name": "Updated Name"
}
```

## Known Limitations and Assumptions

The API assumes that the name field is a required attribute for creating and updating users. It validates that the name is a string.

## Setup and Deployment Instructions

### Local Setup

1. Clone the repository:

```bash
git clone https://github.com/samuelogboye/hng-task-two
```

Navigate to to hng-task-two directory

```bash
cd hng-task-two
```

2. Create a virtual environment (optional but recommended):

```bash
python -m venv venv
```

```bash
source venv/bin/activate  # On Windows, use venv\Scripts\activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Create a .env file in the project root directory with the following content:

```bash
DATABASE_URI=mysql+pymysql://username:password@localhost/mydatabase
```

5. Run the application:

```bash
python app.py
```

## API Endpoints

    POST /api/: Create a new user.
    GET /api/<int:user_id>: Get user details by ID.
    PUT /api/<int:user_id>: Update user details by ID.
    PATCH /api/<int:user_id>: Partially update user details by ID.
    DELETE /api/<int:user_id>: Delete a user by ID.
    GET /api/users: List all users.

## Configuration

You can customize the application by modifying the environment variables in the .env file.
Testing

To run tests, use the following command:

```bash
pytest
```

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE) file for details.
