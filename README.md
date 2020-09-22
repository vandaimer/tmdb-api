## TMDB API

Service that connect on TMDb API and return informations about *upcoming movies*.

- Stack
	- Flask Framework (Python)
	- Docker
	- Docker Compose
- Third-party libraries
	- Flask: Python Framework
	- gunicorn:  Python WSGI HTTP Server
	- requests: Library to make HTTP requests
	- Flask-Caching: Library to help to work with cache in function level
	- Flask-Cors: Library to allow CORS
	- pytest: Suite test library
	- requests-mock: Requests library mock
	- pytest-mock: Library to help to mock objects
	- flake8: Tool for code style guide
- Architecture
	- I thought in a simple REST API, so it has a views package (controles), when has the logic business and a services package, when has the comuniction with external services or database etc.
-  Assumptions
	- The application does not need storage any data
	- The application can have an cache for genres data (one day cache timeout)
	- The movie search will be implemented only on the frontend
- Special build instructions
	- You're going to have docker and docker-compose installed
	- Run **docker-compose up dev** to run as development mode
	- Run **docker-compose up prod** to run as production mode
	- Run **docker-compose run --rm tests** to run the unittests
	- Run **docker-compose run --rm flake8** to run flake8
	- To easy production deploy you can run **docker-compose up -d prod**.
- Endpoints: After run the application, you can check the API endpoins.
- ```GET /api/v1/helthcheck```
	- ```GET /api/v1/movie/upcoming```
	- ```GET /api/v1/movie/upcoming?page=([0-9]+)```

## Running the project
- Run docker-compose up dev
- Go to the browser on ```http://localhost:8000/api/v1/healthcheck``` or ```http://localhost:8000/api/v1/movie/upcoming```
