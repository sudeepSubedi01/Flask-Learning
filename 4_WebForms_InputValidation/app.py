from flask import Flask, render_template, url_for, redirect, flash
from forms import SignupForm, LoginForm


app = Flask(__name__)
app.config['SECRET_KEY'] = 'this_is_a_secret_key'

@app.route('/')
@app.route('/home')
def home():
  return render_template('home.html', title= 'Home')



@app.route('/signup', methods=['GET','POST'])
def signup():
  s_form = SignupForm()
  if s_form.validate_on_submit():
    flash(f'Registration Successful for {s_form.username.data}')
    return redirect(url_for('home'))
  return render_template('signup.html', title= 'SignUp', form = s_form)



@app.route('/login', methods=['GET','POST'])
def login():
  l_form = LoginForm()
  user_email = l_form.email.data
  user_pwd = l_form.password.data

  if l_form.validate_on_submit():
    if user_email == 'hello@gmail.com' and user_pwd == 'asd' :
      flash('Success login')
      return redirect(url_for('home'))
    else:
      flash('Incorrect email or password')
  return render_template('login.html', title= 'LogIn', form = l_form)



if __name__ == '__main__':
  app.run(debug=True)