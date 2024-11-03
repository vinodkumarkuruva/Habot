1. Introduction : 
 The project aims to Build a basic REST API to manage employees in a company, focusing on CRUD operations, RESTful principles, and authentication.
2. Technologies : 
  Flask
  SQLAlchemy
  Migrate
  SQLite (or any other preferred database)
  Authentication: Flask-JWT-Extended
3. Features : 
   - User Signup: Users register with Username, password.
   - User Login: Users log in with Username and password.
   - Create_Employee : Users add Employee via email, assigning roles and department to them .
   - Operations : Focusing on full CRUD operations on employee.
   - Filtering: Allow filtering of employees by department and role.
   -  Pagination: Limit results per page to 10 employees with pagination support 
   - Authentication: Use token-based authentication (JWT) to secure the endpoints. Only authenticated users should access these endpoints.

4. Installation and Setup

  1. Clone the Repositry :
     
      1 . https://github.com/vinodkumarkuruva/Hackathon.git cd Hackathon
      2 . Prerequisites - Python 3.7+: Ensure that Python is installed on your system Flask - As a Framework 
      3 . Steps to Set Up - Create a virtual environment : python3 -m venv < name of virtual Environment >
                          To activate the virtual Environment   :    < name of virtual Environment >/Scripts/activate 
                           Install dependencies                  :    pip install -r requirements.txt
                           Set up the database                   :    flask db init
                         	                                            flask db migrate -m "Initial migration"
                                                                      flask db upgrade
                           Run the server                        :    Python run.py 
                           * The application will start and be accessible at http://127.0.0.1:5000
5.Other Info :

--> Error Handling: The application returns appropriate HTTP 400 status codes for Successful and bad requests.
--> Modularity: The application is designed to be modular, with separate services handling business logic, making the codebase easy to maintain and extend.
-->All APIs require data in JSON format. Some APIs, such as authentication, return a JWT token to be used in subsequent requests.
