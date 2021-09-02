from flask import Flask, render_template, url_for, request, redirect, flash
from flask_wtf import FlaskForm
from wtforms import StringField, ValidationError
import phonenumbers
from wtforms.validators import DataRequired
from inference import *
from os import getenv
from dotenv import load_dotenv

class RegisterationForm(FlaskForm):
    phone = StringField('Emergency Contact', validators= [DataRequired()])
    def validate_phone(FlaskForm, field):
        if len(field.data) > 16:
            raise ValidationError('Invalid phone number.')
        try:
            input_number = phonenumbers.parse(field.data)
            if not (phonenumbers.is_valid_number(input_number)):
                raise ValidationError('Invalid phone number.')
        except:
            input_number = phonenumbers.parse("+1" + field.data)
            if not (phonenumbers.is_valid_number(input_number)):
                raise ValidationError('Invalid phone number.')




load_dotenv()

SECRET_KEY = getenv('SECRET_KEY', None)
app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY

@app.route("/",  methods = ['GET', 'POST'])
def register():
    form = RegisterationForm()
    if form.validate_on_submit():
        flash(f'Emergency Contact Saved!', 'success')

        return redirect(url_for('activate'))
        #return render_template('base_test.html')
    else:
        return render_template('register.html', form = form)


@app.route("/activate", methods = ['GET', 'POST'])
def activate():
    msg = ''
    if request.form.get('action') == 'Walk':

        fall = inference('test_data/WAL_acc_1_1.txt')

        if fall is True:
            msg =  """Fall is Detected! 
                  Message is being sent to the emergency contact."""


    if request.form.get('action') == 'Jog':

        fall = inference('test_data/JOG_acc_1_1.txt')

        if fall is True:
            msg =  """Fall is Detected! 
                  Message is being sent to the emergency contact."""


    if request.form.get('action') == 'FW Fall':

        fall = inference('test_data/FOL_acc_1_1.txt')

        if fall is True:
            msg =  """Fall is Detected! 
                  Message is being sent to the emergency contact."""


    if request.form.get('action') == 'Jump':

        fall = inference('test_data/JUM_acc_1_1.txt')

        if fall is True:
            msg =  """Fall is Detected! 
                  Message is being sent to the emergency contact."""


    if request.form.get('action') == 'BW Fall':

        fall = inference('test_data/BSC_acc_1_1.txt')

        if fall is True:
            msg =  """Fall is Detected! 
                  Message is being sent to the emergency contact."""


    if request.form.get('action') == 'Side Fall':

        fall = inference('test_data/SDL_acc_1_1.txt')

        if fall is True:
            msg =  """Fall is Detected! 
                  Message is being sent to the emergency contact."""


    if request.form.get('action') == 'Stand':

        fall = inference('test_data/STD_acc_1_1.txt')

        if fall is True:
            msg =  """Fall is Detected! 
                  Message is being sent to the emergency contact."""


    if request.form.get('action') == 'Car-step in':

        fall = inference('test_data/CSI_acc_1_1.txt')

        if fall is True:
            msg = """Fall is Detected! 
                  Message is being sent to the emergency contact."""

    if request.form.get('action') == 'Stair down':

        fall = inference('test_data/STN_acc_1_1.txt')

        if fall is True:
            msg = """Fall is Detected! 
                  Message is being sent to the emergency contact."""


    return render_template('base_test.html', predict_content = msg)


if __name__ == '__main__':
    app.run()

