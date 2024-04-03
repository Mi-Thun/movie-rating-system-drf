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
- PostgreSQL

1. **Clone the Repository**
   git clone https://github.com/mi-thun/movie-rating-system-drf.git
   cd movie-rating-system

2. **Create a Virtual Environment**
   For macOS and Linux:
   python3 -m venv venv
   source venv/bin/activate

3. **Install Dependencies**
   pip install -r requirements.txt

4. **Environment Configuration**
   Rename `.env.example` to `.env` and update the file with your PostgreSQL database credentials and other settings.

5. **Database Setup**
   sudo -u postgres psql
   CREATE DATABASE bg_db;
   CREATE USER bg_user WITH PASSWORD 'bg123';
   GRANT ALL PRIVILEGES ON DATABASE bg_db TO bg_user;
   \q
   python manage.py makemigrations
   python manage.py migrate
   create a superuser

6. **Run the Development Server**
   python manage.py runserver

Visit `http://127.0.0.1:8000/` in your web browser to confirm the project is running successfully.

### Using the API

- To **Login**, send a POST request to `/api/login/` with your username and password to obtain a token.
- Use the obtained token for authentication when making further requests.
- To **Add a Movie**, send a POST request to `/api/movies/` with the movie details.
- To **View All Movies** or **Search for a Movie**, send a GET request to `/api/movies/` with optional `?search=<movie_name>` query parameters.
- To **Rate a Movie**, send a POST request to /api/ratings/ including the movie ID and your rating value in the request body.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or create an issue for any features, bug fixes, or improvements.

## License

[MIT License](LICENSE.md)
