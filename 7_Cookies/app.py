from flask import Flask, render_template, url_for,flash,redirect,make_response,request
from forms import LoginForm
app = Flask(__name__)
app.config['SECRET_KEY'] = 'this_is_secret_key'

@app.route('/')
@app.route('/home', methods=['GET','POST'])
def home():
  return render_template('home.html', title='Home')

@app.route('/about')
def about():
  user_name = request.cookies.get('user_name')
  if user_name is None:
    flash('Login Required')
    return redirect(url_for('login', title='login', next=request.url))
  else:
    flash(f"Hello {user_name}, welcome to the about page")
  return render_template('about.html', title='About')

@app.route('/contact')
def contact():
  user_name = request.cookies.get('user_name')
  if user_name is None:
    flash('Login Required')
    return redirect(url_for('login', title='login', next=request.url))
  else:
    flash(f"Hello {user_name}, welcome to the contact page")
  return render_template('contact.html', title='Contact')

@app.route('/login', methods=['GET','POST'])
def login():
  l_form = LoginForm()
  if l_form.validate_on_submit():
    user_name = l_form.username.data
    response = make_response('')
    response.set_cookie('user_name', user_name)
    flash(f'Session created for: {user_name}')
    next_url = request.args.get('next') or url_for('home')
    # return redirect(next_url or url_for('home'))
    response.headers['Location'] = next_url
    response.status_code=302
    return response
  return render_template('login.html', title='login', form=l_form)

if __name__ == '__main__':
  app.run(debug=True)
 