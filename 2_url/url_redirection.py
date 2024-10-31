from flask import Flask, redirect, url_for
import time

app = Flask(__name__)

@app.route('/')
def home():
  return 'hey'

@app.route('/passed')
def passed():
  return "YAY!! You have passed"

@app.route('/failed')
def failed():
  return "OPPS!! You have failed"



#url redirection
@app.route('/score/<name>/<int:num>')
def score(name,num):
  if num>50:
    time.sleep(2)
    return redirect(url_for('passed'))
    # return redirect('/')
  else:
    time.sleep(2)
    return redirect(url_for('failed'))

if __name__ == '__main__':
  app.run(debug=True)