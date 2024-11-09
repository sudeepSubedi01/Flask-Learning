# Setup
## Setting up the environment:
- virtualenv env
- Set-ExecutionPolicy unrestricted  <br>
(if error encountered go to powershell admin and then run this and choose YES)
- pip install virtualenv
- .\env\Scripts\activate.ps1
- pip install flask

## Run the code:
- .\env\Scripts\activate.ps1
- python filepath


# Creating Database
- Install SQLAlchemy:   pip install flask-sqlalchemy <br>
- Import: from flask_sqlalchemy import SQLAlchemy <br>

# Creating Database File
- create the class
- create db object of SQLAlchemy(app)

- open python interpreter:
python
from TodoApp import db,app
with app.app_context():
  db.create_all()

- now todo.db is created in the folder 'instance'