#
from flask import Flask, render_template, url_for, redirect, flash, session, request

from functools import wraps

app = Flask(__name__)
app.secret_key = "flask_manejandodatos.es"
methods = ['GET', 'POST']
GET, POST = methods

def requiere_login(f):
	@wraps(f)
	def wrap(*args, **kkargs):
		if 'logged_in' in session:
			return f(*args, **kkargs)
		else:
			flash('Necesitas hacer LogIn antes!')
			return redirect(url_for('login'))
	return wrap
	
@app.route('/')
def home():
	return render_template('index.html')
	
@app.route('/saludo')
def saludo():
	return render_template('saludo.html')

@app.route('/privada')
@requiere_login
def privada():
	return render_template('privada.html')

@app.route('/login', methods=methods)
def login():
	error = None
	if request.method == POST:
		if request.form['username'] != 'admin' or request.form['password'] != 'admin':
			error = 'Error en las credenciales'
		else:
			session['logged_in'] = True
			flash('Estas dentro')
			return redirect(url_for('home'))
	return render_template('login.html', error=error)

@app.route('/logout')
def logout():
	session.pop('logged_in', None)
	flash('Estas fuera')
	print "Logout"
	return redirect(url_for('home'))
	
if __name__ == '__main__':
	app.run(debug=True)