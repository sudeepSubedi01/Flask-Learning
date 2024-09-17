from flask import Flask, render_template,request,redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

with app.app_context():
    db.create_all()

class Todo(db.Model):
  sn = db.Column(db.Integer, primary_key=True)
  title = db.Column(db.String(200), nullable=False)
  description = db.Column(db.String(500), nullable=False)
  date_created = db.Column(db.DateTime, default=datetime.utcnow)

  def __repr__(self) -> str:  #connetion to the database
    return f"{self.sn} - {self.title} - {self.description}"
  
@app.route('/', methods=['POST','GET'])
def homePage():
  if(request.method == 'POST'):
    # print('Sent to database')
    # print(request.form['title'])
    titleInput = request.form['title']
    descriptionInput = request.form['description']
    todo = Todo(title= titleInput, description=descriptionInput)
    db.session.add(todo)
    db.session.commit()
  # todo = Todo(title='First Todo', description='Start investing in the stock market')  #when the web app is refreshed, each time this is run and database is updated based on session
  # db.session.add(todo)
  # db.session.commit()
  allTodo = Todo.query.all()  #displaying in the html document
  return render_template('05_TodoApp.html', allTodo = allTodo)

@app.route('/show')
def products():
  allTodo = Todo.query.all() # returns a List by running repr function
  print(allTodo)
  print(len(allTodo))
  return 'This is the products page'

@app.route('/delete/<int:sn>')
def delete(sn):
  deleteTodo = Todo.query.filter_by(sn=sn).first()
  db.session.delete(deleteTodo)
  db.session.commit()
  # return "This is delete page"
  return redirect('/')


if __name__ == '__main__':
  with app.app_context():
    db.create_all()
  app.run(debug=True, port=8000)

#checking if the database updates
#again again