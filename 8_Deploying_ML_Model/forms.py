import pandas as pd
from flask_wtf import FlaskForm
from wtforms import DateField,SelectField,TimeField,IntegerField,SubmitField
from wtforms.validators import DataRequired

train = pd.read_csv('data/train.csv')
val = pd.read_csv('data/val.csv')
x_data = pd.concat([train,val],axis=0).drop(columns=['price'])

class InputForm(FlaskForm):
  airline = SelectField(label='Airline', choices=x_data['airline'].unique)
  date_of_journey = DateField(label='Date of Journey', validators=[DataRequired()])
  source = SelectField(label='Source', choices=x_data['source'].unique())
  destination = SelectField(label='Destination', choices=x_data['source'].unique())
  dep_time = TimeField(label='Departure Time', validators=[DataRequired()])
  arrival_time = TimeField(label='Arrival Time', validators=[DataRequired()])
  duration = IntegerField(label='Duration', validators=[DataRequired()])
  total_stops = IntegerField(label='Total Stops', validators=[DataRequired()])
  additional_info = SelectField(label='Total Stops', choices=x_data['additional_info'].unique())
  predict_btn = SubmitField(label='Predict')