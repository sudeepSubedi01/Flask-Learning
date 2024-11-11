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
3. Run these:
   ```py
   from app import app,db
   app_context = app.app_context()
   app_context.push()
   db.create_all()
   ```

# Insering a row in .db file
```py
from app import Employee
michael = Employee(name='Michael', age=42, email='michael@gmail.com')
db.session.add(michael)
db.session.commit()
```

# Insering rows in .db file
```py
from app import Employee
obj_1 = Employee(name='name1', age=42, email='name1@gmail.com')
obj_2 = Employee(name='name2', age=42, email='name2@gmail.com')
obj_n = Employee(name='name3', age=42, email='name3@gmail.com')
db.session.add_all([obj_1, obj_2, ....., obj_n])
db.session.commit()
```

# Fetching all rows from .db file
```py
emp = Employee.query.all()      # returns a list of type Employee (class)
emp                             # prints list
type(emp)                       # <class 'list'>
emp[0]                          # returns first element of list
type(emp[0])                    # <class 'app.Employee'>
emp[0].name                     # 'Michael'
```

# Fetching first row from .db file
```py
emp = Employee.query.first()
```

# Fetching random rows from .db file
```py
Employee.query.filter_by(name='Trump').all()
```

# Fetching rows from .db file by id
```py
db.session.get(Employee,2)
```

# Updating data
```py
michael.age = 100
db.session.commit()
```

# Deleting Rows
```py
db.session.delete(trump)
db.session.commit()
```

# db.Model
- parent class for all models in a Flask application using SQLAlchemy.
- Each class that inherits from db.Model represents a table in the database, and each attribute in the class corresponds to a column in that table.

# db.create_all()
- when this function is called, SQLAlchemy automatically creates a table with name same as that of the class and columns defined in the class

# _ _ tablename _ _
- default table name is name of the class in lowrcase
- sets the name of the table other than the default one

---
---
---
---
---
---
# one-to-many relation
```
Database -> ipl
Tables -> Team(t_id,team,state)  
          Player(id,name,nationality,team_id) 
```
```
Each Team can have multiple Player and one Player can be associated with one and only one Team. So the relation is one-to-many.
```
# Foreign Key
```py
team_id = db.Column(db.Integer, db.ForeignKey('iplteams.id'))
```
- This code references the **id** of Team table (primary key).<br>
- This ensures that the value in **team_id** for any Player record must match a valid id in the Team table, guaranteeing that each player is associated with an existing team.
# Relationship
```py
members = db.relationship('Player', backref='team')
```
- Establishes one to many relation between Team and Player tables.
- The **members** attribute in Team acts as a collection of all the Player instances associated with that one particular team.
- The **backref='team'** argument adds a team attribute to each Player instance, which refers to the specific Team instance the player belongs to.

# Code
```py
Team.query.all()                    # returns all rows (objects of Team class)
Team.query.first()                  # returns first row (object of Team class)
csk_team = Team.query.first() 
csk_team.members                    # returns all instances of that particular team in Player table
for i in csk_team.members: 
   print(i.name)

```



























# Data
```py
csk = Team(team='CSK', state='Tamil Nadu') 
rcb = Team(team='RCB', state='Karnataka') 
mi = Team(team='MI', state= 'Maharashtra') 

msd = Player (name='MS Dhoni', nationality='Indian', team=csk) 
moeen = Player (name='Moeen Ali', nationality='English', team=csk) 
jadeja = Player (name='Ravindra Jadeja', nationality='Indian', team=csk) 
kohli = Player(name='Virat Kohli', nationality='Indian', team=rcb) 
faf = Player (name=' FAF Du Plesis', nationality='South African', team=rcb) 
siraj = Player (name='Siraj Mohammed', nationality='Indian', team=rcb) 
rohit = Player (name='Rohit Sharma', nationality='Indian', team=mi) 
hardik = Player (name='Hardik Pandya', nationality='Indian', team=mi) 
tim = Player (name='Tim David', nationality='Australian', team=mi) 

steve = Customer (name='Steve', email='steve@mail.com') 
tony = Customer(name='Tony', email='tony@mail.com') 
peter = Customer (name='Peter', email='peter@mail.com') 
matt = Customer(name='Matt', email='matt@mail.com')

bowl =  Product(product='Bowl', price=5) 
plate = Product(product='Plate', price=8) 
knife = Product (product='Knife', price=3)  
scissors = Product(product='Scissors', price=2.5)
cup  = Product(product='Cup', price=1.5)
```