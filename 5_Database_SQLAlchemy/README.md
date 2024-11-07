# ORM, Object-Relational Mapping
- a programming technique that allows developers to interact with databases in an object-oriented way rather than writing complex SQL queries directly
- ORM translates structure and records in database into python classes and objects

# ORM Working
1. Mapping Classes to Tables
- Each class represents a database table. The attributes of the class represent the columns, and each object of the class represents a row in the table.
2. Object Representation
- Instance of the class represents a row in the table
3. Database Operations
- ORM allows you to perform CRUD operations using object methods.
4. Relationships
- ORM supports relationships between different tables using foreign keys and relationships in classes.

# SQLAlchemy; library
- SQL toolkit and Object-Relational Mapping (ORM) library for Python

# Flask-SQLAlchemy
- pip install Flask Flask-SQLAlchemy
- extension for Flask that simplifies using SQLAlchemy within Flask applications.

# How to use Flask-SQLAlchemy
1. Import sqlalchemy from flask_sqlalchemy
2. Initialize flask app
3. Configure the database URI
- Tells SQLAlchemy type of database to connect to and its location
- For sqlite database: app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db' <br> To save resources: app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
4. Initialize SQLAlchemy with flask app: db = SQLAlchemy(app)

# SQLite
- lightweight, serverless, self-contained RDBMS that is used in applications where a full-fledged database server like MySQL or PostgreSQL would be overkill
- SQLite databases are stored in a single file on disk with a .sqlite or .db extension
- Applications access the database by reading and writing directly to this file using the SQLite API

# Creating .db file
1. Create model and app
2. Open python interpreter
3. <pre>Run these:
   from app import app,db
   app_context = app.app_context()
   app_context.push()
   db.create_all()
   </pre>

# Insering a row in .db file
<pre>
from app import Employee
michael = Employee(name='Michael', age=42, email='michael@gmail.com')
db.session.add(michael)
db.session.commit()
</pre>

# Insering rows in .db file
<pre>
from app import Employee
obj_1 = Employee(name='name1', age=42, email='name1@gmail.com')
obj_2 = Employee(name='name2', age=42, email='name2@gmail.com')
obj_n = Employee(name='name3', age=42, email='name3@gmail.com')
db.session.add_all([obj_1, obj_2, ....., obj_n])
db.session.commit()
</pre>

# Fetching all rows from .db file
<pre>
emp = Employee.query.all()      # returns a list of type Employee (class)
emp                             # prints list
type(emp)                       # <class 'list'>
emp[0]                          # returns first element of list
type(emp[0])                    # <class 'app.Employee'>
emp[0].name                     # 'Michael'
</pre>

# Fetching first row from .db file
emp = Employee.query.first()

# Fetching random rows from .db file
<pre>
Employee.query.filter_by(name='Trump').all()
</pre>

# Fetching rows from .db file by id
db.session.get(Employee,2)

# Updating data
<pre>
michael.age = 100
db.session.commit()
</pre>

# Deleting Rows
<pre>
db.session.delete(trump)
db.session.commit()
</pre>
