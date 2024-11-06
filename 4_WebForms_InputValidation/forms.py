from flask_wtf import FlaskForm
from wtforms import StringField, SelectField,DateField, PasswordField,SubmitField,BooleanField
from wtforms.validators import DataRequired, Length, Email, Optional,EqualTo

class SignupForm(FlaskForm):
  username = StringField('username', validators=[DataRequired(), Length(2,30) ])
  email = StringField('email', validators=[DataRequired(), Email() ])
  gender = SelectField('Gender', choices=['Male','Female','Other'], validators=[Optional()])
  dob = DateField('Date of Birth', validators=[DataRequired()])
  password = PasswordField('password', validators=[DataRequired(), Length(3,30)])
  confirm_password = PasswordField('confirm_password', validators=[DataRequired(), Length(3,30), EqualTo('password')])
  submit = SubmitField('SignUp')

  
class LoginForm(FlaskForm):
  email = StringField('email', validators=[DataRequired(), Email() ])
  password = PasswordField('password', validators=[DataRequired(), Length(3,30)])
  remember_me = BooleanField('Remember Me', validators=[DataRequired()])
  submit = SubmitField('Login')

  