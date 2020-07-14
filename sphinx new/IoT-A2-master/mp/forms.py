from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, SelectField, FileField, BooleanField, PasswordField, HiddenField, FloatField, SelectMultipleField
from wtforms.validators import DataRequired, Email, Regexp, Length
from wtforms_validators import AlphaNumeric
from wtforms.widgets import TextArea, CheckboxInput, ListWidget
from wtforms.widgets.html5 import NumberInput
from wtforms.fields.html5 import EmailField, DateField

class MultiCheckboxField(SelectMultipleField):
    widget = ListWidget(prefix_label=False)
    option_widget = CheckboxInput()

class LoginForm(FlaskForm):
    email = EmailField('Email address', 
    [
        DataRequired(), 
        Email()
    ])
    password = PasswordField('Password', 
    [
        DataRequired(),
    ])
    submit = SubmitField('Login')

class RegisterForm(FlaskForm):
    username = StringField('Username', 
    [
        DataRequired(),
        AlphaNumeric(message='Only alphanumeric characters are accepted.'),
        Length(min=4, message='Please input a username that is at least 4 characters long.')
    ])
    password = PasswordField('Password', 
        [
            DataRequired()
        ]
    )
    firstName = StringField('First name', [DataRequired()])
    lastName = StringField('Last name', [DataRequired()])
    email = EmailField('Email address', [DataRequired(), Email()])
    submit = SubmitField('Register')

class BookingForm(FlaskForm):
    # retrieved from the currently logged in user
    userId = HiddenField()
    # retrieved from the currently selected car
    carId = HiddenField()
    startDay = IntegerField('Start Day', [DataRequired()])
    startMonth = IntegerField('Start Month', [DataRequired()])
    endDay = IntegerField('End Day', [DataRequired()])
    endMonth = IntegerField('End Month', [DataRequired()])
    submit = SubmitField('Book')

class SearchForm(FlaskForm):
    query = StringField('Enter query here:')
    submit = SubmitField('Search')

class UserForm(FlaskForm):
    username = StringField('Username', 
    [
        DataRequired()
    ])
    password = PasswordField('Password', 
        [
            DataRequired()
        ]
    )
    firstName = StringField('First name', [DataRequired()])
    lastName = StringField('Last name', [DataRequired()])
    email = EmailField('Email address', [DataRequired(), Email()])
    userType = SelectField('Type', choices=[
        ('customer', 'Customer'),
        ('engineer', 'Engineer'),
        ('manager', 'Manager')
    ])
    submit = SubmitField('Create User')

class CarForm(FlaskForm):
    make = StringField('Make', [DataRequired()])
    bodyType = StringField('Body Type', [DataRequired()])
    colour = StringField('Colour', [DataRequired()])
    seats = IntegerField('Seats', [DataRequired()], widget=NumberInput())
    xCoordinate = FloatField(widget=NumberInput())
    yCoordinate = FloatField(widget=NumberInput())
    costPerHour = FloatField('Cost Per Hour', [DataRequired()], widget=NumberInput())
    submit = SubmitField('Create Car')

class ReportForm(FlaskForm):
    description = StringField('Description', widget=TextArea())
    submit = SubmitField('Submit Report')