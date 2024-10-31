from flask import Flask

app = Flask(__name__)

@app.route('/')       # Multiple Endpoints can call same function
@app.route('/home')
def home():
 return 'This is the home page that you  are browsing'

@app.route('/about')
def about():
  return '<p>Welcome to ABOUT section<p>'

@app.route('/welcome/<name>')       # Path Parameter
def welcome(name):
  return f'welcome {name.title()}'

@app.route('/number/<int:num>')       # Path Parameter and specifying its data type
def addition(num):
  return f'welcome {num + 10}'

@app.route('/numbers/<num1>/<num2>')       # Multiple Path Parameter
def add_nums(num1,num2):
  return f'welcome {num1 + num2}'

if __name__ == '__main__':
  app.run(debug=True)