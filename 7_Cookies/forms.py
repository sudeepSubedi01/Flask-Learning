from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import DataRequired, Length,Email,Optional,EqualTo

class LoginForm(FlaskForm):
  username = StringField('Username',validators=[DataRequired()])
  password = PasswordField('Password',validators=[DataRequired(), Length(3)])
  submit = SubmitField('LogIn')