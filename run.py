#
from flask import Flask, render_template, url_for, redirect

app = Flask(__name__)
methods = ['GET', 'POST']
GET, POST = methods

@app.route('/')
def home():
	return render_template('index.html')
	
@app.route('/saludo')
def saludo():
	return render_template('saludo.html')

@app.route('/privada')
def privada():
	return render_template('privada.html')

if __name__ == '__main__':
	app.run(debug=True)