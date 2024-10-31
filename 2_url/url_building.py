from flask import Flask, redirect, url_for
import time

app = Flask(__name__)

@app.route('/')
def home():
  return 'hey'

@app.route('/passed/<sname>/<marks>')
def passed(sname,marks):
  return f"YAY!! {sname.title()}, you have passed with {marks} marks"

@app.route('/failed/<sname>/<marks>')
def failed(sname,marks):
  return f"OPPS!! {sname.title()}, you have failed with {marks} marks"



#url redirection and building
@app.route('/score/<name>/<int:num>')
def score(name,num):
  if num>50:
    time.sleep(2)
    return redirect(url_for('passed', sname=name, marks=num))
    # return redirect('/')
  else:
    time.sleep(2)
    return redirect(url_for('failed', sname=name, marks=num))

if __name__ == '__main__':
  app.run(debug=True)

# http://localhost:5000/score/Trump/89
# http://localhost:5000/score/Biden/16