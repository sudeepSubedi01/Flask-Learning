from flask import Flask, make_response,request

app = Flask(__name__)
@app.route('/')
@app.route('/home')
def home():
  response = make_response('welcome to home')
  return response

@app.route('/set_cookie')
def set_cookie():
  response = make_response('welcome to set cookie')
  response.set_cookie('name1','value1')
  response.set_cookie('name2','value2')
  return response

@app.route('/get_cookie')
def get_cookie():
  value = request.cookies.get('name1')
  return value

if __name__ == '__main__':
  app.run(debug=True)