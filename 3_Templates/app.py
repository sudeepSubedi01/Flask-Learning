from flask import Flask,render_template, url_for
from employees_data import data

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
  return render_template('home.html', title='Home')

@app.route('/about')
def about():
  return render_template('about.html', title='About')

@app.route('/evaluate/<int:num>')
def calculate(num):
  return render_template('evaluate.html', number=num, title='Check your number')

@app.route('/employees')
def emp_info():
  return render_template('employees.html', title='Employee Info' , data=data)


if __name__ == '__main__':
  app.run(debug=True)