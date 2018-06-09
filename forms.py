from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, TimeField, TextAreaField
from wtforms.validators import DataRequired, Length, EqualTo


class RegForm(FlaskForm):
    username = StringField('username', validators=[DataRequired(), Length(max=40, min=3)])
    email = StringField('email', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired(), Length(max=40, min=3)])
    confirm = StringField('repassword', validators=[DataRequired(), Length(max=40, min=3),
                                                    EqualTo('password', message='Passwords must match')])


class LoginForm(FlaskForm):
    username = StringField('username', validators=[DataRequired(), Length(max=40, min=3)])
    password = PasswordField('password', validators=[DataRequired(), Length(max=40, min=3)])


class OfferForm(FlaskForm):
    name = StringField('name', validators=[DataRequired(), Length(min=3, max=120)])
    capacity = StringField('capacity', validators=[DataRequired()])
    cost = StringField('cost', validators=[DataRequired(), Length(min=0, max=120)])
    description = TextAreaField('description', validators=[DataRequired(), Length(min=3, max=1000)])