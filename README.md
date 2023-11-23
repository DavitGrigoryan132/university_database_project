# University Database Project
# FastAPI CRUD Application - API Documentation

## Lessons

### Create Lesson

- **Endpoint:** `/lessons/`
- **Method:** POST
- **Request Body:** JSON with lesson details.
- **Response:** Lesson details in JSON format.

### Read Lesson

- **Endpoint:** `/lessons/{date}/{time}`
- **Method:** GET
- **Response:** Lesson details in JSON format.

### Update Lesson

- **Endpoint:** `/lessons/{date}/{time}`
- **Method:** PUT
- **Request Body:** JSON with updated lesson details.
- **Response:** Updated lesson details in JSON format.

### Delete Lesson

- **Endpoint:** `/lessons/{date}/{time}`
- **Method:** DELETE
- **Response:** Deleted lesson details in JSON format.

### List All Lessons

- **Endpoint:** `/lessons/`
- **Method:** GET
- **Response:** List of lessons in JSON format.

## Lecturers

### Create Lecturer

- **Endpoint:** `/lecturers/`
- **Method:** POST
- **Request Body:** JSON with lecturer details.
- **Response:** Lecturer details in JSON format.

### Read Lecturer

- **Endpoint:** `/lecturers/{lecturer_id}`
- **Method:** GET
- **Response:** Lecturer details in JSON format.

### Update Lecturer

- **Endpoint:** `/lecturers/{lecturer_id}`
- **Method:** PUT
- **Request Body:** JSON with updated lecturer details.
- **Response:** Updated lecturer details in JSON format.

### Delete Lecturer

- **Endpoint:** `/lecturers/{lecturer_id}`
- **Method:** DELETE
- **Response:** Deleted lecturer details in JSON format.

### List All Lecturers

- **Endpoint:** `/lecturers/`
- **Method:** GET
- **Response:** List of lecturers in JSON format.

## Subjects

### Create Subject

- **Endpoint:** `/subjects/`
- **Method:** POST
- **Request Body:** JSON with subject details.
- **Response:** Subject details in JSON format.

### Read Subject

- **Endpoint:** `/subjects/{name}`
- **Method:** GET
- **Response:** Subject details in JSON format.

### Update Subject

- **Endpoint:** `/subjects/{name}`
- **Method:** PUT
- **Request Body:** JSON with updated subject details.
- **Response:** Updated subject details in JSON format.

### Delete Subject

- **Endpoint:** `/subjects/{name}`
- **Method:** DELETE
- **Response:** Deleted subject details in JSON format.

### List All Subjects

- **Endpoint:** `/subjects/`
- **Method:** GET
- **Response:** List of subjects in JSON format.

**Note:** Ensure the FastAPI application is running, and you can access the API documentation at [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) or ReDoc at [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc) to interact with the API.
