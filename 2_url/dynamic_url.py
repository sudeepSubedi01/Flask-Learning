from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
 return 'Welcome to my site.'

# Dynamic URL
@app.route('/welcome/<name>')        
def welcome(name):
 return f'Welcome to my site, {name}.'


if __name__ == '__main__':
  app.run(debug=True)