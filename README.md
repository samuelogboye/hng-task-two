# My Flask API

A simple Flask API for managing user data with a MySQL database.

## Overview

This Flask API allows you to perform CRUD operations on user data. It uses SQLAlchemy to interact with a MySQL database.

## Getting Started

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

## UML Diagram

![UML DIAGRAM](UML-Diagram.png)

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
