from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
  return 'we can access static files by: localhost:8000/static/sampleFile.txt'

@app.route('/welcomepage')
def welcome():
  return 'this is the welcome page in my site'

if __name__ == '__main__':
  app.run(debug=True,port=8000)