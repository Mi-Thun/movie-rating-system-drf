# Movie Rating System

## Project Overview

The Visionary Tech Solutions Movie Rating System is a Django REST API designed to provide users with the capability to rate movies and search through a curated list of films. This project serves as a test assessment to demonstrate REST API development skills, including CRUD operations, authentication, and advanced querying capabilities.

### Features

- User authentication system allowing for secure login and registration.
- Ability for authenticated users to add, update, delete, and view movies.
- Users can rate movies and view the average rating of each movie.
- Advanced movie search functionality based on movie name or genre.
- Environment variable management for secure and flexible configuration.
- PostgreSQL database integration for robust data storage and retrieval.

## Getting Started

### Prerequisites

Ensure you have the following installed on your system:

- Python 3.8 or higher
- pip (Python package manager)
- PostgreSQL - For Remote Access

1. **Clone the Repository**
   git clone `https://github.com/mi-thun/movie-rating-system-drf.git`
   cd movie-rating-system

2. **Create a Virtual Environment**
   For macOS and Linux:

   - `python3 -m venv venv`
   - `source venv/bin/activate`

3. **Install Dependencies**

   - `pip install -r requirements.txt`

4. **Environment Configuration**

   - Rename `.env.example` to `.env` and update the file with your PostgreSQL database credentials and other settings.

5. **Database Setup**

   - `sudo -u postgres psql`
   - `CREATE DATABASE bg_db;`
   - `CREATE USER bg_user WITH PASSWORD 'bg123';`
   - `GRANT ALL PRIVILEGES ON DATABASE bg_db TO bg_user;`

   - `python manage.py makemigrations`
   - `python manage.py migrate`
   - `python manage.py createsuperuser`

6. **Run the Development Server**
   - `python manage.py runserver`

Visit `http://127.0.0.1:8000/` in your web browser to confirm the project is running successfully.

### Using the API

- To **Login**, send a POST request to `/api/login/` with your username and password to obtain a token.
- Use the obtained token for authentication when making further requests.
- To **Add a Movie**, send a POST request to `/api/movies/` with the movie details.
- To **View All Movies** or **Search for a Movie**, send a GET request to `/api/movies/` with optional `?search=<movie_name>` query parameters.
- To **Rate a Movie**, send a POST request to /api/ratings/ including the movie ID and your rating value in the request body.

## Postman Collection

For API testing and exploration, a Postman collection is provided with the project. This collection contains pre-configured requests for all the API endpoints, making it easier to test and interact with the API. File name `vts coding test drf.postman_collection.json`

To use the collection:

1. Download and install [Postman](https://www.getpostman.com/).
2. Import the provided collection file into Postman.
3. Ensure your local server is running as the collection is configured to point to `localhost`.

To create an API document based on the provided Postman collection, we'll structure the document with an overview section, followed by detailed endpoints. This document will describe each API endpoint, including the method, URL, headers, request body, and any authorization required. 

# API Documentation 

## Overview

This document outlines the API endpoints for Django Rest Framework (DRF) application. The API supports operations such as user login, logout, user management, and movie-related functionalities including adding movies, searching movies, and rating movies.

Base URL: `http://127.0.0.1:8000/api/`

## Authentication

Some endpoints require authentication. This is achieved by sending a Token in the Authorization header. The token must be acquired through the login process.

## Endpoints

### Login

- **Method**: POST
- **URL**: `/login/`
- **Auth Required**: No
- **Headers**: None
- **Body**: 
  ```json
  {
    "username": "user@example.com",
    "password": "password"
  }
  ```
- **Description**: Authenticates the user and returns a token for accessing protected endpoints.

### Logout

- **Method**: POST
- **URL**: `/logout/`
- **Auth Required**: Yes
- **Headers**:
  - Authorization: Token `<user_token>`
- **Body**: None
- **Description**: Logs out the user and invalidates the user's token.

### Get All Users (Check User)

- **Method**: GET
- **URL**: `/users/`
- **Auth Required**: Yes
- **Headers**:
  - Authorization: Token `<user_token>`
- **Body**: None
- **Description**: Retrieves a list of all users. This action checks if the user exists or not.

### Get All Users (Admin Only)

- **Method**: GET
- **URL**: `/users/`
- **Auth Required**: Yes
- **Headers**:
  - Authorization: Token `<admin_token>`
- **Body**: None
- **Description**: Retrieves a list of all users. Only accessible by admin users.

### Add New User (Admin Only)

- **Method**: POST
- **URL**: `/users/`
- **Auth Required**: Yes
- **Headers**:
  - Authorization: Token `<admin_token>`
- **Body**: 
  ```json
  {
    "name": "New User",
    "phone": "0000000000",
    "email": "newuser@example.com",
    "password": "password"
  }
  ```
- **Description**: Allows an admin to add a new user.

### Get All Movies

- **Method**: GET
- **URL**: `/movies/`
- **Auth Required**: Yes
- **Headers**:
  - Authorization: Token `<admin_token>`
- **Body**: None
- **Description**: Retrieves a list of all movies.

### Add Movie

- **Method**: POST
- **URL**: `/movies/`
- **Auth Required**: Yes
- **Headers**:
  - Authorization: Token `<user_token>`
- **Body**: 
  ```json
  {
    "name": "Movie Name",
    "genre": "Genre",
    "rating": "PG",
    "release_date": "YYYY-MM-DD"
  }
  ```
- **Description**: Adds a new movie to the database.

### Search Movie

- **Method**: GET
- **URL**: `/movies/?search="<Movie Name>"`
- **Auth Required**: Yes
- **Headers**:
  - Authorization: Token `<user_token>`
- **Body**: None
- **Description**: Searches for movies by name.

### Add a Rating

- **Method**: POST
- **URL**: `/ratings/`
- **Auth Required**: Yes
- **Headers**:
  - Authorization: Token `<user_token>`
- **Body**: 
  ```json
  {
    "user_id": 1,
    "movie_id": 3,
    "rating": 5
  }
  ```
- **Description**: Allows a user to add a rating to a movie.

### Get All Ratings

- **Method**: GET
- **URL**: `/ratings/`
- **Auth Required**: Yes
- **Headers**:
  - Authorization: Token `<user_token>`
- **Description**: Retrieves all movie ratings.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or create an issue for any features, bug fixes, or improvements.

## License

[MIT License](LICENSE.md)
