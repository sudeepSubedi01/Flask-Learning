from flask import Flask,render_template

app=Flask(__name__)


@app.route('/')
def renderNavbar():
  return render_template('04_SimpleApp.html')




if (__name__ == '__main__'):
  app.run(debug=True,port=5601)