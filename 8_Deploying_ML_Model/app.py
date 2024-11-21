from flask import Flask,render_template,url_for
from forms import InputForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret_key'

@app.route('/')
@app.route('/home')
def home():
  return render_template('home.html', page_title='Home')

@app.route('/about')
def about():
  return render_template('about.html', page_title='About')

@app.route('/login',methods=['GET','POST'])
def login():
  return render_template('login.html', page_title='Login')

@app.route('/prediction')
def prediction():
  i_form = InputForm()
  return render_template('prediction.html',form=i_form)


if __name__=='__main__':
  app.run(debug=True)

