#import statements go here 
from flask import Flask, request, render_template, redirect, url_for, flash
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import Required

import requests
import json

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'
app.debug = True


@app.route('/')
def home():
	return "Hello, world!"
    
#create class to represent WTForm that inherits flask form

class SimpleForm(FlaskForm):
	artist = StringField('Enter an artist name', validators=[Required()])
	number = IntegerField('how many results are you looking for?', validators=[Required()])
 	email = StringField('what is your email?', validators=[Required()])
	submit = SubmitField('Submit')

@app.route('/itunes-form')
def itunes_form():
	simpleform = SimpleForm(request.form)

    #what code goes here?
	return render_template('itunes-form.html', form=simpleform) # HINT : create itunes-form.html to represent the form defined in your class

@app.route('/itunes-result', methods = ['GET', 'POST'])
def itunes_result():
    #what code goes here?
    # HINT : create itunes-results.html to represent the results and return it
    form = SimpleForm(request.form)
    if request.method == 'POST' and form.validate_on_submit():
    	artist = form.artist.data
        number = form.number.data
        email = form.email.dat
        params ={}
        params['term'] = artist
        params['limit'] = number
        response = requests.get('https://itunes.apple.com/search', params = params)
        response_py = json.loads(response.text)['results']
	flash('All fields are required!')
	return render_template('itunes-results.html, result_html = response') #this redirects you to itunes_form if there are errors

if __name__ == '__main__':
	app.run()
