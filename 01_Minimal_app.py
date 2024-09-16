from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
  return render_template('index.html')
  #return "hello world this is my home in this"

@app.route('/welcomepage')
def welcome():
  return 'this is the welcome page in my site'

if __name__ == '__main__':
  app.run(debug=True,port=8000)