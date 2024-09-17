from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
  return render_template('03_Templates.html')
  #return "hello world this is my home in this"

if __name__ == '__main__':
  app.run(debug=True)