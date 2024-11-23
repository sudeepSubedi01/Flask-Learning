from flask import Flask,render_template,url_for
from forms import InputForm
import pandas as pd
import joblib

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret_key'

model = joblib.load('model.joblib')

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

@app.route('/prediction',methods=['GET','POST'])
def prediction():
  i_form = InputForm()
  if i_form.validate_on_submit():
    x_new = pd.DataFrame(dict(
      airline=[i_form.airline.data],
      date_of_journey=[i_form.date_of_journey.data.strftime('%Y-%m-%d')],
      source=[i_form.source.data],
      destination=[i_form.destination.data],
      dep_time=[i_form.dep_time.data.strftime('%H:%M:%S')],
      arrival_time=[i_form.arrival_time.data.strftime('%H:%M:%S')],
      duration=[i_form.duration.data],
      total_stops=[i_form.total_stops.data],
      additional_info=[i_form.additional_info.data],
    ))
    predicted_value = model.predict(x_new)[0]
    message = f'The predicted price is {predicted_value} INR'
  else:
    message  = 'Input data invalid'
  return render_template('prediction.html',form=i_form, msg=message)


if __name__=='__main__':
  app.run(debug=True)